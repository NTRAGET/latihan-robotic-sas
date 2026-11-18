nasabah = {
    "nama": "Rahfi Al'araaf",
    "pin": "rahfi ganteng",
    "saldo": 1000000000
}

riwayat = []

percobaan = 0
maksimal_percobaan = 3

def cek_saldo():
    print("\n========== SALDO BHOS ==========")
    print("Nama Nasabah :", nasabah["nama"])
    print("Saldo Anda   : Rp", format(nasabah["saldo"], ",").replace(",", "."))
    print("================================")

def setor_tunai():
    print("\n========== SETOR TUNAI ==========")

    try:
        jumlah = int(input("Masukkan jumlah uang yang bos ingin setor: Rp "))

        if jumlah > 0:
            nasabah["saldo"] += jumlah

            riwayat.append(
                "Setor Tunai: Rp " + format(jumlah, ",").replace(",", ".")
            )

            print("Uhuyyy...Setor Tunai Berhasil!")
            print("Saldo Bos Sekarang: Rp", format(nasabah["saldo"], ",").replace(",", "."))

        else:
            print("Jumlah setor harus lebih dari 0!")

    except ValueError:
        print("Input harus berupa angka!")

def tarik_tunai():
    print("\n========== TARIK TUNAI BHOS ==========")

    try:
        jumlah = int(input("Masukkan jumlah uang yang ingin ditarik: Rp "))

        if jumlah <= 0:
            print("Jumlah penarikan harus lebih dari 0!")

        elif jumlah > nasabah["saldo"]:
            print("Maaf, Saldo Anda Tidak Cukup! Dasar Miskin")

        else:
            nasabah["saldo"] -= jumlah

            riwayat.append(
                "Tarik Tunai: Rp " + format(jumlah, ",").replace(",", ".")
            )

            print("Penarikan berhasil!")
            print("Saldo sekarang: Rp", format(nasabah["saldo"], ",").replace(",", "."))

    except ValueError:
        print("Input harus berupa angka!")

def riwayat_transaksi():
    print("\n========== RIWAYAT TRANSAKSI TUAN ==========")

    if len(riwayat) == 0:
        print("Belum ada transaksi.")

    else:
        for nomor, transaksi in enumerate(riwayat, start=1):
            print(f"{nomor}. {transaksi}")

    print("=======================================")

print("===================================")
print("       SELAMAT DATANG DI ATM       ")
print("      BANK TOYYIB x BANK RAHFI     ")
print("===================================")

while percobaan < maksimal_percobaan:

    pin_input = input("Masukkan PIN ATM Anda: ")

    if pin_input == nasabah["pin"]:
        print("\nLogin berhasil!")
        break

    else:
        percobaan += 1
        sisa = maksimal_percobaan - percobaan

        print("PIN yang Anda masukkan salah!")

        if sisa > 0:
            print("Sisa kesempatan:", sisa)
        else:
            print("Kesempatan habis. Kartu ATM diblokir sementara.")

if percobaan < maksimal_percobaan:

    aktif = True

    while aktif:

        print("\n===================================")
        print("       BANK TOYYIB x BANK RAHFI    ")
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
            riwayat_transaksi()

        elif pilihan == "5":
            print("\nTerima kasih telah menggunakan")
            print("ATM BANK TOYYIB.")
            print("Silakan ambil kartu Anda.")
            aktif = False

        else:
            print("Pilihan tidak valid! Silakan pilih menu 1-5.")

else:
    print("\nAkses ATM ditolak.")
