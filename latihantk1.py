from tkinter import * #import library tkinter
import sqlite3        #import library SQLite

#Fungsi Ketika Button di Klik
#Button 1 / Mencari Rekomendasi Prodi
def bclick(): 

    global prodi_terpilih   #Menjadikan Variable prodi_terpilih sebagai global
    Matkul = {
        "Teknik": e2.get(),
        "Kedokteran": e3.get(),
        "Kedokteran": e4.get(),
        "Bahasa": e5.get(),
        "Bahasa": e6.get()
        
    }

    #Mencari prodi terpilih berdasarkan nilai matakuliah
    prodi_terpilih = max(Matkul, key=Matkul.get)

    #menampilkan prodi terpilih pada label hasil / label result
    Res.config(text=f"Hasil Prediksi: {prodi_terpilih}")

#Button 2 Menyimpan Nama, Nilai Fisika, Nilai Biologi, Nilai Bahasa Inggris, 
#dan prodi_terpilih kedalam database
def simpan_nilai():
    
    #Membuka / Membuat database SQLite
    conn = sqlite3.connect("dbtkinter.db")
    cursor = conn.cursor()

    #Membuat Tabel jika belum ada
    cursor.execute('''CREATE TABLE IF NOT EXISTS hasil_prediksi
    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nama STRING,               
    nilai_FIS INTEGER, 
    nilai_BIO INTEGER,
    nilai_BING INTEGER,
    prodi_terpilih TEXT)''')

    # Memasukkan data mata pelajaran ke dalam tabel
    cursor.execute("INSERT INTO hasil_prediksi (nama, nilai_FIS, nilai_BIO, nilai_BING, prodi_terpilih ) VALUES (?, ?, ?, ?, ?)",
    (enama.get() ,e2.get(), e4.get(), e6.get() ,prodi_terpilih))

    # Melakukan commit dan menutup koneksi
    conn.commit()
    conn.close()


window = Tk()
window.title = "Aplikasi Rekomendasi Prodi"
window.resizable(0,0)                       #Window Resizeable = NO
window.geometry('330x650')                  #Windows Size = lebar x tinggi

#BUTTON
button1 = Button(text="Cari Hasil!", command=bclick)
button1.grid(column=0, row=13,sticky='WE', padx= 50)

button2 = Button(text="Simpan Nilai", command=simpan_nilai)
button2.grid(column=1,row=13,sticky='WE')


#LABEL BESAR
Judul1 = Label(text='Aplikasi Rekomendasi Prodi', font=("Arial", 16))
Judul1.grid(row=0, rowspan=1, columnspan=2, sticky= 'WE', pady= 20, padx= 20)

Judul2 = Label(text="Masukkan Nilai MataKuliah: ")
Judul2.grid(row=2, column=0)


#LABEL KECIL
#Menempatkan Label pada kolom 0 / sebelah kiri

labelnama = Label(text="Masukkan Nama: ")
labelnama.grid(column=0, row=1)

mk1 = Label(text="Matematika :")
mk1.grid(column=0, row=3)

mk2 = Label(text="Fisika :")
mk2.grid(column=0, row=4)

mk3 = Label(text="Kimia :")
mk3.grid(column=0, row=5)

mk4 = Label(text="Biologi :")
mk4.grid(column=0, row=6)

mk5 = Label(text="Bahasa Indonesia :")
mk5.grid(column=0, row=7)

mk6 = Label(text="Bahasa Inggris :")
mk6.grid(column=0, row=8)

mk7 = Label(text="Sejarah Indonesia :")
mk7.grid(column=0, row=9)

mk8 = Label(text="Geografi :")
mk8.grid(column=0, row=10)

mk9 = Label(text="Ekonomi :")
mk9.grid(column=0, row=11)

mk10 = Label(text="Sosiologi :")
mk10.grid(column=0, row=12)


#Membuat Entry
enama = Entry(window)
enama.grid(column=1, row=1, pady=10)

e1 = Entry(window)
e1.grid(column=1, row=3, pady=10)
e2 = Entry(window)
e2.grid(column=1, row=4, pady=10)
e3 = Entry(window)
e3.grid(column=1, row=5, pady=10)
e4 = Entry(window)
e4.grid(column=1, row=6, pady=10)
e5 = Entry(window)
e5.grid(column=1, row=7, pady=10)
e6 = Entry(window)
e6.grid(column=1, row=8, pady=10)
e7 = Entry(window)
e7.grid(column=1, row=9, pady=10)
e8 = Entry(window)
e8.grid(column=1, row=10, pady=10)
e9 = Entry(window)
e9.grid(column=1, row=11, pady=10)
e10 = Entry(window)
e10.grid(column=1, row=12, pady=10)

#Label Hasil / Result Label
Res = Label(text="Masukkan nilai terlebih dahulu!", font=("Garamond",15))
Res.grid(columnspan=2, row=14, pady= 20)

window.mainloop()