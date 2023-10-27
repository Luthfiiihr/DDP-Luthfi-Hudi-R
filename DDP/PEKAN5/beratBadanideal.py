#tinggi = int (input("Masukan tinggi Badan Anda: "))

#Untuk laki-laki
#BeratL = ( tinggi - 100) - (tinggi - 100) * 0.1


#Untuk Perempuan
#BeratP = ( tinggi - 100) - (tinggi - 100) * 0.15

print("""
=========================
Sistem penghitung berat badan ideal 

pilih jenis kelamin:
laki-laki = 1
perempuan = 2 
""")

jk = int(input("Masukan pilihan jenis kelamin:"))
tinggi = int (input("Masukan tinggi badan:"))

match jk :
    case 1:
        ideal = ( tinggi - 100) - (tinggi - 100) * 0.1
        print("berat badan ideal laki-laki untuk tinggi", tinggi,"adalah", ideal)
    case 2:
        ideal = ( tinggi - 100) - (tinggi - 100) * 0.15
        print("berat badan ideal perempuan untuk tinggi", tinggi,"adalah", ideal)
    case _:
        print("Pilihan yang ada msukan tidak valid")
