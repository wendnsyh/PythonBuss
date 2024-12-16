import pandas as pd
import os
from datetime import datetime
current = datetime.now()
tahun = current.year
bulan = current.month
hari = current.day

print("""----------------------------------------------------
-            SELAMAT DATANG DI WEBSITE             -
-        PT. TRANSPORTATION AIR W NUSANTARA        -
----------------------------------------------------
""")
email=input("Masukkan E-Mail\t :")
password=input("Masukan Password :")

nama=[]
day=[]
tujuan=[]
jumlahtiket=[]
kodetiket=[]
hargatiket=[]
jam=[]
total_harga=[]



def pilihbuss():
    print("""----------------------------------------------------
-           SELAMAT DATANG DI WEBSITE              -
-       PT. TRANSPORTATION AIR W NUSANTARA         -
----------------------------------------------------
silahkan pilih pembelian tiket
 
1. Bus AKAP
2. Bus Pariwisata
----------------------------------------------------
            """)

def akap():
    if jenisbus == 1:
        print("""Pilih Jenis Bus AKAP
    A. ALJ
    B. ALS
    """)
        jenisakap=str(input("Pilih Jenis Bus Akap: "))
        if jenisakap =="A" or jenisakap=="a":
                print("""
            ---------------------------------------------------------
                         JURUSAN BUS AKAP ALJ
            KODE           TUJUAN                  HARGA

            1A        Jakarta - Bali            Rp. 550.000
            2A        Jakarta - Banyuwangi      Rp. 500.000
            3A        Jakarta - Surabaya        RP. 480.000
            4A        Jakarta - Ngawi           Rp. 450.00
            5A        Jakarta - Wonogiri        Rp. 425.000
            6A        Jakarta - Semarang        Rp. 400.000
            7A        Jakarta - Yogyakarta      Rp. 375.000
            8A        Jakarta - Solo            Rp. 350.000
            9A        Jakarta - Tegal           Rp. 325.000
            10A       Jakarta - Cirebon         Rp. 300.000
            11A       Jakarta - Kuningan        Rp. 275.000
            12A       Jakarta - Bandung         Rp. 250.000
            -------------------------------------------------------
                """)
                
                i=1
                for i in range (i):
                     print("Data Pelanggan ke :")
                     kodetiket.append(str(input("Kode tiket [1A-12A] : ")))
                     jumlahtiket.append(int(input("Banyak jumlah tiket yang dipilih  : ")))
                     day_p=str(input("Pilih Hari yang di inginkan [Senin - Minggu] :"))
                     nama_p=str(input("Masukan Nama :"))
                     if (kodetiket[i]=="1A") or (kodetiket[i]=="1a"):
                        nama.append(nama_p)
                        day.append(day_p)
                        tujuan.append("Jakarta - Bali")
                        jam.append("16:00 - 17:00")
                        hargatiket.append(550000)
                        total_harga.append(jumlahtiket[i]*int(550000))
                     elif (kodetiket[i]=="2A") or (kodetiket[i]=="2a"):
                        nama.append(nama_p)
                        day.append(day_p)
                        tujuan.append("Jakarta - Banyuwangi")
                        jam.append("16:30 - 17:30")
                        hargatiket.append(500000)
                        total_harga.append(jumlahtiket[i]*int(500000))
                     elif (kodetiket[i]=="3A") or (kodetiket[i]=="3a"):
                        nama.append(nama_p)
                        day.append(day_p)
                        tujuan.append("Jakarta - Surabaya")
                        jam.append("17:00 - 18:00")
                        hargatiket.append(480000)
                        total_harga.append(jumlahtiket[i]*int(480000))
                     elif (kodetiket[i]=="4A") or (kodetiket[i]=="4a"):
                        nama.append(nama_p)
                        day.append(day_p)
                        tujuan.append("Jakarta - Ngawi")
                        jam.append("17:15 - 18:15")
                        hargatiket.append(450000)
                        total_harga.append(jumlahtiket[i]*int(450000))  
                     elif (kodetiket[i]=="5A") or (kodetiket[i]=="5a"):
                        nama.append(nama_p)
                        day.append(day_p)
                        tujuan.append("Jakarta - Wonogiri")
                        jam.append("17:30 - 18:30")
                        hargatiket.append(425000)
                        total_harga.append(jumlahtiket[i]*int(425000))
                     elif (kodetiket[i]=="6A") or (kodetiket[i]=="6a"):
                        nama.append(nama_p)
                        day.append(day_p)
                        tujuan.append("Jakarta - Semarang")
                        jam.append("18:30 - 19:30")
                        hargatiket.append(400000)
                        total_harga.append(jumlahtiket[i]*int(400000))
                     elif (kodetiket[i]=="7A") or (kodetiket[i]=="7a"):
                        nama.append(nama_p)
                        day.append(day_p)
                        tujuan.append("Jakarta - Yogyakarta")
                        jam.append("18:45 - 19:45")
                        hargatiket.append(375000)
                        total_harga.append(jumlahtiket[i]*int(375000))
                     elif (kodetiket[i]=="8A") or (kodetiket[i]=="8a"):
                         nama.append(nama_p)
                         day.append(day_p)
                         tujuan.append("Jakarta - Solo")
                         jam.append("19:00 - 20:00")
                         hargatiket.append(350000)
                         total_harga.append(jumlahtiket[i]*int(350000))
                     elif (kodetiket[i]=="9A") or (kodetiket[i]=="9a"):
                        nama.append(nama_p)
                        day.append(day_p)
                        tujuan.append("Jakarta - Tegal")
                        jam.append("19:15 - 20:15")
                        hargatiket.append(325000)
                        total_harga.append(jumlahtiket[i]*int(325000))
                     elif (kodetiket[i]=="10A") or (kodetiket[i]=="10a"):
                        nama.append(nama_p)
                        day.append(day_p)
                        tujuan.append("Jakarta - Cirebon")
                        jam.append("10:00 - 10:30")
                        hargatiket.append(300000)
                        total_harga.append(jumlahtiket[i]*int(300000))
                     elif (kodetiket[i]=="11A") or (kodetiket[i]=="11a"):
                        nama.append(nama_p)
                        day.append(day_p)
                        tujuan.append("Jakarta - Kuningan")
                        jam.append("09:00 - 09:30")
                        hargatiket.append(275000)
                        total_harga.append(jumlahtiket[i]*int(275000))
                     elif (kodetiket[i]=="12A") or (kodetiket[i]=="l2a"):
                        nama.append(nama_p)
                        day.append(day_p)
                        tujuan.append("Jakarta - Bandung")
                        jam.append("08:00 - 08:30")
                        hargatiket.append(250000)
                        total_harga.append(jumlahtiket[i]*int(250000))
                     else:
                        nama.append("Error")
                        day.append("Error")
                        tujuan.append("Error")
                        jam.append("Error")
                        hargatiket.append(0)
                        total_harga.append(jumlahtiket[i]*0)
                     i=1
                     
        elif jenisakap=="B" or jenisakap=="b":
            print("""
        -------------------------------------------------
                    JURUSAN BUS AKAP ALS
        KODE         TUJUAN               HARGA
         1B      Jakarta - Lampung      Rp. 300.000
         2B      Jakarta - Palembang    Rp. 350.000
         3B      Jakarta - Jambi        Rp. 375.000
         4B      Jakarta - Padang       Rp. 410.000
         5B      Jakarta - Riau         Rp. 450.000
         6B      Jakarta - Medan        Rp. 485.000
         7B      Jakarta - Aceh         Rp. 525.000
        --------------------------------------------------
              """)
            
            x=1
            for x in range(x):
                print("Data Pelanggan ke :")
                kodetiket.append(str(input("Kode tiket [1B-7B] : ")))
                jumlahtiket.append(int(input("Banyak jumlah tiket yang dipilih  : ")))
                day_p=str(input("Pilih Hari yang di inginkan [Senin - Minggu] :"))
                nama_p=str(input("Masukan Nama :"))
                if (kodetiket[x]=="1B") or (kodetiket[x]=="1b"):
                     nama.append(nama_p)
                     day.append(day_p)
                     tujuan.append("Jakarta - Lampung")
                     jam.append("16:00 - 17:00")
                     hargatiket.append(300000)
                     total_harga.append(jumlahtiket[x]*int(300000))
                elif (kodetiket[x]=="2B") or (kodetiket[x]=="2b"):
                     nama.append(nama_p)
                     day.append(day_p)
                     tujuan.append("Jakarta - Palembang")
                     jam.append("16:30 - 17:30")
                     hargatiket.append(350000)
                     total_harga.append(jumlahtiket[x]*int(350000))
                elif (kodetiket[x]=="3B") or (kodetiket[x]=="3b"):
                     nama.append(nama_p)
                     hari.append(hari_p)
                     tujuan.append("Jakarta - Jambi")
                     jam.append("17:00 - 18:00")
                     hargatiket.append(375000)
                     total_harga.append(jumlahtiket[i]*int(375000))
                elif (kodetiket[x]=="4B") or (kodetiket[x]=="4b"):
                     nama.append(nama_p)
                     day.append(day_p)
                     tujuan.append("Jakarta - Padang")
                     jam.append("18:00 - 19:00")
                     hargatiket.append(410000)
                     total_harga.append(jumlahtiket[x]*int(410000))
                elif (kodetiket[x]=="5B") or (kodetiket[x]=="5b"):
                     nama.append(nama_p)
                     day.append(day_p)
                     tujuan.append("Jakarta - Riau")
                     jam.append("19:00 - 20:00")
                     hargatiket.append(450000)
                     total_harga.append(jumlahtiket[x]*int(450000))
                elif (kodetiket[x]=="6B") or (kodetiket[x]=="6b"):
                     nama.append(nama_p)
                     day.append(day_p)
                     tujuan.append("Jakarta - Medan")
                     jam.append("20:00 - 21:00")
                     hargatiket.append(485000)
                     total_harga.append(jumlahtiket[x]*int(485000))     
                elif (kodetiket[x]=="7B") or (kodetiket[x]=="7b"):
                     nama.append(nama_p)
                     day.append(day_p)
                     tujuan.append("Jakarta - Aceh")
                     jam.append("21:00 - 22:00")
                     hargatiket.append(525000)
                     total_harga.append(jumlahtiket[x]*int(525000))
                else:
                    nama.append("Error")
                    day.append("Error")
                    tujuan.append("Error")
                    jam.append("Error")
                    hargatiket.append(0)
                    total_harga.append(jumlahtiket[x]*0)
        
        
                x=1
       
            
