######## LATIHAN #################
##
######## 10.1 Sebuah Contoh ######
##################################
##
##import time
##
##def jumlahkan_cara_1(n):
##    hasilnya=0
##    for i in range (1,n+1):
##        hasilnya+=i
##    return hasilnya
##
##def jumlahkan_cara_2(n):
##    return (n*(n+1))/2
##
##print("cara 2",jumlahkan_cara_2(1000000))
##
##for i in range(5):
##    awal = time.time()
##    h = jumlahkan_cara_2(1000000)
##    akhir = time.time()
##    print("Jumlah adalah %d,memerlukan waktu %9.8f detik" % (h,akhir-awal))
##
######## 10.3 Kasus terburuk,rata-rata dan terbaik #####
########################################################
##
##import time
##import random
##
##def insertionsort(a):
##    for i in range(1,len(a)):
##        nilai = a[i]
##        b = i
##        while b >0 and nilai<a[b - 1]:
##            a[b]=a[b-1]
##            b -=1
##        a[b]=nilai
##
##print("===============================Average Case====================")    
##
##for i in range (5):
##    L = list(range(3000))
##    random.shuffle(L)
##    awal = time.time()
##    U = insertionsort(L)
##    akhir = time.time()
##    print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik" % (len(L),akhir-awal))
##
##print("===============================Worst Case====================") 
##for i in range (5):
##    L = list(range(3000))
##    L = L[::-1]
##    awal = time.time()
##    U = insertionsort(L)
##    akhir = time.time()
##    print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik" % (len(L),akhir-awal))
##
##print("===============================Best Case====================") 
##for i in range (5):
##    L = list(range(3000))
##    awal = time.time()
##    U = insertionsort(L)
##    akhir = time.time()
##    print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik" % (len(L),akhir-awal))
##
###### 10.4 Menganalisis Kode Python ######
###########################################

##x = 5
##y = x
##z = x + y*8
##d = x > 0 and x < 100
##f = [3,2,4,5]
##v = f[0:2]
##
##i = 32
##while i >= i:
##    count += 1
##    i = 1//2
##    print('i =',i,' ','count =', count)

##### 10.5 Analisis pewaktuan menggunakan timeit #####
######################################################
    
from timeit import timeit

timeit('sqrt(2)','from math import sqrt',number = 10000)

timeit('sqrt(2)','from math import sqrt',number = 100000)

timeit('sqrt(2)','from math import sqrt',number = 1000000)

timeit("1+2")

timeit("sin (pi/3)", setup = "from math import sin,pi")

timeit("sin (1.047)", setup = "from math import sin")

#######10.5.1 Melihat O(n^2) pada nested loop#######
####################################################

import timeit
import matplotlib.pyplot as plt

## Ini fungsi nested loop yang akan diuji:
def kalangBersusuh(n):
    for i in range(n):
        for j in range (n):
            i+j

## Ini fungsi pengujinya:
def ujiKalangBersusuh(n):
    ls=[]
    jangkauan=range(1,n+1)
    siap = "from __main__ import kalangBersusuh"
    for i in jangkauan:
        print('i = ',i) #baris ini bisa dihidupkan atau dimatikan
        t=timeit.timeit("kalangBersusuh(" +str(i) +")",setup=siap,number=1)
        ls.append(t)
    return ls

## Pemanggilan pengujian
n = 1000
LS = ujiKalangBersusuh(n)
## LS adalah list hasil uji kecepatan, dari n sedikit ke banyak.

## Menggambar grafik. dibawah ini saja yang diulang saat me-nyetel skala.
plt.plot(LS)    # Mem-plot hasil uji
skala=7700000   # <--------setel skala ini sesuai hasilmu
plt.plot([x*x/skala for x in range (1,n+1)]) # Grafik x^2 untuk pembanding
plt.show()      # Tunjukkan plotnya

