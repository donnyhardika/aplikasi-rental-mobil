# === PROGRAM CRUD RENTAL MOBIL ===
# Nama: Donny Aditya Hardika

# Data awal (list of dictionaries)
rental_mobil = [
    {"id": 1, "merk": "Toyota Avanza", "tahun": 2023, "harga": 400000, "status": "Tersedia"},
    {"id": 2, "merk": "Honda Brio", "tahun": 2024, "harga": 350000, "status": "Tersedia"},
    {"id": 3, "merk": "Daihatsu Sigra", "tahun": 2025, "harga": 300000, "status": "Tersedia"}
]

# Fungsi tampilkan data
def tampilkan_data():
    print("\n=== DATA RENTAL MOBIL ===")
    print(f"{'ID':<4} | {'Merk':<15} | {'Tahun':<6} | {'Harga':<12} | {'Status':<10}")
    print("-" * 55)
    for mobil in rental_mobil:
        print(f"{mobil['id']:<4} | {mobil['merk']:<15} | {mobil['tahun']:<6} | Rp{mobil['harga']:<10,} | {mobil['status']:<10}")

# Data awal next_id untuk penambahan data baru
next_id = len(rental_mobil) + 1

# Fungsi cari mobil
def cari_mobil():
    kata = input("Masukkan kata kunci merk: ").lower()
    hasil = [m for m in rental_mobil if kata in m["merk"].lower()]
    if not hasil:
        print("! Tidak ada mobil yang cocok.")
    else:
        print("\nHasil pencarian:")
        print(f"{'ID':<4} | {'Merk':<15} | {'Tahun':<6} | {'Harga':<12} | {'Status':<10}")
        print("-" * 55)
        for m in hasil:
            print(f"{m['id']:<4} | {m['merk']:<15} | {m['tahun']:<6} | Rp{m['harga']:<10,} | {m['status']:<10}")

# Fungsi tambah data mobil
def tambah_data():
    global next_id
    merk = input("Masukkan merk mobil: ")
    try:
        tahun = int(input("Masukkan tahun mobil: "))
    except ValueError:
        print("Tahun harus berupa angka!")
        return
    if tahun < 1990 or tahun > 2025:
        print("Tahun harus antara 1990–2025!")
        return
    try:
        harga = int(input("Masukkan harga sewa per hari: "))
    except ValueError:
        print("Harga harus berupa angka!")
        return
    if harga <= 0:
        print("Harga harus lebih dari 0!")
        return

    status = input("Masukkan status mobil (tersedia/dirental): ").lower()
    if status not in ["tersedia", "dirental"]:
        print("Status harus 'tersedia' atau 'dirental'!")
        return

    mobil = {"id": next_id, "merk": merk, "tahun": tahun, "harga": harga, "status": status}
    rental_mobil.append(mobil)
    print(f"Mobil dengan ID {next_id} berhasil ditambahkan.")
    next_id += 1

# Fungsi update data
def update_data():
    try:
        id_mobil = int(input("Masukkan ID mobil yang ingin diupdate: "))
    except ValueError:
        print("ID harus berupa angka!")
        return
    for m in rental_mobil:
        if m["id"] == id_mobil:
            print(f"Data lama: {m}")
            merk = input("Merk baru: ")
            try:
                tahun = int(input("Tahun baru: "))
            except ValueError:
                print("Tahun harus berupa angka!")
                return
            if tahun < 1990 or tahun > 2025:
                print("Tahun harus antara 1990–2025!")
                return
            try:
                harga = int(input("Harga baru: "))
            except ValueError:
                print("Harga harus berupa angka!")
                return
            if harga <= 0:
                print("Harga harus lebih dari 0!")
                return

            status = input("Status baru (tersedia/dirental): ").lower()
            if status not in ["tersedia", "dirental"]:
                print("Status harus 'tersedia' atau 'dirental'!")
                return

            konfirmasi = input("Apakah yakin ingin mengubah data ini? (y/n): ")
            if konfirmasi.lower() == "y":
                m["merk"] = merk
                m["tahun"] = tahun
                m["harga"] = harga
                m["status"] = status
                print("Data berhasil diubah.")
            else:
                print("Perubahan dibatalkan.")
            return
    print("ID mobil tidak ditemukan.")

# Fungsi hapus data
def hapus_data():
    try:
        id_mobil = int(input("Masukkan ID mobil yang ingin dihapus: "))
    except ValueError:
        print("ID harus berupa angka!")
        return
    for m in rental_mobil:
        if m["id"] == id_mobil:
            print(f"Data: {m}")
            konfirmasi = input("Apakah yakin ingin menghapus data ini? (y/n): ")
            if konfirmasi.lower() == "y":
                rental_mobil.remove(m)
                print("Data berhasil dihapus.")
            else:
                print("Penghapusan dibatalkan.")
            return
    print("ID mobil tidak ditemukan.")

# Menu utama
while True:
    print("\n=== MENU RENTAL MOBIL ===")
    print("1. Lihat Data Mobil")
    print("2. Cari Mobil")
    print("3. Tambah Data Mobil")
    print("4. Update Data Mobil")
    print("5. Hapus Data Mobil")
    print("6. Keluar Program")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampilkan_data()
    elif pilihan == "2":
        cari_mobil()
    elif pilihan == "3":
        tambah_data()
    elif pilihan == "4":
        update_data()
    elif pilihan == "5":
        hapus_data()
    elif pilihan == "6":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")

# end of program
