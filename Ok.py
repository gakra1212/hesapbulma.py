import requests
from bs4 import BeautifulSoup
import sys
import time
def animated(text):
  for x in text:
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.005)
logo = '''


   _____       _              
  / ____|     | |             
 | |  __  __ _| | ___ __ __ _ 
 | | |_ |/ _` | |/ / '__/ _` |
 | |__| | (_| |   <| | | (_| |
  \_____|\__,_|_|\_\_|  \__,_|
                              
                              


'''
animated(logo)

# Kullanıcıdan kullanıcı adı alalım
username = input("Aramak İstediğiniz Kişi: ")

# Sosyal medya platformları için URL'leri oluşturma
social_media_urls = {
    "Instagram": f"https://www.instagram.com/{username}",
    "Twitter": f"https://twitter.com/{username}",
    "Facebook": f"https://www.facebook.com/{username}",
    "LinkedIn": f"https://www.linkedin.com/in/{username}",
    "TikTok": f"https://www.tiktok.com/@{username}",
    "Reddit": f"https://www.reddit.com/user/{username}",
    "Snapchat": f"https://www.snapchat.com/add/{username}",
    "Kwai": f"https://www.kwai.com/{username}"  # Kwai için URL ekledik
}

# Sayfa kontrol fonksiyonu
def check_account(url):
    try:
        # URL'yi istekte bulunuyoruz
        response = requests.get(url)
        # Eğer HTTP yanıtı 200 ise sayfa var demektir
        if response.status_code == 200:
            return "Başarılı"
        elif response.status_code == 404:
            return "İsmi Farklı"
        else:
            return "Kullanmıyor"
    except Exception as e:
        return f"Hata: {str(e)}"


for platform, url in social_media_urls.items():
    result = check_account(url)
    print(f"{platform} - {result}")
