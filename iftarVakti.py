import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# Web sayfasından veriyi çekme
url = 'https://www.sabah.com.tr/istanbul-namaz-vakitleri'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# Akşam namazı vaktini bulma
vakitler_div = soup.find('div', class_='vakitler boxShadowSet')
if vakitler_div is not None:
    vakitler = vakitler_div.find_all('span')
    aksam = vakitler[4].text

    # Tarih ve saat hesaplama
    bugun = datetime.now()
    yarin = bugun + timedelta(days=1)
    aksam_saat = datetime.strptime(aksam, "%H:%M")
    kalan_sure = datetime.combine(yarin, aksam_saat.time()) - datetime.now()

    # Sonucu yazdırma
    dakika_kismi = int((kalan_sure.total_seconds() % 3600) // 60)
    kalan_saat = int(kalan_sure.total_seconds() // 3600)
    print(f"İftara kalan süre: {kalan_saat} saat {dakika_kismi} dakika\n")
    print(f"İstanbul'da önümüz akşam namazı vakti: {aksam}\n")


else:
    print("Hata: Vakitler bulunamadı.")


