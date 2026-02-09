print(25+30)

# operator

sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)
print(sum3)

# operator aritmatika

x = 40
y = 7

print(x + y)    # penjumlahan
print(x - y)    # pengurangan
print(x * y)    # perkalian
print(x / y)    # pembagian
print(x % y)    # modulus (sisa bagi)
print(x ** y)   # pangkat
print(x // y)   # pembagian bulat

# operator assignment

angka = [1, 2, 3, 4, 5]

if (jumlah := len(angka)) > 4:
    print(f"Terdapat {jumlah} elemen.")

# operator perbandingan

x = 9
y = 10

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# operator logika

x = 9
print(x > 0 and x < 10) # operator and


x = 8
print(x < 5 or x > 10) # operator or


x = 7
print(not(x > 3 and x < 10)) # operator not

# operator identitas

x = ["kelinci", "burung"]
y = ["kelinci", "burung"]
z = x

print(x is z)
print(x is y)

x = ["kelinci", "burung"]
y = ["kelinci", "burung"]

print(x is not y)

x = [10, 9, 8]
y = [10, 9, 8]

print(x == y) # is, mengecek ketika dua variable memiliki nilai yang sama di memori
print(x is y) # ==, mengecek ketika dua variable menunjuk ke object yang sama

# operator keanggotaan

angka = ["dua", "tiga", "empat"]
print("empat" in angka)

angka = ["dua", "tiga", "empat"]
print("lima" not in angka)

text = "Universitas Riau"

print("U" in text)
print("Universitas" in text)
print("g" not in text)

# operator bitwise

print(6 & 3)

print(6 | 3)

print(6 ^ 3)

print(~3)

print(3 << 2)

print(8 >> 2)

# operator presedens

print((6 + 3) - (6 + 3))

print(100 + 5 * 3)

print(5 + 4 - 7 + 3)