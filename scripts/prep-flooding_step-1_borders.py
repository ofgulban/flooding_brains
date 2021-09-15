"""Find borders of a selected tissue in a segmentation file."""

import os
import subprocess

# Path to LayNii (folder where it is installed in your system)
LAYNII_PATH = "/home/faruk/Git/LAYNII"

# Segmentation nifti (tissues are labeled with integers)
FILE = "/home/faruk/gdrive/temp_flooding_brains/data/dolphin/dolphin_cerebrum_RH_15.nii.gz"

# Voxels labelled with this integer will be considered
TISSUE_LABEL = 1

# -----------------------------------------------------------------------------
# Run LayNii
command = os.path.join(LAYNII_PATH, "LN2_BORDERIZE ")
command += "-input {} ".format(FILE)
command += "-label {} ".format(TISSUE_LABEL)
command += "-jumps 3 "
print(command)
subprocess.run(command, shell=True)

print('Finished.\n')
