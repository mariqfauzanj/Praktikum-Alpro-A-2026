def input_angka(pesan, tipe='int'):
    while True:
        try:
            nilai = input(pesan)
            if tipe == 'int':
                return int(nilai)
            elif tipe == 'float':
                return float(nilai)
        except ValueError:
            print(f'Input tidak valid! Masukkan angka {tipe}.')

umur = input_angka('Masukkan umur Anda: ', 'int')
berat = input_angka('Masukkan berat badan (kg): ',
'float')
print(f'Umur: {umur}, Berat: {berat} kg')