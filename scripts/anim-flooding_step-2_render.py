"""Used for rendering frames as png files."""

import os
import numpy as np
import pyvista as pv
import nibabel as nb

FILES = [
    "/home/faruk/gdrive/temp_flooding_brains/data/dolphin/dolphin_cerebrum_RH_15_borders_planes_geodistance_zoomed.nii.gz",
    ]

OUTDIRS = [
    "/home/faruk/gdrive/temp_flooding_brains/frames/movie-dolphin_slices",
    ]


# CAMPOS = [[750, 227, 158], [137, 140, 111], [0, 0, -1]]
# CAMPOS = [[-518, 181, -177], [149, 184, 122], [0, 0, -1]]
CAMPOS = [[113, 967, 102], [143, 110, 102], [0, 0, 1]]  # dolphin slices

NR_FRAMES = 24 * 1
CMAP = "bone"  # user _r to reverse colormap
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

    # Get data
    data = nb.load(file).get_fdata()
    # Flip dims
    data = np.transpose(data, [1, 0, 2])
    data = data[:, :, ::-1]
    # Clip data
    data[data != 0] -= np.min(data[data != 0])
    data[data == 0] = -1

    # Space scalar maximums
    CMIN = 0
    CMAX = np.max(data[data != 0])
    cmap_max = np.linspace(CMIN, CMAX, NR_FRAMES+1)[1:]

    # Add reversal
    # cmap_max = np.hstack([cmap_max, cmap_max[::-1]])

    # Set opacity to make min and max invisible
    opacity = np.ones(255)
    opacity[0] = CMIN - 1
    opacity[-1] = CMIN - 1

    # Prep pyvista plotter
    p = pv.Plotter(window_size=RESOLUTION, off_screen=True)
    p.set_background(BACKGROUND)
    p.disable_anti_aliasing()
    p.camera_position = CAMPOS

    # Render frames
    for i, v in enumerate(cmap_max):
        print("  Frame {}/{}".format(i+1, np.size(cmap_max)))

        temp = np.copy(data)
        temp[temp > v] = v
        p.add_volume(temp, show_scalar_bar=False, cmap=CMAP, clim=[CMIN, v],
                     shade=False, opacity=opacity, blending="composite")
        out_name = "frame-{}.png".format(str(i+1).zfill(3))
        p.screenshot(os.path.join(outdir, out_name))
        p.clear()

p.close()

print("Finished.")
