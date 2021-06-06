"""Find borders of a selected tissue in a segmentation file."""

import os
import subprocess

# Path to LayNii (folder where it is installed in your system)
LAYNII_PATH = "/home/faruk/Git/LAYNII"

FILE1 = "path/to/okapi_cerebrum_RH_v06_borders.nii.gz"
FILE2 = "path/to/okapi_cerebrum_RH_v06_borders_points4.nii.gz"

# Number of points that will be generated on the borders
NR_POINTS = 4

# -----------------------------------------------------------------------------
# Run LayNii
command = os.path.join(LAYNII_PATH, "LN2_GEODISTANCE ")
command += "-domain {} ".format(FILE1)
command += "-init {} ".format(FILE2)
print(command)
subprocess.run(command, shell=True)

print('Finished.\n')
