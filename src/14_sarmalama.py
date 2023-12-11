class Ogrenci:
    def __init__(self, ad, soyad):
        self.__ad = ad  # __ad, private bir veri alanıdır
        self.__soyad = soyad  # __soyad, private bir veri alanıdır
        self.__notlar = {}  # __notlar, private bir veri alanıdır

    def adi_al(self):
        return self.__ad

    def soyadi_al(self):
        return self.__soyad

    def not_ekle(self, ders, not_degeri):
        self.__notlar[ders] = not_degeri

    def notlari_goster(self):
        return self.__notlar

# Ogrenci sınıfını kullanma
ogrenci1 = Ogrenci("Ahmet", "Yılmaz")

# private veri alanlarına doğrudan erişim engellidir
#print(ogrenci1.__ad)  # Hata alırsınız

# Ancak sınıf içinde tanımlanan metodlar aracılığıyla erişim sağlanabilir
print("Ad:", ogrenci1.adi_al())  # Çıktı: Ad: Ahmet
print("Soyad:", ogrenci1.soyadi_al())  # Çıktı: Soyad: Yılmaz

# private veri alanlarına not_ekle metodu aracılığıyla erişim
ogrenci1.not_ekle("Matematik", 90)
ogrenci1.not_ekle("Fizik", 85)

# private veri alanlarını notlari_goster metodu aracılığıyla erişim
print("Notlar:", ogrenci1.notlari_goster())  
# Çıktı: Notlar: {'Matematik': 90, 'Fizik': 85}
