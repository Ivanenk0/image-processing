import numpy as np
import matplotlib.pyplot as plt

# --- TASK 1 ---

mono = np.zeros((30, 30), dtype=int)
mono[10:20, 10:20] = 1
mono[15:25, 5:15] = 2

# --- TASK 2 ---

fig, ax = plt.subplots(2,2, figsize=(7,7))
ax[0,0].imshow(mono)
ax[0,0].set_title('Mono')
ax[0,1].imshow(mono, cmap='binary')
ax[0,1].set_title('Mono Binary')

fig.tight_layout()
fig.savefig('..\output_image\lab1.2-result.png')

# --- TASK 3 ---

color = np.zeros((30, 30, 3), dtype=float)
color[15:25, 5:15, 0] = 1
color[10:20, 10:20, 1] = 1
color[5:15, 15:25, 2] = 1

negative = 1 - color

ax[1, 0].imshow(color)
ax[1, 0].set_title("Colored image")
ax[1, 1].imshow(negative)
ax[1, 1].set_title("Negative image")

fig.tight_layout()
fig.savefig('..\output_image\lab1.3-result.png')