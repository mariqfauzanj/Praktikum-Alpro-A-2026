# no.2

def is_password_valid(password):
    password = "Password123"
    is_Aktif = True

    if password:
        if is_Aktif:
            print("Login sukses")
        else:
            print("Login Error")

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
