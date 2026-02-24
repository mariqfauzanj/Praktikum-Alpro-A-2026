try:
    angka1 = int(input('Masukkan angka pertama: '))
    angka2 = int(input('Masukkan angka kedua: '))
    print(f'Hasil pembagian dari {angka1} dan {angka2} adalah {angka1 / angka2}')
except ZeroDivisionError:
    print('Tidak bisa membagi dengan nol!')
except ValueError:
    print('Harus berupa angka bulat!')
except IndexError:
    print('Index di luar jangkauan!')
finally:
    print('Program berhasil dijalankan.')