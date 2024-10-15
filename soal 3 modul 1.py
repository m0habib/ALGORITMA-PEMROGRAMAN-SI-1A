def konversi_usd_ke_idr(usd, kurs):
    return usd * kurs

kurs = 15040  

usd = float(input("Masukkan jumlah uang dalam USD: "))

idr = konversi_usd_ke_idr(usd, kurs)

print(f"{usd} USD sama dengan {idr} IDR.")
