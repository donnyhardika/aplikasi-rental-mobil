# === PROGRAM CRUD RENTAL MOBIL ===
# Nama: Donny Aditya Hardika

# Data awal (list of dictionaries)
rental_mobil = [
    {"id": 1, "merk": "Toyota Avanza", "tahun": 2020, "harga": 350000},
    {"id": 2, "merk": "Honda Brio", "tahun": 2021, "harga": 300000},
]

# Fungsi tampilkan data
def tampilkan_data():
    print("\n=== DATA RENTAL MOBIL ===")
    print(f"{'ID':<4} {'Merk':<15} {'Tahun':<6} {'Harga':<10}")
    print("-" * 40)
    for mobil in rental_mobil:
        print(f"{mobil['id']:<4} {mobil['merk']:<15} {mobil['tahun']:<6} Rp{mobil['harga']:<10,}")

# Fungsi tambah data
def tambah_data():
    id_baru = len(rental_mobil) + 1
    merk = input("Masukkan merk mobil: ")
    tahun = int(input("Masukkan tahun mobil: "))
    harga = int(input("Masukkan harga sewa per hari: "))
    rental_mobil.append({"id": id_baru, "merk": merk, "tahun": tahun, "harga": harga})
    print("Data berhasil ditambahkan!")

# Fungsi update data
def update_data():
    tampilkan_data()
    id_update = int(input("Masukkan ID mobil yang ingin diupdate: "))
    for mobil in rental_mobil:
        if mobil["id"] == id_update:
            mobil["merk"] = input("Merk baru: ")
            mobil["tahun"] = int(input("Tahun baru: "))
            mobil["harga"] = int(input("Harga baru: "))
            print("Data berhasil diupdate!")
            return
    print("ID tidak ditemukan!")

# Fungsi hapus data
def hapus_data():
    tampilkan_data()
    id_hapus = int(input("Masukkan ID mobil yang ingin dihapus: "))
    for mobil in rental_mobil:
        if mobil["id"] == id_hapus:
            rental_mobil.remove(mobil)
            print("Data berhasil dihapus!")
            return
    print("ID tidak ditemukan!")

# Menu utama
while True:
    print("\n=== MENU RENTAL MOBIL ===")
    print("1. Lihat Data Mobil")
    print("2. Tambah Data Mobil")
    print("3. Update Data Mobil")
    print("4. Hapus Data Mobil")
    print("5. Keluar Program")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampilkan_data()
    elif pilihan == "2":
        tambah_data()
    elif pilihan == "3":
        update_data()
    elif pilihan == "4":
        hapus_data()
    elif pilihan == "5":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
