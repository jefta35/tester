import subprocess

def buka_tambah_pasien():
    subprocess.run(["python", "tambah_pasien.py"])

def buka_tampil_pasien():
    subprocess.run(["python", "tampil_pasien.py"])

def menu_utama():
    while True:
        print("\n" + "=" * 40)
        print(" KLINIK SEHAT ".center(40, "="))
        print("=" * 40)
        print("1. Tambah Pasien")
        print("2. Tampilkan Pasien")
        print("0. Keluar")
        print("=" * 40)
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            buka_tambah_pasien()
        elif pilihan == "2":
            buka_tampil_pasien()
        elif pilihan == "0":
            print("Terima kasih.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    menu_utama()