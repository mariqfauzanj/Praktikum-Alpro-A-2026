#1

angka_list = [10, 20, 30]
try:
    idx = int(input('Masukkan index (0-2): '))
    print(f'Nilai: {angka_list[idx]}')
except ValueError:
    print('Harus berupa angka bulat!')
except IndexError:
    print('Index di luar jangkauan!')
finally:
    print('Selesai.')

# jika input yang diberikan adalah nol, huruf, angka negatif:

# 1. ketika input adalah 0, tidak terjadi error dan outputnya adalah "Nilai: 10"
#    menjalankan blok finally mencetak "Selesai."

# 2. ketika input adalah huruf (misalnya 'a'), terjadi ValueError
#    mencetak "Harus berupa angka bulat!" dan menkalankan blok finally mencetak "Selesai."

# 3. ketika input adalah angka negatif (misalnya -1), tidak terjadi error karena
#    terjadi negative indexing menghasilkan "Nilai: 30" dan menjalankan blok finally
#    mencetak "Selesai."