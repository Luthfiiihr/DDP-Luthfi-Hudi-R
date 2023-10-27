print(""" menghitung luas bangun datar
      pilih bangun datar yang ingin di hitung
      1. Menghitung luas bangun persegi
      2. menghitung luas bangun lingkaran
      3. menghitung luas bangun segitiga
       """)
rumusLuas=int (input("menhitung luas bangun datar:"))

match rumusLuas:
    case 1 :
        s= int(input("masukan angka:"))
        rumus1 = (s*s)
        print("hasil dari luas bangun persegi",rumus1)

    case 2 :
        π= int(3.14)
        r= int(input("masukan angka:"))
        rumus2 = (π*r*r)
        print("hasil dari luas bangun lingkaran",rumus2)      

    case 3 :
        a= int(input("masukan angka:"))
        t= int(input("masukan angka:"))
        rumus3 = (1/2*a*t)
        print("hasil dari luas bangun segitiga",rumus3)

    case _ :
        print("pilihan yang anda masukan tidak valid")      

