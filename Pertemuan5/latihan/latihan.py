#a
def Tambah(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return None
    baris, kolom = len(A), len(A[0])
    hasil = [[A[i][j] + B[i][j] for j in range(kolom)] for i in range(baris)]
    return hasil

#b
def Kurang(A, B):
    baris, kolom = len(A), len(A[0])
    hasil = [[A[i][j] - B[i][j] for j in range(kolom)] for i in range(baris)]
    return hasil

#c
def Skalar(matriks, k):
    hasil = []
    for baris in matriks:
        baris_baru = [elemen * k for elemen in baris]
        hasil.append(baris_baru)
    return hasil

A = [[5, 3, 1],
      [2, 8, 4],
      [6, 0, 7]]

B = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

C_tambah = Tambah(A, B)
print('Hasil penjumlahan matriks A dan B:')
for baris in C_tambah:
    print(baris)

C_kurang = Kurang(A, B)
print('Hasil pengurangan matriks A dan B:')
for baris in C_kurang:
 print(baris)

C_skalar = Skalar(A, 4)
print('Hasil skalar A:')
for baris in C_skalar:
    print(baris)
