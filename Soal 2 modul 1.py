def cari_a_b(U5, total_U8_U12):

    for b in range(-100, 100):  
        a = (total_U8_U12 - 18 * b) / 2
        if a + 4 * b == U5:  
            return a, b

def hitung_jumlah_suku_pertama(a, b, n):
    return (n / 2) * (2 * a + (n - 1) * b)

U5 = float(input("Masukkan nilai suku ke-5 dari deret (U5): "))
total_U8_U12 = float(input("Masukkan jumlah dari suku ke-8 dan suku ke-12 (U8 + U12): "))

a, b = cari_a_b(U5, total_U8_U12)

jumlah_8_suku_pertama = hitung_jumlah_suku_pertama(a, b, 8)

print(f"Suku pertama (a) = {a}")
print(f"Beda (b) = {b}")
print(f"Jumlah 8 suku pertama adalah {jumlah_8_suku_pertama:.2f}")
