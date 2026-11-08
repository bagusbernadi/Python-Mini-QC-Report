# Gaya bersama untuk ketiga grafik (latar putih, warna dari palet baku).
# Butuh: pip install matplotlib   (di luar materi Part 1, hanya untuk grafik)
import matplotlib
matplotlib.use("Agg")           # simpan ke file, tanpa jendela
import matplotlib.pyplot as plt

INK = "#0b0b0b"      # teks utama
INK2 = "#52514e"     # teks sekunder
MUTED = "#898781"    # sumbu dan label pendukung
GRID = "#e1e0d9"     # garis grid tipis
BIRU = "#2a78d6"     # seri utama
GOOD = "#0ca30c"     # status baik   (grade A / OK)
WARN = "#fab219"     # peringatan    (grade B)
CRIT = "#d03b3b"     # kritis        (grade C / NG)


def mulai(lebar=9, tinggi=4.8):
    """Buat figure putih dengan sumbu bersih."""
    plt.rcParams.update({
        "font.family": ["Inter", "DejaVu Sans"],
        "font.size": 11,
        "text.color": INK,
        "axes.labelcolor": INK2,
        "xtick.color": INK2,
        "ytick.color": INK2,
    })
    fig, ax = plt.subplots(figsize=(lebar, tinggi), dpi=150, facecolor="white")
    ax.set_facecolor("white")
    for sisi in ("top", "right"):
        ax.spines[sisi].set_visible(False)
    for sisi in ("left", "bottom"):
        ax.spines[sisi].set_color(MUTED)
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.tick_params(length=0)
    return fig, ax


def koma(ax):
    """Angka sumbu y memakai koma desimal."""
    from matplotlib.ticker import FuncFormatter
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:g}".replace(".", ",")))


def judul(ax, teks, sub):
    ax.set_title(teks, loc="left", fontsize=14, fontweight="bold", color=INK, pad=30)
    ax.text(0, 1.04, sub, transform=ax.transAxes, fontsize=10.5, color=INK2, va="bottom")


def simpan(fig, nama):
    fig.tight_layout()
    fig.savefig(f"img/{nama}.png", facecolor="white")
    print("tersimpan: img/" + nama + ".png")
