#kalkulator
while true :
    print("Pilih operasi matematika:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

    if pilihan == '5':
        print("keluar")
        break

    num1 = float(input("Masukkan angka pertama: "))
    num2 = float(input("Masukkan angka kedua: "))

    if pilihan == '1':
        hasil = num1 + num2
        print(f"Hasil: {num1} + {num2} = {hasil}")
    elif pilihan == '2':
        hasil = num1 - num2
        print(f"Hasil: {num1} - {num2} = {hasil}")
    elif pilihan == '3':
        hasil = num1 * num2
        print(f"Hasil: {num1} * {num2} = {hasil}")
    elif pilihan == '4':
        if num2 != 0:
            hasil = num1 / num2
            print(f"Hasil: {num1} / {num2} = {hasil}")
        else:
            print("Error: Pembagian dengan nol tidak diperbolehkan.")
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        