def pw ():
    if jenisbus == 2 :
        print("""Pilih Jenis Bus Pariwisata
    A. YOGYARTA
    B. BANDUNG
    C. BOGOR
    """)
        tu_prwst=str(input("Pilih Tujuan Pariwasata Sesuai Abjad: "))
        if tu_prwst =="A" or tu_prwst == "a":
            print("""
          KODE          TUJUAN          HARGA
                        WISATA
        ---------------------------------------------
          YG1       Candi Prambanan   Rp. 350.000
          YG2       Candi Borobudur   Rp. 350.000
          YG3       Gunung Merapi     Rp. 300.000
          YG4       Malioboro         Rp. 280.000
        ---------------------------------------------
        """)
           
            p=1
            for p in range (p):
                print("Data Pelanggan :")
                kodetiket.append(str(input("Kode tiket sesuai abjad: ")))
                jumlahtiket.append(int(input("Banyak jumlah tiket yang dipilih  : ")))
                day_p=str(input("Pilih Hari yang di inginkan [Senin - Minggu] :"))
                nama_p=str(input("Masukan Nama :"))
                if (kodetiket[p]=="YG1") or (kodetiket[p]=="yg1"):
                    nama.append(nama_p)
                    day.append(day_p)
                    tujuan.append("Candi Prambanan")
                    jam.append("07:00 - 07:30")
                    hargatiket.append(350000)
                    total_harga.append(jumlahtiket[p]*int(350000))
                elif (kodetiket[p]=="YG2") or (kodetiket[p]=="YG2"): 
                    nama.append(nama_p)
                    day.append(day_p)
                    tujuan.append("Candi Borobudur")
                    jam.append("07:00 - 07:30")
                    hargatiket.append(350000)
                    total_harga.append(jumlahtiket[p]*int(350000))
                elif (kodetiket[p]=="YG3") or (kodetiket[p]=="yg3"): 
                    nama.append(nama_p)
                    day.append(day_p)
                    tujuan.append("Gunung Merapi")
                    jam.append("07:30 - 08:00")
                    hargatiket.append(300000)
                    total_harga.append(jumlahtiket[p]*int(300000))
                elif (kodetiket[p]=="YG4") or (kodetiket[p]=="yg4"): 
                    nama.append(nama_p)
                    day.append(day_p)
                    tujuan.append("Malioboro")
                    jam.append("08:00 - 08:30")
                    hargatiket.append(280000)
                    total_harga.append(jumlahtiket[p]*int(280000))
                else :
                    nama.append("Erorr")
                    day.append("Erorr")
                    tujuan.append("Error")
                    jam.append("Error")
                    hargatiket.append(0)
                    total_harga.append(jumlahtiket[p]*int(0))
                p=1
                
        elif tu_prwst == "B" or tu_prwst == "b":
            print("""    
             KODE          TUJUAN                HARGA
                           WISATA
            -------------------------------------------------
              BD1      Lembang                    Rp. 250.000
              BD2      Museum Asia - Afrika       Rp. 250.000
              BD3      Tangkuban Perahu           Rp. 250.000
              BD4      Floating Market            Rp. 230.000
              BD5      Paris Van Java             Rp. 225.000
            --------------------------------------------------
             """)
            
            b=1
            for b in range(b):
                print("Data Pelanggan :")
                kodetiket.append(str(input("Kode tiket sesuai abjad: ")))
                jumlahtiket.append(int(input("Banyak jumlah tiket yang dipilih  : ")))
                day_p=str(input("Pilih Hari yang di inginkan [Senin - Minggu] :"))
                nama_p=str(input("Masukan Nama :"))
                if (kodetiket[b]=="BD1") or (kodetiket[b]=="bd1"):
                    nama.append(nama_p)
                    day.append(day_p)
                    tujuan.append("Lembang")
                    jam.append("07:00 - 07:30")
                    hargatiket.append(250000)
                    total_harga.append(jumlahtiket[b]*int(250000))
                elif (kodetiket[b]=="BD2") or (kodetiket[b]=="bd2"):
                    nama.append(nama_p)
                    day.append(day_p)
                    tujuan.append("Museum Asia - Afrika")
                    jam.append("07:15 - 08:45")
                    hargatiket.append(250000)
                    total_harga.append(jumlahtiket[b]*int(250000))
                elif (kodetiket[b]=="BD3") or (kodetiket[b]=="bd3"):
                    nama.append(nama_p)
                    day.append(day_p)
                    tujuan.append("Tangkuban Perahu")
                    jam.append("07:45 - 08:15")
                    hargatiket.append(250000)
                    total_harga.append(jumlahtiket[b]*int(250000))
                elif (kodetiket[b]=="BD4") or (kodetiket[b]=="bd4"):
                    nama.append(nama_p)
                    day.append(day_p)
                    tujuan.append("Floating Market")
                    jam.append("08:00 - 08:30")
                    hargatiket.append(230000)
                    total_harga.append(jumlahtiket[b]*int(230000))
                elif (kodetiket[b]=="BD5") or (kodetiket[b]=="bd"):
                    nama.append(nama_p)
                    day.append(day_p)
                    tujuan.append("Paris Van Java")
                    jam.append("08:15 - 08:45")
                    hargatiket.append(225000)
                    total_harga.append(jumlahtiket[b]*int(225000))
                else :
                    nama.append("Error")
                    day.append("Error")
                    tujuan.append("Error")
                    jam.append("Error")
                    hargatiket.append(0)
                    total_harga.append(jumlahtiket[b]*int(0))
                b=1
                
        elif  tu_prwst == "C" or tu_prwst == "c":
            print("""
        ----------------------------------------------
           KODE          TUJUAN           HARGA
                         WISATA
            BG1        Taman Safary      Rp. 200.000
            BG2        Cimory            Rp. 200.000
            BG3        Taman Matahari    Rp. 200.000
            BG4        Kebun Raya Bogor  Rp. 185.000
            BG5        Kota Bunga        Rp. 170.000
        -----------------------------------------------
                 """)
          
            d=1
            for d in range (d):
                print("Data Pelanggan :")
                kodetiket.append(str(input("Kode tiket sesuai abjad: ")))
                jumlahtiket.append(int(input("Banyak jumlah tiket yang dipilih  : ")))
                day_p=str(input("Pilih Hari yang di inginkan [Senin - Minggu] :"))
                nama_p=str(input("Masukan Nama :"))
                if (kodetiket[d]=="BG1") or (kodetiket[d]=="bg1"):
                    nama.append(nama_p)
                    day.append(day_p)
                    tujuan.append("Taman Safary")
                    jam.append("07:30 - 08:00")
                    hargatiket.append(200000)
                    total_harga.append(jumlahtiket[d]*int(200000))
                elif (kodetiket[d]=="BG2") or (kodetiket[d]=="bg2"):
                    nama.append(nama_p)
                    day.append(day_p)
                    tujuan.append("Cimory")
                    jam.append("08:00 - 08:30")
                    hargatiket.append(200000)
                    total_harga.append(jumlahtiket[d]*int(200000))
                elif (kodetiket[d]=="BG3") or (kodetiket[d]=="bg3"):
                    nama.append(nama_p)
                    day.append(day_p)
                    tujuan.append("Taman Matahari")
                    jam.append("08:30 - 09:00")
                    hargatiket.append(200000)
                    total_harga.append(jumlahtiket[d]*int(200000))
                elif (kodetiket[d]=="BG4") or (kodetiket[d]=="bg4"):
                    nama.append(nama_p)
                    day.append(day_p)
                    tujuan.append("Kebun Raya Bogor")
                    jam.append("08:30 - 09:00")
                    hargatiket.append(185000)
                    total_harga.append(jumlahtiket[d]*int(185000))
                elif (kodetiket[d]=="BG5") or (kodetiket[d]=="bg5"):
                    nama.append(nama_p)
                    day.append(day_p)
                    tujuan.append("Kota Bunga")
                    jam.append("08:45 - 09:15")
                    hargatiket.append(170000)
                    total_harga.append(jumlahtiket[d]*int(170000))
                else :
                    nama.append("Error")
                    day.append("Error")
                    tujuan.append("Error")
                    jam.append("Error")
                    hargatiket.append(0)
                    total_harga.append(jumlahtiket[d]*int(0))  
                d=1
    


