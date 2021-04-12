# Nama : Daffa Putra Alwansyah
# NIM : L200190031
# Kelas : B

# Nomor 1
# def cetakSiku(baris):
#        kolom = 0
#        for x in range(baris+1):
#              for y in range(kolom):
#                     print("*", end = " ")
#             print("")
#             kolom += 1

# Pemanggilan:
# cetakSiku(5))

# Output:
# *
# * *
# * * *
# * * * *
# * * * * *

# Nomor 2
# code:

# def gambarlahPersegiEmpat(a,b):
#     for x in range (a):
#         if x == 0 or x == a-1:
#             print ("@"*b)
#         else:
#             print("@"+" "*(b-2)+"@")

# pemanggilan:
# gambarlahPersegiEmpat(4,5)
# Output:
# @@@@@
# @          @
# @          @
# @@@@@

# Nomor 3
# A
# code:

# def jumlahHurufVokal(kata):
#    jmlvokal = 0
#    huruf = 0
#    vokal = "aiueoAIUEO"
#    for x in kata:
#        huruf = huruf+ 1
#        if x in vokal:
#            jmlvokal = jmlvokal+ 1
#    print(huruf,",", jmlvokal)

# pemanggilan:
# jumlahHurufVokal("Surakarta")

# Output:
# 9 , 4

# B
# code:
# def jumlahHurufKonsonan(kata):
#    jmlkonsonan = 0
#    huruf = 0
#    konsonan = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
#    for x in kata:
#        huruf = huruf+1
#        if x in konsonan:
#                   jmlkonsonan = jmlkonsonan+1

#    print(huruf,",",jmlkonsonan)

# pemanggilan:
# jumlahHurufKonsonan("Surakarta")

# Output:
# 9,5
# Nomor 4
# code:

# def rerata(x):
#     bnykData = 0
#     total = 0
#     for i in x:
#         bnykData += 1
#         total = total + i
#         hasil = (total/bnykData)
#     return hasil

# pemanggilan:
# rerata([1,2,3,4,5])

# Output:
# 3.0
# Nomor 5

# from math import sqrt as sq
# def apakahPrima(n):
#    n = int(n)
#    assert n>=0 
#    primaKecil = [2,3,5,7,11]
#    bukanPrKecil = [0,1,4,6,8,9,10]
#    if n in primaKecil:
#        return True
#    elif n in bukanPrKecil:
#        return False
#    else:
#        for i in range (2,int(sq(n))+1):
#            if n % i == 0:
#                return False
#        return True
# Pemanggilan:
# apakahPrima(17)

# Output:
# True

# Nomor 6
# def cekPrima():
#    y = range(1001)
#    for i in range(1,1001):
#        x = 0
#        for j in range(i):
#            if i%(j+1) == 0:
#                x+= 1
#        if x == 2:
#            print(i)

# pemanggilan:
# cekPrima()

# Output:
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
# 23
# 29
# 31
# 37
# 41
# 43
# 47
# 53
# 59
# 61
# 67
# 71
# 73
# 79
# 83
# 89
# 97
# 101
# 103
# 107
# 109
# 113
# 127
# 131
# 137
# 139
# 149
# 151
# 157
# 163
# 167
# 173
# 179
# 181
# 191
# 193
# 197
# 199
# 211
# 223
# 227
# 229
# 233
# 239
# 241
# 251
# 257
# 263
# 269
# 271
# 277
# 281
# 283
# 293
# 307
# 311
# 313
# 317
# 331
# 337
# 347
# 349
# 353
# 359
# 367
# 373
# 379
# 383
# 389
# 397
# 401
# 409
# 419
# 421
# 431
# 433
# 439
# 443
# 449
# 457
# 461
# 463
# 467
# 479
# 487
# 491
# 499
# 503
# 509
# 521
# 523
# 541
# 547
# 557
# 563
# 569
# 571
# 577
# 587
# 593
# 599
# 601
# 607
# 613
# 617
# 619
# 631
# 641
# 643
# 647
# 653
# 659
# 661
# 673
# 677
# 683
# 691
# 701
# 709
# 719
# 727
# 733
# 739
# 743
# 751
# 757
# 761
# 769
# 773
# 787
# 797
# 809
# 811
# 821
# 823
# 827
# 829
# 839
# 853
# 857
# 859
# 863
# 877
# 881
# 883
# 887
# 907
# 911
# 919
# 929
# 937
# 941
# 947
# 953
# 967
# 971
# 977
# 983
# 991
# 997

# Nomor 7
# code:
# def faktorPrima(x):
#    listprima = []
#    prima = 2
#    while prima <=x:
#        if x%prima==0:
#            x/=prima
#            listprima.append(prima)
#        else:
#            prima+=1
#    return listprima

