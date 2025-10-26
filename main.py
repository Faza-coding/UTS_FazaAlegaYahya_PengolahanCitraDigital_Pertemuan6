# ============================================
# PENGOLAHAN CITRA DIGITAL
# SEGMENTASI CITRA - THRESHOLDING PERTEMUAN 6
# Faza Alega Yahya - 231011400414
# ============================================

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. BACA CITRA DAN PREPROCESSING
image = cv2.imread('IHI.jpeg')  # ganti dengan path gambar kamu
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5,5), 0)

# ------------------------------------------------
# 2. GLOBAL THRESHOLDING (MANUAL)
# ------------------------------------------------
T = 127
_, thresh_global = cv2.threshold(gray, T, 255, cv2.THRESH_BINARY)

# ------------------------------------------------
# 3. OTSU’S THRESHOLDING (OTOMATIS)
# ------------------------------------------------
T_otsu, thresh_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# ------------------------------------------------
# 4. ADAPTIVE THRESHOLDING
# ------------------------------------------------
thresh_mean = cv2.adaptiveThreshold(gray, 255,
                                    cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY, 11, 2)

thresh_gauss = cv2.adaptiveThreshold(gray, 255,
                                     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY, 11, 2)

# ------------------------------------------------
# 5. MORPHOLOGICAL CLEANING
# ------------------------------------------------
kernel = np.ones((3,3), np.uint8)
cleaned = cv2.morphologyEx(thresh_gauss, cv2.MORPH_CLOSE, kernel)

# ------------------------------------------------
# 6. TAMPILKAN SEMUA HASIL DALAM SATU HALAMAN
# ------------------------------------------------
fig, axs = plt.subplots(2, 3, figsize=(15,10))

# Citra asli
axs[0,0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0,0].set_title('Citra Asli')
axs[0,0].axis('off')

# Grayscale
axs[0,1].imshow(gray, cmap='gray')
axs[0,1].set_title('Citra Grayscale')
axs[0,1].axis('off')

# Global Thresholding
axs[0,2].imshow(thresh_global, cmap='gray')
axs[0,2].set_title(f'Global Thresholding (T={T})')
axs[0,2].axis('off')

# Otsu Thresholding
axs[1,0].imshow(thresh_otsu, cmap='gray')
axs[1,0].set_title(f'Otsu Thresholding (T={T_otsu:.2f})')
axs[1,0].axis('off')

# Adaptive Mean
axs[1,1].imshow(thresh_mean, cmap='gray')
axs[1,1].set_title('Adaptive Thresholding (Mean)')
axs[1,1].axis('off')

# Adaptive Gaussian + Cleaning
axs[1,2].imshow(cleaned, cmap='gray')
axs[1,2].set_title('Adaptive Gaussian + Morph Cleaning')
axs[1,2].axis('off')

plt.tight_layout()
plt.show()
