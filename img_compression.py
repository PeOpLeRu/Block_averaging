import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import face

def block_mean(arr, yb=8, xb=8):
    new_shape = yb, xb
    new_arr = np.zeros(new_shape)
    block_size_y = arr.shape[0] // yb + arr.shape[0] % yb
    step_y = arr.shape[0] // yb
    block_size_x = arr.shape[1] // xb + arr.shape[1] % xb
    step_x = arr.shape[1] // xb
    
    it_y = 0

    for y in range(0, arr.shape[0], step_y):
        it_x = 0
        for x in range(0, arr.shape[1], step_x):
            new_arr[it_y, it_x] = np.mean(arr[y:y+block_size_y, x:x+block_size_x])

            it_x += 1
            if it_x >= new_arr.shape[1]:
                break
   
        it_y += 1
        if it_y >= new_arr.shape[0]:
            break

    return new_arr


img = face(gray=True)

print("\rcalculation: 1/7", end='')

plt.subplot(171)
plt.title("original")
plt.imshow(img, cmap="gray")

print("\rcalculation: 2/7", end='')

plt.subplot(172)
plt.title("1/2 size")
img_copy_1 = block_mean(img, 384, 512)
plt.imshow(img_copy_1, cmap="gray")

print("\rcalculation: 3/7", end='')

plt.subplot(173)
plt.title("1/3 size")
img_copy_2 = block_mean(img, 256, 341)
plt.imshow(img_copy_2, cmap="gray")

print("\rcalculation: 4/7", end='')

plt.subplot(174)
plt.title("1/4 size")
img_copy_3 = block_mean(img, 192, 256)
plt.imshow(img_copy_3, cmap="gray")

print("\rcalculation: 5/7", end='')

plt.subplot(175)
plt.title("1/10 size")
img_copy_4 = block_mean(img, 77, 102)
plt.imshow(img_copy_4, cmap="gray")

print("\rcalculation: 6/7", end='')

plt.subplot(176)
plt.title("1/20 size")
img_copy_4 = block_mean(img, 38, 51)
plt.imshow(img_copy_4, cmap="gray")

print("\rcalculation: 7/7", end='')

plt.subplot(177)
plt.title("1/30 size")
img_copy_4 = block_mean(img, 26, 34)
plt.imshow(img_copy_4, cmap="gray")

print("\rcalculation: 100%")

plt.show()