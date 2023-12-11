class Araba:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def bilgileri_goster(self):
        print(f"{self.marka} {self.model}")


araba1 = Araba("Toyota", "Corolla")
araba2 = Araba("Honda", "Civic")

araba1.bilgileri_goster()  # Çıktı: Toyota Corolla
araba2.bilgileri_goster()  # Çıktı: Honda Civic