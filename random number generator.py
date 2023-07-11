import sys
from tabulate import tabulate
import math

# Mengatur pengkodean karakter yang didukung oleh sistem operasi
if sys.stdout.encoding != 'utf-8':
    sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

class LCG:
    def __init__(self, seed, a, c, m):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m

    def generate(self):
        x = self.seed
        while True:
            x = (self.a * x + self.c) % self.m
            yield x

# Inisiasi Variabel
Zo = 10120257
a = 111
c = 333
m = 512
rata_rata = 170.8
simpangan_baku = 12
iterasi = 20

lcg = LCG(Zo, a, c, m)
random_generator = lcg.generate()

# Menyiapkan data untuk tabel
table_data = []

# Generate random numbers dan simpan ke dalam array
angka_acak = []
for _ in range(iterasi + 1):
    angka = next(random_generator)
    angka_acak.append(angka)

# Run Program
for orang in range(iterasi):
    Zi = angka_acak[orang]
    Ui = Zi / m
    Zi_next = angka_acak[orang + 1]
    Ui_next = Zi_next / m
    Z = math.sqrt(-2 * math.log(Ui)) * math.cos(2 * math.pi * Ui_next)
    X = rata_rata + (simpangan_baku * Z)

    row = [orang + 1, Zi, Zi_next, Ui, Ui_next, math.sqrt(-2 * math.log(Ui)), math.cos(2 * math.pi * Ui_next), Z, X]
    table_data.append(row)

# Menampilkan output dalam bentuk tabel
headers = ["i", "Zi", "Zi+1", "Ui", "Ui+1", "(-2lnUi)^1/2", "cos(2πUi+1)", "Z", "X=μ+σZ"]
print(tabulate(table_data, headers=headers, tablefmt="grid"))
