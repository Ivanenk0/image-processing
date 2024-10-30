import numpy as np
import matplotlib.pyplot as plt
import skimage as ski



fig, ax = plt.subplots(2, 2, figsize=(10, 7))

cat = ski.data.chelsea()

ax[0, 0].imshow(cat)
ax[0, 0].set_title("Chelsea")

mono_cat = np.mean(cat, axis=2)
mono_cat = mono_cat[::8, ::8]

ax[0, 1].imshow(mono_cat, cmap='binary_r')
ax[0, 1].set_title("Mono")

rotation_matrix = np.array([[np.cos(0.261799388), - np.sin(0.261799388), 0],
                   [np.sin(0.261799388), np.cos(0.261799388), 0],
                   [0, 0, 1]])

shear_matrix = np.array([[1, 0.5, 0],
                [0, 1, 0],
                [0, 0, 1]])

# ------ rotation -------

rotation_tform = ski.transform.AffineTransform(matrix=rotation_matrix)
rotate_cat = ski.transform.warp(mono_cat, inverse_map=rotation_tform.inverse)

ax[1, 0].imshow(rotate_cat, cmap='binary_r')
ax[1, 0].set_title("Rotate")

# ------ shear -------

shear_tform = ski.transform.AffineTransform(matrix=shear_matrix)

shear_cat = ski.transform.warp(mono_cat, inverse_map=shear_tform.inverse)

ax[1, 1].imshow(shear_cat, cmap='binary_r')
ax[1, 1].set_title("Shear")

fig.savefig("../output_images/lab3.1-result.png")

# -------- zad 3 ------------

fig, ax = plt.subplots(1, 2, figsize=(9, 6), sharex=True, sharey=True)

height, width = mono_cat.shape  # dimensions of the image
x_coords, y_coords = np.meshgrid(np.arange(width), np.arange(height))
coords = np.stack([x_coords.ravel(), y_coords.ravel()], axis=-1)

# 2. Append a column of ones to the coordinates array to get coords.shape (2166, 3)
coords = np.column_stack((coords, np.ones(coords.shape[0])))

transformed_coords = coords@rotation_matrix
intensities = mono_cat.flatten()

# Plot the points
ax[0].scatter(coords[:, 0], coords[:, 1], c=intensities, cmap='binary_r')
ax[0].set_title('Original Pixel Positions')

ax[1].scatter(transformed_coords[:, 0], transformed_coords[:, 1], c=intensities, cmap='binary_r')
ax[1].set_title('Transformed Pixel Positions')

fig.savefig("../output_images/lab3.2-result.png")