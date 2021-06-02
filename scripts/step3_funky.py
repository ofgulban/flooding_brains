"""Used for rendering frames as png files."""

import os
import numpy as np
import pyvista as pv
import nibabel as nb

SCALAR = "/home/faruk/Documents/temp_flooding_brains/data/okapi/okapi_N4.nii.gz"
DIST = "/home/faruk/Documents/temp_flooding_brains/data/okapi/okapi_cerebrum_RH_v05_borders_inputrim_centroids1_geodistance.nii.gz"
MASK = "/home/faruk/Documents/temp_flooding_brains/data/okapi/okapi_cerebrum_RH_v05_inputrim_columns10000.nii.gz"
OUTDIR = "/home/faruk/Documents/temp_flooding_brains/test"

CAMPOS = [[-518, 181, -177], [149, 184, 122], [0, 0, -1]]
NR_FRAMES = 24*5
CMAP = "CET_L1"
BACKGROUND = "black"
RESOLUTION = (720, 720)
CLIM = (0, 200)

# =============================================================================
# Output directory
if not os.path.exists(OUTDIR):
    os.makedirs(OUTDIR)
print("  Output directory: {}".format(OUTDIR))

# Get scalars
data = nb.load(SCALAR).get_fdata()

# Get distances
dist = nb.load(DIST).get_fdata()

# Get mask
mask = np.asarray(nb.load(MASK).dataobj)
dims = mask.shape

# Set opacity to make min and max invisible
opacity = np.ones(255)
opacity[0] = 0
opacity[-1] = 0

# Prep pyvista plotter
p = pv.Plotter(window_size=RESOLUTION, off_screen=True)
p.set_background(BACKGROUND)
p.disable_anti_aliasing()
p.camera_position = CAMPOS

dmax = np.linspace(0, np.max(dist), NR_FRAMES+1)[1:]
# Render frames
for i, d in enumerate(dmax):
    print("  Frame {}/{}".format(i+1, NR_FRAMES))

    # Select voxels that will be rendered
    idx0 = dist > 0
    idx1 = dist > d - 5
    idx2 = dist < d
    idx3 = (idx1 * idx2) * idx0
    ids = np.unique(mask[idx3])
    idx4 = np.in1d(mask.reshape(np.prod(dims)), ids)
    idx4 = idx4.reshape(dims)
    temp = np.copy(data)
    temp[~idx4] = CLIM[0]

    # Render
    p.add_volume(temp, show_scalar_bar=False, cmap=CMAP, clim=CLIM,
                 shade=False, opacity=opacity, blending="composite")
    out_name = "frame-{}.png".format(str(i+1).zfill(3))
    p.screenshot(os.path.join(OUTDIR, out_name))
    p.clear()

p.close()

print("Finished.")
