

# Soal 1
# Membuat Modul Perhitungam Luas & Keliling Bangun Datar


# 1.)Persegi
def persegi(sisi):
    luas = sisi*sisi
    keliling = 4*sisi
    print("Luas Persegi :", luas)
    print("Keliling Persegi :", keliling)

# 2.)Persegi Panjang
def persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    print("Luas Persegi Panjang :", luas)
    print("Keliling Persegi Panjang:", keliling)

# 3.) Lingkaran 
def Lingkaran(jari_jari):
    phi = 3.14
    luas = phi * jari_jari * jari_jari
    keliling =  2 * phi * jari_jari
    print("Luas Lingkaran :", luas)
    print("Keliling Lingkaran :", keliling)

# 4.) Segitiga
def segitiga(alas, tinggi):
    luas = 1/2 * alas * tinggi
    keliling = alas * 3
    print("Luas Segitiga :", luas)
    print("Keliling Segitiga :", keliling)

# 5.) Belah Ketupat
def belah_ketupat(diagonal1, diagonal2, sisi):
    luas = 1/2 * diagonal1 * diagonal2
    keliling = 4 * sisi
    print("Luas Belah Ketupat :", luas)
    print("Keliling Belah Ketupat :", keliling)

# 6.) Jajar Genjang
def jajar_genjang(alas, tinggi, sisi_miring):
    luas = alas * tinggi
    keliling = 2 * alas + sisi_miring
    print("Luas Jajar Genjang :", luas)
    print("Keliling Jajar Genjang :", keliling)

# 7.) Layang-layang
def layang_layang(diagonal1, diagonal2, sisi_atas, sisi_bawah):
    luas = 1/2 * diagonal1 * diagonal2
    keliling = (sisi_atas * 2) + (sisi_bawah * 2)
    print("Luas Layang-Layang :", luas)
    print("Keliling Layang-Layang :", keliling)