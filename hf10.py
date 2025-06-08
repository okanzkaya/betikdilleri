class Ogrenciler:
    def __init__(self):
        self.ogrenciler = []

    def ogrenci_ekle(self, ogrenci):
        self.ogrenciler.append(ogrenci)
    def ogrenci_listele(self):
        for i in self.ogrenciler:
            print(i)
class Ogrenci:
    def __init__(self, ad, soyad, ogrno):
        self.ad = ad
        self.soyad = soyad
        self.ogrno = ogrno

    def __str__(self):
        return f"{self.ad} {self.soyad}, öğrenci no: {self.ogrno}"

class Siniflar:
    def __init__(self):
        self.siniflar = []

    def sinif_ekle(self, sinif):
        self.siniflar.append(sinif)

class Sinif:
    def __init__(self, sinifno):
        self.sinifno = sinifno
        self.ogrenci_listesi = []
        self.ders_listesi = []
    def ogrenci_ekle(self, ogrenci):
        self.ogrenci_listesi.append(ogrenci)
    def ders_ekle(self, ogrenci):
        self.ders_listesi.append(ders)
class Ders:
    def __init__(self, dersadi):
        self.ad = dersadi
    def ders_ekle(self, dersadi):
        self.dersler.append(dersadi)
class Dersler:
    def __init__(self):
        self.dersler = []
    def ders_ekle(self, dersadi):
        self.dersler.append(dersadi)
        
ornekogrenci = Ogrenci("İsim", "Soyisim", 34)
ogrenci_listesi = Ogrenciler()
ogrenci_listesi.ogrenci_ekle(ornekogrenci)

orneksinif = Sinif(1)
orneksinif.ogrenci_ekle(ornekogrenci)
sinif_listesi = Siniflar()
sinif_listesi.sinif_ekle(orneksinif)

ornekders = Ders("betik")
ders_listesi = Dersler()
ders_listesi.ders_ekle(ornekders)

ogrenci_listesi.ogrenci_listele()
