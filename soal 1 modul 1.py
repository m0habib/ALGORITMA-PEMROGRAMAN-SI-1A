def hitung_volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

panjang = float(input("Masukkan panjang balok: "))
lebar = float(input("Masukkan lebar balok: "))
tinggi = float(input("Masukkan tinggi balok: "))

volume = hitung_volume_balok(panjang, lebar, tinggi)

print(f"Volume balok adalah {volume} satuan kubik.")
