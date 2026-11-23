from abc import ABC, abstractmethod



class WahanaBawahAir(ABC):
 
    total_wahana = 0
    organisasi = "SAS Robotic Laboratory"

    def __init__(self, nama_wahana: str, kapasitas_baterai: float):
        self.__nama_wahana = nama_wahana
        self.__kapasitas_baterai = kapasitas_baterai  # dalam Wh
        self.__kedalaman_saat_ini = 0.0  # dalam meter
        WahanaBawahAir.total_wahana += 1

    def get_nama(self) -> str:
        return self.__nama_wahana

    def get_baterai(self) -> float:
        return self.__kapasitas_baterai

    def set_baterai(self, nilai_baru: float):
        if nilai_baru >= 0:
            self.__kapasitas_baterai = nilai_baru
        else:
            print("[Peringatan] Kapasitas baterai tidak boleh negatif!")

    def get_kedalaman(self) -> float:
        return self.__kedalaman_saat_ini

    def _update_kedalaman(self, kedalaman: float):
        self.__kedalaman_saat_ini = kedalaman

    @abstractmethod
    def jalankan_misi(self, target_kedalaman: float):
        pass

    def status_sistem(self) -> str:
        return (
            f"[{self.__nama_wahana}] Baterai: {self.__kapasitas_baterai:.1f} Wh | "
            f"Kedalaman: {self.__kedalaman_saat_ini:.1f} m"
        )

    @classmethod
    def info_divisi(cls) -> str:
        return f"Divisi Riset: {cls.organisasi} | Total Unit Aktif: {cls.total_wahana}"

    @staticmethod
    def hitung_tekanan_hidrostatis(kedalaman: float, massa_jenis_air: float = 1025.0) -> float:
        """Menghitung tekanan hidrostatis (dalam kPa) pada kedalaman tertentu."""
        gravitasi = 9.81
        tekanan_pascal = massa_jenis_air * gravitasi * kedalaman
        return tekanan_pascal / 1000.0

    def __str__(self) -> str:
        return f"Wahana '{self.__nama_wahana}' (Baterai: {self.__kapasitas_baterai:.1f} Wh)"

    def __add__(self, other):
        """Menggabungkan kapasitas baterai dari dua wahana."""
        if isinstance(other, WahanaBawahAir):
            return self.__kapasitas_baterai + other.get_baterai()
        raise TypeError("Penjumlahan hanya didukung antar sesama objek WahanaBawahAir.")


class AUV(WahanaBawahAir):
    def __init__(self, nama_wahana: str, kapasitas_baterai: float, algoritma_navigasi: str):
        super().__init__(nama_wahana, kapasitas_baterai)
        self.__algoritma_navigasi = algoritma_navigasi

    def jalankan_misi(self, target_kedalaman: float):
        konsumsi = target_kedalaman * 1.5
        if self.get_baterai() >= konsumsi:
            self._update_kedalaman(target_kedalaman)
            self.set_baterai(self.get_baterai() - konsumsi)
            tekanan = self.hitung_tekanan_hidrostatis(target_kedalaman)
            print(
                f"[AUV - {self.get_nama()}] Menyelam secara otonom ke {target_kedalaman} m "
                f"menggunakan navigasi {self.__algoritma_navigasi}. "
                f"(Tekanan: {tekanan:.2f} kPa)"
            )
        else:
            print(f"[AUV - {self.get_nama()}] Baterai tidak mencukupi untuk menyelam ke {target_kedalaman} m.")


class ROV(WahanaBawahAir):
    def __init__(self, nama_wahana: str, kapasitas_baterai: float, panjang_kabel_tether: float):
        super().__init__(nama_wahana, kapasitas_baterai)
        self.__panjang_kabel_tether = panjang_kabel_tether

    def jalankan_misi(self, target_kedalaman: float):
        if target_kedalaman > self.__panjang_kabel_tether:
            print(
                f"[ROV - {self.get_nama()}] Gagal menyelam! Target {target_kedalaman} m "
                f"melebihi panjang kabel tether ({self.__panjang_kabel_tether} m)."
            )
            return

        konsumsi = target_kedalaman * 0.8
        if self.get_baterai() >= konsumsi:
            self._update_kedalaman(target_kedalaman)
            self.set_baterai(self.get_baterai() - konsumsi)
            tekanan = self.hitung_tekanan_hidrostatis(target_kedalaman)
            print(
                f"[ROV - {self.get_nama()}] Dikendalikan operator via tether ke {target_kedalaman} m. "
                f"(Tekanan: {tekanan:.2f} kPa)"
            )
        else:
            print(f"[ROV - {self.get_nama()}] Daya cadangan tidak cukup.")


if __name__ == "__main__":
    print("=== SIMULASI WAHANA BAWAH AIR (SAS ROBOTIC) ===\n")

    auv_1 = AUV("SAS-AUV-01", kapasitas_baterai=500.0, algoritma_navigasi="SLAM + IMU")
    rov_1 = ROV("SAS-ROV-01", kapasitas_baterai=350.0, panjang_kabel_tether=50.0)

    # Menggunakan Class Method
    print(WahanaBawahAir.info_divisi())
    print("-" * 55)

    print("Objek 1:", auv_1)
    print("Objek 2:", rov_1)

    total_baterai = auv_1 + rov_1
    print(f"Total Gabungan Kapasitas Baterai: {total_baterai:.1f} Wh")
    print("-" * 55)

    daftar_wahana = [auv_1, rov_1]
    for wahana in daftar_wahana:
        wahana.jalankan_misi(30.0)
        print(" ->", wahana.status_sistem())

    print("-" * 55)
    rov_1.jalankan_misi(65.0)
