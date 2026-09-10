nama = input("Nama: ")

nilai_tugas = float(input("Nilai Tugas: "))
nilai_uts = float(input("Nilai UTS: "))
nilai_uas = float(input("Nilai UAS: "))

nilai_akhir = (
    nilai_tugas * 0.20 +
    nilai_uts * 0.30 +
    nilai_uas * 0.50
)

print("\n=== HASIL ===")
print(f"Nama         : {nama}")
print(f"Nilai Akhir  : {nilai_akhir:.2f}")