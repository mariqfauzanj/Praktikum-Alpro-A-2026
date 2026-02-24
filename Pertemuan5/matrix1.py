matriks_3x3 = [[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

matriks_2x4 = [[10, 20, 30, 40],
 [50, 60, 70, 80]]
print('Matriks 3x3:', matriks_3x3)
print('Matriks 2x4:', matriks_2x4)

N, M = 4, 4
matriks_default = [[0 for j in range(M)] for i in range(N)]
print('Matriks default:', matriks_default)

matriks_neg = [[-1 for j in range(5)] for i in range(3)]
print('Matriks -1:', matriks_neg)