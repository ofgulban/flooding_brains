"""Used in thingsonthings.org LN2_MULTILATERATE blog post."""

import numpy as np
import nibabel as nb

FILE1 = "/home/faruk/Documents/temp_flooding_brains/brainweb/nii/phantom_1pt0mm_normal_wht.nii.gz"
FILE2 = "/home/faruk/Documents/temp_flooding_brains/brainweb/nii/phantom_1pt0mm_normal_csf.nii.gz"
FILE3 = "/home/faruk/Documents/temp_flooding_brains/brainweb/nii/phantom_1pt0mm_normal_gry.nii.gz"

OUTFILE = "/home/faruk/Documents/temp_flooding_brains/brainweb/phantom_1pt0mm_normal_rim.nii.gz"

# -----------------------------------------------------------------------------
nii = nb.load(FILE1)
dims = nii.shape + (3,)

temp = np.zeros(dims)
temp[..., 0] = nb.load(FILE1).get_fdata()
temp[..., 1] = nb.load(FILE2).get_fdata()
temp[..., 2] = nb.load(FILE3).get_fdata()

winner = np.argmax(temp, axis=-1) + 1

img = nb.Nifti1Image(winner, affine=nii.affine, header=nii.header)
nb.save(img, OUTFILE)

print("Finished.")
