# no.1

def fizzbuzz_plus(n):
    for n in range(1, n + 1):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        elif n % 7 == 0:
            print("Seven")
        else:
            print(n)

fizzbuzz_plus(21)

# no.2

def is_password_valid(password):
    is_hurufBesar = False
    is_angka = False
    if len(password) >= 8:
        for n in password:
            if n == " ":
                return False
            if n.isupper():
                is_hurufBesar = True
            if n.isnumeric():
                is_angka = True
        if is_hurufBesar and is_angka:
            return True
        else:
            return False
    else:
        return False

# no.3

def hitung_nilai(tugas, uts, uas):
    nilai = (tugas*0.3) + (uts*0.3) + (uas*0.4)

    print("Nilai: ", nilai)
    if nilai >= 85:
        print("Grade: A")
    elif nilai >= 70:
        print("Grade: B")
    elif nilai >= 55:
        print("Grade: C")
    elif nilai >= 40:
        print("Grade: D")
    elif nilai < 40:
         print("Grade: E")

hitung_nilai(80, 75, 90)
