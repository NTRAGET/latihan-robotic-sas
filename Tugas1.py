Nama_Bank = "Bank SAS"

nasabah = {
    "nama": "Rasyhid Ridho",
    "pin": "225599",
    "saldo": 1500000,
    "mutasi": []
}

def input_nominal(pesan):
    teks = input(pesan)
    teks = teks.replace(",", "").replace(".", "")
    if teks.isdigit() == False:
        print("Input harus berupa angka!")
        return input_nominal(pesan)
    nominal = int(teks)
    if nominal <= 0:
        print("Nominal harus lebih dari 0!")
        return input_nominal(pesan)
    return nominal

def mutasi( jenis, nominal):
    transaksi = {
        "jenis": jenis,
        "nominal": nominal,
        "saldo akhir":nasabah["saldo"]
    }
    nasabah["mutasi"].append(transaksi)

def verifikasi_pin():
    for percobaan in range(3):
        pin = input("Masukkan PIN Anda: ")
        if pin == nasabah["pin"]:
            return True
        else:
            sisa = 2 -percobaan
            if sisa > 0:
                print(f"PIN salah! Anda memiliki {sisa} percobaan lagi.")
            else:
                print("Pin salah 3 kali loh ya, Akun diblokir")
                return False

def cek_saldo():
    print(f"Saldo Anda saat ini: Rp {nasabah['saldo']:,}")

def tarik_tunai():
    nominal = input_nominal("Masukkan nominal tarik tunai: Rp  ")
    if nominal > 0:
        if nominal <= nasabah["saldo"]:
            nasabah["saldo"] -= nominal
            mutasi("Tarik Tunai", nominal)
            print(f"Berhasil melakukan tarik tunai sebesar Rp {nominal:,}. Saldo Anda saat ini: Rp {nasabah['saldo']:,}")
        else:
            print("Saldo tidak mencukupi untuk melakukan tarik tunai.")

def setor_tunai():
    nominal = input_nominal("Masukkan nominal setor tunai: Rp  ")
    if nominal > 0:
        nasabah["saldo"] += nominal
        mutasi("Setor Tunai", nominal)
        print(f"Berhasil melakukan setor tunai sebesar Rp {nominal:,}. Saldo Anda saat ini: Rp {nasabah['saldo']:,}")

def lihat_mutasi():
    print("Riwayat Mutasi Transaksi:")
    if len(nasabah["mutasi"]) == 0:
        print("Belum ada transaksi yang dilakukan.")
    else:
        print("Mutasi Transaksi:")
        for transaksi in nasabah["mutasi"]:
            print(f"{transaksi['jenis']}: Rp {transaksi['nominal']:,} | Saldo Akhir: Rp {transaksi['saldo akhir']:,}")

def tampilkan_menu():
    print(f"Selamat datang di {Nama_Bank}!")
    print("1. Cek Saldo")
    print("2. Tarik Tunai")
    print("3. Setor Tunai")
    print("4. Lihat Mutasi Transaksi")
    print("0. Keluar")

def main():
        while True:
            tampilkan_menu()
            pilihan = input("Pilih menu (1-4) atau 0 untuk keluar: ")
            if pilihan == "1":
                cek_saldo()
            elif pilihan == "2":
                tarik_tunai()
            elif pilihan == "3":
                setor_tunai()
            elif pilihan == "4":
                lihat_mutasi()
            elif pilihan == "0":
                print("Terima kasih telah menggunakan layanan kami.")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

print("Selamat datang di Bank SAS!")
if verifikasi_pin():   
    main()
