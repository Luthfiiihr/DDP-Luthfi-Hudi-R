

daftar_buah = ['rambutan', 'jambu', 'mangga', 'pepaya', 'pisang']

# Mengakses dengan index
print("========================")
print (daftar_buah[-4:-1])
print("========================")
# Len (Untuk menghitung jumlah daftar list)
print(len(daftar_buah))
print("========================")
# Cek keberadaan nilai
if "pisang" in daftar_buah:
    print("Terdapat pisang")
    print("========================")
else :
    print ("Tidak terdapat pisang")
    print("========================")

# Looping list
for Buah in daftar_buah :
    print (Buah)