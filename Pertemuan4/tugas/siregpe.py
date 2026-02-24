class NamaError(Exception):
    pass

class UmurError(Exception):
    pass

def main():
    while True:
        try:
            nama = input('Nama lengkap: ').strip()
            if len(nama.split()) < 3:
                raise NamaError('Nama terlalu pendek! Minimal 3 karakter.')  
                 
            break

        except NamaError as e:
            print(f'[ERROR] {e}')

    while True:
        try:            
            umur = int(input('Umur: ').strip())
            if umur < 17 or umur > 60:
                raise UmurError('Umur tidak memenuhi syarat (17-60 tahun).')
            
            break

        except UmurError as e:
            print(f'[ERROR] {e}')

    while True:
        try:
            email = input('Email: ').strip()
            if '@' not in email:
                raise ValueError("Email tidak valid! Harus mengandung '@'.")
            
            break

        except ValueError as e:
            print(f'[ERROR] {e}')

    while True:
        try:
            no_hp = input('No HP: ').strip()
            if len(no_hp) < 10 or len(no_hp) > 13:
                raise ValueError('No HP tidak valid! Harus antara 10-13 digit angka.')
            
            break

        except ValueError as e:
            print(f'[ERROR] {e}')

    print('Proses input selesai.\n')
    
    print('=== DATA PESERTA ===')
    print(f'Nama   : {nama}')
    print(f'Umur   : {umur} tahun')
    print(f'Email  : {email}')
    print(f'No HP  : {no_hp}')
    print('Status : TERDAFTAR')

print('=== REGISTRASI PESERTA SEMINAR ===')
main()