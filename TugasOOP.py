from abc import ABC, abstractmethod

class Rekening(ABC):

    __total_nasabah = 0

    def __init__(self, nomor, nama, saldo_awal):
        self.__nomor_rekening = nomor
        self.__saldo = saldo_awal
        self.nama_pemilik = nama
        Rekening.__total_nasabah += 1

    def __str__(self):
        return self.nama_pemilik + "|" + self.get_nomor() + "|" + Rekening.format_rp(self.__saldo)

    def __add__(self, other):
        return self.__saldo + other._Rekening__saldo

    def cek_saldo(self):
        return self.__saldo

    def get_nomor(self):
        return self.__nomor_rekening

    def setor(self, nominal):
        if nominal > 0:
            self.__saldo += nominal
        else:
            print("Nominal harus lebih dari 0.")

    def _set_saldo(self, nilai):
        self.__saldo = nilai

    @classmethod
    def get_total_nasabah(cls):
        return cls.__total_nasabah

    @staticmethod
    def format_rp(nominal):
        return "Rp " + f"{int(nominal):,}".replace(",", ".")

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def tarik(self, nominal):
        pass

class RekeningBiasa(Rekening):

    def __init__(self, nomor, nama, saldo_awal, bunga=2):
        super().__init__(nomor, nama, saldo_awal)
        self.bunga = bunga

    def info(self):
        print("Jenis: Rekening Biasa")
        print("NomoR: " + self.get_nomor())
        print("Pemili: " + self.nama_pemilik)
        print("Saldo: " + Rekening.format_rp(self.cek_saldo()))
        print("Bunga: " + str(self.bunga) + "% per tahun")

    def tarik(self, nominal):
        if nominal > self.cek_saldo():
            print("Saldo tidak mencukupi.")
        else:
            self._set_saldo(self.cek_saldo() - nominal)


class RekeningPremium(Rekening):

    def __init__(self, nomor, nama, saldo_awal, bunga=5, limit_tarik=10000000):
        super().__init__(nomor, nama, saldo_awal)
        self.bunga       = bunga
        self.limit_tarik = limit_tarik

    def info(self):
        print("Jenis: Rekening Premium")
        print("Nomor: " + self.get_nomor())
        print("Pemilik: " + self.nama_pemilik)
        print("Saldo: " + Rekening.format_rp(self.cek_saldo()))
        print("Bunga: " + str(self.bunga) + "% per tahun")
        print("Limit tarik: " + Rekening.format_rp(self.limit_tarik))

    def tarik(self, nominal):
        if nominal > self.limit_tarik:
            print("Melebihi limit tarik.")
        elif nominal > self.cek_saldo():
            print("Saldo tidak mencukupi.")
        else:
            self._set_saldo(self.cek_saldo() - nominal)

print("BANK HIHU")
print("")

nasabah1 = RekeningBiasa("HIHU-001", "Althaf Raisil", 1500000)
nasabah2 = RekeningPremium("HIHU-002", "Raisil Siddiq", 15000000)

nasabah1.info()
print("")
nasabah2.info()
print("")

print(nasabah1)
print(nasabah2)
print("")

total = nasabah1 + nasabah2
print("Total saldo: " + Rekening.format_rp(total))
print("Total nasabah: " + str(Rekening.get_total_nasabah()))