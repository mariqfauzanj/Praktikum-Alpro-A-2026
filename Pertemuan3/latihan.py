class Perang:
    def __init__(self, nama, umur, lokasi):
        self.nama = nama
        self.umur = umur
        self.lokasi = lokasi

    def sapa(self):
        return(f"{self.nama} telah bertempur selama {self.umur} tahun dan terletak di {self.lokasi}")
    
    def fire(self):
        print(f"{self.nama}, feuer!")

p1 = Perang("T-34", 90, "Rusia")
p2 = Perang("M4A3T2", 85, "Amerika")
p3 = Perang("Pz.34", 100, "Jerman")

print(p1.sapa())
print(p2.sapa())
print(p3.sapa())

print(p3.fire())

p3.nama = "Tiger II"
print(p3.nama)