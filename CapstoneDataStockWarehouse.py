# Capstone Project Python (Gudang - Data Stok)
# RADIF RAMADAN

# Data Stok Utama 
data_stok = {
    "TEL-001": {"Nama Produk": 'TV LED 42"', "Kategori": "Televisi", "Unit": 15, "Harga Satuan": 2500000},
    "LAP-001": {"Nama Produk": 'Laptop Asus Tuf Gaming F15', "Kategori": "Laptop", "Unit": 8, "Harga Satuan": 7540000},
    "LAP-002": {"Nama Produk": 'Laptop Omen By HP 16', "Kategori": "Laptop", "Unit": 3, "Harga Satuan": 9780000},
    "SMA-001": {"Nama Produk": 'Smartphone Iphone 15', "Kategori": "Smartphone", "Unit": 10, "Harga Satuan": 13429000},
    "KUL-001": {"Nama Produk": 'Kulkas LG GN-B215SQMT', "Kategori": "Kulkas", "Unit": 7, "Harga Satuan": 3000000},
    "MES-001": {"Nama Produk": 'Mesin Cuci Panasonic NA-W76BBZ', "Kategori": "Mesin Cuci", "Unit": 4, "Harga Satuan": 2200000}
}

nama_kolom = ["ID", "Nama Produk", "Kategori", "Unit", "Harga Satuan"]



# FITUR FITUR YANG TERSEDIA

def menu_utama():
    menu = input('''
═════════════════════════════════════════\n👋 SELAMAT DATANG DI JCDSOL ELECSTORAGE 👋\n═════════════════════════════════════════ 
    1. Report Stock Gudang 
    2. Tambah Stock Baru ke Gudang
    3. Update Stock Gudang
    4. Delete Stock Gudang
    5. Exit Program
\nMasukkan Menu yang Anda Inginkan (1-5) : ''')

    if menu == '1':
        print("══"*50)
        menu_report()
    elif menu == '2':
        print("══"*50)
        menu_create()
    elif menu == '3':
        print("══"*50)
        menu_update()    
    elif menu == '4':
        print("══"*50)
        menu_delete()
    elif menu == '5':
        print("😊 😊 😊 Terimakasih Telah Berkunjung 😊 😊 😊")
        exit() 
    else:
        menu_utama()
        
def menu_report():
    print('''
---------- 📄 📄 📄 Menu Report Stock Gudang 📄 📄 📄 ----------

    Pilihan Menu Report Stock Gudang:
    1. Tampilkan Data Stock Gudang
    2. Tampilkan Data Stock Spesifik (Kategori)
    3. Kembali ke Menu Utama
    ''')
    user_input = input("Tampilan Stok Yang Ingin Dipilih (1-3) : ")

    if user_input == '1':
        print("══"*50)
        tampilan_data()
        yes_no(menu_report,menu_utama)
    elif user_input == '2':
        print("══"*50)
        def report_sub2():
            data_stok_list = [{**{'Kode Produk': key}, **value} for key, value in data_stok.items()]
            kategori_yang_dicari = input("\n▣ Masukkan kategori produk yang ingin ditampilkan: ").title()
            kategori_ditemukan = False
            for produk in data_stok_list:
                if produk['Kategori'] == kategori_yang_dicari:
                    kategori_ditemukan = True
                    break
            if kategori_ditemukan:
                print(f"\n------- Info Barang Berkategori '{kategori_yang_dicari}'-------\n")
                print(f"{nama_kolom[0]: <10}|{nama_kolom[1]: <35}|{nama_kolom[2]: <15}|{nama_kolom[3]: <5}|{nama_kolom[4]: <10}")
                print("══════════+═══════════════════════════════════+═══════════════+═════+════════════")
                for produk in data_stok_list:
                    if produk['Kategori'] == kategori_yang_dicari:
                        harga_satuan = int(produk['Harga Satuan'])
                        harga_satuan_formatted = f"Rp {harga_satuan:,.0f}"
                        print(f"{produk['Kode Produk']: <10}|{(produk['Nama Produk']): <35}|{(produk['Kategori']): <15}|{str(produk['Unit']): <5}|{harga_satuan_formatted: <15}")       
            else:
                print(f"Kategori '{kategori_yang_dicari}' tidak ditemukan dalam Data Stock Gudang.")
                report_sub2()
        report_sub2()
        yes_no(menu_report,menu_utama)
    elif user_input == '3':
        menu_utama()
    else:
        menu_report() 

