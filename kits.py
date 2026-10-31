

while True:
    print("===*****************===")
    print(" kalkulator")
    print("1.penjumlahan")
    print("2.pengurangan")
    print("3.pembagian")
    print("4.perkalian")
    print("5.keluar")
    
    pilihan =int(input("masukan pilihan: "))

    if pilihan == 5:
          print (" gak ada kocak pilihanya cuman 4 ")      
          break             

    a = int(input("masukan nilai a: "))
    b = int(input("masukan nilai b: "))


    
    if pilihan ==1:
             def penjumlahan (a, b):
                 print(f"{a} + {b} = {a + b}")
    
    elif pilihan ==2:
             def pengurangan (a, b):
                  print(f"{a} - {b} = {a - b}")

    elif pilihan ==3:
              def pembagian (a, b):
                  print(f"{a} / {b} = {a / b}")

    elif pilihan ==4:
             def perkalian (a, b):
                 print(f"{a} * {b} = {a * b}")    
         
    if pilihan ==1:
         penjumlahan (a, b)

    elif pilihan ==2: 
         pengurangan (a, b)

    elif pilihan ==3:
         pembagian (a, b)

    elif pilihan ==4:
          perkalian (a, b)
    