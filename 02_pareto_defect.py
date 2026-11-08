# =======================================================
# PROJECT 2: Pareto Defect Versi Teks
# Materi: list, dict, for (termasuk nested), operator in/not in
# Data: SIMULASI (dummy), bukan data perusahaan
# =======================================================

# Log defect harian (satu item = satu unit NG)
log_defect = (
    ["scratch"] * 14 + ["coating damage"] * 31 + ["fiber break"] * 9
    + ["contamination"] * 22 + ["misalignment"] * 6 + ["crack"] * 3
)

# 1) Hitung frekuensi tiap jenis defect -> dict
frekuensi = {}
for d in log_defect:
    if d not in frekuensi:      # operator membership
        frekuensi[d] = 0
    frekuensi[d] += 1

# 2) Urutkan dari terbanyak ke tersedikit (selection sort dengan nested loop)
pasangan = []
for nama in frekuensi:
    pasangan.append([nama, frekuensi[nama]])

for i in range(len(pasangan)):
    terbesar = i
    for j in range(i + 1, len(pasangan)):
        if pasangan[j][1] > pasangan[terbesar][1]:
            terbesar = j
    pasangan[i], pasangan[terbesar] = pasangan[terbesar], pasangan[i]

# 3) Cetak tabel + bar + persentase kumulatif
total = len(log_defect)
kumulatif = 0

print(f"{'Defect':<16} {'Jml':>4} {'%':>6} {'Kum %':>7}  Bar")
print("-" * 60)
for nama, jumlah in pasangan:
    persen = jumlah / total * 100
    kumulatif += persen
    bar = "█" * round(persen / 2)       # 1 blok = 2%
    tanda = " <- vital few" if kumulatif - persen < 80 else ""
    print(f"{nama:<16} {jumlah:>4} {persen:>6.1f} {kumulatif:>7.1f}  {bar}{tanda}")

print("-" * 60)
print(f"Total NG: {total} unit")
