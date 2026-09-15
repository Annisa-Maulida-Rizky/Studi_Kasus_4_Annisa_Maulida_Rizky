buku = {
    "Judul" : "Bumi",
    "Penulis" : "Tere Liye",
    "Tahun Terbit" : "2014"
}

while True:
    print("Menu: ")
    print("1. Tampilkan data buku")
    print("2. Tambahkan Penerbit")
    print("3. Ubah data Penulis")
    print("4. Hapus data Penerbit")

    Pilih_menu = input("Pilih menu(ketik keluar untuk berhenti): ")

    if Pilih_menu == "keluar":
        break

    if Pilih_menu == "1":

        print("Berikut adalah data buku: ")
        print(buku)

    elif Pilih_menu == "2":
        buku["Penerbit"] = "Gramedia Pustaka Utama"

        print("Setelah ditambahkan: ")
        print(buku)

    elif Pilih_menu == "3":
        buku.update({"Penulis" : "Darwis"})

        print("Setelah diupdate: ")
        print(buku)

    elif Pilih_menu == "4":
        if "Penerbit" in buku:
            buku.pop("Penerbit")

            print("Setelah dihapus: ")
            print(buku)
        else:
            print("Belum ada data Penerbit")


    else:
        print("Pilihan tidak ada. Harap pilih ulang sesuai menu")