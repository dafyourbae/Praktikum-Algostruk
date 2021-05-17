#Nomor1

#Persegi
def luas_persegi(): #membuat fungsi luas persegi
    print("Program menghitung luas Persegi")
    sisi = float(input("Input sisi persegi: ")) #variabel sisi untuk menginput nilai sisi, type data float
    luas = sisi * sisi #variabel menghitung luas persegi 
    print ("Luas Persegi: ", str(luas), "satuan luas") #menampilkan hasil Luas Persegi dan mengconvert ke string
    
#Lingkaran
def luas_lingkaran(): #membuat fungsi luas lingkaran
    print("Program menghitung luas Lingkaran")
    phi = 3.14 #variabel phi dengan nilai 3.14
    jari = float(input("Input jari-jari lingkaran: ")) #variabel jari untuk menginput nilai jari-jari, type data float
    luas = phi * jari * jari #variabel untuk menghitung Luas Lingkaran
    print("Luas lingkaran: ", str(luas), "satuan luas") # menampilkan hasil Luas Lingkaran dan mengkonvert ke string
    
#Segitiga sama sisi
def luas_segsamasisi(): #Membuat fungsi luas segitiga sama sisi
    print("Program menghitung luas Segitiga Sama Sisi")
    alas = float(input("Input alas: ")) #variabel alas untuk menginput nilai alas, type data float
    tinggi = float(input("Input tinggi: ")) #variabel tinggi untuk menginput input tinggi, type data float
    luas = (1/2) * alas * tinggi #variabel untuk menghitung luas Segitiga Sama Sisi
    print("Luas Segitiga Sama Sisi: ", str(luas), "satuan luas") #menampilkan hasil Luas Segitiga Sama Sisi dan mengkonvert ke string
 
#BelahKetupat
def luas_belahketupat(): #Membuat fungsi luas belah ketupat
    print("Program menghitung luas Belah Ketupat")
    d1 = float(input("Masukan diagonal 1 Belah Ketupat: ")) #variabel d1 untuk menginput nilai diagonal 1, type data float
    d2 = float(input("Masukan diagonal 2 Belah Ketupat: ")) #variabel d2 untuk menginput nilai diagonal 2, type data float
    luas = (1/2) * d1 * d2 #variabel untuk menghitung luas Belah Ketupat
    print("Luas Belah Ketupat: ", str(luas), "satuan luas") #menampilkan hasil Luas Belah Ketupat dan mengkonvert ke string


##Nomor 2
#A
A = [[1,2]] #ordo 1x2
B = [[1,2,3], [1,2,3]] #ordo 2x3
def kali_matriks(matriks1,matriks2): #membuat fungsi dengan nama kali_matriks
    p = [] #menampung baris matriks
    for a in range(len(matriks1)): #iterasi matriks A
        #menampung kolom perbaris
        new =[]
        for b in range(len(matriks2[0])): #iterasi matriks B
            #perkalian periteem pada kolom
            x = 0
            for c in range(len(matriks2)):
                x += matriks1[a][c] * matriks2[c][b]
            #hasil perkalian dimasukan ke dalam kolom baris new
            new.append(x)
        p.append(new) #hasil dimasukan kedalam list p
    print("Hasil dari perkalian ordo:" , p)

#B
def matriks_identitas(a):
    print("matriks identitas ordo: "+str(a)+"x"+str(a)) #menampilkan ordo
    #variabel matriks_id berisi iterasi untuk membuat kolom dan baris pada matriks
    matriks_id = [[1 if j == C else 0 for j in range(a)] for C in range(a)]
    for x in matriks_id: #iterasi didalam matriks
        print(x) #menampilkan hasil

##Nomor 3
class MhsTIF(object): #membuat kelas mhsTIF
    def __init__(self,nama,umur,warnaKulit): #membuat inisialiasi propeti
        self.nama = nama #inisialiasai self.nama
        self.umur = umur #inisialiasi self.umur
        self.warnaKulit = warnaKulit #inisialiasi self.warnaKulit
        
#membuat 11 data pada kelas mhsTIF
c0 = MhsTIF('Daffa', 20, "Sawo Matang")
c1 = MhsTIF('Putra', 21, "Kuning Langsat")
c2 = MhsTIF('Alwansyah', 19, "Hitam")
c3 = MhsTIF('Ammar', 23, "Putih")
c4 = MhsTIF('Markotong', 22, "Hitam")
c5 = MhsTIF('Noval', 20, "Sawo Matang")
c6 = MhsTIF('Haris', 24, "Putih")
c7 = MhsTIF('Pandu', 25, "Sawo Matang")
c8 = MhsTIF('Khasan', 23, "Sawo Matang")
c9 = MhsTIF('Hanafi', 21, "Hitam")
c10 = MhsTIF('Dimas', 20, "Kuning Langsat")
#memasukan var c0-c10 kedalam Daftar
Daftar=[c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

##Fungsi Tampil Nama
def dataNama(x): #membuat fungsi dataNama
    for i in x: #melakukan iterasi
        print(i.nama) #setelah iterasi menampilkan nama
        
##Fungsi Tampil Umur
def dataUmur(x): #membuat fungsi dataUmur
    for i in x: #melakukan iterasi
        print(i.umur) #setelah iterasi manmpilkan umur
        
##Fungsi Tampil Warna Kulit
def warnaKulit(x):
    for i in x: #melakukan iterasi
        print(i.warnaKulit) #setelah iterasi menampilkan warna kulit

##Nomor 4
#Linier Search
def cari_kulit(x): #fungsi mencari kulit
    for i in range(len(Daftar)): #iterasi pada Daftar
        if x == Daftar[i].warnaKulit: #jika key == warna kulit didaftar, maka
            #menampilkan nama dan warna kulit pada iterasi Daftar
            print(Daftar[i].nama,"memiliki warna kulit: ",Daftar[i].warnaKulit)


#Nomor 5
#Fungsi swap yang digunakan untuk menukar posisi
def swap(i,j,k):
    temp = i[j]
    i[j]=i[k]
    i[k]=temp
    
#Funsi cari umur dari terkecil
#Bubble Sort
def urut_umur(i):
    p = len(i)
    #melakukan iterasi pada Daftar - 1
    for x in range(p-1):
        #melakukan iterasi Daftar - iterasi - 1
        for y in range(p-x-1):
            #jika data current lebih besar dari selanjutnya maka akan dilakukan swap
            if i[y].umur > i[y+1].umur:
                swap(i,y,y+1)
                
#Fungsi untuk mengecek Daftar
def cek_umur(Daftar):
    for z in Daftar: #iterasi pada Daftar
        print(z.nama, z.umur, z.warnaKulit) #menampilkan isi pada Daftar


