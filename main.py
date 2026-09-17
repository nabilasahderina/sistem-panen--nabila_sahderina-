def hitung_total_panen(daftar_panen): return sum(daftar_panen)
panen_padi = [120, 150, 135, 160]
total = hitung_total_panen(panen_padi)
print(f"Total Hasil Panen Padi: {total} kg")
def hitung_diskon(total, persen): return total * (persen / 100)
