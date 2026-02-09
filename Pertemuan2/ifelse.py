# if

a = 70
b = 250
if b > a:
  print("b lebih besar a")

apakah_masuk = True
if apakah_masuk:
  print("Selamat datang!")

# elif

a = 35
b = 35
if b > a:
  print("b lebih besar dari a")
elif a == b:
  print("a dan b sama")

nilai = 75
if nilai >= 85:
  print("Nilai: A")
elif nilai >= 75:
  print("Nilai: B")
elif nilai >= 60:
  print("Nilai: C")
elif nilai >= 50:
  print("Nilai: D")
elif nilai >= 40:
  print("Nilai: E")
elif nilai < 40:
  print("Nilai: F")

# else

a = 700
b = 699
if b > a:
  print("b lebih besar dari a")
elif a == b:
  print("a dan b sama")
else:
  print("a lebih besar dari b")

# shorthand if

a = 5
b = 2
if a > b: print("a is greater than b")

# shorthand if ... else

a = 20
b = 300
print("A") if a > b else print("B")

a = 350
b = 350
print("A") if a > b else print("=") if a == b else print("B")

# nested if

x = 41
if x > 10:
  print("Di atas 10,")
  if x > 25:
    print("dan di atas 25!")
  else:
    print("namun tidak di atas 25.")

nilai = 85
kehadiran = 90
submitted = True

if nilai >= 50:
  if kehadiran >= 75:
    if submitted:
      print("Lulus.")
    else:
      print("Lulus dengan nilai B+.")
  else:
    print("Lulus dengan nilai C.")
else:
  print("Ga lulus.")

# pass statement

a = 50
if a < 0:
  print("Nilai negatif.")
elif a == 0:
  pass # Nol, tanpa hasil
else:
  print("Nilai positif.")