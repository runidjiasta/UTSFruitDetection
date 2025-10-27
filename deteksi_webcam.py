import cv2
from ultralytics import YOLO

# 1. Load model 'best.pt' kamu
# Pastikan file 'best.pt' ada di folder yang sama
model = YOLO('best.pt') 

# 2. Nyalakan webcam
# Angka 0 berarti webcam default di laptop
cap = cv2.VideoCapture(0)

# Cek apakah webcam berhasil dinyalakan
if not cap.isOpened():
    print("Error: Tidak bisa membuka webcam.")
    exit()

print("Webcam menyala. Tekan 'q' pada jendela video untuk keluar.")

# 3. Looping per frame
while True:
    # Baca satu frame dari webcam
    success, frame = cap.read()

    # Jika webcam gagal membaca frame
    if not success:
        print("Gagal membaca frame dari webcam.")
        break

    # 4. Lakukan deteksi YOLOv8 pada frame
    results = model(frame, stream=True)

    # 5. Loop hasil deteksi untuk menggambar bounding box
    for r in results:
        annotated_frame = r.plot() 
        
        # 6. Tampilkan frame yang sudah ada box-nya
        cv2.imshow("Deteksi Webcam Real-time - Tekan 'q' untuk keluar", annotated_frame)

    # 7. Buat tombol 'q' untuk keluar dari loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 8. Selesai, matikan webcam dan tutup semua jendela
cap.release()
cv2.destroyAllWindows()
print("Webcam dimatikan.")