while True:
    pilihbuss()
    try:
        jenisbus=int(input("Masukan Pilihan Buss :"))
    except:
        print("Pilihan Salah, Silahkan Input Ulang")
    if(jenisbus==1):
        akap()
        break
    elif(jenisbus==2):
        pw()
        break
    else:
        jenisbus==0
        print("Silahkan Input ulang :")

        
menu= {
    "Kode tiket"    :kodetiket,
    "Nama"          : nama,
    "Tujuan"        : tujuan,
    "Hari"          : day,
    "Jam"           : jam,
    "Jumlah Tiket "  : jumlahtiket,
    "Harga Tiket "   : hargatiket,
    "Total Harga ."   : total_harga
}

menu1={
    "Kode Tiket"   : kodetiket,
    "Tujuan"       : tujuan,
    "Hari"         : day,
    "Jam"          : jam,
}

daftarmenu=pd.DataFrame(menu)
daftarmenu1=pd.DataFrame(menu1)
pd.set_option('display.max_rows',1000)
daftarmenu.index +=1
daftarmenu1.index +=1

print("-----------------------------------------------------------------------------------------------------------------")
print("{}/{}/{}". format(hari, bulan, tahun))     
print("============================================Struk Pemesanan======================================================")
print("-----------------------------------PT TRANSPORTATION AIR W NUSANTARA---------------------------------------------")
print(daftarmenu)
print("=================================================================================================================")
total = int(sum(total_harga))
print("Total harga yang harus di bayar : Rp.",total)


