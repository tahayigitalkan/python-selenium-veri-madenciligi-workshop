class EvcilHayvan:
    def __init__(self, isim):
        self.isim = isim

    def konus(self):
        pass

class Kedi(EvcilHayvan):
    def konus(self):
        return "Miyav"

class Kopek(EvcilHayvan):
    def konus(self):
        return "Hav Hav"


tekir = Kedi("Tekir")
print(tekir.isim, tekir.konus()) # Çıktı: Tekir Miyav
husky = Kopek("Husky")
print(husky.isim, husky.konus()) # Çıktı: Husky Hav Hav