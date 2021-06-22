############SOAL MAHASISWA###########
#==========No 1==========
##from timeit import timeit
##import random
##
##print("=====Jumlahkan Cara 1=====")
##
##def jumlahkan_cara_1(n):
##    hasilnya = 0
##    for i in range(1, n+1):
##        hasilnya = hasilnya + i
##    return hasilnya
##
##for i in range(5):
##    siap = "from __main__ import jumlahkan_cara_1"
##    h = jumlahkan_cara_1(1000000)
##    t = timeit("jumlahkan_cara_1(1000000)", setup=siap, number=1)
##    print("Jumlah adalah %d, memerlukan %9.8f detik" % (h, t))
##
##print("=====Jumlahkan Cara 2=====")
##
##def jumlahkan_cara_2(n):
##    return (n*(n+1))/2
##
##for i in range(5):
##    siap = "from __main__ import jumlahkan_cara_2"
##    h = jumlahkan_cara_2(1000000)
##    t = timeit("jumlahkan_cara_2(1000000)", setup=siap, number=1)
##    print("Jumlah adalah %d, memerlukan %9.8f detik" % (h, t))
##
##
##print("=====Insertion Sort=====")
##
##def insertionSort(A):
##    n = len(A)
##    for i in range(1, n):
##        nilai = A[i]
##        pos = i
##        while pos > 0 and nilai < A[pos - 1]:
##            A[pos] = A[pos - 1]
##            pos = pos -1
##        A[pos] = nilai
##
##for i in range(5):
##    siap = "from __main__ import insertionSort,L"
##    L = list(range(3000))
##    random.shuffle(L)
##    t = timeit("insertionSort(L)", setup=siap, number=1)
##    print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(L), t))

#==========No 2==========
##from timeit import timeit
##import random
##
##print("=====Sorted average case=====")
##
##for i in range(5):
##    g = list(range(3000))
##    random.shuffle(g)
##    t = timeit("sorted(g)", setup="from __main__ import g",number=1)
##    print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(g), t))
##
##print("=====Sorted best case=====")
##
##for i in range(5):
##    g = list(range(3000))
##    t = timeit("sorted(g)", setup="from __main__ import g",number=1)
##    print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(g), t))
##
##print("=====Sorted worst case=====")
##
##for i in range(5):
##    g = list(range(3000))
##    g = g[::-1]
##    t = timeit("sorted(g)", setup="from __main__ import g",number=1)
##    print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(g), t))

###==========No 3a==========
##import time
##import random
##import timeit
##import matplotlib.pyplot as plt
##
##def a(n):
##    test = 0
##    for i in range(n):
##        for j in range(n):
##            test = test + i * j
##
##def ujia(n):
##    ls = []
##    jangkauan = range(1, n+1)
##    siap = 'from __main__ import a'
##    for i in jangkauan:
##        t = timeit.timeit('a(' + str(i) + ')', setup = siap, number = 1)
##        ls.append(t)
##    return ls
##
##n = 10
##LS = ujia(n)
##
##plt.plot(LS)
##skala = 7700000
##plt.plot([x*x/skala for x in range(1, n+1)])
##plt.show()
#==========No 3b==========
##import time
##import random
##import timeit
##import matplotlib.pyplot as plt
##
##def a(n):
##    test = 0
##    for i in range(n):
##        for j in range(i):
##            test = test + i * j
##
##def ujia(n):
##    ls = []
##    jangkauan = range(1, n+1)
##    siap = 'from __main__ import a'
##    for i in jangkauan:
##        t = timeit.timeit('a(' + str(i) + ')', setup = siap, number = 1)
##        ls.append(t)
##    return ls
##
##n = 1000
##LS = ujia(n)
##
##plt.plot(LS)
##skala = 7700000
##plt.plot([x*x/skala for x in range(1, n+1)])
##plt.show()
###==========No 3c==========
##import time
##import random
##import timeit
##import matplotlib.pyplot as plt
##
##def a(n):
##    test = 0
##    for i in range(n):
##        test = test + 1
##    for j in range(n):
##        test = test - 1
##
##def ujia(n):
##    ls = []
##    jangkauan = range(1, n+1)
##    siap = 'from __main__ import a'
##    for i in jangkauan:
##        t = timeit.timeit('a(' + str(i) + ')', setup = siap, number = 1)
##        ls.append(t)
##    return ls
##
##n = 10
##LS = ujia(n)
##
##plt.plot(LS)
##skala = 7700000
##plt.plot([x*x/skala for x in range(1, n+1)])
##plt.show()
###==========No 3d==========
##import time
##import random
##import timeit
##import matplotlib.pyplot as plt
##
##def a(n):
##    i = n
##    while i > 0:
##        k = 2 + 2
##        i = i // 2
##
##def ujia(n):
##    ls = []
##    jangkauan = range(1, n+1)
##    siap = 'from __main__ import a'
##    for i in jangkauan:
##        t = timeit.timeit('a(' + str(i) + ')', setup = siap, number = 1)
##        ls.append(t)
##    return ls
##
##n = 10
##LS = ujia(n)
##
##plt.plot(LS)
##skala = 7700000
##plt.plot([x*x/skala for x in range(1, n+1)])
##plt.show()
###==========No 3e==========
##import time
##import random
##import timeit
##import matplotlib.pyplot as plt
##
##def a(n):
##    for i in range(n):
##        for j in range(n):
##            for k in range(n):
##                m = i + j + k + 2019
##
##def ujia(n):
##    ls = []
##    jangkauan = range(1, n+1)
##    siap = 'from __main__ import a'
##    for i in jangkauan:
##        t = timeit.timeit('a(' + str(i) + ')', setup = siap, number = 1)
##        ls.append(t)
##    return ls
##
##n = 100
##LS = ujia(n)
##
##plt.plot(LS)
##skala = 7700000
##plt.plot([x*x/skala for x in range(1, n+1)])
##plt.show()
###==========No 3f==========
##import time
##import random
##import timeit
##import matplotlib.pyplot as plt
##
##def a(n):
##    for i in range(n):
##        if i % 3 == 0:
##            for j in range(n // 2):
##                j+=j
##        elif i % 2 == 0:
##            for j in range(5):
##                j+=j
##        else:
##            for j in range(n):
##                j+=j
##
##def ujia(n):
##    ls = []
##    jangkauan = range(1, n+1)
##    siap = 'from __main__ import a'
##    for i in jangkauan:
##        t = timeit.timeit('a(' + str(i) + ')', setup = siap, number = 1)
##        ls.append(t)
##    return ls
##
##n = 100
##LS = ujia(n)
##
##plt.plot(LS)
##skala = 7700000
##plt.plot([x*x/skala for x in range(1, n+1)])
##plt.show()
###==========No 3g==========
##import time
##import random
##import timeit
##import matplotlib.pyplot as plt
##
##def a(n):
##    for i in range(n):
##        if i % 3 == 0:
##            for j in range(n // 2):
##                j+=j
##        elif i % 2 == 0:
##            for j in range(5):
##                j+=j
##        else:
##            for j in range(n):
##                j+=j
##
##def ujia(n):
##    ls = []
##    jangkauan = range(1, n+1)
##    siap = 'from __main__ import a'
##    for i in jangkauan:
##        t = timeit.timeit('a(' + str(i) + ')', setup = siap, number = 1)
##        ls.append(t)
##    return ls
##
##n = 100
##LS = ujia(n)
##
##plt.plot(LS)
##skala = 7700000
##plt.plot([x*x/skala for x in range(1, n+1)])
##plt.show()

