from abc import ABC, abstractmethod


# ABSTRACTION
class MotorYamaha(ABC):
    jumlah_motor = 0

    def __init__(self, nama, cc, top_speed):
        self.nama = nama
        self.cc = cc
        # ENCAPSULATION
        self.__top_speed = top_speed
        MotorYamaha.jumlah_motor += 1

    # ENCAPSULATION
    @property
    def top_speed(self):
        return self.__top_speed

    # ENCAPSULATION
    def ubah_top_speed(self, nilai):
        if MotorYamaha.validasi_kecepatan(nilai):
            self.__top_speed = nilai
        else:
            print(f"{self.nama}: kecepatan {nilai} km/jam tidak valid")

    def hitung_waktu(self, jarak_km):
        return jarak_km / self.__top_speed * 60

    def hitung_jarak(self, menit):
        return self.__top_speed * menit / 60

    # ABSTRACTION
    @abstractmethod
    def karakter(self):
        pass

    @classmethod
    def total_motor(cls):
        return cls.jumlah_motor

    @classmethod
    def dari_string(cls, data):
        cc, top_speed = data.split(",")
        return cls(int(cc), int(top_speed))

    @staticmethod
    def validasi_kecepatan(nilai):
        return 0 < nilai <= 200

    def __str__(self):
        return f"{self.nama} {self.cc}cc | top speed {self.__top_speed} km/jam"

    def __add__(self, other):
        return self.__top_speed + other.top_speed


# INHERITANCE
class BysonFI(MotorYamaha):
    def __init__(self, cc=150, top_speed=115):
        super().__init__("Yamaha Byson FI", cc, top_speed)

    # POLYMORPHISM
    def karakter(self):
        return "Naked bike bermesin pendingin udara, torsi bawah responsif"


# INHERITANCE
class VixionR(MotorYamaha):
    def __init__(self, cc=155, top_speed=125):
        super().__init__("Yamaha Vixion R", cc, top_speed)

    # POLYMORPHISM
    def karakter(self):
        return "Naked sport bermesin VVA, tenaga atas lebih galak"


# INHERITANCE
class MT15(MotorYamaha):
    def __init__(self, cc=155, top_speed=130):
        super().__init__("Yamaha MT-15", cc, top_speed)

    # POLYMORPHISM
    def karakter(self):
        return "Hyper naked dengan mesin VVA, rangka ringan dan agresif"


if __name__ == "__main__":
    byson = BysonFI()
    vixion = VixionR()
    mt15 = MT15()

    daftar_motor = [byson, vixion, mt15]
    jarak = 60

    for motor in daftar_motor:
        print(motor)
        print("  Karakter:", motor.karakter())

    print()
    for motor in daftar_motor:
        waktu = motor.hitung_waktu(jarak)
        print(f"{motor.nama}: {jarak} km ditempuh dalam {waktu:.1f} menit")

    print()
    for motor in daftar_motor:
        print(f"{motor.nama}: dalam 30 menit menempuh {motor.hitung_jarak(30):.1f} km")

    tercepat = max(daftar_motor, key=lambda m: m.top_speed)
    print()
    print("Motor tercepat:", tercepat.nama)

    print("Validasi 130 km/jam:", MotorYamaha.validasi_kecepatan(130))
    print("Validasi 300 km/jam:", MotorYamaha.validasi_kecepatan(300))
    print("Total top speed Vixion R + MT-15:", vixion + mt15, "km/jam")
    print("Total jumlah motor:", MotorYamaha.total_motor())

    byson.ubah_top_speed(120)
    byson.ubah_top_speed(300)
    print(byson)
