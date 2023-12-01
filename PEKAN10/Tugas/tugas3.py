def duplikasi(daftar_buah):
    buah_duplikasi = []
    for buah in daftar_buah:
        buah_duplikasi.append(buah)
        buah_duplikasi.append(buah)
    return buah_duplikasi

buah_asli = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
hasil_duplikasi = duplikasi(buah_asli)
print(hasil_duplikasi)