###==========No 7==========
##import time
##import random
##import timeit
##import matplotlib.pyplot as plt
##
##def a(n):
##    L = list(range(30))
##    L = L[::-1]
##    for i in range(n):
##        L.append(n)
##
##def ujia(n):
##    ls = []
##    jangkauan = range(1, n+1)
##    siap = 'from __main__ import a'
##    for i in jangkauan:
##        t = timeit.timeit('a(' + str(i) + ')', setup = siap, number = 1)
##        ls.append(t)
##    return ls
##
##n = 10
##LS = ujia(n)
##
##plt.plot(LS)
##skala = 7700000
##plt.plot([x*x/skala for x in range(1, n+1)])
##plt.show()
###==========No 8==========
##import time
##import random
##import timeit
##import matplotlib.pyplot as plt
##
##def a(n):
##    L = list(range(30))
##    L = L[::-1]
##    for i in range(n):
##        for b in range(n):
##            L.insert(i,b)
##
##def ujia(n):
##    ls = []
##    jangkauan = range(1, n+1)
##    siap = 'from __main__ import a'
##    for i in jangkauan:
##        t = timeit.timeit('a(' + str(i) + ')', setup = siap, number = 1)
##        ls.append(t)
##    return ls
##
##n = 100
##LS = ujia(n)
##
##plt.plot(LS)
##skala = 7700000
##plt.plot([x*x/skala for x in range(1, n+1)])
##plt.show()

###==========No 9a==========
##
import timeit
import time
import matplotlib.pyplot as plt


def carilurus(wadah, target):
    n = len(wadah)
    for i in range(n):
        if wadah[i] == target:
            return True
    return False

def tim():
    z=100
    a = [8, 7, 2, 1, 3, 2, 10]
    awal = time.time()
    U = carilurus(a, z)
    akhir=time.time()
    print("Worst case")
    print("mengurutkan %d bilangan, memerlukan %8.7f detik" %(U,akhir-awal))

tim()
###==========No 9b==========
import time
import random
import timeit
import matplotlib.pyplot as plt

def carilurus(wadah, target):
    n = len(wadah)
    for i in range(n):
        if wadah[i] == target:
            return True
    return False

def tim():
    z=100
    a = [8, 7, 2, 1, 3, 2, 10]
    awal = time.time()
    U = carilurus(a, z)
    akhir=time.time()
    print("Worst case")
    print("mengurutkan %d bilangan, memerlukan %8.7f detik" %(U,akhir-awal))

tim()


def a(n):
    z=100
    a = [8, 7, 2, 1, 3, 2, 10]
    U = carilurus(a, n)

def ujia(n):
    ls = []
    jangkauan = range(1, n+1)
    siap = 'from __main__ import a'
    for i in jangkauan:
        t = timeit.timeit('a(' + str(i) + ')', setup = siap, number = 1)
        ls.append(t)
    return ls

n = 10
LS = ujia(n)

plt.plot(LS)
skala = 7700000
plt.plot([x*x/skala for x in range(1, n+1)])
plt.show()
