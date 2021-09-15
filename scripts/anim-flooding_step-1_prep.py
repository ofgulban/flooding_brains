"""Used for figuring out the camera position."""

import numpy as np
import pyvista as pv
import nibabel as nb

FILE1 = "/home/faruk/gdrive/temp_flooding_brains/data/dolphin/dolphin_cerebrum_RH_15_borders_points16_geodistance_onebyone.nii.gz"

CAMPOS = [[-518, 181, -177], [149, 184, 122], [0, 0, -1]]

CMAP = "CET_L1"
RESOLUTION = (720, 720)

# =============================================================================
# Render middle gray matter geodesic distance as Panel B (moving element)
nii = nb.load(FILE1)
data_orig = np.copy(nii.get_fdata())

opacity = np.ones(255)
opacity[0] = 0  # make zeros invisible

# Get data and clip it
data = nii.get_fdata()
data[data != 0] -= np.min(data[data != 0])
data[data == 0] = -1

p = pv.Plotter(window_size=RESOLUTION, off_screen=False)
p.set_background("black")
p.camera_position = CAMPOS
p.add_volume(data, cmap=CMAP, show_scalar_bar=False,
             shade=False, opacity=opacity, blending="composite")
p.enable_anti_aliasing()

p.show(interactive=True)

# Convert camera position to integers and for nicer print
campos = list()
for i in range(3):
    campos.append([])
    for j in range(3):
        campos[i].append(round(p.camera_position[i][j]))

print("You can copy-paste the following into 'anim_flooding_step-2_render.py':\n")
print("CAMPOS = {}\n".format(campos))

p.close()

print("Finished.")
