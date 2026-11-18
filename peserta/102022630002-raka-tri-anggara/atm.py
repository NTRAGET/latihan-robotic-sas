NAMA_BANK = "ATM BANK RAKA X BANK TOYYIB"
MAKS_PERCOBAAN = 3

nasabah = {
    "pin": "123456",
    "saldo": 1500000,
}

mutasi = []

def format_rupiah(nominal):
    return "Rp " + f"{nominal:,}".replace(",", ".")

def baca_nominal(pesan):
    teks = input(pesan).strip()
    if not teks.isdigit():
        print("Nominal harus berupa angka bulat positif.")
        return None
    nominal = int(teks)
    if nominal <= 0:
        print("Nominal harus lebih dari 0.")
        return None
    return nominal

def verifikasi_pin():
    for percobaan in range(1, MAKS_PERCOBAAN + 1):
        pin = input("Masukkan PIN: ").strip()
        if pin == nasabah["pin"]:
            print("Login berhasil.")
            return True
        sisa = MAKS_PERCOBAAN - percobaan
        if sisa > 0:
            print(f"PIN salah. Sisa percobaan: {sisa}")
    print("Kartu diblokir karena 3 kali salah memasukkan PIN.")
    return False

def cek_saldo():
    print(f"Saldo rekening Anda: {format_rupiah(nasabah['saldo'])}")

def setor_tunai():
    nominal = baca_nominal("Nominal setor: Rp ")
    if nominal is None:
        return
    nasabah["saldo"] += nominal
    mutasi.append(f"Setor  + {format_rupiah(nominal)}")
    print(f"Setor berhasil. Saldo sekarang: {format_rupiah(nasabah['saldo'])}")

def tarik_tunai():
    nominal = baca_nominal("Nominal tarik: Rp ")
    if nominal is None:
        return
    if nominal > nasabah["saldo"]:
        print("Saldo tidak mencukupi.")
        return
    nasabah["saldo"] -= nominal
    mutasi.append(f"Tarik  - {format_rupiah(nominal)}")
    print(f"Tarik berhasil. Saldo sekarang: {format_rupiah(nasabah['saldo'])}")

def riwayat_mutasi():
    if not mutasi:
        print("Belum ada transaksi.")
        return
    print("--- Riwayat Mutasi ---")
    for nomor, catatan in enumerate(mutasi, start=1):
        print(f"{nomor}. {catatan}")

def tampilkan_menu():
    print()
    print("=" * 30)
    print(f" {NAMA_BANK}")
    print("=" * 30)
    print("[1] Cek Saldo")
    print("[2] Setor Tunai")
    print("[3] Tarik Tunai")
    print("[4] Riwayat Mutasi")
    print("[0] Keluar")

def main():
    print(f"Selamat datang di {NAMA_BANK}")
    if not verifikasi_pin():
        return
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            cek_saldo()
        elif pilihan == "2":
            setor_tunai()
        elif pilihan == "3":
            tarik_tunai()
        elif pilihan == "4":
            riwayat_mutasi()
        elif pilihan == "0":
            print("Terima kasih telah menggunakan layanan kami.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")


if __name__ == "__main__":
    main()