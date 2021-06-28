from prettytable import PrettyTable
import pandas as pd

df = pd.read_excel(r'./pertandingan.xlsx', engine='openpyxl')
df_list = df.values.tolist()
   
while True:
    print("===Menu Pilihan===")
    print("Masukan 1 untuk mengurutkan tempat")
    print("Masukan 2 untuk mengurutkan waktu awal ke akhir")
    print("Masukan 3 untuk mengurutkan waktu akhir ke awal")
    print("Masukan 4 untuk keluar aplikasi")
    input_menu = int(input("Masukan menu pilihan:"))
    class pildun:
        def __init__(self,pick):
            self.negara = pick[0]
            self.tempat = pick[1]
            self.waktu = pick[2]
            
    table = PrettyTable(["Pertandingan","Tempat","Jadwal"])
    list_pd = []
    for i in range(len(df_list)):
        list_pd.append(pildun(df_list[i]))
    
    if input_menu ==1:
        def sort_place(data):
            x = len(data)
            for i in range (x):
                for j in range(0,x-1,1):
                    if data[j].tempat > data[j+1].tempat:
                        data[j], data[j+1] = data[j+1], data[j]
        sort_place(list_pd)
        for i in list_pd:
            table.add_row([i.negara, i.tempat, i.waktu])
        print(table)
        
    if input_menu ==2:
        def sort_place(data):
            x = len(data)
            for i in range (x):
                for j in range(0,x-1,1):
                    if data[j].waktu > data[j+1].waktu:
                        data[j], data[j+1] = data[j+1], data[j]
        sort_place(list_pd)
        for i in list_pd:
            table.add_row([i.negara, i.tempat, i.waktu])
        print(table)

    if input_menu ==3:
        def sort_place(data):
            x = len(data)
            for i in range (x):
                for j in range(0,x-1,1):
                    if data[j].waktu < data[j+1].waktu:
                        data[j], data[j+1] = data[j+1], data[j]
        sort_place(list_pd)
        for i in list_pd:
            table.add_row([i.negara, i.tempat, i.waktu])
        print(table)
        
    if input_menu == 4:
        print("Keluar Aplikasi")
        break

    if input != int(1,2,3 and 4):
        print("salah input")

 
        

    
    
