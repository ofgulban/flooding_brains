"""Used in thingsonthings.org LN2_MULTILATERATE blog post."""

import os
import pyvista as pv
import nibabel as nb
import numpy as np

FILENAME = "/home/faruk/gdrive/temp_flooding_brains/data/dolphin/dolphin_cerebrum_RH_15_borders_planes_geodistance_zoomed.nii.gz"
OUTDIR = "/home/faruk/gdrive/temp_flooding_brains/frames/movie-dolphin_planes_orbit"
OUTNAME = "dolphin_planes_orbit.mp4"

NR_FRAMES = 180

CAMPOS = [[605, 571, 564], [143, 110, 102], [0, 0, 1]]

# =============================================================================
# Output directory
if not os.path.exists(OUTDIR):
    os.makedirs(OUTDIR)
print("  Output directory: {}".format(OUTDIR))

# =============================================================================
# Get data
nii = nb.load(FILENAME)
data = nii.get_fdata()

# Flip dims
data = np.transpose(data, [1, 0, 2])
data = data[:, :, ::-1]

# Get data and clip it
data[data != 0] -= np.min(data[data != 0])
data[data == 0] = -1

# Data range
CMAX = np.max(data[data != 0])

# Set opacity to make min and max invisible
opacity = np.ones(255)
opacity[0] = -1
opacity[-1] = -1

# Render volume
p = pv.Plotter(window_size=(720, 720))
p.add_volume(data, cmap="bone", clim=[0, CMAX],
             opacity=opacity, shade=False, show_scalar_bar=False)
p.set_background("black")
p.show(auto_close=False)

# Orbit animation
path = p.generate_orbital_path(n_points=NR_FRAMES)
p.open_movie(os.path.join(OUTDIR, OUTNAME))
p.orbit_on_path(path, write_frames=True)

# Convert camera position to integers and for nicer print
campos = list()
for i in range(3):
    campos.append([])
    for j in range(3):
        campos[i].append(round(p.camera_position[i][j]))

print("You can copy-paste the following into 'anim_flooding_step-2_render.py':\n")
print("CAMPOS = {}\n".format(campos))

p.close()
