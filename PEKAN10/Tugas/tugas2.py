buah_asli = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

def balik (nama_buah):
    buah_buahan = len(nama_buah)
    buah_terbalik = []
    for i in range (buah_buahan -1, -1, -1):
        buah_terbalik.append (nama_buah[i])

    return buah_terbalik

buah_terbalik = balik(buah_asli)
print(buah_terbalik)