def menu_create():
    def menu_create_sub1():
        print("\n«------ Silahkan Input Stock Baru ke Gudang ------»")
        while True:
            nama_produk = input("▣ Masukkan nama produk: ").title()
            if any(detail['Nama Produk'].lower() == nama_produk.lower() for detail in data_stok.values()):
                print("Nama produk sudah ada dalam data. Silakan masukkan nama produk yang berbeda.")
            else:
                break
        kategori = input("▣ Masukkan kategori: ").title()
        while True:
            unit = (input("▣ Masukkan Jumlah Unit: "))
            if not unit.isdigit():
                print("\n⚠ Warning Error: Masukkan Nilai Berupa Angka!!!")
                continue
            harga_satuan = (input("▣ Masukkan Harga Satuan: "))
            if not harga_satuan.isdigit():
                print("\n⚠ Warning Error: Masukkan Nilai Berupa Angka!!!")
                continue
            break
        # Generate Kode Produk baru Jika Produk baru
        prefix = nama_produk[:3].upper()
        nomor = 1
        for kode in data_stok.keys():
            if kode.startswith(prefix):
                nomor += 1
        kode_produk = f"{prefix}-{str(nomor).zfill(3)}"
        
        def tambah_data():
            data_stok[kode_produk] = {
                "Nama Produk": nama_produk,
                "Kategori": kategori,
                "Unit": unit,
                "Harga Satuan": harga_satuan
            }

        yes_no(tambah_data, menu_create)
        print(f"Produk berhasil ditambahkan dengan Kode Produk: {kode_produk}")
    print("══"*50)
    print('''
---------- ✏️ ✏️ ✏️  Menu Tambah Stock Baru ke Gudang ✏️ ✏️ ✏️ ----------

    Pilihan Menu Tambah Stock Baru ke Gudang:
    1. Menambah Stock Baru ke Gudang
    2. Menampilkan Semua Data pada Gudang
    3. Kembali ke Menu Utama
    ''')
    user_input = input("Pilih Perintah yang Anda Inginkan (1-3) : ")

    if user_input == '1':
        print("══"*50)
        menu_create_sub1()
        yes_no(menu_create,menu_utama)
    elif user_input == '2':
        print("══"*50)
        tampilan_data()
        yes_no(menu_create,menu_utama)
    elif user_input == '3':
        print("══"*50)
        menu_utama()
    else:
        menu_create()
    
def menu_update():
    def update_sub1():
        while True:
            tampilan_data()
            item_updatestok = input("\n▣ Masukkan Nama Produk yang Ingin Anda update: ").title()
            item_update_key = None
            for kode, detail_produk in data_stok.items():
                if detail_produk['Nama Produk'].lower() == item_updatestok.lower():
                    item_update_key = kode
                    break
            else:
                print("Item yang anda masukkan tidak ada di list, update tidak bisa dilakukan.")
                break
            
            if item_update_key:
                while True:
                    print("══"*50)
                    jenis_update = int(input(f'''\n---------- Update Field (Kolom) Data Stok "{item_updatestok}"  ----------\n
        1. Nama Barang 
        2. Kategori 
        3. Unit 
        4. Harga Satuan 
        5. Kembali ke Menu Update
                                                
    Field yang ingin Anda Update (1-5): '''))
                    
                    if jenis_update == 1:
                        item_baru = input("\n▣ Masukkan Nama Produk Baru: ").title()
                        if any(detail['Nama Produk'].lower() == item_baru.lower() for detail in data_stok.values()):
                            print("Nama Produk Sudah Ada, Masukkan Nama Baru")
                            yes_no(update_sub1, menu_utama)
                        else:
                            def update_nama():
                                data_stok[item_update_key]['Nama Produk'] = item_baru
                                tampilan_data()
                                print("\nNama Produk Berhasil Diupdate.")
                            yes_no(update_nama, update_sub1)
                            break

                    elif jenis_update == 2:
                        kategori_baru = input("\n▣ Masukkan Detail Kategori Baru: ").title()
                        def update_kategori():
                            data_stok[item_update_key]['Kategori'] = kategori_baru
                            tampilan_data()
                            print("\nKategori Berhasil Diupdate.")
                        yes_no(update_kategori, update_sub1)
                        break
                            
                    elif jenis_update == 3:
                        unit_baru = int(input("\n▣ Masukkan Jumlah Stok Baru: "))
                        def update_unit():
                            data_stok[item_update_key]['Unit'] = unit_baru
                            tampilan_data()
                            print("\nJumlah Stok Berhasil Diupdate.")
                        yes_no(update_unit, update_sub1)
                        break

                    elif jenis_update == 4:
                        harga_baru = int(input("\n▣ Masukkan Harga Satuan Produk Baru: "))
                        def update_harga():
                            data_stok[item_update_key]['Harga Satuan'] = harga_baru
                            tampilan_data()
                            print("\nHarga Satuan Produk Berhasil Diupdate.")
                        yes_no(update_harga, update_sub1)
                        break
                    else:
                        menu_update()
            break           
        print("══"*50)
        yes_no(menu_update, menu_utama)
    print("══"*50)
    print('''
---------- ⚙️⚙️⚙️   Menu Update Stock dari Gudang ⚙️⚙️⚙️ ----------

    Pilihan Menu Update Stock dari Gudang:
    1. Update Stock dari Gudang
    2. Menampilkan Semua Data pada Gudang
    3. Kembali ke Menu Utama
    ''')
    user_input = input("Pilih Perintah yang Anda Inginkan (1-3) : ")

    if user_input == '1':
        print("══"*50)
        update_sub1()
        yes_no(menu_update,menu_utama)
    elif user_input == '2':
        print("══"*50)
        tampilan_data()
        yes_no(menu_update,menu_utama)
    elif user_input == '3':
        print("══"*50)
        menu_utama()
    else:
        menu_update()
    
