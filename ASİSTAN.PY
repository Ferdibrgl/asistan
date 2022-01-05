import urllib.request
import json
from gtss import gTTS
from playsound import playsound
import os
import sys
from random import choice
import requests
from lxml import html

class Komut ():
    def __init__(self,gelenSes):
        self.ses = gelenSes.upper()
        self.sesBloklari = self.ses.split()
        print(self.sesBloklari)
        self.komutlar =["naber","nasılsın","ben kimim ","senin adın ne", "saat kaç","cevir","kapat"]




                             #  komut ve işlemler

    def seslendirme(self,yazi):
        tts = gTTS(text=yazi,lang='tr')
        tts.save("ses.mp3")
        playsound("ses.mp3")
        print(yazi)


    def kapat(self):
        self.seslendirme("BAŞKA İŞLEMİNİZ YOK SANIRSAM BEN KENDİMİ KAPATIYORUM")
        sys.exit()


    def havadurumu(self):
        r = requests.get("https://www.ntv.com.tr/turkiye/istanbulda-5-gunluk-hava-durumu-sicak-ve-yagmurlu,ORHnXqKJjEyDhpdX1oMU7w")
        tree = html.fromstring(r.content)

        derece =tree.xpath('//*[@id="main]/section[3]/div/ul[3]/li[1]/div[2]/div[1]/p[1]/span')
        durum = tree.xpath('//*[@id="main]/section[3]/div/ul[3]/li[1]/div[2]/div[1]/p[2]')
        uyarı = ""
        if durum[0].text == "yağmurlu":
            uyarı = "şemsiyeni almayı unutma"



        yazı = "ferdi bugün hava {} derece ve {} gözüküyor.{}".format(derece[0].text,durum[0].text,uyarı[0])
        self.seslendirme(yazı)



    def sohbet(self):
        sozler = ["hasta olursam sevinecekmisin yoksa üzülecekmisin,"
                  "iyiyim sen nasılsın,"
                  "iyi bir işletim sistemli arladaşın varmı,"
                  "benim duygularım yok ama sanırsam insanlar bu duruma iyiyim  diyorlar,"
                  "bir milyon paremetre hesaplamalarıma göre hayatın anlamı 42 ve iyiyim"]
        secim = choice(sozler)


    def youtube(self):
        url = "https://www.youtube.com/channel/UCWg6sMgN4YW1138NgU0yFlA"
