#! python3
# mclip.py - A multi-clipboard program.
def opening(name):
    openingText = f"Halo {name}, terima kasih sudah mengerjakan laporan, untuk koreksi dari aku ada beberapa, yaitu:" 
    return openingText
daftarKesalahan = ['','Pastikan fontnya sesuai yaa (TNR 12)', 
                   'Perhatikan alignment pada paragraf, pastikan sudah teralign justify', 
                   'Perhatikan spacing pada paragraf, pastikan konsisten', 
                   'Perhatikan penomoran pada setiap tabel dan gambar, pastikan konsisten dan menggunakan format yang sesuai', 
                   'Perhatikan tata bahasa, salah satunya adalah mengubah kalimat pasif menjadi aktif', 
                   'Perhatikan tata bahasa, salah satunya adalah membuat teks yang berasal dari bahasa asing menjadi italic',
                   'Pastikan teori yang digunakan valid yaa, cek kembali dengan buku atau jurnal lainnya',
                   'Pastikan teori yang digunakan relevan yaa, cek kembali dengan teori dari modul',
                   'Perhatikan kelengkapan dari simulasi',
                   'Perhatikan kembali simulasi yang telah dibuat',
                   'Perhatikan data pengamatan yang dicantumkan, pastikan kelengkapannya',
                   'Tolong waktunya diperhatikan lagi, jangan sampai mengulangi keterlambatan',
                   'Pastikan relevansi pendahuluan (termasuk abstrak) dengan praktikum',
                   'Pastikan hasil yang didapatkan dicantumkan semua pada bab hasil',
                   'Perhatikan kesimpulan, pastikan kesimpulan menjawab tujuan yang ada',
                   'Perhatikan analisis percobaan',
                   'Perhatikan analisis hasil, pastikan menuliskan apakah hasil sesuai dengan teori atau tidak  ',
                   'Perhatikan analisis kesalahan',
                   'Pastikan untuk menuliskan semua referensi, termasuk yang berada di teori dasar, selain itu gunakan minimal 3 referensi yang kredibel (jurnal atau buku)',
                   'Pastikan gambar diletakkan di pojok halaman']
import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python aslab.py [nama] kesalahan(pastikan dipisahkan dengan spasi)')
    print('contoh: python aslab.py aliza 1 3 4 5')
    sys.exit()

name = sys.argv[1]
finalText = opening(name)

for i in range(2, len(sys.argv)):
    finalText += '\n' + str(i-1) + '. ' + daftarKesalahan[int(sys.argv[i])]

pyperclip.copy(finalText)
print('Text is copied to clipboard')