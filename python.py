siswa ={"raka", "budi", "siti"}

for nama in siswa:
    nilai_matematika = int(input("Masukkan nilai matematika untuk " + nama + ": "))
    nilai_bahasa_indonesia = int(input("Masukkan nilai bahasa Indonesia untuk " + nama + ": "))
    nilai_bahasa_inggris = int(input("Masukkan nilai bahasa Inggris untuk " + nama + ": "))

    total_nilai = nilai_matematika + nilai_bahasa_indonesia + nilai_bahasa_inggris
    rata_rata = total_nilai / 3

    print("Rata-rata nilai: ", rata_rata )
    
