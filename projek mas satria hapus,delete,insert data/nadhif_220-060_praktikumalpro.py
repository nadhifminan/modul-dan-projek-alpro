data1=[]
data2=[]
stop=False
while not(stop):
    print("""
+-----------------------------+
|     MENU DATA MAHASISWA     |
+-----------------------------+
| 1.Tambah Mahasiswa          |
| 2.Edit Mahasiswa            |
| 3. Hapus Mahasiswa          |
| 4.Tampilan Data             |
| 5.Quit                      |
+-----------------------------+
    """)
    pilihan=int(input('-->Masukkan Pilihan :'))
    if pilihan==1:
        namanya=input('Nama mahasiswa :')
        data1.append(namanya)
        nimnya=int(input('NIM Mahasiswa :'))
        data2.append(nimnya)
        print(data2)
        print('!! Data berhasil ditambahkan')
    elif pilihan==2:
        caridata=int(input('Cari NIM Mahasiswa :'))
        a = data2.index(caridata)
        print(f'''
+-------------------------+
|     DATA MAHASISWA      |
+-------------------------+
Nama Mahasiswa :
{data1[a]}
NIM Mahasiswa  :
{data2[a]}
---------------------------
== Edit mahasiswa ==
          ''')
    elif pilihan==3:
        namanya3=input('-->masukkan Nama Mahasiswa:')
        h=data1.index(namanya3)
        data1.pop(h)
        data2.pop(h)
        print('!!data berhasil diedit!!')
    elif pilihan==4:
        for i in range(len(data1)):
            print('''
+-------------------------+
|     DATA MAHASISWA      |
+-------------------------+
                ''')
            for i in range(len(data1)):
                print(f'''
+-----------------------------------+
| Nama Mahasiswa :{data1[i]}        |
| NIM Mahasiswa  :{data2[i]}        |
+-----------------------------------+
                    ''')
    elif pilihan==5:
        stop=True
    else:
        print('!!Menu yang anda pilih tidak ada di menu silahkan pilih menu yang lain!!')