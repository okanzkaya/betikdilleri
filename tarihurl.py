def tarih_to_url(tarih):
    gun, ay, yil = tarih.split('.')
    return yil + '/' + ay + '/' + gun

def haber_url_olustur(tarih):
    url_tarih = tarih_to_url(tarih)
    return "https://haber.com/" + url_tarih

print(haber_url_olustur("19.03.2025"))