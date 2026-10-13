import csv
import os
from models import Pasien

def simpan_pasien():
    print("\n=== TAMBAH DATA PASIEN ===")
    id_pasien = input("ID Pasien   : ").strip()
    nama = input("Nama Pasien : ").strip()
    keluhan = input("Keluhan     : ").strip()
    gol_darah = input("Gol. Darah  : ").strip()

    if not id_pasien or not nama or not keluhan or not gol_darah:
        print("\n[PERINGATAN] Semua kolom harus diisi!\n")
        return

    pasien = Pasien(id_pasien, nama, keluhan, gol_darah)
    file_exists = os.path.exists("pasien.csv")

    with open("pasien.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["ID Pasien", "Nama", "Keluhan", "Gol. Darah", "Status"])
        writer.writerow(pasien.to_list())

    print("\n[BERHASIL] Data pasien berhasil ditambahkan.\n")

def main():
    while True:
        print("=== MENU TAMBAH PASIEN ===")
        print("1. Tambah Pasien")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            simpan_pasien()
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.\n")

if __name__ == "__main__":
    main()