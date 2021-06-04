"""Used for rendering frames as png files."""

import numpy as np
import nibabel as nb

FILE1 = "/home/faruk/Documents/temp_flooding_brains/data/ding_flat/ding_flat_test.nii.gz"
FILE2 = "/home/faruk/Documents/temp_flooding_brains/data/ding_flat/ding_flat_L2.nii.gz"

OUTFILE = "/home/faruk/Documents/temp_flooding_brains/data/ding_flat/ding_flat_moves.nii.gz"
TEMP = "/home/faruk/Documents/temp_flooding_brains/data/ding_flat/ding_flat_coords.nii.gz"

# Data range
MIN, MAX = 9000, 14000
NR_STEPS = 24*2
CAMPOS = [[127, 126, 117], [29, 28, 19], [0, 0, 1]]

NR_CAKE_LAYERS = 5

# =============================================================================
# Get data
nii = nb.load(FILE1)
data = nii.get_fdata()

# Quantize norm
norm = nb.load(FILE2).get_fdata()
norm /= norm.max()
norm *= NR_CAKE_LAYERS
norm = np.ceil(norm)
norm *= -1
norm[norm != 0] += NR_CAKE_LAYERS

# Prepare coordinates
dims = data.shape
nr_layers = dims[2]
coords_xyz = np.asarray(np.indices(dims))
coords_xyz = np.transpose(coords_xyz, [1, 2, 3, 0])

# New z coordinates
coords_new = np.copy(coords_xyz)
for i in range(1, NR_CAKE_LAYERS+1):
    coords_new[norm == i, 2] += i * nr_layers
coords_new = np.round(coords_new)

# -----------------------------------------------------------------------------
# Interpolate voxel particle tractories
flat_xyz = np.reshape(coords_xyz, [np.prod(dims), 3])
flat_new = np.reshape(coords_new, [np.prod(dims), 3])
nr_voxels = np.prod(dims)

traj = np.zeros((nr_voxels, NR_STEPS, 3))
for i in range(nr_voxels):
    traj[i, :, 0] = np.linspace(flat_xyz[i, 0], flat_new[i, 0], NR_STEPS)
    traj[i, :, 1] = np.linspace(flat_xyz[i, 1], flat_new[i, 1], NR_STEPS)
    traj[i, :, 2] = np.linspace(flat_xyz[i, 2], flat_new[i, 2], NR_STEPS)

# -----------------------------------------------------------------------------
# Transform volume data
new_data = np.zeros([dims[0], dims[1], dims[2]*NR_CAKE_LAYERS, NR_STEPS])
count = np.copy(new_data)
for i in range(nr_voxels):
    idx0 = int(traj[i, 0, 0])
    idx1 = int(traj[i, 0, 1])
    idx2 = int(traj[i, 0, 2])

    for j in range(NR_STEPS):
        new_idx0 = int(traj[i, j, 0])
        new_idx1 = int(traj[i, j, 1])
        new_idx2 = int(traj[i, j, 2])
        # Move voxels like particles
        new_data[new_idx0, new_idx1, new_idx2, j] += data[idx0, idx1, idx2]
        count[new_idx0, new_idx1, new_idx2, j] += 1

# Normalize summed values with counts to attain mean
new_data[count != 0] /= count[count != 0]

# Save as nifti
img = nb.Nifti1Image(new_data, affine=nii.affine, header=nii.header)
nb.save(img, OUTFILE)

print("Finished.")
