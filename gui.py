import tkinter as tk
from tkinter import messagebox 

# Membuka main window
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")

# Membuat label untuk judul
labelJudul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
labelJudul.pack(pady=10)

# Membuat input nilai untuk 10 mata pelajaran
inputNilai = []
for i in range(10):
    lblMataPelajaran = tk.Label(root, text=f"Nilai Mata Pelajaran {i+1}:")
    lblMataPelajaran.pack(pady=3)
    entNilai = tk.Entry(root)
    entNilai.pack(pady=3)
    inputNilai.append(entNilai)

def hasilPrediksi():
    try:
        for entry in inputNilai:  # Memastikan nilai yang diinput sesuai
            nilai = int(entry.get())
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")
        
        # Menampilkan hasil prediksi apabila semua nilai yang diinput sesuai
        labelHasil.config(text="Hasil Prediksi: Program Studi Teknologi Informasi")
    
    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve)) # Menampilkan pesan error jika ada kesalahan input

# Membuat tombol prediksi
btnPrediksi = tk.Button(root, text="Hasil Prediksi", command=hasilPrediksi)
btnPrediksi.pack(pady=20)

# Membuat label untuk menampilkan hasil prediksi
labelHasil = tk.Label(root, text="Hasil Prediksi: ")
labelHasil.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()