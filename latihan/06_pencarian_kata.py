teks = "Saya sedang belajar Python"

kata_dicari = "Python"

if kata_dicari in teks:
    print("Kata ditemukan")
else:
    print("Kata tidak ditemukan")

print(teks.find(kata_dicari))