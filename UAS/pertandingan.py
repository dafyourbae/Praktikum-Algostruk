##Daffa Putra Alwansyah (L200190031)

from prettytable import PrettyTable #import pretty tabble biar rapi
import pandas as pd #import library pandas untuk import file xlsx

#membuat variabel untuk membaca excel
df = pd.read_excel(r'./pertandingan.xlsx', engine='openpyxl')
#merubah kelist
df_list = df.values.tolist()

#membuat perulangan input user
while True:
    print("===Menu Pilihan===")
    print("Masukan 1 untuk mengurutkan tempat")
    print("Masukan 2 untuk mengurutkan waktu awal ke akhir")
    print("Masukan 3 untuk mengurutkan waktu akhir ke awal")
    print("Masukan 4 untuk keluar aplikasi")
    #membuat variabel input
    input_menu = int(input("Masukan menu pilihan:"))

    #membuat kelas dan function init pildun
    class pildun:
        def __init__(self,pick):
            self.negara = pick[0]
            self.tempat = pick[1]
            self.waktu = pick[2]
    #membuat variabel table agar output masuk ke tabel      
    table = PrettyTable(["Pertandingan","Tempat","Jadwal"])
    #membuat list kosong
    list_pd = []
    #membuat perulangan untuk mengappend
    for i in range(len(df_list)):
        list_pd.append(pildun(df_list[i]))

    #membuat kondisi untuk user saat melakukan input
    if input_menu ==1:
        def sort_place(data):
            x = len(data)
            for i in range (x):
                for j in range(0,x-1,1):
                    #jika index kiri lebih besar dari index kanan maka swap
                    if data[j].tempat > data[j+1].tempat:
                        #swap langsung
                        data[j], data[j+1] = data[j+1], data[j]
        sort_place(list_pd)
        #melakukan add pada row table
        for i in list_pd:
            table.add_row([i.negara, i.tempat, i.waktu])
        print(table)
        
    #membuat kondisi untuk user saat melakukan input    
    if input_menu ==2:
        def sort_place(data):
            x = len(data)
            for i in range (x):
                for j in range(0,x-1,1):
                    #jika index kiri lebih besar dari index kanan maka swap
                    if data[j].waktu > data[j+1].waktu:
                        #swap langsung
                        data[j], data[j+1] = data[j+1], data[j]
        sort_place(list_pd)
        #melakukan add pada row table
        for i in list_pd:
            table.add_row([i.negara, i.tempat, i.waktu])
        print(table)
        
    #membuat kondisi untuk user saat melakukan input
    if input_menu ==3:
        def sort_place(data):
            x = len(data)
            for i in range (x):
                for j in range(0,x-1,1):
                    #jika index kiri lebih kecil dari index kanan maka swap
                    if data[j].waktu < data[j+1].waktu:
                        #swap langsung
                        data[j], data[j+1] = data[j+1], data[j]
        sort_place(list_pd)
        #melakukan add pada row table
        for i in list_pd:
            table.add_row([i.negara, i.tempat, i.waktu])
        print(table)

    #membuat kondisi untuk user saat melakukan input
    if input_menu == 4:
        print("Keluar Aplikasi")
        break


 
        

    
    
