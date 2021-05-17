####Latihan 1
##def swap(a,b,c):
##    tmp=a[b]
##    a[b]=a[c]
##    a[c]=tmp
##
##K = [50,20,70,10]
##swap(K,1,3)
##
##
####Latihan 2
##def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
##    posisiYangTerkecil = dariSini
##    for i in range(dariSini+1, sampaiSini):
##        if A[i] < A[posisiYangTerkecil]:
##            posisiYangTerkecil = i
##    return posisiYangTerkecil
##
##A = [18, 13, 44, 25, 66, 107, 78, 89]
##j = cariPosisiYangTerkecil(A, 2, len(A))
##
##
##L = [10,51,2,18,4,31,13,5,23,64,29]
####Latihan 3
##def bubbleSort(A):
##    n = len(A)
##    for i in range(n-1):
##        for j in range(n-i-1):
##            if A[j] > A[j+1]:
##                swap(A,j,j+1)
##    return A
##
####Latihan 4
##def selectionSort(A):
##    n = len(A)
##    for i in range(n - 1):
##        indexKecil = cariPosisiYangTerkecil(A,i,n)
##        if indexKecil != i:
##            swap(A,i,indexKecil)
##    return A
##            
####Latihan 5
##def insertionSort(A):
##    n = len(A)
##    for i in range(1, n):
##        nilai = A[i]
##        pos = i
##        while pos > 0 and nilai < A[pos-1]:
##            A[pos] = A[pos - 1]
##            pos = pos - 1
##        A[pos] = nilai
##    return A
#============================================================================
#============================================================================
class MhsTIF(object):
    def __init__(self,nama,nim,kotaTinggal,us):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kotaTinggal
        self.uangSaku = us

c0 = MhsTIF('Ika', 'L20019001', 'Sukoharjo', 240000)
c1 = MhsTIF('Budi', 'L20019003', 'Sragen', 230000)
c2 = MhsTIF('Ahmad', 'L20019002', 'Surakarta', 250000)
c3 = MhsTIF('Chandra', 'L20019004', 'Surakarta', 235000)
c4 = MhsTIF('Eka', 'L20019006', 'Boyolali', 240000)
c5 = MhsTIF('Fandi', 'L20019005', 'Salatiga', 250000)
c6 = MhsTIF('Deni', 'L20019007', 'Klaten', 245000)
c7 = MhsTIF('Galuh', 'L20019009', 'Wonogiri', 245000)
c8 = MhsTIF('Janto', 'L20019008', 'Klaten', 245000)
c9 = MhsTIF('Hasan', 'L20019011', 'Karanganyar', 270000)
c10 = MhsTIF('Khalid', 'L20019010', 'Purwodadi', 265000)

Daftar=[c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

#Nomor 1
def swap(i,j,k):
    tmp=i[j]
    i[j]=i[k]
    i[k]=tmp

def urutNim(i):
    n = len(i)
    for x in range(n-1):
        for y in range(n-x-1):
            if i[y].nim > i[y+1].nim:
                swap(i,y,y+1)
    
def cekNim(x):
    for y in x:
        print(y.nama, y.nim, y.kotaTinggal)



                
# Nomer 2
a = [10,9,8,7,6,5,4,3,2,1]
b = [20,19,18,17,16,15,14,13,12,11]

def urut(a,b):
    c = a + b
    for i in range(1,len(c)):
        nilai = c[i]
        pos = i
        while pos > 0 and nilai<c[pos - 1]:
            c[pos]=c[pos-1]
            pos -=1
        c[pos]=nilai
    print(c)

## Nomer 3
def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[1] < A[posisiTerkecil]:
            posisiTerkecil = 1
    return posisiTerkecil

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)
            
def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)
def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        posisi = i
        while posisi > 0 and nilai < A[posisi-1]:
            A[posisi] = A[posisi-1]
            posisi = posisi-1
        A[posisi] = nilai
        
from time import time as detak
from random import shuffle as kocok

k = [i for i in range(1,6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak();bubbleSort(u_bub);ak=detak();print("Bubble: %g detik"%(ak-aw));
aw = detak();selectionSort(u_sel);ak=detak();print("Selection: %g detik"%(ak-aw));
aw = detak();insertionSort(u_ins);ak=detak();print("Insertion: %g detik"%(ak-aw));

