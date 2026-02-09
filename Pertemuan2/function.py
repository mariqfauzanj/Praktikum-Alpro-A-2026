def fungsiWatashi():
  print("Halo! Watashi sedang belajar!")

fungsiWatashi()


def fungsiFungsian(name="Riki"):
  print("Hai", name)

fungsiFungsian("kawan")
fungsiFungsian()

# beda parameter dan argument

def salamDariKawan(): # ini parameter
  return "Hai sanak!"

message = salamDariKawan() # ini argument
print(message)

# *args argh...

def fungsiKata(*args):
    print("Type:", type(args))
    print("Argumen ke-1:", args[0])
    print("Argumen ke-2:", args[1])
    print("Semua argumen:", args)

fungsiKata("Mule", "You", "No")

# scope

def myfunc(): # local
  x = 300
  print(x)

myfunc()

x = 300 # global

def myfunc():
  print(x)

myfunc()

print(x)

# lambda (half-life)

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))