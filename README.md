Pertemuan 10 - String dan Pengolahan Teks

##  Identitas

- Nama: Airin Erlikasna Br Perangin Angin
- NIM: 2225250196
- Program Studi: Pendidikan Matematika

##  Tujuan

Mempelajari dan menerapkan string Python untuk mengakses karakter, mengolah teks, membersihkan data, memisahkan kata, melakukan pencarian, dan menormalisasi data mahasiswa.

##  Struktur Folder

- "latihan/": berisi enam file latihan Python.
- "tugas/": berisi program normalisasi data mahasiswa.
- "README.md": dokumentasi tugas.
- ".gitignore": mengabaikan file yang tidak perlu diunggah.

##  Cara Menjalankan

Program dijalankan melalui terminal VS Code menggunakan Python 3. Contoh:

"python latihan/01_dasar_string.py"

##  Hasil Praktik

Pada Pertemuan 10, saya telah melakukan enam latihan mengenai string dan pengolahan teks menggunakan Python serta mengerjakan satu tugas utama tentang normalisasi data mahasiswa.

1. Dasar String: Menampilkan teks, menghitung panjang teks menggunakan "len()", serta mengubah huruf menjadi huruf kapital dan huruf kecil.
2. Indeks dan Slicing: Mengakses karakter berdasarkan indeks dan mengambil bagian tertentu dari string.
3. Method String: Menggunakan "strip()", "title()", dan "upper()" untuk membersihkan serta mengubah format teks.
4. Membersihkan Teks: Menghapus spasi berlebih dan merapikan teks menggunakan "strip()" dan "replace()".
5. Split dan Join: Memisahkan kalimat menjadi beberapa kata menggunakan "split()" dan menggabungkannya kembali menggunakan "join()".
6. Pencarian Kata: Memeriksa keberadaan kata menggunakan "in" dan mencari posisi kata menggunakan "find()".
7. Tugas Normalisasi Data Mahasiswa: Membuat program untuk merapikan nama mahasiswa, menormalkan kode kelas, menghitung jumlah kata, dan menghasilkan inisial nama.

Berdasarkan praktik yang telah dilakukan, saya mempelajari penggunaan string dan berbagai method Python untuk mengolah teks. Tugas utama juga membantu saya memahami penerapan pengolahan teks dalam program sederhana.


## Test Case

| No. | Input Nama | Input Kode Kelas | Hasil yang Diharapkan | Status |
|---|---|---|---|---|
| 1 | aan hendrayana | pmat a 2026 | Aan Hendrayana, PMAT-A-2026, 2 kata, AH | Berhasil |
| 2 | fATHIYYAH mUTHMAINNAH | kelas b | Fathiyyah Muthmainnah, KELAS-B, 2 kata, FM | Berhasil |
| 3 | BUDI | pmtk 01 | Budi, PMTK-01, 1 kata, B | Berhasil |

##  Refleksi

Melalui praktikum Pertemuan 10, saya mempelajari cara mengolah string dalam Python, seperti menggunakan "strip()", "split()", "join()", "title()", dan "upper()". Saya juga belajar membuat fungsi untuk membersihkan nama mahasiswa, merapikan kode kelas, menghitung jumlah kata, dan membuat inisial nama. Dari pengujian yang dilakukan, saya memahami bahwa pengolahan string dapat membantu membuat data menjadi lebih rapi dan konsisten.

## Jawaban Kuis

1. Apa perbedaan string dan list pada Python?

String adalah tipe data untuk menyimpan teks berupa kumpulan karakter, sedangkan list digunakan untuk menyimpan beberapa elemen dalam satu variabel. String bersifat immutable, sedangkan list dapat diubah setelah dibuat.

2. Mengapa string disebut immutable?

String disebut immutable karena isi atau karakter di dalamnya tidak dapat diubah secara langsung setelah string dibuat. Jika ingin mengubah teks, kita perlu membuat string baru.

3. Apa hasil dari "'Python'[1:4]"?

Hasilnya adalah "yth". Indeks dimulai dari 0, sehingga indeks 1 adalah "y", indeks 2 adalah "t", dan indeks 3 adalah "h". Indeks akhir 4 tidak ikut diambil.

4. Apa fungsi "strip()"?

Method "strip()" digunakan untuk menghapus spasi atau karakter whitespace di awal dan akhir string, tanpa menghapus spasi di antara kata-kata.

5. Kapan "lower()" lebih tepat daripada "title()"?

"lower()" lebih tepat digunakan ketika seluruh teks perlu diubah menjadi huruf kecil, misalnya untuk menyamakan format teks sebelum dibandingkan. Sementara itu, "title()" digunakan untuk membuat huruf pertama setiap kata menjadi kapital.

6. Apa perbedaan "split()" dan "join()"?

"split()" digunakan untuk memisahkan string menjadi list berdasarkan pemisah tertentu. Sebaliknya, "join()" digunakan untuk menggabungkan elemen-elemen string menjadi satu string dengan pemisah yang ditentukan.

7. Bagaimana memeriksa apakah kata "'data'" terdapat dalam suatu string?

Gunakan operator "in", seperti contoh berikut:

teks = "Pengolahan data mahasiswa"

print("data" in teks)

Hasilnya adalah "True" karena kata ""data"" terdapat dalam string tersebut.

8. Apa arti hasil "-1" dari "find()"?

Hasil "-1" menunjukkan bahwa kata atau substring yang dicari tidak ditemukan di dalam string.

9. Mengapa normalisasi teks perlu dilakukan sebelum perbandingan?

Normalisasi teks diperlukan agar format teks menjadi seragam, misalnya dengan mengubah huruf menjadi huruf kecil, menghapus spasi berlebih, dan merapikan penulisan. Dengan demikian, perbandingan teks menjadi lebih konsisten dan mengurangi kesalahan akibat perbedaan format.

10. Perintah apa yang digunakan untuk mengirim commit ke GitHub?

Perintah yang digunakan adalah:

git push

Jika ingin mengirim branch "main" ke repositori GitHub sekaligus mengatur hubungan upstream pada pengiriman pertama, gunakan:

git push -u origin main

