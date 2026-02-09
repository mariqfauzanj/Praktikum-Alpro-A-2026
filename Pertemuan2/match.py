bahasa = 3
match bahasa:
  case 1:
    print("English")
  case 2:
    print("Indonesia")
  case 3:
    print("Python")
  case 4:
    print("C")

bahasa = 4
match bahasa:
  case 6:
    print("Rust")
  case 7:
    print("C")
  case _:
    print("Python")

suka = 5
pilih = 4
match pilih:
  case 1 | 2 | 3 | 4 | 5 if suka == 4:
    print("C")
  case 1 | 2 | 3 | 4 | 5 if suka == 5:
    print("Python")
  case _:
    print("None")