def menu_delete():
    def menu_delete_sub1():
        print("══"*50)
        print('''\n---------- Hapus Data Stock dari Gudang ----------\n
        1. Hapus Data Stock di Gudang (Per Baris)
        2. Hapus Data sesuai Filtering Anda
        3. Hapus Semua Data di Gudang
        4. Kembali ke Menu Delete
        ''')
        user_input_delete = int(input('Delete yang Ingin Dipilih (1-4): '))    
        if user_input_delete == 1:
            tampilan_data()
            item_deletestok = input("Masukkan nama item yang mau dihapus: ").title()
            
            # Mencari Kode Produk berdasarkan Nama Produk
            item_delete_key = None
            for kode, detail_produk in data_stok.items():
                if detail_produk['Nama Produk'].lower() == item_deletestok.lower():
                    item_delete_key = kode
                    break
            
            if item_delete_key:
                def hapus_produk():
                    del data_stok[item_delete_key]
                    tampilan_data()
                    print("Produk berhasil dihapus.")
                yes_no(hapus_produk, menu_delete)
            else:
                menu_delete_sub1()  
        if user_input_delete == 2:
            tampilan_data()
            kategori_hapus = input("▣ Masukkan kategori yang mau dihapus: ").title()

            def hapus():
                global data_stok
                data_stok = {kode: detail for kode, detail in data_stok.items() if detail['Kategori'].lower() != kategori_hapus.lower()}
                tampilan_data()
                print(f"Semua produk dengan kategori '{kategori_hapus}' berhasil dihapus.")
                yes_no(menu_delete, menu_utama) 
                
            yes_no(hapus, menu_delete)
            
        if user_input_delete == 3:
            def hapus():
                global data_stok
                data_stok.clear()
                tampilan_data()
                print("Semua produk di gudang berhasil dihapus.")
                yes_no(menu_delete, menu_utama) 

            yes_no(hapus, menu_delete)
        
        if user_input_delete == 4:
            menu_delete()
        else:
            menu_delete_sub1()
    print("══"*50)
    print('''
---------- 🗑️ 🗑️ 🗑️  Menu Delete Stock Gudang 🗑️ 🗑️ 🗑️ ----------

    Pilihan Menu Delete Stock Gudang:
    1. Hapus Data Stock di Gudang
    2. Menampilkan Semua Data pada Gudang
    3. Kembali ke Menu Utama
    ''')
    user_input = input("Tampilan Stok Yang Ingin Dipilih (1-3) : ")

    if user_input == '1':
        print("══"*50)
        menu_delete_sub1()
        yes_no(menu_delete,menu_utama)
    elif user_input == '2':
        print("══"*50)
        tampilan_data()
        yes_no(menu_delete,menu_utama)
    elif user_input == '3':
        print("══"*50)
        menu_utama()
    else:
        menu_delete()
                
# Function Pendukung Untuk (menampilkan data) dan (Yes or No Question)    
    
def tampilan_data():
    print("\n▓▓▓ Laporan Stok JCDSOL Elecstorage ▓▓▓\n")
    print(f"{nama_kolom[0]: <10}|{nama_kolom[1]: <35}|{nama_kolom[2]: <15}|{nama_kolom[3]: <5}|{nama_kolom[4]: <10}")
    print("══════════+═══════════════════════════════════+═══════════════+═════+════════════")
    for i in data_stok.keys():
        harga_satuan = int(data_stok[i]['Harga Satuan'])
        harga_satuan_formatted = f"Rp {harga_satuan:,.0f}"
        print(f"{i: <10}|{(data_stok[i]['Nama Produk']): <35}|{(data_stok[i]['Kategori']): <15}|{str(data_stok[i]['Unit']): <5}|{harga_satuan_formatted: <15}")
    if len(data_stok) == 0:
        print("\t\tTidak ada Record yang tersedia.")   
    
def yes_no(yes, no):
    yes_no_input = input("\nApakah anda ingin melanjutkan (Y/N)? ").lower()
    if yes_no_input == 'y':
        yes()
    elif yes_no_input == 'n':
        no()
    else:
        print("\nINFO!! : Input yang anda masukkan salah")
        yes_no(yes, no)

   
menu_utama()

