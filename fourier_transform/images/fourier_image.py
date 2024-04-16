import numpy as np
import matplotlib.pyplot as plt
from skimage import io

image_path = r"insert .jpg location here, using \ between depth thingy"
image = io.imread(image_path, as_gray = True)

fft_result = np.fft.fft2(image)
magnitude_spectrum = np.abs(fft_result)

#shift mag0 to centre
shifted_spectrum = np.fft.fftshift(magnitude_spectrum)


plt.figure(figsize=(8, 6))
plt.imshow(np.log1p(shifted_spectrum), cmap='gray')
plt.title('Mangnitude Spectrum (log scale)')
plt.axes('off')
plt.show