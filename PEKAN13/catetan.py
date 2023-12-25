class Orang :
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def cetak(self):
        print("Nama Saya", self.fname, self.lname)

    def makan(self):
        print("saya bisa makan")

class Mahasiswa (Orang):
    def __init__(self, fname, lname, prodi, angkatan):
        super().__init__(fname,lname)
        self.prodi = prodi
        self.angkatan = angkatan

    def cetak(self):
        print("Nama Saya", self.fname, self.lname, self.prodi, self.angkatan)

class Pegawai (Orang):
    def bekerja(self):
        print("Saya bekerja", self.fname, self.lname)
    


# Object Orang
x = Orang ("Agus","Lapar Buk")
x.cetak()

# Object Mahasiswa
x = Mahasiswa ("Anton","Giting","Teknik Informatika","2023")
x.cetak()
x.makan()


# Object Pegawai
ww = Pegawai ("Anton","Hudi")
ww.bekerja()