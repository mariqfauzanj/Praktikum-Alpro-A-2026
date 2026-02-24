try:
    angka = int(input('Masukkan angka positif: '))
    if angka < 0:
        raise ValueError('Angka harus positif!')
    hasil = 100 / angka
except ValueError as e:
    print(f'Input tidak valid: {e}')
except ZeroDivisionError:
    print('Error: Angka tidak boleh nol!')
else:
    print(f'Berhasil! Hasil = {hasil}')
finally:
    print('Program selesai.')