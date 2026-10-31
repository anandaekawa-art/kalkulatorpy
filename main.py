import random

angka_acak = random.randint(1, 25)
print("Tebak angka antara 1 sampai 25")

for i in range(5):
    tebakan = int(input("Masukkan tebakan Anda: "))
    if tebakan == angka_acak:
        print("Selamat! Tebakan Anda benar.")
        break
    elif tebakan < angka_acak:
        print("Angka yang ditebak terlalu rendah.")
    else:
        print("Angka yang ditebak terlalu tinggi.")
else:
    print("Maaf, Anda telah kehabisan kesempatan. Angka yang benar adalah:", angka_acak)