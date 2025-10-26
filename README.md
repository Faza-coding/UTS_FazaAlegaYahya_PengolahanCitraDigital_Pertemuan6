
# README – Praktikum Segmentasi Citra (Thresholding)

## Deskripsi Singkat

Program ini merupakan implementasi dari segmentasi citra berbasis thresholding sesuai dengan materi Pertemuan 6 – Pengolahan Citra Digital.
Tujuannya adalah memisahkan objek dan latar belakang pada citra berdasarkan intensitas pixel menggunakan berbagai teknik thresholding dari yang sederhana hingga adaptif.

## Metode yang Digunakan

1. Global Thresholding (Manual)
   Menggunakan nilai ambang tetap (misalnya T = 127).
   Cocok untuk citra dengan pencahayaan seragam.

2. Otsu’s Thresholding (Otomatis)
   Mencari nilai ambang optimal secara otomatis dengan memaksimalkan perbedaan antar kelas (foreground dan background).

3. Adaptive Thresholding
   Nilai ambang dihitung berdasarkan lingkungan (neighborhood) sekitar setiap pixel.
   Cocok untuk citra dengan pencahayaan tidak merata.

   * Mean Adaptive
   * Gaussian Adaptive

4. Morphological Cleaning
   Tahap pembersihan hasil segmentasi dengan operasi closing (dilation + erosion) untuk menutup lubang kecil dan memperbaiki bentuk objek.

## Kebutuhan Sistem

* Python 3.x
* Library yang dibutuhkan:

  ```
  pip install opencv-python numpy matplotlib
  ```
* File gambar (misal: IHI.jpeg)

## Cara Menjalankan

1. Simpan kode dalam file bernama `thresholding_segmentation.py`
2. Pastikan gambar (IHI.jpeg) ada di folder yang sama
3. Jalankan program:

   ```
   python thresholding_segmentation.py
   ```
4. Hasil visualisasi akan muncul dalam satu jendela matplotlib yang menampilkan seluruh tahap pengolahan.

---

# Penjelasan Kode

```
import cv2
import numpy as np
import matplotlib.pyplot as plt
```

Mengimpor library utama:

* cv2 untuk pengolahan citra
* numpy untuk operasi numerik
* matplotlib untuk menampilkan hasil visualisasi

---

## 1. Baca dan Preprocessing Citra

```
image = cv2.imread('IHI.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5,5), 0)
```

Membaca citra berwarna dan mengonversinya ke grayscale.
Melakukan Gaussian Blur untuk mengurangi noise agar thresholding lebih stabil.

---

## 2. Global Thresholding (Manual)

```
T = 127
_, thresh_global = cv2.threshold(gray, T, 255, cv2.THRESH_BINARY)
```

Menggunakan nilai ambang tetap T=127.
Pixel dengan intensitas di atas 127 menjadi putih (255), sisanya hitam (0).

---

## 3. Otsu’s Thresholding (Otomatis)

```
T_otsu, thresh_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
```

Nilai threshold T dihitung otomatis oleh algoritma Otsu berdasarkan distribusi intensitas (histogram).
Cocok untuk citra dengan dua puncak intensitas (bimodal).

---

## 4. Adaptive Thresholding

```
thresh_mean = cv2.adaptiveThreshold(gray, 255,
                                    cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY, 11, 2)

thresh_gauss = cv2.adaptiveThreshold(gray, 255,
                                     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY, 11, 2)
```

Mean Adaptive menggunakan rata-rata nilai piksel di sekitarnya sebagai ambang.
Gaussian Adaptive menggunakan pembobotan Gaussian (hasil lebih halus).

Parameter penting:

* blockSize = 11 → ukuran area lokal (harus ganjil)
* C = 2 → konstanta yang dikurangkan dari rata-rata lokal

---

## 5. Morphological Cleaning

```
kernel = np.ones((3,3), np.uint8)
cleaned = cv2.morphologyEx(thresh_gauss, cv2.MORPH_CLOSE, kernel)
```

Melakukan operasi closing (dilation diikuti erosion) untuk menutup lubang kecil dan menyatukan bagian objek yang terputus.
Kernel 3x3 digunakan sebagai structuring element.

---

# 6. Visualisasi Hasil

```
fig, axs = plt.subplots(2, 3, figsize=(15,10))
```

Menampilkan enam hasil dalam satu jendela:

| Baris | Kolom | Gambar                    | Keterangan          |
| ----- | ----- | ------------------------- | ------------------- |
| 1     | 1     | Citra Asli                | Input RGB           |
| 1     | 2     | Grayscale                 | Setelah konversi    |
| 1     | 3     | Global Thresholding       | Nilai tetap T=127   |
| 2     | 1     | Otsu Thresholding         | Nilai otomatis      |
| 2     | 2     | Adaptive Mean             | Threshold per area  |
| 2     | 3     | Adaptive Gaussian + Morph | Hasil paling bersih |

```
plt.tight_layout()
plt.show()
```
Menyesuaikan tata letak dan menampilkan hasil akhir.

# Kesimpulan

* Global Thresholding efektif untuk citra dengan pencahayaan seragam
* Otsu’s Method lebih adaptif untuk citra dengan dua distribusi intensitas
* Adaptive Thresholding unggul untuk pencahayaan tidak merata
* Morphological Cleaning membantu memperbaiki hasil segmentasi akhir
