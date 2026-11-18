# Simulator Mesin ATM - Tugas Akhir Basic Python (Day 3)
#
# Fitur:
# 1. Login PIN (maksimal 3 kali percobaan)
# 2. Cek saldo
# 3. Setor tunai
# 4. Tarik tunai
# 5. Riwayat mutasi

# ==============================
# DATA NASABAH (Dictionary)
# ==============================
# Dictionary menyimpan nama, PIN, dan saldo nasabah
nasabah = {
    "nama": "Lale",
    "pin": "123456",
    "saldo": 1500000
}

# List untuk mencatat riwayat transaksi (mutasi)
riwayat = []


# ==============================
# FUNGSI-FUNGSI
# ==============================

# Fungsi untuk mengubah angka jadi tulisan rupiah
# Contoh: 1500000 -> Rp 1.500.000
def format_rupiah(angka):
    # {:,} memberi pemisah koma, lalu koma kita ganti jadi titik
    teks = "{:,}".format(angka).replace(",", ".")
    return "Rp " + teks


# Fungsi untuk cek PIN, maksimal 3 kali percobaan
# Hasilnya True kalau PIN benar, False kalau salah 3 kali
def verifikasi_pin():
    percobaan = 0  # hitungan berapa kali salah

    while percobaan < 3:
        pin_input = input("Masukkan PIN Anda: ")

        # Cek apakah PIN yang diketik sama dengan PIN di dictionary
        if pin_input == nasabah["pin"]:
            print("PIN benar. Selamat datang,", nasabah["nama"] + "!")
            return True
        else:
            percobaan = percobaan + 1
            sisa = 3 - percobaan
            print("PIN salah! Sisa percobaan:", sisa)

    # Kalau sampai sini berarti sudah salah 3 kali
    print("Kartu diblokir karena salah PIN 3 kali.")
    return False


# Fungsi untuk menampilkan saldo nasabah saat ini
def cek_saldo():
    print("Saldo Anda:", format_rupiah(nasabah["saldo"]))


# Fungsi untuk menambah saldo, lalu mencatat ke riwayat
def setor_tunai():
    # Ambil input sebagai teks dulu
    teks = input("Masukkan jumlah setoran: Rp ")

    # Kalau isinya bukan angka, hentikan fungsi
    if not teks.isdigit():
        print("Input harus berupa angka!")
        return

    # Teks sudah pasti angka, jadi aman diubah ke integer
    jumlah = int(teks)

    if jumlah <= 0:
        # Setoran tidak boleh nol atau minus
        print("Jumlah setoran harus lebih dari 0.")
    else:
        # Tambah saldo
        nasabah["saldo"] = nasabah["saldo"] + jumlah
        # Catat ke list riwayat
        riwayat.append("Setor tunai  : + " + format_rupiah(jumlah))
        print("Setoran berhasil!")
        cek_saldo()


# Fungsi untuk mengurangi saldo (kalau saldo cukup), lalu mencatat ke riwayat
def tarik_tunai():
    # Ambil input sebagai teks dulu
    teks = input("Masukkan jumlah penarikan: Rp ")

    # Kalau isinya bukan angka, hentikan fungsi
    if not teks.isdigit():
        print("Input harus berupa angka!")
        return

    # Teks sudah pasti angka, jadi aman diubah ke integer
    jumlah = int(teks)

    if jumlah <= 0:
        print("Jumlah penarikan harus lebih dari 0.")
    elif jumlah > nasabah["saldo"]:
        # Uang yang ditarik lebih besar dari saldo
        print("Saldo tidak cukup!")
    else:
        # Kurangi saldo
        nasabah["saldo"] = nasabah["saldo"] - jumlah
        # Catat ke list riwayat
        riwayat.append("Tarik tunai  : - " + format_rupiah(jumlah))
        print("Penarikan berhasil!")
        cek_saldo()


# Fungsi untuk menampilkan semua riwayat transaksi
def lihat_mutasi():
    print("--- RIWAYAT MUTASI ---")

    # Kalau list masih kosong, berarti belum ada transaksi
    if len(riwayat) == 0:
        print("Belum ada transaksi.")
    else:
        nomor = 1
        # Tampilkan satu per satu isi list
        for catatan in riwayat:
            print(str(nomor) + ".", catatan)
            nomor = nomor + 1


# Fungsi untuk menampilkan pilihan menu ATM
def tampilkan_menu():
    print()
    print("=== BANK LALE ===")
    print("[1] Cek Saldo")
    print("[2] Setor Tunai")
    print("[3] Tarik Tunai")
    print("[4] Riwayat Mutasi")
    print("[5] Keluar")


# ==============================
# PROGRAM UTAMA
# ==============================

# Fungsi utama: login dulu, lalu jalankan menu terus-menerus
def main():
    # Langkah 1: verifikasi PIN
    if not verifikasi_pin():
        return  # berhenti kalau PIN gagal

    # Langkah 2: ulangi menu sampai nasabah memilih keluar
    jalan = True
    while jalan:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")

        # Jalankan fungsi sesuai pilihan
        if pilihan == "1":
            cek_saldo()
        elif pilihan == "2":
            setor_tunai()
        elif pilihan == "3":
            tarik_tunai()
        elif pilihan == "4":
            lihat_mutasi()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan ATM kami.")
            jalan = False  # menghentikan loop
        else:
            print("Pilihan tidak valid, coba lagi.")


# Program mulai dari sini
main()