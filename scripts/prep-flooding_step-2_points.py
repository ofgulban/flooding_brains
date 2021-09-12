"""Find borders of a selected tissue in a segmentation file."""

import os
import subprocess

# Path to LayNii (folder where it is installed in your system)
LAYNII_PATH = "/home/faruk/Git/LAYNII"

# Borders nifti file generated in the previous step.
FILE = "/home/faruk/gdrive/temp_flooding_brains/data/dolphin/dolphin_cerebrum_RH_15_borders.nii.gz"

# Number of points that will be generated on the borders
# NR_POINTS = [1, 4, 16]
NR_POINTS = [100]

# -----------------------------------------------------------------------------
# Run LayNii
for i in NR_POINTS:
    command = os.path.join(LAYNII_PATH, "LN2_IFPOINTS ")
    command += "-domain {} ".format(FILE)
    command += "-nr_points {} ".format(i)
    print(command)
    subprocess.run(command, shell=True)

print('Finished.\n')
