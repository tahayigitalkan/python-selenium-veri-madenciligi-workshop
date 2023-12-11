class Sekil:
    def alan_hesapla(self):
        pass

class Dikdortgen(Sekil):
    def __init__(self, uzunluk, genislik):
        self.uzunluk = uzunluk
        self.genislik = genislik

    def alan_hesapla(self):
        return self.uzunluk * self.genislik

class Kare(Sekil):
    def __init__(self, kenar_uzunlugu):
        self.kenar_uzunlugu = kenar_uzunlugu

    def alan_hesapla(self):
        return self.kenar_uzunlugu ** 2


# Çok biçimlilik örneği
sekil1 = Dikdortgen(5, 3)
print("diktortgen", sekil1.alan_hesapla()) # Çıktı: 15
sekil2 = Kare(4)
print("kare", sekil2.alan_hesapla()) # Çıktı: 16

