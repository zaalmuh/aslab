# aslab
Aplikasi berbasis command-line yang membuat feedback secara otomatis dan meng-copy ke clipboard feedback yang diinginkan.

## Setup
1. Clone repository ke local computer anda
2. Tempatkan aslab.py dan aslab.bat pada satu folder
3. edit path pada aslab.bat dengan path yang diinginkan, default: "C:\aslab.py"
4. Untuk menjalankan program dan menyalin feedback, pergi ke windows run, dapat dengan menggunakan shortcut Windows + R, kemudian ketikkan path untuk aslab.bat, seperti "C:\aslab.bat" diikuti dengan nama mahasiswa dan nomor kesalahan yang diperbuat, jika terdapat lebih dari 1, pisahkan dengan spasi, contoh:
> C:\aslab.bat aliza 1 2
4. Feedback akan tersalin ke clipboard dengan format sebagai berikut (sebagai contoh):
```
Halo aliza, terima kasih sudah mengerjakan laporan, untuk koreksi dari aku ada beberapa, yaitu:
1. Pastikan fontnya sesuai yaa (TNR 12)
2. Perhatikan alignment pada paragraf, pastikan sudah teralign justify
```
5. Feedback yang tersalin ke clipboard dapat di-paste ke file text manapun yang diinginkan
6. Pengaturan jenis kesalahan dan nomornya dapat dilihat pada file aslab.py

Selamat Mencoba!
