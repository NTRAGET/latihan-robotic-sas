from abc import ABC, abstractmethod

class Robot (ABC):
    jumlah_robot = 0

    def __init__(self, nama, baterai = 100):
        self.nama = nama
        self.__baterai = 0
        self.set_baterai(baterai)

        Robot.jumlah_robot += 1

    def get_baterai(self):
        return self.__baterai

    def set_baterai (self, nilai):
        if Robot.validasi_baterai (nilai):
            self.__baterai = nilai
        else:
            print(f"Nilai {nilai} tidak valid (harus 0-100)")

    def kurangi_baterai(self, jumlah):
        self.__baterai = max(0, self.__baterai - jumlah)

    def isi_daya(self, jumlah):
        self.__baterai = min(100, self.__baterai + jumlah)
        print(f"{self.nama} sedang diisi daya, baterai sekarang {self.__baterai} %")

    def cek_baterai_cukup(self, kebutuhan):
        if self.__baterai < kebutuhan:
            print(f"{self.nama} baterai tidak cukup ({self.__baterai}%), butuh {kebutuhan}")
            return False
        return True

    @staticmethod
    def validasi_baterai(nilai):
        return isinstance(nilai, (int, float)) and 0 <= nilai <= 100

    @classmethod
    def total_robot(cls):
        return cls.jumlah_robot

    @abstractmethod
    def mulai_bekerja(self):
        pass

    def __add__(self, other):
        if isinstance(other, Robot):
            return TimRobot([self, other])
        return NotImplemented
    
    def __str__(self):
        return f"[{self.__class__.__name__}] {self.nama} | Baterai: {self.__baterai}%"

class RobotPembersih(Robot):
    def __init__(self, nama, baterai=100, area="Ruang Tamu"):
        super().__init__(nama, baterai)
        self.area = area

    def mulai_bekerja(self):
        if self.cek_baterai_cukup(10):
            print(f"{self.nama} membersihkan lantai di area {self.area}.")
            self.kurangi_baterai(10)

class RobotPengantar(Robot):
    def __init__(self, nama, baterai=100, tujuan = "input_tujuan"):
        super().__init__(nama, baterai)
        self.tujuan = tujuan

    def mulai_bekerja(self):
        if self.cek_baterai_cukup(15):
            print(f"{self.nama} mengantarkan pesanan ke {self.tujuan}")
            self.kurangi_baterai(15)

class RobotKeamanan(Robot):
    def __init__(self, nama, baterai=100, lokasi = "Gerbang utama"):
        super().__init__(nama, baterai)
        self.lokasi = lokasi

    def mulai_bekerja(self):
        if self.cek_baterai_cukup(20):
            print(f"{self.nama} menjaga di area {self.lokasi}")
            self.kurangi_baterai(20)

class TimRobot:
    def __init__(self, anggota):
        self.anggota = list(anggota)

    def __add__(self, other):
        if isinstance(other, Robot):
            return TimRobot(self.anggota + [other])
        if isinstance(other, TimRobot):
            return TimRobot(self.anggota + other.anggota)
        return NotImplemented

    def __len__(self):
        return len(self.anggota)

    def __str__(self):
        daftar =", ".join(r.nama for r in self.anggota)
        return f"TimRobot ({len(self)} anggota): {daftar}"

    def mulai_kerja(self):
        for robot in self.anggota:
            robot.mulai_bekerja()

