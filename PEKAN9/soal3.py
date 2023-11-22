#Nomer 3

def ganjil(nilai):
    for i in range(nilai+1):
        if i % 2 != 0:
            print("Angka Ganjil:", i)
ganjil(100)