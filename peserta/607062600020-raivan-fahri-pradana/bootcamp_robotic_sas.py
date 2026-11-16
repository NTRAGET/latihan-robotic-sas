import time


def sapa_peserta(nama):
    "Fungsi menampilkan salam pembuka"
    return f"Hello World! Selamat datang di Bootcamp Robotic SAS, {nama}!"


def tambah(a, b):
    "Fungsi Penjumlahan"
    return a + b


def kurang(a, b):
    "Fungsi Pengurangan"
    return a - b


def kali(a, b):
    "Fungsi Perkalian"
    return a * b


def bagi(a, b):
    "Fungsi Pembagian"
    if b == 0:
        return "Error (Tidak bisa membagi dengan nol)"
    return a / b


def main():
    print("      PROGRAM UTAMA BOOTCAMP     ")

    nama_input = input("\n Masukkan nama Anda: ")
    print(sapa_peserta(nama_input))
    print("\n ------------------------------------")

    time.sleep(1)
    print("\n--- KALKULATOR ARITMATIKA SEDERHANA ---")

    angka1 = float(input("Masukkan angka pertama : "))
    angka2 = float(input("Masukkan angka kedua   : "))

    print("\n[HASIL PERHITUNGAN]")
    print(f"Penjumlahan ({angka1} + {angka2}) : {tambah(angka1, angka2)}")
    print(f"Pengurangan ({angka1} - {angka2}) : {kurang(angka1, angka2)}")
    print(f"Perkalian   ({angka1} * {angka2}) : {kali(angka1, angka2)}")
    print(f"Pembagian   ({angka1} / {angka2}) : {bagi(angka1, angka2)}")

    print("--------------------------------------")
    print("\n[INFO] Program berhasil dijalankan!")


if __name__ == "__main__":
    main()