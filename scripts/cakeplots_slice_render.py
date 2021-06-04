"""Used in thingsonthings.org LN2_MULTILATERATE blog post."""

import os
import numpy as np
import pyvista as pv
import nibabel as nb

# Scalar file (e.g. activtion map or anatomical image)
FILE1 = "/home/faruk/Documents/temp_flooding_brains/data/ding_flat/ding_flat_moves.nii.gz"
OUTDIR = "/home/faruk/Documents/temp_flooding_brains/data/ding_flat/movie"

CLIM = (9000, 14000)

# -----------------------------------------------------------------------------
# Load data
data1 = nb.load(FILE1).get_fdata()
nr_frames = data1.shape[-1]

# Colorbar
sargs = dict(width=0.25, height=0.1, vertical=False,
             position_x=0.05, position_y=0.05,
             font_family="courier",
             title_font_size=22,
             label_font_size=18,
             n_labels=3, fmt="%.0f")

frame_order = np.arange(nr_frames)
frame_order = np.hstack([frame_order, frame_order[::-1]])

opacity = np.ones(255)
opacity[0] = 0

# -----------------------------------------------------------------------------
p = pv.Plotter(window_size=(640, 720), off_screen=True)
p.set_background("black")
# p.camera_position = CAMPOS
for i, j in enumerate(frame_order):
    print("  Frame {}/{}".format(i+1, frame_order.size))

    # Get data and clip it
    temp = np.copy(data1[..., j])
    pvdata = pv.wrap(temp)

    p.add_volume(pvdata, stitle="Intensity", cmap="gray", clim=CLIM,
                 scalar_bar_args=sargs, blending="composite", opacity=opacity)
    p.add_text("Cakeplot", font="courier", font_size=18)

    out_name = "frame-{}.png".format(str(i).zfill(3))
    p.screenshot(os.path.join(OUTDIR, out_name))
    p.clear()

p.close()

print("Finished.")
