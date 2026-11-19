data_nasabah = {
    "pin" : "1234",
    "nama" : "Andityo Wisnu Nugroho",
    "saldo" : 5000000
}

data_mutasi = []

def login():
    for i in range(3):  # Validasi login maks 3 kali
        input_pin = input("Masukkan PIN Anda: ")
        if input_pin == data_nasabah["pin"]:
            print("PIN benar. Selamat datang!")
            return True
        else:
            print("PIN salah. Silakan coba lagi.")
    print("Anda sudah mencoba 3 kali. Akses ditolak.")
    return False

def cek_saldo():
    print(f"Saldo Anda saat ini: Rp {data_nasabah['saldo']}")
    print("\n")

def tarik_tunai():
    jumlah_tarik = int(input("Masukkan jumlah yang ingin ditarik: "))
    if jumlah_tarik < 0:
        print("Jumlah penarikan tidak valid.")
    elif jumlah_tarik <= data_nasabah["saldo"]:
        data_nasabah["saldo"] -= jumlah_tarik
        data_mutasi.append(("Tarik Tunai ", jumlah_tarik))  
        print(f"Penarikan berhasil. Saldo baru Anda: Rp {data_nasabah['saldo']}")
        print("\n")
    else:
        print("Saldo tidak mencukupi.")

def setor_tunai():
    jumlah_setor = int(input("Masukkan jumlah yang ingin disetor: "))
    if jumlah_setor < 0:
        print("Jumlah setoran tidak valid.")
    else:
        data_nasabah["saldo"] += jumlah_setor
        print(f"Setoran berhasil. Sisa saldo Anda: Rp {data_nasabah['saldo']}")
        data_mutasi.append(("Setor Tunai ", jumlah_setor))
        print("\n")

def cek_mutasi():
    if data_mutasi:
        print("Mutasi Transaksi:")
        for transaksi in data_mutasi:
            print(f"{transaksi[0]}: Rp {transaksi[-1]}")
    else:
        print("Belum ada transaksi.")

def main():
    print("========================")
    print("    ATM BANK TOYYIB     ")
    print("========================\n")

    if login():
        print(f"Selamat datang, {data_nasabah['nama']}!")
        print("1. Cek Saldo")
        print("2. Tarik Tunai")
        print("3. Setor Tunai")
        print("4. Cek Mutasi")
        print("5. Keluar\n")
        pilih_menu = input("Pilih menu (1-5): ")
        if pilih_menu == "1":
            cek_saldo()
            kembali = input("Apakah Anda ingin kembali ke menu utama? (y/n): ")
            if kembali.lower() == "y":
                main()
            else:
                print("Terima kasih telah menggunakan layanan ATM BANK TOYYIB.")
        elif pilih_menu == "2":
            tarik_tunai()
            kembali = input("Apakah Anda ingin kembali ke menu utama? (y/n): ") 
            if kembali.lower() == "y":
                main()
            else:
                print("Terima kasih telah menggunakan layanan ATM BANK TOYYIB.")
        elif pilih_menu == "3":
            setor_tunai()
            kembali = input("Apakah Anda ingin kembali ke menu utama? (y/n): ")
            if kembali.lower() == "y":
                main()
            else:
                print("Terima kasih telah menggunakan layanan ATM BANK TOYYIB.")
        elif pilih_menu == "4":
            cek_mutasi()
            kembali = input("Apakah Anda ingin kembali ke menu utama? (y/n): ")
            if kembali.lower() == "y":
                main()
            else:
                print("Terima kasih telah menggunakan layanan ATM BANK TOYYIB.")
        elif pilih_menu == "5":
            print("Terima kasih telah menggunakan layanan ATM BANK TOYYIB.")
        else:
            print("Pilihan tidak valid.")

main()