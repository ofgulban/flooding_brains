"""Used for figuring out the camera position."""

import numpy as np
import pyvista as pv
import nibabel as nb

FILE = "/home/faruk/gdrive/temp_flooding_brains/data/okapi/okapi_cerebrum_RH_v05_borders.nii.gz"

OUTFILE = "/home/faruk/gdrive/temp_flooding_brains/data/okapi/okapi_cerebrum_RH_v05_borders_noise.nii.gz"

# =============================================================================
# Load nifti
nii = nb.load(FILE)
data = np.asarray(nii.dataobj)
dims = data.shape

# Generate noise
noise = np.random.random(np.prod(dims)) * 2 - 1
noise = np.reshape(noise, dims)

img = nb.Nifti1Image(noise, affine=nii.affine, header=nii.header)
nb.save(img, OUTFILE)

print("Finished.")
