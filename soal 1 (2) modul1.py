import math

def hitung_tinggi_tabung(luas_selimut, diameter):
    jari_jari = diameter / 2  
    tinggi = luas_selimut / (2 * math.pi * jari_jari)
    return tinggi

def hitung_volume_tabung(diameter, luas_selimut):
    jari_jari = diameter / 2  
    tinggi = hitung_tinggi_tabung(luas_selimut, diameter)  
    volume = math.pi * jari_jari ** 2 * tinggi  
    return volume

diameter = float(input("Masukkan diameter alas tabung (cm): "))
luas_selimut = float(input("Masukkan luas selimut tabung (cm²): "))

volume = hitung_volume_tabung(diameter, luas_selimut)

print(f"Volume tabung adalah {volume:.2f} cm³.")
