# =======================================================
# PROJECT 1: Kalkulator Yield & Grade Batch (PLC Splitter)
# Materi: list, dict, set, operator, if-elif-else, for
# Data: SIMULASI (dummy), bukan data perusahaan
# =======================================================

# Setiap batch = dict; kumpulan batch = list
batches = [
    {"batch": "B001", "produk": "1x8", "total": 500, "good": 492},
    {"batch": "B002", "produk": "1x4", "total": 480, "good": 462},
    {"batch": "B003", "produk": "1x8", "total": 520, "good": 482},
    {"batch": "B004", "produk": "1x2", "total": 450, "good": 447},
    {"batch": "B005", "produk": "1x4", "total": 510, "good": 503},
    {"batch": "B006", "produk": "1x8", "total": 495, "good": 450},
    {"batch": "B007", "produk": "1x2", "total": 470, "good": 462},
    {"batch": "B008", "produk": "1x8", "total": 505, "good": 499},
]

BATAS_A = 98.0  # yield >= 98% -> grade A
BATAS_B = 95.0  # yield >= 95% -> grade B, selain itu grade C

jumlah_grade = {"A": 0, "B": 0, "C": 0}  # dict penghitung
produk_unik = set()                       # set: tidak ada duplikat
total_semua = 0
good_semua = 0

print(f"{'Batch':<6} {'Produk':<7} {'Total':>6} {'Good':>6} {'Yield %':>8}  Grade")
print("-" * 44)

for b in batches:
    yield_persen = b["good"] / b["total"] * 100

    if yield_persen >= BATAS_A:
        grade = "A"
    elif yield_persen >= BATAS_B:
        grade = "B"
    else:
        grade = "C"

    jumlah_grade[grade] += 1
    produk_unik.add(b["produk"])
    total_semua += b["total"]
    good_semua += b["good"]

    print(f"{b['batch']:<6} {b['produk']:<7} {b['total']:>6} {b['good']:>6} {yield_persen:>8.2f}  {grade}")

print("-" * 44)
print(f"Yield keseluruhan : {good_semua / total_semua * 100:.2f}% ({good_semua}/{total_semua})")
print("Jumlah batch/grade:", jumlah_grade)
print("Jenis produk      :", sorted(produk_unik))