# pemanggilan:
# faktorPrima(10)

# Output:
# [2, 5]

# Nomor 8
# code:
# def apakahTerkandung(a,b):
#    if a in b:
#        return True
#    else:
#        return False

# pemanggilan:
# apakahTerkandung("ind","indonesia tanah air beta")

# Output:
# True

# Nomor 9
# code:
# def cetak():
#    for i in range(1,100):
#        if i % 3 == 0 and i % 5 == 0 :
#            print ("Python UMS")
#        elif i % 3 == 0:
#            print("Python")
#        elif i % 5 == 0:
#            print ("UMS")
#        
#        else:
#            print (i)

# pemanggilan:
# cetak()

# Output:
# 1
# 2
# Python
# 4
# UMS
# Python
# 7
# 8
# Python
# UMS
# 11
# Python
# 13
# 14
# Python UMS
# 16
# 17
# Python
# 19
# UMS
# Python
# 22
# 23
# Python
# UMS
# 26
# Python
# 28
# 29
# Python UMS
# 31
# 32
# Python
# 34
# UMS
# Python
# 37
# 38
# Python
# UMS
# 41
# Python
# 43
# 44
# Python UMS
# 46
# 47
# Python
# 49
# UMS
# Python
# 52
# 53
# Python
# UMS
# 56
# Python
# 58
# 59
# Python UMS
# 61
# 62
# Python
# 64
# UMS
# Python
# 67
# 68
# Python
# UMS
# 71
# Python
# 73
# 74
# Python UMS
# 76
# 77
# Python
# 79
# UMS
# Python
# 82
# 83
# Python
# UMS
# 86
# Python
# 88
# 89
# Python UMS
# 91
# 92
# Python
# 94
# UMS
# Python
# 97
# 98
# Python

# Nomor 10
# code:
# def selesaikanABC(a,b,c):
#    x = 0
#    x = (b**2)-(4*a*c)
#    if x == 0:
#        print("Determinan 0, persamaan mempunyai satu akar kembar")
#    elif x > 0:
#        print("Determinan positif,persamaan mempuynai akar real")
#    elif x < 0:
#        print("Determinan negatif, Persamaan tidak mempunyai akar real")

# Pemanggilan:
# selesaikanABC(1,2,3)

# Output:
# Determinan negatif, Persamaan tidak mempunyai akar real

# Nomor 11
# code:
# def apakahKabisat(x):
#    if x % 4==0:
#        if x % 100==0:
#            if x %400==0:
#                print(True)
#            else:
#                print(False)
#        else:
#            print(True)
#    else:
#        print(False)
# pemanggilan:
# apakahKabisat(2004)

# Output:
# True

# Nomor 12
# import random
# tebak_angka = random.randrange(1,101)
# tebak = 0
# percobaan = 0

# print("Permainan tebak angka.")
# print("saya menyiapakan angka bulat 1 sampai 100, coba tebak:")

# while tebak_angka != tebak:
#    percobaan+=1
#    tebak = int(input("Masukan tebakan ke-"+str(percobaan)+":"))
#    if tebak == tebak_angka:
#        print("ya anda,Benar!")
#        break
#    elif tebak < tebak_angka:
#        print("Tebakanmu terlalu kecil coba lagi:")
#        
#    else:
#        print("Tebakanmu terlalu berar coba lagi:")

# Output:
# Permainan tebak angka.
# saya menyiapakan angka bulat 1 sampai 100, coba tebak:
# Masukan tebakan ke-1:20
# Tebakanmu terlalu berar coba lagi:
# Masukan tebakan ke-2:19
# Tebakanmu terlalu berar coba lagi:
# Masukan tebakan ke-3:18
# Tebakanmu terlalu berar coba lagi:
# Masukan tebakan ke-4:17
# Tebakanmu terlalu berar coba lagi:
# Masukan tebakan ke-5:16
# Tebakanmu terlalu berar coba lagi:
# Masukan tebakan ke-6:11
# Tebakanmu terlalu kecil coba lagi:
# Masukan tebakan ke-7:13
# Tebakanmu terlalu berar coba lagi:
# Masukan tebakan ke-8:12
# ya anda,Benar!

