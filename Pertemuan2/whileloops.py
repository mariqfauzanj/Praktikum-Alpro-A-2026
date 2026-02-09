i = 1
while i < 5:
  print("Tes", i)
  i += 1

i = 1
while i < 6:
  print("Break", i)
  if i == 2:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print("Continue", i)

i = 1
while i < 4:
  print(i)
  i += 1
else:
  print("Hai!")