"""Find borders of a selected tissue in a segmentation file."""

import os
import subprocess

# Path to LayNii (folder where it is installed in your system)
LAYNII_PATH = "/home/faruk/Git/LAYNII"

FILE1 = "/home/faruk/gdrive/temp_flooding_brains/data/dolphin/dolphin_cerebrum_RH_15_borders.nii.gz"
FILE2 = [
    "/home/faruk/gdrive/temp_flooding_brains/data/dolphin/dolphin_cerebrum_RH_15_borders_points100.nii.gz",
    ]

# -----------------------------------------------------------------------------
# Run LayNii
for i in FILE2:
    command = os.path.join(LAYNII_PATH, "LN2_GEODISTANCE ")
    command += "-domain {} ".format(FILE1)
    command += "-init {} ".format(i)
    print(command)
    subprocess.run(command, shell=True)

print('Finished.\n')
