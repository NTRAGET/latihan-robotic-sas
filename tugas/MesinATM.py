print("Selamat Datang di Mesin ATM Bank Ku")

#Data
nasabah = {
    "nama": "Atika",
    "pin": "2987",
    "saldo": 1500000
}
riwayat = []
tampilan_menu = ["1.Cek Saldo", "2.Setor Tunai", "3.Tarik Tunai", "4.Riwayat Transaksi", "5.Keluar"]


#login
percobaan = 0
login = False

while percobaan < 3:
    pin_input = input("Masukan PIN: ")

    if pin_input == nasabah["pin"]:
        login = True
        print("Login berhasil!")
        print("Selamat datang,", nasabah["nama"])
        break

    percobaan += 1
    print("PIN salah!")

    if percobaan < 3:
        print("Sisa percobaan:", 3 - percobaan)
    else:
        print("Kesempatan habis. Kartu diblokir.")

#tampilan menu
if login:
    while True:
        print("Tampilan Menu:")
        for item in tampilan_menu:
            print(item)

        pilihan = int(input("Masukan Pilihan Menu: "))
        # 1. Cek Saldo
        if pilihan == 1:
            print("Anda memilih menu Cek Saldo")
            print("Saldo rekening Anda: Rp.", nasabah["saldo"])

        # 2. Setor Tunai
        elif pilihan == 2:
            print("Anda memilih menu Setor Tunai")
            setor = int(input("Masukan jumlah setor tunai: Rp."))
            nasabah["saldo"] += setor
            riwayat.append(["Setor Tunai", setor, nasabah["saldo"]])
            print("Setor tunai berhasil!")
            print("Saldo rekening Anda: Rp.", nasabah["saldo"])

        # 3. Tarik Tunai
        elif pilihan == 3:
            tarik = int(input("Masukan jumlah tarik tunai: Rp."))
            if tarik <= nasabah["saldo"]:
                nasabah["saldo"] -= tarik
                riwayat.append(["Tarik Tunai", tarik, nasabah["saldo"]])
                print("Penarikan berhasil! Silakan ambil uang Anda.")
                print("Saldo rekening Anda: Rp.", nasabah["saldo"])
            else:
                print ("Saldo Kurang!!!")


        # 4. Riwayat Transaksi
        elif pilihan == 4:
            print("Anda memilih menu Riwayat Transaksi")
            if len(riwayat) == 0:
                print("Belum ada transaksi.")
            else:
                for jenis, jumlah, sisa in riwayat:
                    print("Jenis      :", jenis)
                    print("Jumlah     :Rp.", jumlah)
                    print("Sisa saldo: Rp.", sisa)

        # 5. Keluar
        elif pilihan == 5:
            print("Anda memilih menu Keluar")
            print("Terima kasih telah menggunakan ATM Bank Ku!")
            break

        else:
            print("Pilihan tidak valid")