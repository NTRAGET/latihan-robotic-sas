def verif_pin(data_user):
    maks_percobaan = 3
    percobaan = 0

    while percobaan < maks_percobaan:
        pin_input = input("Masukkan PIN Anda (6 digit): ")
        if pin_input == data_user["pin"]:
            print("\nLogin berhasil! Selamat datang.\n")
            return True
        else:
            percobaan += 1
            sisa = maks_percobaan - percobaan
            if sisa > 0:
                print(f"PIN salah! Sisa percobaan: {sisa} kali.\n")
            else:
                print("\nPIN salah 3 kali. Kartu Anda terblokir sementara.")
    return False


def cek_saldo(data_user):
    print(f"\nSaldo rekening Anda saat ini: Rp {data_user['saldo']:,}")


def setor_tunai(data_user, riwayat):
    try:
        nominal = int(input("\nMasukkan nominal setor tunai: Rp "))
        if nominal <= 0:
            print("harus lebih dari Rp 0.")
            return

        data_user["saldo"] += nominal
        riwayat.append(f"Setor Tunai  : +Rp {nominal}")
        print(f"Setor tunai sebesar Rp {nominal} berhasil.")
        cek_saldo(data_user)
    except ValueError:
        print("Input tidak valid. Harap masukkan angka saja.")


def tarik_tunai(data_user, riwayat):
    try:
        nominal = int(input("\nMasukkan nominal tarik tunai: Rp "))
        if nominal <= 0:
            print("Nominal tarik harus lebih dari Rp 0.")
            return

        if nominal > data_user["saldo"]:
            print("Transaksi gagal! Saldo tidak mencukupi.")
            cek_saldo(data_user)
            return

        data_user["saldo"] -= nominal
        riwayat.append(f"Tarik Tunai  : -Rp {nominal}")
        print(f"Tarik tunai sebesar Rp {nominal} berhasil.")
        cek_saldo(data_user)
    except ValueError:
        print("Input tidak valid. Harap masukkan angka saja.")


def tampilkan_mutasi(riwayat):
    print("\n=== RIWAYAT MUTASI TRANSAKSI ===")
    if not riwayat:
        print("Belum ada transaksi yang tercatat.")
    else:
        for nomor, transaksi in enumerate(riwayat, start=1):
            print(f"{nomor}. {transaksi}")


def jalankan_atm():
    nasabah = {
        "pin": "123456",
        "saldo": 1500000
    }
    riwayat_mutasi = []

    if not verif_pin(nasabah):
        return

    while True:
        print("\n----------------------------------------")
        print("MENU TRANSAKSI:")
        print("[1] Cek Saldo")
        print("[2] Setor Tunai")
        print("[3] Tarik Tunai")
        print("[4] Riwayat Mutasi")
        print("[5] Keluar")
        print("----------------------------------------")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            cek_saldo(nasabah)
        elif pilihan == "2":
            setor_tunai(nasabah, riwayat_mutasi)
        elif pilihan == "3":
            tarik_tunai(nasabah, riwayat_mutasi)
        elif pilihan == "4":
            tampilkan_mutasi(riwayat_mutasi)
        elif pilihan == "5":
            print("\nTerima kasih telah menggunakan layanan BANK PYTHON ATM.")
            break
        else:
            print("\nPilihan tidak valid. Silakan pilih angka 1 sampai 5.")


if __name__ == "__main__":
    jalankan_atm()