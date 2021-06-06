"""Find borders of a selected tissue in a segmentation file."""

import os
import subprocess

# Path to LayNii (folder where it is installed in your system)
LAYNII_PATH = "/home/faruk/Git/LAYNII"

# Borders nifti file generated in the previous step.
FILE = "/path/to/okapi_cerebrum_RH_v06_borders.nii.gz"

# Number of points that will be generated on the borders
NR_POINTS = 4

# -----------------------------------------------------------------------------
# Run LayNii
command = os.path.join(LAYNII_PATH, "LN2_IFPOINTS ")
command += "-domain {} ".format(FILE)
command += "-nr_points {} ".format(NR_POINTS)
print(command)
subprocess.run(command, shell=True)

print('Finished.\n')
