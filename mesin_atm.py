nasabah = {
    "sawit_nasional": 1000000,
    "19jutapekerjaan": 19000000,
    "a":100000
}

jumlah_coba = 0
mutasi = []


def cek_saldo(p):
  return f"Saldo Anda Tersisa : Rp {nasabah[p]:,}"


def setor_saldo(p):
  nominal = int(input("Masukan Nominal Setor : "))
  if nominal > 0:
    nasabah[p] += nominal
    mutasi.append(f"Setor Tunai sebesar Rp {nominal:,}")
    print(f"Saldo disetor sebesar : Rp {nominal:,}")
    print(f"Saldo Anda : Rp {nasabah[p]:,}")
  else:
    print("Nominal setor harus lebih dari 0!")


def tarik_saldo(p):
  nominal = int(input("Masukan Nominal Tarik : "))
  if nominal <= 0:
    print("Nominal tarik harus lebih dari 0!")
  elif nominal > nasabah[p]:
    print("Maaf, saldo Anda tidak mencukupi!")
  else:
    nasabah[p] -= nominal
    mutasi.append(f"Tarik Tunai sebesar Rp {nominal:,}")
    print(f"Saldo ditarik sebesar : Rp {nominal:,}")
    print(f"Saldo Anda : Rp {nasabah[p]:,}")


def riwayat_mutasi():
  print("=== Riwayat Mutasi ===")
  if len(mutasi) == 0:
    print("Belum ada riwayat transaksi.")
  else:
    for index, i in enumerate(mutasi):
      print(f"{index + 1}. {i}")


while True:
  print("\n=== Selamat Datang di Bank Eiro ===")
  nama = input("Masukan Nama Anda : ")
  print(f"Selamat datang {nama}")
  pwd = input("Silahkan Masukan Password Anda : ")

  if pwd in nasabah:
    jumlah_coba = 0 
    while True:
      print("\n=== Menu ===")
      print("1. Cek Saldo")
      print("2. Setor Saldo")
      print("3. Tarik Saldo")
      print("4. Riwayat Mutasi")
      print("5. Keluar")

      menu = int(input("Pilih Menu [1/2/3/4/5] : "))

      if menu == 1:
        print(cek_saldo(pwd))
      elif menu == 2:
        setor_saldo(pwd)
      elif menu == 3:
        tarik_saldo(pwd)
      elif menu == 4:
        riwayat_mutasi()
      elif menu == 5:
        print("Terima kasih telah menggunakan Bank Eiro!")
        break
      else:
        print("Pilih Menu Dengan Benar !!")
  else:
    print("PIN salah Silahkan Coba Lagi !!")
    jumlah_coba += 1
    if jumlah_coba == 3:
      print("Telah Mencapai Batas 3x !!")
      break