tinggi = int (input("Masukan tinggi Badan Anda: "))

#Untuk laki-laki
BeratL = ( tinggi - 100) - (tinggi - 100) * 0.1


#Untuk Perempuan
BeratP = ( tinggi - 100) - (tinggi - 100) * 0.15

print("Berat badan ideal laki-laki: ", BeratL, "kg")
print("Berat badan ideal perempuan: ", BeratP, "kg")