"""Used for rendering frames as png files."""

import os
import numpy as np
import pyvista as pv
import nibabel as nb

FILES = [
    "/path/to/okapi_cerebrum_RH_v06_borders_points4_geodistance.nii.gz",
    ]

OUTDIRS = [
    "/path/to/movie",
    ]


CAMPOS = [[-518, 181, -177], [149, 184, 122], [0, 0, -1]]
NR_FRAMES = 24*5
CMAP = "flag"
BACKGROUND = "black"
RESOLUTION = (720, 720)

# =============================================================================
for m in range(len(FILES)):
    print("Movie {}/{}".format(m+1, len(FILES)))

    file = FILES[m]
    outdir = OUTDIRS[m]

    # Output directory
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    print("  Output directory: {}".format(outdir))

    # Get data and clip it
    data = nb.load(file).get_fdata()
    data[data == 0] = -1

    cmax = np.linspace(0, np.max(data), NR_FRAMES+1)[1:]

    # Set opacity to make min and max invisible
    opacity = np.ones(255)
    opacity[0] = 0
    opacity[-1] = 0

    # Prep pyvista plotter
    p = pv.Plotter(window_size=RESOLUTION, off_screen=True)
    p.set_background(BACKGROUND)
    p.disable_anti_aliasing()
    p.camera_position = CAMPOS

    # Render frames
    for i, v in enumerate(cmax):
        print("  Frame {}/{}".format(i+1, NR_FRAMES))

        temp = np.copy(data)
        temp[temp > v] = v
        p.add_volume(temp, show_scalar_bar=False, cmap=CMAP, clim=[0, v],
                     shade=False, opacity=opacity, blending="composite")
        out_name = "frame-{}.png".format(str(i+1).zfill(3))
        p.screenshot(os.path.join(outdir, out_name))
        p.clear()

p.close()

print("Finished.")
