# Untuk menyimpan data yang diakses bukan dengan indeks
# ● Data disimpan sebagai pasangan dari key dan value
# ● Dituliskan dengan diapit kurung kurawal { } dan dipisah dengan titik dua (:)

data_diri = {"Nama":"Luthfi","Mapel":"DDP"}

# Mengkases dictionary
print("========================")
print(data_diri["Nama"])
print("========================")
# Menambahkan item
data_diri["Jurusan"] = "Teknik Informatika"
print(data_diri)

# Update Item
data_diri["Nama"] = "Qich"
print (data_diri)

# Menghapus item
data_diri.pop("Nama")
print(data_diri)

# Mengecek keberadaan key
if "Nama" in data_diri:
    print ("Nama ada")

else :
    print ("Tidak ada Nama")
# Masih Gagal