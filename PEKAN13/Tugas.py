class Animal:

    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def info(self):
        print("="*40)
        print("Nama  :", self.nama)
        print("Makanan :", self.makanan)
        print("Hidup :", self.hidup)
        print("Berkembang Biak :", self.berkembang_biak)

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, habitat, jenis_ikan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.habitat = habitat
        self.jenis_ikan = jenis_ikan

    def cetak(self):
        super().info()
        print("Habitat :", self.habitat)
        print("Jenis Ikan :", self.jenis_ikan)



class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, beracun, cara_memangsa):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.beracun = beracun
        self.cara_memangsa = cara_memangsa

    def cetak(self):
        super().info()
        print("Beracun :", self.beracun)
        print("Cara Memangsa :", self.cara_memangsa)


class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, berbahaya, membangun_sarang):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.berbahaya = berbahaya
        self.membangun_sarang = membangun_sarang

    def cetak(self):
        super().info()
        print("Berbahaya :", self.berbahaya)
        print("Membangun Sarang :", self.membangun_sarang)


# Ikan
ikan = Ikan("Nemo", "plankton", "di air", "beranak", "di laut", "Ikan badut")
ikan.cetak()

# Ular
ular = Ular("Ular sawah", "Tikus", "di darat", "bertelur", "tidak beracun", "Melilitkan badan ular ke musuh")
ular.cetak()

# Burung
burung = Burung("Burung Hantu", "Tikus", "di udara", "bertelur", "tidak berbahaya", "pohon")
burung.cetak()
