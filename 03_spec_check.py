# =======================================================
# PROJECT 3: Pemeriksa Spesifikasi & Aturan Line Stop
# Materi: tuple, while, for, break, continue, nested if, and/or/not
# Data: SIMULASI (dummy), spesifikasi hanya contoh
# =======================================================

# Spesifikasi insertion loss (dB) = tuple (tidak boleh diubah): (min, max)
SPEC_IL = (7.0, 10.5)
BATAS_NG_BERUNTUN = 3   # 3 NG berturut-turut -> line stop

# Hasil ukur per unit; None = alat gagal baca (data tidak valid)
hasil_ukur = [
    9.8, 10.1, None, 9.5, 10.7, 9.9, 10.2,
    10.8, 11.2, 10.9, 9.7, 9.6,           # 3 NG beruntun -> proses berhenti
    9.4, 9.8,                              # tidak akan diperiksa
]

jumlah_ok = 0
jumlah_ng = 0
ng_beruntun = 0
dilewati = 0
berhenti_di = None

i = 0
while i < len(hasil_ukur):
    nilai = hasil_ukur[i]
    nomor = i + 1
    i += 1

    if nilai is None:                      # data tidak valid -> lewati
        dilewati += 1
        print(f"Unit {nomor:>2}: (tidak terbaca, dilewati)")
        continue

    if SPEC_IL[0] <= nilai <= SPEC_IL[1]:  # dalam spesifikasi
        jumlah_ok += 1
        ng_beruntun = 0
        status = "OK"
    else:
        jumlah_ng += 1
        ng_beruntun += 1
        status = "NG"

    print(f"Unit {nomor:>2}: {nilai:>5.1f} dB  {status}")

    if ng_beruntun >= BATAS_NG_BERUNTUN:
        berhenti_di = nomor
        print(f">>> LINE STOP: {ng_beruntun} NG berturut-turut pada unit {nomor}")
        break

print("-" * 40)
print(f"OK: {jumlah_ok} | NG: {jumlah_ng} | Dilewati: {dilewati}")
if berhenti_di is not None:
    sisa = len(hasil_ukur) - berhenti_di
    print(f"Proses dihentikan di unit {berhenti_di}; {sisa} unit belum diperiksa.")
else:
    print("Semua unit selesai diperiksa.")
