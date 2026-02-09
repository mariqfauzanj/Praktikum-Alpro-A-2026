kendaraan = ["mobil", "sepeda", "kuda"]
for x in kendaraan:
  print(x)

for x in "Python":
  print(x)

kendaraan = ["mobil", "sepeda", "kuda"]
for x in kendaraan:
  print(x)
  if x == "sepeda":
    break

kendaraan = ["mobil", "sepeda", "kuda"]
for x in kendaraan:
  if x == "sepeda":
    break
  print(x)

kendaraan = ["mobil", "sepeda", "kuda"]
for x in kendaraan:
  if x == "sepeda":
    continue
  print(x)

for x in range(5):
  print(x)

for x in range(2, 5):
  print(x)

for x in range(2, 14, 3):
  print(x)

warna = ["putih"]
benda = ["mobil", "kapal"]
for x in benda:
  for y in warna:
    print(x, y)