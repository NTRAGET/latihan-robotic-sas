nasabah = {
    "nama": "Athaya",
    "pin": "123456",
    "saldo": 1500000
}
riwayat = []
def cek_saldo():
    print("\n========== CEK SALDO ==========")
    print("Nama Nasabah :", nasabah["nama"])
    print("Saldo Anda   : Rp", format(nasabah["saldo"], ","))
    print("===============================")
def setor_tunai():
    print("\n========== SETOR TUNAI ==========")

    jumlah = int(input("Masukkan jumlah uang: Rp "))

    if jumlah <= 0:
        print("Jumlah setor harus lebih dari 0!")
    else:
        nasabah["saldo"] += jumlah
        riwayat.append(
            "Setor tunai: Rp " + format(jumlah, ",")
        )
        print("Setor tunai berhasil!")
        print("Saldo sekarang: Rp", format(nasabah["saldo"], ","))

def tarik_tunai():
    print("\n========== TARIK TUNAI ==========")

    jumlah = int(input("Masukkan jumlah uang: Rp "))

    if jumlah <= 0:
        print("Jumlah penarikan harus lebih dari 0!")

    elif jumlah > nasabah["saldo"]:
        print("Maaf, Anda Miskinnn !")

    else:
        nasabah["saldo"] -= jumlah

        riwayat.append(
            "Tarik tunai: Rp " + format(jumlah, ",")
        )

        print("Penarikan berhasil!")
        print("Saldo sekarang: Rp", format(nasabah["saldo"], ","))

def riwayat_transaksi():
    print("\n========== RIWAYAT TRANSAKSI ==========")

    if len(riwayat) == 0:
        print("Belum ada transaksi.")

    else:
        for i, transaksi in enumerate(riwayat, start=1):
            print(i, ".", transaksi)

    print("=======================================")

def ubah_pin():
    print("\n========== UBAH PIN ==========")

    pin_lama = input("Masukkan PIN lama: ")

    if pin_lama == nasabah["pin"]:

        pin_baru = input("Masukkan PIN baru (6 digit): ")

        if len(pin_baru) == 6 and pin_baru.isdigit():
            nasabah["pin"] = pin_baru
            riwayat.append("Perubahan PIN berhasil")

            print("PIN berhasil diubah!")

        else:
            print("PIN harus terdiri dari 6 angka!")

    else:
        print("PIN lama salah!")
def menu_utama():

    while True:
        print("\n================================")
        print("       BANK AMBA ATM")
        print("================================")
        print("1. Cek Saldo")
        print("2. Setor Tunai")
        print("3. Tarik Tunai")
        print("4. Riwayat Transaksi")
        print("5. Ubah PIN")
        print("6. Keluar")
        print("================================")
        pilihan = input("Pilih menu (1-6): ")
        if pilihan == "1":
            cek_saldo()
        elif pilihan == "2":
            setor_tunai()
        elif pilihan == "3":
            tarik_tunai()
        elif pilihan == "4":
            riwayat_transaksi()
        elif pilihan == "5":
            ubah_pin()
        elif pilihan == "6":
            print("\nTerima kasih telah menggunakan")
            print("BANK AMBA ATM")
            print("Silakan ambil kartu Anda.")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")
print("================================")
print("       SELAMAT DATANG")
print("        BANK AMBA")
print("================================")

kesempatan = 3

while kesempatan > 0:

    pin_input = input("Masukkan PIN ATM: ")

    if pin_input == nasabah["pin"]:

        print("\nLogin berhasil!")
        print("Selamat datang Broo,", nasabah["nama"])

        menu_utama()
        break

    else:
        kesempatan -= 1

        print("PIN salah!")
        print("Sisa kesempatan:", kesempatan)

if kesempatan == 0:
    print("\nKartu diblokir sementara!")
    print("Anda telah salah memasukkan PIN 3 kali Loh Yaaa.")