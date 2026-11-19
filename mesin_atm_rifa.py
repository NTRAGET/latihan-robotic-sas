#Tugas akhir: mesin atm (simulasi transaksi perbankan berbasis terminal dengan Python)

data_nasabah = {
    "pin": "123456",
    "saldo": 1000000
}

riwayat_transaksi = []


def cek_saldo(nasabah):
    print(f"Saldo Anda saat ini: Rp{nasabah['saldo']:,}")


def setor_tunai(nasabah, riwayat):
    nominal_input = input("Masukkan nominal setor tunai: Rp")
    if not nominal_input.isdigit():
        print("Input tidak valid! Masukkan angka bulat positif saja.")
    elif int(nominal_input) <= 0:
        print("Nominal setor harus lebih dari Rp0.")
    else:
        nominal = int(nominal_input)
        nasabah["saldo"] += nominal
        riwayat.append(f"Setor Tunai  : +Rp{nominal:,}")
        print(f"Setor tunai sebesar Rp{nominal:,} berhasil.")
        cek_saldo(nasabah)


def tarik_tunai(nasabah, riwayat):
    nominal_input = input("Masukkan nominal tarik tunai: Rp")
    if not nominal_input.isdigit():
        print("Input tidak valid! Masukkan angka bulat positif saja.")
    elif int(nominal_input) <= 0:
        print("Nominal penarikan harus lebih dari Rp0.")
    elif int(nominal_input) > nasabah["saldo"]:
        print("Transaksi gagal! Saldo Anda tidak mencukupi.")
    else:
        nominal = int(nominal_input)
        nasabah["saldo"] -= nominal
        riwayat.append(f"Tarik Tunai  : -Rp{nominal:,}")
        print(f"Tarik tunai sebesar Rp{nominal:,} berhasil.")
        cek_saldo(nasabah)


def mutasi_rekening(riwayat):
    print("===== RIWAYAT TRANSAKSI (MUTASI) =====")
    if len(riwayat) == 0:
        print("Belum ada transaksi pada sesi ini.")
    else:
        for nomor, transaksi in enumerate(riwayat, start=1):
            print(f"{nomor}. {transaksi}")


percobaan = 0
maks_percobaan = 3
sesi_aktif = False


print("===== SELAMAT DATANG DI ATM =====")
while percobaan < maks_percobaan and not sesi_aktif:
    pin_input = input("Masukkan PIN Anda: ")
    if pin_input == data_nasabah["pin"]:
        print("\nAutentikasi PIN berhasil!\n")
        sesi_aktif = True
    else:
        percobaan += 1
        sisa = maks_percobaan - percobaan
        if sisa > 0:
            print(f"PIN salah! Sisa kesempatan mencoba: {sisa} kali.\n")
        else:
            print("\nAnda telah salah memasukkan PIN 3 kali. Kartu diblokir.")


while sesi_aktif:
    print("======== MENU UTAMA ATM ========")
    print("1. Cek Saldo")
    print("2. Setor Tunai")
    print("3. Tarik Tunai")
    print("4. Mutasi Rekening")
    print("5. Keluar")
    print("================================")

    pilihan = input("Pilih layanan (1-5): ")
    print()

    if pilihan == "1":
        cek_saldo(data_nasabah)
    elif pilihan == "2":
        setor_tunai(data_nasabah, riwayat_transaksi)
    elif pilihan == "3":
        tarik_tunai(data_nasabah, riwayat_transaksi)
    elif pilihan == "4":
        mutasi_rekening(riwayat_transaksi)
    elif pilihan == "5":
        print("Terima kasih telah menggunakan ATM.")
        sesi_aktif = False
    else:
        print("Pilihan tidak tersedia. Silakan masukkan angka 1 hingga 5.")
    
    print()

