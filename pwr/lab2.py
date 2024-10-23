import numpy as np
import matplotlib.pyplot as plt

# --- TASK 1 ---

fig, ax = plt.subplots(3,3, figsize=(10, 10))

# Próbkowanie funkcji liniowej
x = np.linspace(0, 4*np.pi, 40)
y = np.sin(x)

ax[0,0].plot(x, y)

# Inicjalizacja nowego wymiaru tablicy
two_dimension_sinus = y[:, None] * y[None, :]
#two_dimension_sinus = y[:, np.newaxis] * y[np.newaxis, :]

value_min = np.min(two_dimension_sinus)
value_max = np.max(two_dimension_sinus)

ax[0,1].imshow(two_dimension_sinus, cmap='magma')
ax[0,1].set_title('2D sin min: %.3f, max: %.3f' % (value_min, value_max))

# Normalizacja przedziałowa
two_dimension_sinus -= np.min(two_dimension_sinus)
two_dimension_sinus /= np.max(two_dimension_sinus)

value_min = np.min(two_dimension_sinus)
value_max = np.max(two_dimension_sinus)

ax[0,2].imshow(two_dimension_sinus, cmap='magma')
ax[0,2].set_title('2D sin min: %.3f, max: %.3f' % (value_min, value_max))

fig.savefig("../output_images/lab2.1-result.png")

# --- TASK 2 ---

TWO_BIT = 2**2-1
FOUR_BIT = 2**4-1
EIGHT_BIT = 2**8-1

# --- 2 bit Image Discretization

# Kwantyzacja i zaokrąglenie do liczb całkowitych
scaled_2bit_img = two_dimension_sinus * TWO_BIT
scaled_2bit_img = np.rint(scaled_2bit_img)

value_min = np.min(scaled_2bit_img)
value_max = np.max(scaled_2bit_img)

ax[1,0].imshow(scaled_2bit_img, cmap='magma')
ax[1,0].set_title('2D sin min: %d, max: %d' % (value_min, value_max))

# --- 4 bit Image Discretization

scaled_4bit_img = two_dimension_sinus * FOUR_BIT
scaled_4bit_img = np.rint(scaled_4bit_img)

value_min = np.min(scaled_4bit_img)
value_max = np.max(scaled_4bit_img)

ax[1,1].imshow(scaled_4bit_img, cmap='magma')
ax[1,1].set_title('2D sin min: %d, max: %d' % (value_min, value_max))

# --- 8 bit Image Discretization

scaled_8bit_img = two_dimension_sinus * EIGHT_BIT
scaled_8bit_img = np.rint(scaled_8bit_img)

value_min = np.min(scaled_8bit_img)
value_max = np.max(scaled_8bit_img)

ax[1,2].imshow(scaled_8bit_img, cmap='magma')
ax[1,2].set_title('2D sin min: %d, max: %d' % (value_min, value_max))

fig.savefig("../output_images/lab2.2-result.png")

# --- TASK 3 ---

# Zaszumienie sygnału.
noise = np.random.normal(two_dimension_sinus)
ax[2,0].imshow(noise, cmap='magma')
ax[2,0].set_title('n = 1')

n = [50,1000]

for i in range(n[0]):
    noise += np.random.normal(two_dimension_sinus)

ax[2,1].imshow(noise, cmap='magma')
ax[2,1].set_title('n = %d' % n[0])

for i in range(n[1]):
    noise += np.random.normal(two_dimension_sinus)

ax[2,2].imshow(noise, cmap='magma')
ax[2,2].set_title('n = %d' % n[1])

fig.savefig("../output_images/lab2.3-result.png")
