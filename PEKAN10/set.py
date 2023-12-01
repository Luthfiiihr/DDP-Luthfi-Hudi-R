# Set berarti himpunan
# ● Tidak ada duplikasi, tidak ada jaminan urutan (Akan acak-ackan)
# ● Di Python dituliskan dengan dikurung oleh kurung kurawal { }

motor = {"beat", "vario", "aerox", "pcx"}
mobil = {"Civic", "Nissan GTR","Mini Cooper"}
print (motor)

# Menambah Item
motor.add ("nmax")
motor.add ("mio")
print(motor)

# Menghapus Item (beat)
motor.remove("beat")
print (motor)

# Set Union(Menggabunngkan)
kendaraan = motor.union(mobil)
print (kendaraan)

# Update
motor.update(mobil)
print(motor)