"""Used for figuring out the camera position."""

import numpy as np
import pyvista as pv
import nibabel as nb

FILE1 = "/path/to/myimage_geodistance.nii.gz"

NR_FRAMES = 240

CAMPOS = [[-518, 181, -177], [149, 184, 122], [0, 0, -1]]

CMAP = "CET_L1"
RESOLUTION = (720, 720)

# =============================================================================
# Render middle gray matter geodesic distance as Panel B (moving element)
nii = nb.load(FILE1)
data_orig = np.copy(nii.get_fdata())
values = np.linspace(0, np.max(data_orig), NR_FRAMES)

opacity = np.ones(255)
opacity[0] = 0  # make zeros invisible

# Get data and clip it
data = nii.get_fdata()
data[data == 0] = -1

cmax = np.linspace(0, np.max(data_orig), NR_FRAMES+1)[1:]

p = pv.Plotter(window_size=RESOLUTION, off_screen=False)
p.set_background("white")
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
print(campos)

p.close()

print("Finished.")
