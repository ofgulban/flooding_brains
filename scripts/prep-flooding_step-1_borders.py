"""Find borders of a selected tissue in a segmentation file."""

import os
import subprocess

# Path to LayNii (folder where it is installed in your system)
LAYNII_PATH = "/home/faruk/Git/LAYNII"

# Segmentation nifti (tissues are labeled with integers)
FILE = "/home/faruk/gdrive/temp_flooding_brains/data/okapi/okapi_cerebrum_RH_v06.nii.gz"

# Voxels labelled with this integer will be considered
TISSUE_LABEL = 1

# Output directory
OUTDIR = "/home/faruk/gdrive/temp_flooding_brains/data/okapi/"

# -----------------------------------------------------------------------------
# Determine output basename
filename = os.path.basename(FILE)
basename, ext = filename.split(os.extsep, 1)
outname = os.path.join(OUTDIR, "{}_test.{} ".format(basename, ext))

# Run LayNii LN2_BORDERIZE
command = os.path.join(LAYNII_PATH, "LN2_BORDERIZE ")
command += "-input {} ".format(FILE)
command += "-label {} ".format(TISSUE_LABEL)
command += "-output {} ".format(outname)
print(command)
subprocess.run(command, shell=True)

print('Finished.\n')
