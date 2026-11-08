# Grafik Project 2: Pareto defect (batang = % tiap defect, garis = % kumulatif)
# Data sama dengan 02_pareto_defect.py (SIMULASI)
from gaya import *

data = [("coating damage", 31), ("contamination", 22), ("scratch", 14),
        ("fiber break", 9), ("misalignment", 6), ("crack", 3)]
total = sum(j for _, j in data)

fig, ax = mulai(9.5, 5)
kum, xs, ys = 0, [], []
for x, (nama, jumlah) in enumerate(data):
    persen = jumlah / total * 100
    kum += persen
    xs.append(x); ys.append(kum)
    ax.bar(x, persen, width=0.6, color=BIRU)
    label = f"{persen:.1f}%".replace(".", ",") + f"\n({jumlah} unit)"
    if x == 0:   # batang pertama: label di dalam batang agar tidak menimpa titik kumulatif
        ax.text(x, persen - 2, label, ha="center", va="top", fontsize=9, color="white", fontweight="bold")
    else:
        ax.text(x, persen + 1.2, label, ha="center", fontsize=9, color=INK)

ax.plot(xs, ys, color=INK, linewidth=2, marker="o", markersize=7, markerfacecolor="white", markeredgewidth=2)
for x, y in zip(xs, ys):
    if x == 0:
        continue   # nilainya sama dengan batang pertama
    ax.text(x, y + 3.2, f"{y:.1f}%".replace(".", ","), ha="center", fontsize=9, color=INK2)

ax.axhline(80, color=CRIT, linestyle=(0, (4, 3)), linewidth=1)
ax.text(len(data) - 0.45, 81, "batas 80%", ha="right", fontsize=9, color=CRIT)

ax.set_xticks(range(len(data)))
ax.set_xticklabels([d[0] for d in data], fontsize=10)
ax.set_ylim(0, 112)
koma(ax)
ax.set_ylabel("% dari seluruh NG")
judul(ax, "Pareto defect", f"Total {total} unit NG. Batang = porsi tiap defect, garis = persentase kumulatif. Data simulasi.")
simpan(fig, "grafik_02")
