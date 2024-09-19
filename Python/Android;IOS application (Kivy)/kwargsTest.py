def hitung_segitiga(jenis_rumus, **kwargs):
    if jenis_rumus == 'luas':
        # Rumus luas: 1/2 * alas * tinggi
        alas = kwargs.get('alas', 0)
        tinggi = kwargs.get('tinggi', 0)
        if alas and tinggi:
            luas = 0.5 * alas * tinggi
            return f"Luas segitiga adalah: {luas}"
        else:
            return "Error: Perlu alas dan tinggi untuk menghitung luas!"

    elif jenis_rumus == 'keliling':
        # Rumus keliling untuk segitiga sembarang: a + b + c
        a = kwargs.get('a', 0)
        b = kwargs.get('b', 0)
        c = kwargs.get('c', 0)
        if a and b and c:
            keliling = a + b + c
            return f"Keliling segitiga adalah: {keliling}"
        else:
            return "Error: Perlu tiga sisi (a, b, c) untuk menghitung keliling!"

    elif jenis_rumus == 'sisi_miring':
        # Rumus sisi miring (Teorema Pythagoras): c = √(a² + b²)
        a = kwargs.get('a', 0)
        b = kwargs.get('b', 0)
        if a and b:
            sisi_miring = (a ** 2 + b ** 2) ** 0.5
            return f"Panjang sisi miring segitiga adalah: {sisi_miring}"
        else:
            return "Error: Perlu dua sisi (a, b) untuk menghitung sisi miring!"

    else:
        return "Jenis rumus tidak valid! Pilih antara 'luas', 'keliling', atau 'sisi_miring'."

# Contoh penggunaan:
print(hitung_segitiga('luas', alas=5, tinggi=12))        # Hitung luas segitiga   {"alas" : 5, "tinggi":12}
print(hitung_segitiga('keliling', a=5, b=12, c=13))      # Hitung keliling segitiga
print(hitung_segitiga('sisi_miring', a=5, b=12))         # Hitung sisi miring segitiga