import csv
import os
from models import Pasien

def muat_data():
    daftar_pasien = []
    if not os.path.exists("pasien.csv"):
        print("File pasien.csv tidak ditemukan.")
        return daftar_pasien

    with open("pasien.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)  # Lewati header
        for row in reader:
            pasien = Pasien(
                id_pasien=row[0],
                nama=row[1],
                keluhan=row[2],
                gol_darah=row[3],
                status=row[4]
            )
            daftar_pasien.append(pasien)
    return daftar_pasien

def tampilkan_pasien():
    daftar_pasien = muat_data()
    if not daftar_pasien:
        print("Tidak ada data pasien.")
        return

    print("\n=== DAFTAR PASIEN KLINIK PRATAMA ===\n")
    print(f"{'ID Pasien':12}{'Nama Pasien':22}{'Keluhan':22}{'Gol. Darah':12}{'Status'}")
    print("-" * 80)
    for pasien in daftar_pasien:
        print(
            f"{pasien.id:12}"
            f"{pasien.nama:22}"
            f"{pasien.keluhan:22}"
            f"{pasien.gol_darah:12}"
            f"{pasien.status}"
        )
    print("-" * 80)
    print(f"Total Pasien: {len(daftar_pasien)}")

def main():
    while True:
        print("\n=== MENU ===")
        print("1. Tampilkan Pasien")
        print("2. Refresh Data")
        print("0. Keluar")
        pilihan = input("Pilih: ")
        if pilihan == "1":
            tampilkan_pasien()
        elif pilihan == "2":
            print("Data dimuat ulang...")
            tampilkan_pasien()
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()