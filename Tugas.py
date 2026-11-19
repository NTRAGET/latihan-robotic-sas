data_nasabah = {
        "3011": {
        "nama"  : "Althaf Raisil S",
        "saldo" : 1500000,
        "mutasi": []
    }
}
def format_rp(nominal):
    return "Rp " + f"{nominal:,}".replace(",", ".")
 
def tampilkan_header():
    print("BANK HIHU")
 
def verifikasi_pin():
    tampilkan_header()
    print("Silakan masukkan PIN Anda.\n")
 
    percobaan = 0
    berhasil  = False
 
    while percobaan < 3 and berhasil == False:
        pin        = input("PIN Anda: ")
        percobaan += 1
        if pin in data_nasabah:
            berhasil  = True
            rekening  = data_nasabah[pin]
            print("\n  Login berhasil! Halo, " + rekening["nama"] + "!\n")
        else:
            sisa = 3 - percobaan
            if sisa > 0:
                print("  PIN salah mas. Sisa percobaan: " + str(sisa))
            else:
                print("  Duh, kartu Anda diblokir karena salah memasukkan PIN lebih dari 3x.")
 
    if berhasil == True:
        return data_nasabah[pin]
    else:
        return None
 
def cek_saldo(rekening):
    print("  Cek Saldo")
    print("  Nama   : " + rekening["nama"])
    print(f"  Saldo  : {format_rp(rekening['saldo'])}")
 
def setor_tunai(rekening):
    print("  Setor Tunai")
    nominal = int(input("  Jumlah setor (Rp): "))
    if nominal > 0:
        rekening["saldo"] += nominal
        catatan = "[+] Setor Tunai : " + format_rp(nominal)
        rekening["mutasi"].append(catatan)
        print("  HIHU! Setor tunai berhasil")
        print(f"  Saldo sekarang : {format_rp(rekening['saldo'])}")
    else:
        print("   Nominal harus lebih dari 0.")
 
def tarik_tunai(rekening):
    print("  Tarik Tunai")
    print("  Saldo tersisa : " + format_rp(rekening["saldo"]))
    nominal = int(input("  Jumlah tarik  (Rp): "))
    if nominal <= 0:
        print("  Nominal harus lebih dari 0.")
    elif nominal > rekening["saldo"]:
        print("  Duh, saldo Anda tidak cukup")
        print("  Saldo Anda tersisa: " + format_rp(rekening["saldo"]))
    else:
        rekening["saldo"] -= nominal
        catatan = "[-] Tarik Tunai : " + format_rp(nominal)
        rekening["mutasi"].append(catatan)
        print("  HIHU! Penarikan berhasil")
        print(f"  Saldo sekarang : {format_rp(rekening['saldo'])}")
 
def riwayat_mutasi(rekening):
    print("  Riwayat Mutasi")
 
    if len(rekening["mutasi"]) == 0:
        print("  Belum ada transaksi sir.")
    else:
        for index, catatan in enumerate(rekening["mutasi"]):
            print("  " + str(index + 1) + ". " + catatan)
 
    print(f"\n  Saldo akhir : {format_rp(rekening['saldo'])}")
 
def menu_utama(rekening):
    aktif = True
    while aktif == True:
        print("BANK HIHU — BANK KEMARIN SORE")
        print("  Nasabah : " + rekening["nama"])
        print(f"  Saldo   : {format_rp(rekening['saldo'])}")
        print("  1. Cek Saldo")
        print("  2. Setor Tunai")
        print("  3. Tarik Tunai")
        print("  4. Riwayat Mutasi")
        print("  5. Keluar")
        pilihan = input("  Pilih menu : ")
        if pilihan == "1":
            cek_saldo(rekening)
        elif pilihan == "2":
            setor_tunai(rekening)
        elif pilihan == "3":
            tarik_tunai(rekening)
        elif pilihan == "4":
            riwayat_mutasi(rekening)
        elif pilihan == "5":
            aktif = False
            print("\nHIHU! sampai jumpa lagi sir!")
        else:
            print("   Pilihan tidak valid sir. Masukkan angka 1-5.")
rekening_aktif = verifikasi_pin()
if rekening_aktif != None:
    menu_utama(rekening_aktif)