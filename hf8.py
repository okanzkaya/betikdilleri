import requests
from bs4 import BeautifulSoup

def abc(sayfa_url):
    r = requests.get(sayfa_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    title = soup.find("title").get_text(strip=True)
    meta_date = soup.find("meta", attrs={"name": "datePublished"})
    tarih = meta_date["content"] if meta_date else "Tarih bulunamadı"

    # İçeriği div.article-content veya benzeri bir yapıya göre alıyoruz
    content_div = soup.find("article")
    paragraf = content_div.find_all("p")
    icerik = "\n".join(p.get_text(strip=True) for p in paragraf)

    return title, tarih, icerik

# Örnek kullanım
url = 'https://www.milligazete.com.tr/haber/24487335/rahatsizlanan-mahir-polat-yeniden-silivriye-gonderildi'
title, tarih, icerik = abc(url)

print("Title:", title)
print("Tarih:", tarih)
print("İçerik:", icerik)
