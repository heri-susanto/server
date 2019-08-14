import sqlite3

conn = sqlite3.connect('db_buku.db')

conn.execute('''CREATE TABLE BUKU
         (ID INT PRIMARY KEY     NOT NULL,
         JUDUL           TEXT    NOT NULL,
         PT            TEXT     NOT NULL,
         TEKS        TEXT);''')

print('Table created successfully')
conn.execute("INSERT INTO BUKU (ID,JUDUL,PT,TEKS) \
      VALUES (1, 'JURNALIS INTERNSHIP / MAGANG MAHASISWA NESIATIMES', 'aGrQuFzoOhPgBx9XpyCQ', 'nesiatimescom bagai media beritainformasi bas online terima mahasiswa akhir laku internshipmagang dapat alam kerja bagai tulis berita Analisis konten editor jurnalis muda tanggung jawab kerja jalan tugas sesuai posisi lamar penuh tanggungjawab jujur tuntas syarat alam nonpengalaman lamar milik ingin untuk ajar sangat butuh ahli mampu operasi ms word mampu tulis sesuai urut spok mampu teliti baik mampu tarik simpul cara cepat mampu komunikasi baik kualifikasi priawanita mahasiswa akhir yang sedang tempuh internshipmagang usia bebas waktu kerja jam 9 1500 waktu fleksibel' )")

conn.execute("INSERT INTO BUKU (ID,JUDUL,PT,TEKS) \
      VALUES (2, 'STAFF PAJAK (MAGANG 3 BULAN)', 'TLA4Crmh6VLZOhegwxZz', 'pria wanita usia maksimal 25 tahun didik minimal smk derajat akuntansi jadi nilai lebih fresh graduate silah lamar rajin teliti mudah beri arah sedia ikat kontrak lama 3 bulan sedia gabung cepat domisili daerah tangerang sekitar filling faktur pajak print siap bukti potong kirim supplier jadwal kirim bukti potong' )")

conn.execute("INSERT INTO BUKU (ID,JUDUL,PT,TEKS) \
      VALUES (3, 'MAGANG ADMIN ACCOUNTING', 'ShSdjo1eDnlS7tO2YJcR', 'company description pt buanasakti aneka motor rupa part center khusus kendara mercedes bmw opel chevrolet peugeot sedia suku cadang baik bodypart maupun non bodypart baik oe maupun oem beberapa suku cadang ikan garansi discount tarik pt buanasakti aneka motor bengkel gerak bidang jual awat gerak bidang baik body kendara body repair cat paint specialist oven system dukung lengkap alat equipment canggih tenaga profesional bidang body repair pt buanasakti aneka motor banyak percaya banyak usaha asuransi jalin kerjasama hingga ini job description magang admin accounting' )")

conn.execute("INSERT INTO BUKU (ID,JUDUL,PT,TEKS) \
      VALUES (4, 'MAGANG VISITOR MANAGEMENT', 'dDvQ4I79ukhC4Z59BO3k', 'bantu tim visitor management proses packaging undang telepon visitor akan hadir pamer atur undang kirim unjung bantu registrasi pamer langsung kualifikasi didik minimal sma smk bagai karyawan hari part time maksimal usia 27 tahun sedia kerja full time senin jumat 09 00 18 00' )")

conn.execute("INSERT INTO BUKU (ID,JUDUL,PT,TEKS) \
      VALUES (5, 'MAGANG HUMAS / MEDIA RELATION PRIMA IMAGING', 'OSHG4aqZqLgA0tsXmjJf', 'pt primaimaging pasok fotografi profesional rental studio pusat didik fotografi undang beberapa mahasiswa profesional dinamis gabung kami posisi humas media relation tanggung jawab kerja kelola hubung bagai media masuk online cetak siar kerja sama tim pasar kembang produk teknis bantu blog usaha outlet media sosial kelola hadir acara organisazi photo media layan bagai juru bicara usaha acara acara publik seminar lokakarya dukung luncur produk kampanye pasar program mitra kembang implementasi promosi konsumen kembang pelihara hubung kerja baik media tanggap tanya industri hubung syarat alam magang alam pr relevan ahli syarat mampu implementasi kampanye media masuk media sosial mampu kembang kampanye konsumen kreatif terampil tulis perhati detail kualifikasi wanita pria maksimal 25thn gelar komunikasi massal iklan media tara terampil komunikasi tulis lisan ahli interpersonal kuat mampu kembang hubung komunikasi semua consumer tunjang uang makan transport insentif bonus lembur waktu kerja 3 jam per hari gantung sepakat' )")

conn.execute("INSERT INTO BUKU (ID,JUDUL,PT,TEKS) \
      VALUES (6, 'MAGANG MARKETING', 'wd7Z3mx6Z6Xw7ZfIApKM', 'description 1 buat rencana konten social media cari resep tips info 2 buat hias masakan konten foto video social media 3 koordinasi tim markom design buat konten video produk cosmos 4 tanggung jawab atas bersih properti demo konten social media 5 atur budget demo beli butuh buat konten social media 6 buat lapor realisasi budget tiap minggu 7 jadi mc bawa acara konten video requirements 1 wajib masak hias masakan 2 percaya diri tampil depan kamera bagai mc bawa acara 3 tampil tarik referensi teman kamu' )")

conn.commit()
print('Records created successfully')
conn.close()