#Pembayaran
def BCA():
    import cv2
    img = cv2.imread("BCA.jpeg")
    cv2.imshow('BCA',img)
    cv2.waitKey()
    print("Silahkan Scan Qr Tersebut Agar Melanjutkan Pembayaran")
    print("======================================================")
    print("{}/{}/{}". format(hari, bulan, tahun))
    print("=======================================================")
    print("                        E-Tiket                        ")
    print("========================================================")
    print(daftarmenu1)
    print("========================================================")
    print("Silahkan simpan bukti pembayaran dan E-Tiket.")
    print("-------------------------------------------------------")

def BRI():
    import cv2
    img = cv2.imread("BRI.jpeg")
    cv2.imshow('BRI',img)
    cv2.waitKey()
    print("Silahkan Scan Qr Tersebut Agar Melanjutkan Pembayaran")
    print("======================================================")
    print("{}/{}/{}". format(hari, bulan, tahun))
    print("=======================================================")
    print("                        E-Tiket                        ")
    print("=======================================================")
    print(daftarmenu1)
    print("=======================================================")
    print("Silahkan simpan bukti pembayaran dan E-Tiket.")
    print("-------------------------------------------------------")
    
def MANDIRI():
    import cv2
    img = cv2.imread("MANDIRI.jpeg")
    cv2.imshow('MANDIRI',img)
    cv2.waitKey()
    print("Silahkan Scan Qr Tersebut Agar Melanjutkan Pembayaran")
    print("======================================================")
    print("{}/{}/{}". format(hari, bulan, tahun))
    print("=======================================================")
    print("                        E-Tiket                        ")
    print("=======================================================")
    print(daftarmenu1)
    print("=======================================================")
    print("Silahkan simpan bukti pembayaran dan E-Tiket.")
    print("--------------------------------------------------------")
    
