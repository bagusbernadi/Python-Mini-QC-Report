# Latihan Python dasar (materi DQLab: Python for Data Professional Beginner - Part 1)
# Jalankan: python python_dasar_latihan.py

# =======================================================
# LATIHAN 1: Variabel dan Tipe Data Dasar
# =======================================================

# Variabel dasar
nama = "Budi"  # menyimpan teks/string
umur = 30       # menyimpan angka/integer
is_employed = True  # menyimpan nilai boolean (True/False)

# Menampilkan isi variabel dengan format string
print(f"Nama saya {nama}, umur saya {umur}, sedang bekerja: {is_employed}")


# =======================================================
# LATIHAN 2: List, Tuple, Set, dan Dictionary
# =======================================================

# List: bisa diubah, bisa duplikat
my_list = [1, 2, 3]

# Tuple: tidak bisa diubah (immutable)
my_tuple = (4, 5, 6)

# Set: tidak ada elemen duplikat, tidak terurut
my_set = {7, 8, 9}

# Dictionary: pasangan key-value
my_dict = {
    "nama": "Budi",
    "hobi": "Ngoding"
}

# Menampilkan struktur data
print("List:", my_list)
print("Tuple:", my_tuple)
print("Set:", my_set)
print("Hobi saya adalah:", my_dict["hobi"])


# =======================================================
# LATIHAN 3: Operator Python
# =======================================================

a = 10
b = 3

# Operator aritmatika
print("a + b =", a + b)        # Penjumlahan
print("a ** b =", a ** b)      # Pangkat: 10^3 = 1000

# Operator perbandingan dan logika
print("a > b and a != b:", a > b and a != b)  # True jika dua kondisi terpenuhi

# Operator keanggotaan
print("a in my_list:", a in my_list)  # False karena 10 tidak ada di my_list

# Operator identitas
print("a is b:", a is b)  # False, karena objek a dan b berbeda walau nilainya bisa sama


# =======================================================
# LATIHAN 4: Prioritas Operator & Membership Operators
# =======================================================

# Tanpa kurung: perkalian dilakukan lebih dulu
hasil1 = 2 + 3 * 4     # 3*4 = 12 → 2+12 = 14

# Dengan kurung: penjumlahan dilakukan dulu
hasil2 = (2 + 3) * 4   # 2+3 = 5 → 5*4 = 20

# Menampilkan hasil
print("Hasil tanpa kurung:", hasil1)
print("Hasil dengan kurung:", hasil2)

# Membership operators
angka = 5
angka_list = [1, 3, 5, 7]
huruf = 'a'
kata = "data analyst"

print("Apakah 5 ada di angka_list?", angka in angka_list)            # True
print("Apakah 'a' ada di 'data analyst'?", huruf in kata)            # True
print("Apakah 2 tidak ada di angka_list?", 2 not in angka_list)      # True
print("Apakah 'z' tidak ada di 'data analyst'?", 'z' not in kata)    # True


# =======================================================
# LATIHAN 5: Kondisi / Percabangan
# =======================================================

nilai = 85

# Struktur if-elif-else untuk mengevaluasi nilai
if nilai >= 90:
    print("Nilai A")
elif nilai >= 80:
    print("Nilai B")
else:
    print("Nilai C")

# Nested if: kondisi di dalam kondisi
umur = 30
pekerjaan = "Engineer"

if umur > 18:
    if pekerjaan == "Engineer":
        print("Orang dewasa yang bekerja sebagai Engineer")


# =======================================================
# LATIHAN 6: Perulangan - While, For, Break, Continue
# =======================================================

# WHILE LOOP: Mengulang selama kondisi terpenuhi
x = 0
while x < 3:
    print("Nilai x saat ini:", x)
    x += 1

# FOR LOOP: Iterasi tiap elemen dalam list
buah = ["apel", "pisang", "mangga"]
for item in buah:
    print("Buah:", item)

# BREAK: keluar dari loop ketika kondisi tertentu tercapai
for i in range(5):
    if i == 3:
        break  # keluar dari loop saat i = 3
    print("Loop dengan break:", i)

# CONTINUE: lompat ke iterasi berikutnya jika kondisi terpenuhi
for i in range(5):
    if i == 2:
        continue  # lewati saat i = 2
    print("Loop dengan continue:", i)

# NESTED LOOP: Loop di dalam loop
for i in range(1, 3):      # loop luar: 1 hingga 2
    for j in range(1, 3):  # loop dalam: 1 hingga 2
        print(f"{i} x {j} = {i * j}")
