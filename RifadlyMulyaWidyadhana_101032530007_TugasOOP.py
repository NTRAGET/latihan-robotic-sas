from abc import ABC, abstractmethod

class Games(ABC):
    jumlah_game = 0

    def __init__(self, nama, genre, tahun, ukuran_gb):
        self.__nama = nama
        self.genre = genre
        self.tahun = tahun
        self.ukuran_gb = ukuran_gb
        Games.jumlah_game += 1

    @property
    def nama(self):
        return self.__nama

    def info_game(self):
        print(f"{self.__nama}, dengan genre {self.genre}, rilis tahun {self.tahun} ({self.ukuran_gb} GB).")

    @abstractmethod
    def cara_bermain(self):
        pass

    @classmethod
    def total_game(cls):
        return f"Total game yang terdaftar: {cls.jumlah_game} games."

    @staticmethod
    def game_klasik(tahun):
        return tahun < 2015

    def __str__(self):
        return f"[{self.genre}] {self.__nama} ({self.tahun}) - {self.ukuran_gb} GB"

    def __add__(self, other):
        total_ukuran = self.ukuran_gb + other.ukuran_gb
        return f"Total storage untuk {self.nama} + {other.nama} = {total_ukuran} GB"

class GameMOBA(Games):
    def __init__(self, nama, tahun, ukuran_gb, jumlah_karakter):
        super().__init__(nama, "MOBA", tahun, ukuran_gb)
        self.jumlah_karakter = jumlah_karakter

    def cara_bermain(self):
        print(f"{self.nama}: 5v5 untuk menghancurkan Nexus lawan.")

class GameFPS(Games):
    def __init__(self, nama, tahun, ukuran_gb, sudut_pandang):
        super().__init__(nama, "FPS", tahun, ukuran_gb)
        self.sudut_pandang = sudut_pandang

    def cara_bermain(self):
        print(f"{self.nama}: Gun game dari sudut pandang {self.sudut_pandang}.")

game1 = GameMOBA("LoL", 2009, 35.5, 173)
game2 = GameFPS("Valorant", 2020, 33, "First person")

print(game1)
print(game2)

game1.info_game()
game1.cara_bermain()
game2.info_game()
game2.cara_bermain()

print(game1 + game2)

print(Games.total_game())

print(f"Apakah LoL termasuk game klasik? {Games.game_klasik(game1.tahun)}")

