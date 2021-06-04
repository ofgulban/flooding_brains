"""Process LN2_PATCH_FLATTEN outputs for cake plots."""

import numpy as np
import nibabel as nb

FILE1 = "/home/faruk/Documents/temp_flooding_brains/data/ding_flat/ding_flat_test.nii.gz"
FILE2 = "/home/faruk/Documents/temp_flooding_brains/data/ding_flat/ding_flat_L2.nii.gz"

OUTFILE = "/home/faruk/Documents/temp_flooding_brains/data/ding_flat/ding_flat_test_prep.nii.gz"

NR_CAKE_LAYERS = 5

# -----------------------------------------------------------------------------
nii1 = nb.load(FILE1)
dims = nii1.shape
data = nii1.get_fdata()

# Quantize norm
norm = nb.load(FILE2).get_fdata()
norm /= norm.max()
norm *= NR_CAKE_LAYERS
norm = np.ceil(norm)

# Make space on z axis for cake layers using an extra dimension
new = np.zeros((dims[0], dims[1], NR_CAKE_LAYERS, dims[2]))

# Elevate norm bins center to outwards
nr_layers = dims[2]
for i, j in enumerate(range(NR_CAKE_LAYERS, 0, -1)):
    temp = np.zeros(dims)
    temp[norm == j] = data[norm == j]
    new[:, :, i, :] = temp

# Flatten the extra dimension onto 3rd
new = new.reshape((dims[0], dims[1], NR_CAKE_LAYERS * dims[2]))
img = nb.Nifti1Image(new, affine=nii1.affine, header=nii1.header)
nb.save(img, OUTFILE)

print("Finished.")
