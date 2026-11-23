# Data nasabah menggunakan dictionary
nasabah = {
    "nama": "Farrel Althaf An-Nasai",
    "pin": "123456",
    "saldo": 1500000
}

# List untuk menyimpan riwayat transaksi
riwayat_transaksi = []

# Method login untuk validasi PIN nasabah
def login():

    kesempatan = 3

    print("===================================")
    print("       SELAMAT DATANG DI ATM")
    print("             BANK BCA")
    print("===================================")

    while kesempatan > 0:

        pin = input("Masukkan PIN Anda: ")

        if pin == nasabah["pin"]:
            print("\nLogin berhasil!")
            print("Selamat datang,", nasabah["nama"])
            return True

        else:
            kesempatan -= 1

            print("PIN yang Anda masukkan salah!")
            print("Sisa percobaan:", kesempatan)

    print("\nAkun Anda diblokir sementara.")
    print("Silakan hubungi petugas bank.")

    return False

# Method cek saldo
def cek_saldo():

    print("\n========== CEK SALDO ==========")
    print("Nama Nasabah :", nasabah["nama"])
    print("Saldo Anda   : Rp", format(nasabah["saldo"], ","))

# Method setor tunai
def setor_tunai():

    print("\n========== SETOR TUNAI ==========")

    try:
        jumlah = int(input("Masukkan jumlah uang: Rp "))

        if jumlah > 0:

            nasabah["saldo"] += jumlah

            riwayat_transaksi.append(
                f"Setor Tunai: +Rp{jumlah:,}"
            )

            print("\nSetor tunai berhasil!")
            print("Jumlah setor  : Rp", format(jumlah, ","))
            print("Saldo sekarang: Rp", format(nasabah["saldo"], ","))

        else:
            print("Jumlah setor harus lebih dari 0!")

    except ValueError:
        print("Input harus berupa angka!")

# Method tarik tunai
def tarik_tunai():

    print("\n========== TARIK TUNAI ==========")

    try:
        jumlah = int(input("Masukkan jumlah uang: Rp "))

        if jumlah <= 0:
            print("Jumlah penarikan harus lebih dari 0!")

        elif jumlah > nasabah["saldo"]:
            print("Maaf, saldo Anda tidak mencukupi!")

        else:

            nasabah["saldo"] -= jumlah

            riwayat_transaksi.append(
                f"Tarik Tunai: -Rp{jumlah:,}"
            )

            print("\nPenarikan berhasil!")
            print("Jumlah tarik  : Rp", format(jumlah, ","))
            print("Saldo sekarang: Rp", format(nasabah["saldo"], ","))

    except ValueError:
        print("Input harus berupa angka!")

# Method menampilkan riwayat transaksi
def tampilkan_riwayat():

    print("\n========== RIWAYAT TRANSAKSI ==========")

    if len(riwayat_transaksi) == 0:

        print("Belum ada transaksi.")

    else:

        for nomor, transaksi in enumerate(riwayat_transaksi, start=1):
            print(f"{nomor}. {transaksi}")

    print("=======================================")

# Method menu utama
def menu_utama():

    while True:

        print("\n===================================")
        print("             BANK BCA")
        print("===================================")
        print("1. Cek Saldo")
        print("2. Setor Tunai")
        print("3. Tarik Tunai")
        print("4. Riwayat Transaksi")
        print("5. Keluar")
        print("===================================")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":

            cek_saldo()

        elif pilihan == "2":

            setor_tunai()

        elif pilihan == "3":

            tarik_tunai()

        elif pilihan == "4":

            tampilkan_riwayat()

        elif pilihan == "5":

            print("\nTerima kasih telah menggunakan")
            print("layanan ATM BANK BCA.")
            print("Silakan ambil kartu Anda.")

            break

        else:

            print("\nPilihan tidak tersedia!")
            print("Silakan pilih menu 1 sampai 5.")

# Program utama
if login():

    menu_utama()

else:

    print("\nProgram ATM dihentikan.")