class AplikasiRobot:
    pesan_belum_ada_robot = "Belum ada robot."
    def __init__(self):
        self.daftar_robot = []

    def tampilkan_menu(self):
        print("\n===== SISTEM MANAJEMEN ROBOT =====")
        print("1. Tambah robot baru")
        print("2. Lihat semua robot")
        print("3. Suruh robot bekerja")
        print('4. Isi daya robot')
        print("5. Buat tim robot")
        print("6. Cek total robot")
        print("0. Keluar")

    def tambah_robot(self):
        print("Jenis robot: \n 1.Pembersih\n 2.Pengantar\n 3.Keamanan")
        jenis = input("Pilih jenis: ")

        nama = input("Nama robot: ").strip()
        if not nama:
            print("Nama tidak boleh kosong.")
            return

        try:
            baterai = int(input("Baterai awal (0-100): "))
        
        except ValueError:
            print("Baterai harus berupa angka.")
            return

        if not Robot.validasi_baterai(baterai):
            print("Baterai harus 0-100.")
            return

        if jenis == "1":
            area = input("Area: ")
            robot = RobotPembersih(nama, baterai, area)
        elif jenis == "2":
            tujuan = input("Tujuan pengantaran: ")
            robot = RobotPengantar(nama, baterai, tujuan)
        elif jenis == "3":
            lokasi = input("Lokasi jaga: ")
            robot = RobotKeamanan(nama, baterai, lokasi)
        else:
            print("Jenis tidak valid")
            return

        self.daftar_robot.append(robot)
        print(f"Robot {nama} berhasil dibuat")

    def lihat_robot(self):
        if not self.daftar_robot:
            print(self.pesan_belum_ada_robot)
            return
        for i, robot in enumerate(self.daftar_robot, start=1):
            print(f"{i}. {robot}")

    def jalankan(self):
        while True:
            self.tampilkan_menu()
            pilihan = input ("Pilih Menu (0-7) : ")
            if pilihan == "1":
                self.tambah_robot()

            elif pilihan == "2":
                self.lihat_robot()

            elif pilihan == "3":
                if not self.daftar_robot:
                    print("Belum ada robot")
                else:
                    self.lihat_robot()
                    try:
                        nomor = int(input("Pilih nomor robot: "))
                        if 1 <= nomor <= len(self.daftar_robot):
                            self.daftar_robot[nomor -1 ].mulai_bekerja()
                        else:
                            print("Nomor robot tidak ada")
                    except ValueError:
                        print("Input harus berupa angka")

            elif pilihan == "4":
                if not self.daftar_robot:
                    print(self.pesan_belum_ada_robot)
                else:
                    self.lihat_robot()
                    try:
                        nomor = int(input("Pilih nomor robot: "))
                        if 1 <= nomor <= len(self.daftar_robot):
                            jumlah = int(input("Jumlah daya yang diisi: "))
                            if jumlah > 0:
                                self.daftar_robot[nomor - 1].isi_daya(jumlah)
                            else:
                                print("Jumlah daya yang harus lebih dari 0")
                        else:
                            print("Nomot robot tidak ada")
                    except ValueError:
                        print("Input harus berupa angka")

            elif pilihan == "5":
                if len(self.daftar_robot) < 2:
                    print("Minimal harus ada 2 robot untuk membuat tim")
                else:
                    self.lihat_robot()
                    teks = input("Masukkan nomor robot dipisah koma (contoh: 1,2,3): ")
                    try:
                        nomor_list = [int(x) for x in teks.split(",")]
                        nomor_list = list(dict.fromkeys(nomor_list))
                        if len(nomor_list) < 2:
                            print("Pilih minimal 2 robot berbeda")
                        elif any(n < 1 or n > len(self.daftar_robot) for n in nomor_list):
                            print("Ada nomor robot yang tidak ada")
                        else:
                            terpilih = [self.daftar_robot[n - 1] for n in nomor_list]
                            tim = terpilih[0] + terpilih[1]
                            for robot in terpilih[2:]:
                                tim = tim + robot
                            print(tim)
                            jawab = input("Suruh tim bekerja sekarang (Y/N): ").strip().lower()
                            if jawab == 'y':
                                tim.mulai_kerja()
                    except ValueError:
                        print("Format salah. Gunakan angka dipisah koma")
            
            elif pilihan == "6":
                print(f"Total robot yang sudah dibuat: {Robot.total_robot()}")
            
            elif pilihan == "0":
                print("Terima kasih")
                break
            
            else:
                print("Pilihan tidak valid")

if __name__ == "__main__":
    app = AplikasiRobot()
    app.jalankan()
