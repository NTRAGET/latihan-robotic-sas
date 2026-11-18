
nasabah = {"pin": "123456", "saldo": 1500000}


mutasi = []


def cek_saldo():
  print(f"\nSaldo Anda saat ini: Rp {nasabah['saldo']}")


def setor_tunai():
  nominal = input("\nMasukkan nominal setor tunai: Rp ")
  if nominal.isdigit():
    jumlah = int(nominal)
    if jumlah > 0:
      nasabah["saldo"] = nasabah["saldo"] + jumlah
      mutasi.append(f"Setor Tunai: +Rp {jumlah}")
      print(f"Setor tunai berhasil! Saldo baru: Rp {nasabah['saldo']}")
    else:
      print("Nominal harus lebih dari 0.")
  else:
    print("Input tidak valid, masukkan angka saja.")


def tarik_tunai():
  nominal = input("\nMasukkan nominal tarik tunai: Rp ")
  if nominal.isdigit():
    jumlah = int(nominal)
    if jumlah <= 0:
      print("Nominal harus lebih dari 0.")
    elif jumlah > nasabah["saldo"]:
      print("Maaf, saldo Anda tidak mencukupi.")
    else:
      nasabah["saldo"] = nasabah["saldo"] - jumlah
      mutasi.append(f"Tarik Tunai: -Rp {jumlah}")
      print(f"Tarik tunai berhasil! Sisa saldo: Rp {nasabah['saldo']}")
  else:
    print("Input tidak valid, masukkan angka saja.")


def riwayat_mutasi():
  print("\n--- Riwayat Mutasi ---")
  if len(mutasi) == 0:
    print("Belum ada transaksi.")
  else:
    for item in mutasi:
      print("-", item)


print("=== SELAMAT DATANG DI BANK SAS ===")

percobaan = 0
login_berhasil = False

while percobaan < 3:
  pin_input = input("Masukkan PIN Anda: ")
  if pin_input == nasabah["pin"]:
    login_berhasil = True
    print("Login berhasil!")
    break
  else:
    percobaan = percobaan + 1
    print(f"PIN salah! Sisa percobaan: {3 - percobaan}")

if not login_berhasil:
  print("Akun terblokir karena 3 kali salah memasukkan PIN.")
else:

  while True:
    print("\n=== MENU BANK SAS ATM ===")
    print("[1] Cek Saldo")
    print("[2] Setor Tunai")
    print("[3] Tarik Tunai")
    print("[4] Riwayat Mutasi")
    print("[5] Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
      cek_saldo()
    elif pilihan == "2":
      setor_tunai()
    elif pilihan == "3":
      tarik_tunai()
    elif pilihan == "4":
      riwayat_mutasi()
    elif pilihan == "5":
      print("Terima kasih telah menggunakan layanan BANK SAS.")
      break
    else:
      print("Pilihan tidak valid, silakan coba lagi.")