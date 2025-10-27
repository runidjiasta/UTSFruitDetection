# Proyek Deteksi Objek menggunakan YOLOv8: Deteksi Buah Real-Time

## SIP 107 Rancang Bangun Sistem Berbasis AI

Sebagai bentuk pemenuhan tugas Ujian Tengah Semester (UTS) untuk mata kuliah SIP 107: Rancang Bangun Sistem Berbasis AI, kami membuat, melatih, dan menguji sebuah model deep learning (YOLOv8) yang dapat mendeteksi dan mengklasifikasikan berbagai jenis buah.

Tujuan proyek ini adalah untuk melatih model YOLOv8 agar dapat melakukan deteksi objek buah secara real-time dari feed video atau webcam, sebagai pemenuhan poin (e) dari tugas: **"Lakukan deteksi langsung pada video dan tampilkan bounding box secara real-time."**

## Anggota Kelompok

* Runi Dwi Jiasta (202304560001)
* Teresa Kaena Dharmanyoto (202304560014)
* Caroline Evarista Den Lau (202304560027)
* Andrew Riza Rafhael (202304560030)

## Dataset

Dataset yang digunakan bersumber dari "Fruits dataset for training RT-DETR" di [Kaggle](https://www.kaggle.com/datasets/shaomeitang/fruits-dataset-for-training-rt-detr).

Dataset ini kemudian kami proses, lakukan augmentasi, dan bagi menjadi set train/valid/test menggunakan Roboflow. Model kami dilatih untuk mendeteksi 22 kelas buah yang berbeda (terdiri dari berbagai jenis Apel, Kiwi, dan Jeruk).

* **Link Roboflow Project**: [https://app.roboflow.com/ds/9gdNgUVojB?key=ODPfP2WwEr]

## Isi Repositori

* `Training_Fruit Detection.ipynb`: Notebook Google Colab yang berisi semua kode untuk mengunduh dataset, melatih (`.train()`), dan memvalidasi model YOLOv8s.
* `deteksi_webcam.py`: Script Python untuk menjalankan deteksi objek secara real-time menggunakan webcam di komputer lokal.
* `best.pt`: File bobot (weights) model YOLOv8s yang telah dilatih. Ini adalah file "otak" dari model kami.

## Cara Menjalankan Deteksi Real-Time (di Komputer Lokal)

Model yang telah dilatih (`best.pt`) dapat dijalankan secara lokal di komputer Anda untuk mendeteksi buah secara real-time menggunakan webcam.

1.  **Persiapan Lingkungan**
    * Pastikan Anda memiliki Python dan Anaconda (atau pip) ter-install di komputer Anda.
    * Clone repositori ini atau download file `deteksi_webcam.py` dan `best.pt`.
    * **PENTING**: Letakkan kedua file (`deteksi_webcam.py` dan `best.pt`) di dalam satu folder yang sama.

3.  **Install Library yang Dibutuhkan**
    * Buka Anaconda Prompt (atau Terminal/CMD biasa).
    * Install semua library yang diperlukan dengan satu perintah:
    ```bash
    pip install ultralytics opencv-python torch
    ```

5.  **Jalankan Script Deteksi**
    * Pastikan tidak ada program lain (seperti Zoom, Google Meet, OBS, dll.) yang sedang menggunakan kamera Anda. Jika kamera error, tutup semua program lain dan coba lagi.
    * Di Anaconda Prompt, pindah ke folder tempat Anda menyimpan file (gunakan `cd`):
    ```bash
    # Contoh:
    cd C:\Users\NamaKamu\Documents\ProjekDeteksi
    ```
    * Setelah berada di folder yang benar, jalankan script Python:
    ```bash
    python deteksi_webcam.py
    ```
    * Sebuah jendela akan muncul menampilkan feed webcam Anda. Arahkan kamera ke buah-buahan untuk melihat deteksi.
    * Tekan tombol **'q'** pada keyboard (sambil meng-klik jendela video) untuk keluar.

## Video Hasil Deteksi

Berikut adalah video demo hasil deteksi real-time dari model kami yang telah di-upload ke YouTube:

[Link Video YouTube Anda di Sini]