def DANA():
    import cv2
    img = cv2.imread("DANA.jpeg")
    cv2.imshow('DANA',img)
    cv2.waitKey()
    print("Silahkan Scan Qr Tersebut Agar Melanjutkan Pembayaran")
    print("======================================================")
    print("{}/{}/{}". format(hari, bulan, tahun))
    print("=======================================================")
    print("                        E-Tiket                        ")
    print("=======================================================")
    print(daftarmenu1)
    print("=======================================================")
    print("Silahkan simpan bukti pembayaran dan E-Tiket.")
    print("---------------------------------------------------------")
    
def TUNAI():
     print("Silahkan lakukan pembayaran dalam waktu 24 Jam dari sekarang di pool buss terderkat")
     print("------------------------------------------------------------------------------------")

print("Pembayaran")
print("[1] BCA \n[2] BRI \n[3] MANDIRI \n[4] DANA \n[5] TUNAI")

while True:
    try:
        bayar = int(input("Pilih pembayaran yang tersedia : "))  
        if (bayar == 1):
            BCA()
        elif (bayar==2):
            BRI()
        elif (bayar==3):
            MANDIRI()
        elif (bayar==4):
            DANA()
        elif (bayar==5):
            TUNAI()
        else:
            print("Input yang anda masukkan salah, silahkan input kembali.")
            continue
        break
    except:
        print("Input yang anda masukkan salah, silahkan input kembali.")


def exit():
    os.system("cls")
    os._exit(0)
    print("Terimakasih telah menggunakan program kami.")

while True:
    try:
        ex=input("Terima kasih telah menggunakan Web kami, Tekan Y untuk close web kami:")
        if (ex=="y"):
            exit()
    except:
        print("Terima Kasih")
   