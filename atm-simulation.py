
data_nasabah = {
    "123456": {
        "nama": "Budi Santoso",
        "pin": 1111,
        "saldo": 1500000,
        "mutasi": []
    },
    "654321": {
        "nama": "Siti Aminah",
        "pin": 2222,
        "saldo": 500000,
        "mutasi": []
    }
}

def cetak_header(judul):
    print("\n" + "="*35)
    print(f"   {judul}")
    print("="*35)

def cek_saldo(rekening):
    cetak_header("INFORMASI SALDO")
    nama = data_nasabah[rekening]["nama"]
    saldo = data_nasabah[rekening]["saldo"]
    print(f"Nama Pemilik : {nama}")
    print(f"Total Saldo  : Rp {saldo:,}")

def setor_tunai(rekening):
    cetak_header("SETOR TUNAI")
    try:
        nominal = int(input("Masukkan nominal setor (Rp): "))
        if nominal <= 0:
            print("Gagal: Nominal harus lebih dari 0.")
        else:
            data_nasabah[rekening]["saldo"] += nominal
            
            transaksi = ("Setor Tunai", nominal)
            data_nasabah[rekening]["mutasi"].append(transaksi)
            
            print(f"Setor berhasil! Saldo saat ini: Rp {data_nasabah[rekening]['saldo']:,}")
    except ValueError:
        print("Error: Input harus berupa angka!")

def tarik_tunai(rekening):
    cetak_header("TARIK TUNAI")
    try:
        nominal = int(input("Masukkan nominal tarik (Rp): "))
        saldo_sekarang = data_nasabah[rekening]["saldo"]
        
        if nominal <= 0:
            print("Gagal: Nominal harus lebih dari 0.")
        elif nominal > saldo_sekarang:
            print("Gagal: Saldo tidak mencukupi!")
        else:
            data_nasabah[rekening]["saldo"] -= nominal
            transaksi = ("Tarik Tunai", nominal)
            data_nasabah[rekening]["mutasi"].append(transaksi)
            print(f"Tarik berhasil! Saldo saat ini: Rp {data_nasabah[rekening]['saldo']:,}")
    except ValueError:
        print("Error: Input harus berupa angka!")

def lihat_mutasi(rekening):
    cetak_header("RIWAYAT MUTASI")
    riwayat = data_nasabah[rekening]["mutasi"]
    
    if not riwayat:
        print("Belum ada riwayat transaksi.")
    else:
        for i, trx in enumerate(riwayat):
            jenis = trx[0]
            nominal = trx[1]
            print(f"{i+1}. {jenis} : Rp {nominal:,}")

def menu_transaksi(rekening):
    while True:
        cetak_header(f"MENU ATM - {data_nasabah[rekening]['nama']}")
        print("1. Cek Saldo")
        print("2. Setor Tunai")
        print("3. Tarik Tunai")
        print("4. Lihat Mutasi")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            cek_saldo(rekening)
        elif pilihan == '2':
            setor_tunai(rekening)
        elif pilihan == '3':
            tarik_tunai(rekening)
        elif pilihan == '4':
            lihat_mutasi(rekening)
        elif pilihan == '5':
            print("Terima kasih, jangan lupa bawa kartu ATM Anda.")
            break
        else:
            print("Pilihan tidak valid!")


def mulai_atm():
    cetak_header("SELAMAT DATANG DI MINI ATM CIHUY")
    
    while True:
        no_rek = input("Masukkan Nomor Rekening (ketik 'batal' untuk keluar): ")
        
        if no_rek.lower() == 'batal':
            print("Sesi diakhiri.")
            break
            
        if no_rek in data_nasabah:
            percobaan = 0
            
            while percobaan < 3:
                try:
                    pin_input = int(input("Masukkan PIN (4 Angka): "))
                    
                    if pin_input == data_nasabah[no_rek]["pin"]:
                        print("Login Berhasil!")
                        menu_transaksi(no_rek) 
                        break
                    else:
                        percobaan += 1
                        sisa = 3 - percobaan
                        if sisa > 0:
                            print(f"PIN Salah! Sisa percobaan: {sisa}x")
                        else:
                            print("Kartu Anda terblokir karena salah PIN 3x. Silakan hubungi bank.")
                except ValueError:
                    print("PIN harus berupa angka!")
        else:
            print("Nomor rekening tidak terdaftar di sistem.")


if __name__ == "__main__":
    mulai_atm()