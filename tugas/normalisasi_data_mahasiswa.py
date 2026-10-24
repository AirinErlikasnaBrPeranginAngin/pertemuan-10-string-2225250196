def normalisasi_nama(nama):
    return " ".join(nama.strip().split()).title()


def normalisasi_kelas(kelas):
    return "-".join(kelas.strip().upper().split())


def buat_inisial(nama):
    kata = nama.split()
    return "".join(kata[i][0] for i in range(len(kata)))


nama = input("Masukkan nama mahasiswa: ")
kelas = input("Masukkan kode kelas: ")

nama_bersih = normalisasi_nama(nama)
kelas_bersih = normalisasi_kelas(kelas)
jumlah_kata = len(nama_bersih.split())
inisial = buat_inisial(nama_bersih)

print("\n=== HASIL NORMALISASI DATA ===")
print("Nama          :", nama_bersih)
print("Kode kelas    :", kelas_bersih)
print("Jumlah kata   :", jumlah_kata)
print("Inisial       :", inisial)