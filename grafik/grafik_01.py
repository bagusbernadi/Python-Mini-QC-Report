# Grafik Project 1: yield per batch dengan batas grade A dan B
# Data sama dengan 01_yield_grade.py (SIMULASI)
from gaya import *

batches = [
    ("B001", 500, 492), ("B002", 480, 462), ("B003", 520, 482), ("B004", 450, 447),
    ("B005", 510, 503), ("B006", 495, 450), ("B007", 470, 462), ("B008", 505, 499),
]
BATAS_A, BATAS_B = 98.0, 95.0
WARNA = {"A": GOOD, "B": WARN, "C": CRIT}

fig, ax = mulai()
for x, (nama, total, good) in enumerate(batches):
    y = good / total * 100
    grade = "A" if y >= BATAS_A else ("B" if y >= BATAS_B else "C")
    ax.vlines(x, 88, y, color=GRID, linewidth=2)                     # tangkai
    ax.scatter(x, y, s=110, color=WARNA[grade], edgecolor="white", linewidth=1.5, zorder=3)
    ax.text(x, y + 0.55, f"{y:.1f}% · {grade}".replace(".", ","), ha="center", fontsize=9.5, color=INK, fontweight="bold")

for batas, teks in ((BATAS_A, "Grade A ≥ 98%"), (BATAS_B, "Grade B ≥ 95%")):
    ax.axhline(batas, color=MUTED, linestyle=(0, (4, 3)), linewidth=1)
    ax.text(len(batches) - 0.45, batas + 0.15, teks, ha="left", va="bottom", fontsize=9, color=INK2)

ax.set_xticks(range(len(batches)))
ax.set_xticklabels([b[0] for b in batches])
ax.set_xlim(-0.5, len(batches) + 1.1)
ax.set_ylim(88, 101)
koma(ax)
ax.set_ylabel("Yield (%)")
judul(ax, "Yield per batch", "Titik berwarna menunjukkan grade; dua batch 1x8 (B003, B006) jatuh ke grade C. Data simulasi.")
simpan(fig, "grafik_01")
