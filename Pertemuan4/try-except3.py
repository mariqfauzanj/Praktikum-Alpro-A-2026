class UmurTidakValidError(Exception):
    def __init__(self, umur):
        self.umur = umur
        super().__init__(f'Umur {umur} tidak valid.\nHarus antara 0-150.')

def validasi_umur(umur):
    if umur < 0 or umur > 150:
        raise UmurTidakValidError(umur)
    #print(f'Umur {umur} valid.')
    return True

try:
    validasi_umur(15)
except UmurTidakValidError as e:
    print(f'Error: {e}')