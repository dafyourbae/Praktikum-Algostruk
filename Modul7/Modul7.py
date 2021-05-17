#####=======================Latihan=================
##import re
##s = 'sebuah contoh kata:teh!!'
##cocok = re.findall(r'kata:\w\w\w' , s)
###Pernyataan-IF sesudah findall()akan memeriksa apakah pencarian berhasil:
##if cocok:
##    print('menemukan', cocok)# 'menemukan [kata:teh]'
##else:
##    print('tidak menemukan')
##
###========LATIHAN 7.1==========
#### 'menemukan [kata:bat]'
##import re
##s = 'sebuah contoh kata:batagor!!'
##cocok = re.findall(r'kata:\w\w\w' , s)
##if cocok:
##    print('menemukan', cocok)
##else:
##    print('tidak menemukan')
##
##
##
##
##import re
##s = 'sebuah contoh kata:es teh!!'
##cocok = re.findall(r'kata:\w\w\w' , s)
##if cocok:
##    print('menemukan', cocok)
##else:
##    print('tidak menemukan')
##
###==========LATIHAN 7.2==========
####Dua baris ini mencari pola ’eee’ distring ’teeeh’.
####Seluruh pola harus cocok,tapi itu bisa muncul dimana saja.
####Jika berhasil, \texttt{cocok} adalah daftar semua teks yang cocok.
##import re
##cocok1 = re.findall(r'eee', 'teeeh') #=> cocok == [’eee’]
##cocok2 = re.findall(r'ehs', 'teeeh') #=> cocok == []
##
####.=semuakarakterkecuali\n
##cocok3 = re.findall(r'..h', 'teeeh') #=> cocok == ['eeh']
##
####\d = karakterangka,\w = karakter huruf atau angka
##cocok4 = re.findall(r'\d\d\d', 't123h di 2019 bulan 02') #=> cocok == [’123’,’201’]
##cocok5 = re.findall(r'\w\w\w', '@@a*bc#def*tghh!!') #=> cocok == [’def’,’tgh’]
##
##print(cocok1, cocok2, cocok3, cocok4, cocok5)
##
##
#####==========LATIHAN 7.3.1==========
##import re
####e+ = satu atau lebih e,sebanyak-banyaknya.
##cocok1 = re.findall(r'e+', 'ghdteeeh') #=> cocok == [’teee’]
##
####Menemukan solusi yang paling kiri,dan dari situ mendorong sitanda ‘+’
####sejauh-jauhnya(ingat’paling kiri dan paling besar’).
####Pada contoh ini,perhatikan bahwa pencarian menemukan dua pola yang tepat.
##cocok2 = re.findall(r'e+', 'teeheeee')
##
####\s* = nol atau lebih karakter putih(spasi,tab,dsb.)
####Disini mencari 3 angka,kemungkinan dipisahkan oleh spasi / tab
##polanya = r'\d\s*\d\s*\d'
##cocok3 = re.findall(polanya, 'xx1 2   3xx')
##cocok4 = re.findall(polanya, 'xx12 3xx')
##cocok5 = re.findall(polanya, 'xx123xx')
##
####^->cocok dengan awal string,jadi ini tidak akan menemukan:
##cocok6 = re.findall(r'^k\w+', 'mejakursi') #-> tidak ketemu, cocok==[]
##
####tapi tanpa ^ dia berhasil:
##cocok7 = re.findall(r'k[k\w\s]+', 'mejakursi tamu saya')#=> cocok == [’kursi tamu saya’]
##
##print(cocok1, cocok2, cocok3, cocok4, cocok5, cocok6, cocok7)


###==========LATIHAN 7.3==========
##import re
##s = 'Alamatku adalah dita-b@google.com mas'
##cocok6 = re.findall(r'\w+@\w+', s)
##print(cocok6[0]) 
##
###==========LATIHAN 7.3.2==========
##s = 'Alamatku adalah dita-b@google.com mas'
##import re
##cocok = re.findall(r'[\w.-]+@[\w.-]+', s)
##print(cocok[0])
##
##import re
##cocok = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', s)
##print(cocok[0]) 



#==========LATIHAN 7.4==========

##import re
##s = 'Alamatku adalah dita-b@google.com mas'
##cocok = re.findall(r'([\w.-]+)@([\w.-]+)' ,s)#perhatikan posisi() dipolanya
##cocok ##adalah [(’dita-b’, ’google.com’)]
###Bisa kita pilah satu persatu seperti ini:
##print(cocok[0][0]) # 'dita-b'
##print(cocok[0][1]) # 'google.com'
##
##
##import re
##s = 'Alamatku sri@google.com serta joko@abc.com ok bro. atau don@email.com mungkin daffa12288@gmail.com atau daffa@mail.com'
###Di sini re.findall() mengembalikan list beranggotakan string alamat
##pola = r'[\w\.-]+@[\w\.-]+'
##e = re.findall(pola, s) 
##print(e) 
##
###=>e akan berisi [’sri@google.com’, ’joko@abc.com’, ’don@email.com’]
##pola2 = r'([\w\.-]+)@([\w\.-]+)'
##e2 = re.findall(pola2, s)
##print(e2) 
#####Atau kita cetak satu per satu:
##for tup in e:
##    print('user', tup[0], 'dengan host: ', tup[1])


#==========LATIHAN 7.5==========
##import re
##s = 'Alamatku sri@google.com serta joko@abc.com ok bro. atau don@email.com mungkin daffa12288@gmail.com atau daffa@mail.com bisa jadi otong@mail.com ditambah sayang@yahoo.com'
##
##pola = r'[\w\.-]+@[\w\.-]+'
##e = re.findall(pola, s) #di sini re.findall() mengembalikan list beranggotakan string alamat
##print(e) 
##
##pola2 = r'([\w\.-]+)@([\w\.-]+)'
##e2 = re.findall(pola2, s)
##print(e2) 
##
##for tup in e:
##    print('user', tup[0], 'dengan host: ', tup[1])


#=======================Soal Mahasiswa=================
##import re
#####1  
##a = open('Indonesia.txt','r')
##baca = a.read()
##a.close
##cocok= re.findall(r"\sme\w+",baca)
##print(cocok)
##print("###############################################")
##2
##import re
##a = open('Indonesia.txt','r')
##baca = a.read()
##a.close
##cocok= re.findall(r"di\w+",baca)
##print(cocok)
##print("###############################################")

###3
##import re
##a = open('Indonesia.txt','r')
##baca = a.read()
##a.close
##cocok= re.findall(r"di\s\w+",baca)
##print(cocok)
##print("###############################################")

###4
import re
f = open('KEI.html', 'r', encoding='latin1')
teks = f.read()
f.close()
i = r'\s<td>[\d.\w/]+</td>'
p = r'(\w+)</a></td>' + i + i + i + r'\s<td>([\d.\w/]+)</td>'
cocok = re.findall(p, teks)
cocok1 = [(i[0], float(i[1])) for i in cocok]
print(cocok1)
print("###############################################")
