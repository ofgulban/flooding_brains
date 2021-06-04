"""Used for rendering frames as png files."""

import os
import numpy as np
import pyvista as pv
import nibabel as nb

FILENAME = "/home/faruk/Documents/temp_flooding_brains/data/ding_flat/ding_flat_test_prep.nii.gz"
OUTDIR = "/home/faruk/Documents/temp_flooding_brains/data/ding_flat/"
OUTNAME = "cakeplots_test.mp4"

# Data range
MIN, MAX = 9000, 14000
NR_FRAMES = 24*5
CAMPOS = [[127, 126, 117], [29, 28, 19], [0, 0, 1]]

# =============================================================================
# Get data
nii = nb.load(FILENAME)
data = pv.wrap(nii.get_fdata())

# Render volume
p = pv.Plotter(window_size=(640, 720))
p.add_text("Cakeplot", font="courier", font_size=18)

# Colorbar
sargs = dict(width=0.25, height=0.1, vertical=False,
             position_x=0.05, position_y=0.05,
             font_family="courier",
             title_font_size=22,
             label_font_size=18,
             n_labels=3, fmt="%.0f",)

opacity = np.ones(255)
opacity[0] = 0

p.add_volume(data, stitle="Intensity", cmap="gray", clim=[MIN, MAX],
             scalar_bar_args=sargs, blending="composite", opacity=opacity)
p.set_background("black")
p.camera_position = CAMPOS
p.show(auto_close=False)

# -----------------------------------------------------------------------------
# Convert camera position to integers and for nicer print
campos = list()
for i in range(3):
    campos.append([])
    for j in range(3):
        campos[i].append(round(p.camera_position[i][j]))
print(campos)

# -----------------------------------------------------------------------------
# Orbit animation
path = p.generate_orbital_path(factor=6, viewup=[0, 0, 2], shift=25,
                               n_points=NR_FRAMES)
p.open_movie(os.path.join(OUTDIR, OUTNAME))
p.orbit_on_path(path, write_frames=True)
p.close()

print("Finished.")
