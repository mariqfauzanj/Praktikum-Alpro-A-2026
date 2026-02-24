try:
    angka = int(input('Masukkan angka: '))
    hasil = 100 / angka
    print(f'Hasil: {hasil}')
except ValueError:
    print('Error: Input harus berupa angka!')
except ZeroDivisionError:
    print('Error: Tidak bisa membagi dengan nol!')
except Exception as e:
    print(f'Error tidak terduga: {e}')