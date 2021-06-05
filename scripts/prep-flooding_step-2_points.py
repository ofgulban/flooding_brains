"""Find borders of a selected tissue in a segmentation file."""

import os
import subprocess

# Path to LayNii (folder where it is installed in your system)
LAYNII_PATH = "/home/faruk/Git/LAYNII"

# Borders nifti file generated in the previous step.
FILE = "/home/faruk/gdrive/temp_flooding_brains/data/okapi/okapi_cerebrum_RH_v06_borders.nii.gz"

# Number of points that will be generated on the borders
NR_POINTS = 4

# Output directory
OUTDIR = "/home/faruk/gdrive/temp_flooding_brains/data/okapi/"

# -----------------------------------------------------------------------------
# Determine output basename
filename = os.path.basename(FILE)
basename, ext = filename.split(os.extsep, 1)
outname = os.path.join(OUTDIR, "{}_points{}.{} ".format(basename, NR_POINTS,
                                                        ext))

# Run LayNii LN2_BORDERIZE
command = os.path.join(LAYNII_PATH, "LN2_IFPOINTS ")
command += "-domain {} ".format(FILE)
command += "-nr_points {} ".format(NR_POINTS)
command += "-output {} ".format(outname)
print(command)
subprocess.run(command, shell=True)

print('Finished.\n')
