import math

def kombinasi(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))

n = int(input("Masukkan jumlah total orang: "))
r = int(input("Masukkan jumlah orang yang ingin dipilih: "))

jumlah_cara = kombinasi(n, r)

print(f"Jumlah cara untuk memilih {r} orang dari {n} orang adalah {int(jumlah_cara)} cara.")
