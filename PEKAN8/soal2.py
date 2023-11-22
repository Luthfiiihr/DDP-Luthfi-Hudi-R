#Nomer 2
nilai= int(input("Masukan Nilai:"))
def kelulusan(nilai):
  if nilai <= 60:
    return "Gagal"
  elif nilai <= 70:
    return "Baik"
  elif nilai <= 80:
    return "Sangat Baik"
  elif nilai <= 100:
    return "Gacor Kang"
  else :
    return "Nilai tidak valid"

print(kelulusan(nilai))
