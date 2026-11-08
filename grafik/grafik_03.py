# Grafik Project 3: hasil ukur insertion loss vs spesifikasi, dengan titik line stop
# Data sama dengan 03_spec_check.py (SIMULASI)
from gaya import *

hasil_ukur = [9.8, 10.1, None, 9.5, 10.7, 9.9, 10.2, 10.8, 11.2, 10.9, 9.7, 9.6, 9.4, 9.8]
SPEC_MIN, SPEC_MAX = 7.0, 10.5
LINE_STOP = 10   # unit ke-10 (hasil dari 03_spec_check.py)

fig, ax = mulai(9.5, 5)
ax.axhspan(SPEC_MIN, SPEC_MAX, color="#e6f4ea", zorder=0)
ax.text(0.6, SPEC_MIN + 0.1, "area hijau = dalam spesifikasi (7,0 – 10,5 dB)", fontsize=9, color=INK2, va="bottom")
ax.axhline(SPEC_MAX, color=MUTED, linewidth=1)

diperiksa = [(i + 1, v) for i, v in enumerate(hasil_ukur) if v is not None and i + 1 <= LINE_STOP]
sisa = [(i + 1, v) for i, v in enumerate(hasil_ukur) if v is not None and i + 1 > LINE_STOP]
ax.plot([x for x, _ in diperiksa if x != 3], [v for x, v in diperiksa if x != 3], color=BIRU, linewidth=1.5, zorder=2)

for x, v in diperiksa:
    ng = not (SPEC_MIN <= v <= SPEC_MAX)
    if ng:
        ax.scatter(x, v, s=130, marker="X", color=CRIT, zorder=4)
        ax.text(x, v + 0.22, "NG", ha="center", fontsize=9, color=CRIT, fontweight="bold")
    else:
        ax.scatter(x, v, s=70, color=BIRU, edgecolor="white", linewidth=1.2, zorder=3)

ax.scatter([x for x, _ in sisa], [v for _, v in sisa], s=70, facecolor="white", edgecolor=MUTED, linewidth=1.5, zorder=3)
ax.text(12.5, 9.0, "belum diperiksa", ha="center", fontsize=9, color=MUTED)
ax.annotate("data tidak\nterbaca", xy=(3, 9.9), xytext=(3, 8.5), ha="center", fontsize=9, color=INK2,
            arrowprops=dict(arrowstyle="-", color=MUTED, linestyle=":"))

ax.axvline(LINE_STOP + 0.5, color=CRIT, linestyle=(0, (4, 3)), linewidth=1.2)
ax.text(LINE_STOP + 0.65, 11.65, "LINE STOP\n3 NG berturut-turut", ha="left", va="top", fontsize=9, color=CRIT, fontweight="bold")

ax.set_xticks(range(1, len(hasil_ukur) + 1))
ax.set_xlim(0.4, len(hasil_ukur) + 0.6)
ax.set_ylim(6.6, 11.8)
koma(ax)
ax.set_xlabel("Nomor unit")
ax.set_ylabel("Insertion loss (dB)")
judul(ax, "Hasil ukur terhadap spesifikasi", "Unit 8, 9, 10 berturut-turut NG, sehingga proses berhenti. Data simulasi.")
simpan(fig, "grafik_03")
