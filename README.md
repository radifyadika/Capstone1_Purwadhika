# Capstone1_Purwadhika
Isi Capstone ini adalah sebuah aplikasi sederhana bernama "Mini Aplikasi Warehouse JCDSOL ELECSTORAGE Stock Data" yang dirancang untuk membantu mengelola persediaan barang elektronik di gudang. Aplikasi ini memiliki fitur CRUD (Create, Read, Update, Delete) yang memungkinkan pengguna untuk menambahkan item baru, melihat daftar item yang tersedia, memperbarui informasi item, dan menghapus item dari sistem.

### Prepared by Radif Ramadan as a Student from the JCDS Program's Purwadhika for Capstone Project Module 1 (Programming with Python)

## Application Guide
**• Daftar Tabel Stock Data :**
 
    ID- : Nomor unik untuk setiap data produk (diambil dari 3 huruf pertama Kategori produk)
    Nama Produk : Nama produk yang ada dalam stok gudang
    Kategori : Kelompok atau jenis produk sejenis yang terdapat pada gudang
    Unit : Kuantitas produk yang tersedia pada gudang
    Harga Satuan : Harga per unit produk

**• Fitur (fungsi) yang tersedia pada Aplikasi :**
 
    1. Fungsi menu_utama()
    Fungsi ini digunakan untuk menampilkan tampilan menu utama dari program aplikasi dengan pilihan untuk melihat Report Stock Gudang, 
    Tambah Stock Baru ke Gudang, Update Stock Gudang, Delete Stock Gudang, dan Exit Program.
    
    2. Fungsi menu_report()
    Fungsi ini digunakan untuk menampilkan menu Report Stock Gudang dengan opsi untuk melihat stok secara keseluruhan, stok berdasarkan 
    kategori, dan kembali ke menu utama.
    
    3. Fungsi menu_create()
    Fungsi ini digunakan untuk menambahkan barang baru yang belum terdaftar ke gudang.
    
    4. Fungsi menu_update()
    Fungsi ini digunakan untuk memperbarui informasi barang yang sudah terdaftar di dalam gudang berdasarkan Nama Produk, termasuk 
    perubahan Nama Barang, Kategori Produk, Unit Produk dan Harga Satuan Produk.

    5. Fungsi menu_delete()
    Fungsi ini digunakan untuk menghapus stok barang yang ada dalam program. Fungsi ini dapat menghapus data berdasarkan primary key 
    atau per baris, melakukan penghapusan berdasarkan kategori, atau menghapus semua stok yang ada di gudang. 
    
    6. Fungsi tampilan_data()
    Fungsi ini digunakan untuk menampilkan data dalam bentuk tabel sederhana di layar. 

    7. Fungsi yes_no(yes, no)
    Fungsi ini digunakan untuk mengajukan pertanyaan dengan pilihan Yes atau No, di mana jika jawabannya Yes, program akan melakukan 
    suatu tindakan, dan jika jawabannya No, program akan melakukan tindakan lain.

