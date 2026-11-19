NAMA_BANK = "BANK SUMBER MAKMUR"
MAKS_PERCOBAAN = 3

nasabah = {
    "nama": "Agus",
    "pin": "123456",
    "saldo": 1500000
}

mutasi = []


def format_rupiah(nominal):
    return "Rp " + f"{nominal:,}".replace(",", ".")


def catat_mutasi(jenis, nominal):
    mutasi.append({
        "jenis": jenis,
        "nominal": nominal,
        "saldo_akhir": nasabah["saldo"]
    })


def input_nominal(pesan):
    teks = input(pesan).strip()
    if not teks.isdigit():
        print("Nominal tidak valid. Masukkan angka bulat positif.")
        return None
    nominal = int(teks)
    if nominal <= 0:
        print("Nominal harus lebih dari 0.")
        return None
    return nominal


def verifikasi_pin():
    for percobaan in range(1, MAKS_PERCOBAAN + 1):
        pin = input(f"Masukkan PIN ({percobaan}/{MAKS_PERCOBAAN}): ").strip()
        if pin == nasabah["pin"]:
            print(f"\nLogin berhasil. Selamat datang, {nasabah['nama']}!")
            return True
        print("PIN salah.")
    print("Kartu diblokir sementara karena 3 kali salah PIN.")
    return False


def cek_saldo():
    print(f"\nSaldo rekening Anda: {format_rupiah(nasabah['saldo'])}")


def setor_tunai():
    nominal = input_nominal("Nominal setor: Rp ")
    if nominal is None:
        return
    nasabah["saldo"] += nominal
    catat_mutasi("Setor", nominal)
    print(f"Setor tunai {format_rupiah(nominal)} berhasil.")
    print(f"Saldo sekarang: {format_rupiah(nasabah['saldo'])}")


def tarik_tunai():
    nominal = input_nominal("Nominal tarik: Rp ")
    if nominal is None:
        return
    if nominal > nasabah["saldo"]:
        print("Saldo tidak mencukupi.")
        return
    nasabah["saldo"] -= nominal
    catat_mutasi("Tarik", nominal)
    print(f"Tarik tunai {format_rupiah(nominal)} berhasil.")
    print(f"Saldo sekarang: {format_rupiah(nasabah['saldo'])}")


def riwayat_mutasi():
    print("\n=== RIWAYAT MUTASI ===")
    if not mutasi:
        print("Belum ada transaksi.")
        return
    for nomor, item in enumerate(mutasi, start=1):
        print(f"{nomor}. {item['jenis']:<6} {format_rupiah(item['nominal']):>16} | Saldo: {format_rupiah(item['saldo_akhir'])}")


def tampilkan_menu():
    print(f"\n===== {NAMA_BANK} =====")
    print("[1] Cek Saldo")
    print("[2] Setor Tunai")
    print("[3] Tarik Tunai")
    print("[4] Riwayat Mutasi")
    print("[0] Keluar")


def menu_utama():
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
            print(f"\nTerima kasih telah menggunakan {NAMA_BANK}.")
            break
        else:
            print("Pilihan tidak tersedia.")


def main():
    print(f"Selamat datang di {NAMA_BANK}")
    if verifikasi_pin():
        menu_utama()


if __name__ == "__main__":
    main()