# Nomor 13
# code:
# def Katakan(bil):
#    angka = ["","Satu","Dua","Tiga","Empat","Lima","Enam",
#             "Tujuh","Delapan","Sembilan","Sepuluh","Sebelas"]
#    Hasil = " "
#    n = int(bil)
#    if n>= 0 and n <= 11:
#        Hasil = angka[n]
#    elif n <20:
#        Hasil = Katakan (n-10) + " Belas "
#    elif n <100:
#        Hasil = Katakan (n/10) + " Puluh " + Katakan (n%10)
#    elif n <200:
#        Hasil = " Seratus " + Katakan (n-100)
#    elif n <1000:
#        Hasil = Katakan (n/100) + " Ratus " + Katakan (n%100)
#    elif n <2000:
#        Hasil = " Seribu " + Katakan (n-1000)
#    elif n <1000000:
#        Hasil = Katakan (n/1000) + " Ribu " + Katakan (n%1000)
#    elif n <1000000000:
#        Hasil = Katakan (n/1000000) + " Juta " + Katakan (n%1000000)
#    elif n <1000000000000:
#        Hasil = Terbilang (n/1000000000) + " Milyar " + Katakan (n%1000000000)
#    return Hasil

# Pemanggilan:
# Katakan(200000)

# Output:
# 'Dua Ratus Ribu '

# Nomor 14
# code:
# def formatRupiah(angka):
#     hasil = "Rp. {:,.0f}".format(angka).replace(',','.')
#     return hasil

# Pemanggilan:
# formatRupiah(1500)

# Output:
# 'Rp. 1.500'
# -----------------------------------------------------------------------------------------

###NOMOR 1.1
##a = 4
##b = 5
##c = a + b
##print("Nilai a =", a)
##print("Nilai b=", b)
##print("Sekarang, c = a + b = ", a, '+', b, '=', c)
##print('')
##print("Sudah selesai. ")


### #NOMOR 1.2
##print("Kita perlu bicara sebentar...")
##nm = input("Siapa namamu? (ketik di sini)> ")
##print("Selamat belajar,", nm)
##angkaStr = input("Masukkan sebuah angka antara 1 sampai 100 > " )
##a = int(angkaStr)
##kuadratnya = a*a
##print(nm + ', tahukah kamu bahwa', a, 'kuadrat adalah', kuadratnya,'?')


### #NOMOR 1.3
##def ucapkanSalam():
##    print("Assalamu ’alaikum!")
##
##def sapa(nama):
##    ucapkanSalam() # Ini memanggil fungsi ucapkanSalam() di atas.
##    print("Halo",nama)
##    print("Selamat belajar!")
##
##def kuadratkan(b):
##    h = b*b
##    return h
##
##ucapkanSalam()
##sapa("Mas Wowok")
##b = kuadratkan(5)
##k = 9
##print("Bilangan", k , " , kalau dipangkatkan dua jadinya", kuadratkan(k))


###NOMOR 1.4
##from math import sqrt as akar
##def selesaikanABC(a,b,c):
##    a = float(a) #mengubahjenisintegermenjadifloat
##    b = float(b)
##    c = float(c)
##    D = b**2-4*a*c
##    x1 = (-b + akar(abs(D))) /(2*a)
##    x2 = (-b  - akar(abs(D))) /(2*a)
##    hasil=(x1,x2) #tupleyangterdiridariduaelemen
##    return hasil
##k = selesaikanABC(1,-5,6)
##print(k)
##print(k[0])
##print(k[1])
##print(selesaikanABC(1,2,3))


###NOMOR 1.5
##def apakahGenap(x):
##    if (x%2 == 0):
##        return True
##    else:  
##        return False
##
##print(apakahGenap(48))
##print(apakahGenap(37))



### #NOMOR 1.6
##def tigaAtauLima(x):
##    if (x%3==0 and x%5==0):
##        print("Bilangan itu adalah kelipatan 3 dan 5 sekaligus")  
##    elif x%3==0:
##        print("Bilangan itu adalah kelipatan 3")  
##    elif x%5==0:
##        print("Bilangan itu adalah kelipatan 5") 
##    else:  
##        print("Bilangan itu bukan kelipatan 3 maupun 5")
##
##(tigaAtauLima(9))
##(tigaAtauLima(10))
##(tigaAtauLima(15))
##(tigaAtauLima(17))


###NOMOR 1.7
##staff = { "Santi" : "santi@ums.ac.id", 
##    "Jokowi" : "jokowi@solokab.go.id", 
##    "Endang" : "Endang@yahoo.com",
##    "Sulastri": "Sulastri3@gmail.com" }  
##
##yangDicari = "Santi"  
##if yangDicari in staff:
##    print("emailnya", yangDicari, "adalah" , staff[yangDicari])
##else :
##    print("Tidak ada yang namanya", yangDicari)


###NOMOR 1.8
##for i in range(0,10):
##    print(i)


###NOMOR 1.9
##s="Ini Budi"
##for i in s:
##    print(i)


###NOMOR 1.10
##dd = {"nama":"joko", "umur":21, "asal":"surakarta"} 
##for kunci in dd:
##    print(kunci,"<---->", dd[kunci])


###NOMOR 1.11
##bil = 0
##while(bil*bil<200):
##    print(bil, bil*bil)
##    bil = bil + 1

