#Dictionary data nasabah
data_nasabah = {
    "pin": "310707",
    "saldo": 969000
}

riwayat_mutasi = []

def verifikasi_pin():
    kesempatan = 3
    while kesempatan > 0:
        input_pin = input("Masukkan PIN Anda: ")
        if input_pin == data_nasabah["pin"]:
            print("\n V Login Berhasil! Selamat datang di AKY BANG.")
            return True
        else:
            kesempatan -= 1
            print(f" X PIN salah! Sisa kesempatan: {kesempatan}")
            
    print("\nAkun telah diblokir karna salah masukkin PIN 3 kali :(")
    

def cek_saldo():
    print("\n   [CEK SALDO]   ")
    print(f"Saldo Anda: Rp{data_nasabah['saldo']}")

def setor_tunai():
    print("\n   [SETOR TUNAI]   ")
    jumlah = int(input("Masukkan jumlah setor tunai (Rp): "))
    if jumlah > 0:
        data_nasabah["saldo"] += jumlah
        print(f"Berhasil setor tunai sebesar Rp {jumlah}")
        riwayat_mutasi.append(f"Setor Tunai: +Rp {jumlah}")
        cek_saldo()
    else:
        print("Masukan jumlah yang benar!")

def tarik_tunai():
    print("\n   [TARIK TUNAI]   ")
    jumlah = int(input("Masukkan jumlah tarik tunai (Rp): "))
    
    if jumlah > 0:
        if jumlah <= data_nasabah["saldo"]:
            data_nasabah["saldo"] -= jumlah
            catatan = f"Tarik Tunai: -Rp {jumlah}"
            riwayat_mutasi.append(catatan)
            print(f"Berhasil tarik tunai sebesar Rp {jumlah}")
            cek_saldo()
        else:
            print("Saldo tidak mencukupi !")
    else:
        print("Masukan jumlah yang benar!")

def tampilkan_mutasi():
    print("\n   [RIWAYAT MUTASI]   ")
    if len(riwayat_mutasi) == 0:
        print("Belum ada transaksi saat ini.")
    else:
        print("\n".join(riwayat_mutasi))

print(">========================================<")
print("          STATUS: AKTIF - AKY BANG        ")
print(">========================================<")

#manggil peripikasi dulu kalo betul lanjut ke menu
if verifikasi_pin():
    
    while True:
        print("\n<========================================>")
        print("            MENU ATM                ")
        print("<========================================>")
        print("[1] Cek Saldo")
        print("[2] Setor Tunai")
        print("[3] Tarik Tunai")
        print("[4] Riwayat Mutasi")
        print("[5] Keluar")
        
        pilihan = input("Silakan pilih menu (1-5): ")
        
        if pilihan == '1':
            cek_saldo()
        elif pilihan == '2':
            setor_tunai()
        elif pilihan == '3':
            tarik_tunai()
        elif pilihan == '4':
            tampilkan_mutasi()
        elif pilihan == '5':
            print("\nTerima kasih telah menggunakan AKY BANG.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu 1 hingga 5.")
