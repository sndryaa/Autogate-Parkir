# PROJEK BERPIKIR KOMPUTASIONAL 1
# AUTOGATE PARKIR

# Kelompok 3 :
# 1. Arya Damar Rajendra        (16024357)
# 2. Kiti Andriani              (16024373)
# 3. Felisha                    (16024387)
# 4. Iffah Septianing Ratri     (16024403)
# 5. Inara Nafisa Kazzahra'i    (16024417)
# 6. Sandi Raya Gumilang        (16024444)

from datetime import datetime  # Menginput waktu secara otomatis
import time  # Untuk fungsi hitung mundur

# Fungsi untuk hitung mundur dan menutup palang
def hitung_mundur(detik):
    while detik > 0:
        print(f"Palang akan menutup dalam {detik} detik...", end="")
        time.sleep(1)
        detik -= 1
    print()

# Fungsi untuk deteksi kendaraan melewati portal
def cek_deteksi_kendaraan():
    print("Apakah kendaraan telah melewati portal? [1] Ya, [0] Tidak")
    return int(input("Masukkan pilihan: "))

# Fungsi untuk menutup palang
def tutup_palang():
    deteksi_kendaraan = cek_deteksi_kendaraan()
    if deteksi_kendaraan == 1:
        print("Kendaraan terdeteksi melewati portal. Menutup palang.")
    else:
        print("Kendaraan tidak terdeteksi. Menghitung mundur untuk menutup palang.")
        hitung_mundur(5)  # Hitung mundur sama untuk semua jenis kendaraan
    print("Palang parkir telah menutup.")

b = 0
banyak = []  # Daftar untuk menyimpan data kendaraan yang masuk

while True:
    print("=== PORTAL ITB JATINANGOR ===")
    print("[1] Masuk")
    print("[2] Keluar")
    print("[3] Shutdown")

    menu = int(input("Pilih menu: "))
    print()

    if menu == 1:
        print("- MENU MASUK -")

        while True:
            print("Pilih jenis kendaraan!")
            print("[1] Motor, [2] Mobil")
            kendaraan = int(input("Masukkan jenis kendaraan: "))
            nopol = input("Masukkan nomor plat kendaraan: ")

            waktu_sekarang = datetime.now()
            tanggal_masuk = int(waktu_sekarang.day)
            jam_masuk = int(waktu_sekarang.hour)
            menit_masuk = int(waktu_sekarang.minute)
            detik_masuk = int(waktu_sekarang.second)

            if kendaraan in [1, 2]:
                if kendaraan == 1 :
                    kendaraan = "Motor"
                else:
                    kendaraan = "Mobil"

                print()
                print("Apakah data sudah valid?")
                print("[1] Ya, [2] Tidak")
                validasi = int(input())

                if validasi == 1:
                    # Cetak karcis sebelum deteksi portal
                    print("[================================================]")
                    print("[        KARCIS PARKIR ITB JATINANGOR            ]")
                    print(f"[    Kendaraan : {kendaraan}                           ]")
                    print(f"[    Nomor     : {nopol}                         ]")
                    print(f"[    Waktu     : {waktu_sekarang}      ]")
                    print("[     Kunci kendaraan anda dengan rapat          ]")
                    print("[================================================]")

                    print()
                    # Deteksi kendaraan melewati portal menggunakan tutup_palang()
                    tutup_palang()

                    # Simpan data kendaraan hanya jika terdeteksi melewati portal
                    deteksi = cek_deteksi_kendaraan()
                    if deteksi == 1:
                        karcis = [kendaraan, nopol, tanggal_masuk, jam_masuk, menit_masuk, detik_masuk]
                        banyak += [karcis]
                        b += 1
                        print("Data kendaraan berhasil disimpan.")
                    else:
                        print("Kendaraan tidak terdeteksi melewati portal. Data tidak disimpan.")

                    print("==========================================")
                    print("JUMLAH KENDARAAN TERPARKIR SAAT INI: ", b)
                    print("==========================================")
                    print()
                    break
                else:
                    print("Data tidak valid. Silakan coba lagi.")
                    break
            else:
                print("Jenis kendaraan tidak valid")
                print()
    elif menu == 2:
        print("- MENU KELUAR -")
        nopol = input("Masukkan nomor plat kendaraan: ")

        i = 0
        while i < b:
            if b == 0:
                print("Tidak ada kendaraan terparkir!")
                print()
                break
            else:
                karcis = banyak[i]
                if karcis[1] != nopol:
                    if i < b - 1:
                        i += 1
                    else:
                        print("Kendaraan tidak ditemukan!")
                        print()
                        break
                elif karcis[1] == nopol:
                    print(f"Kendaraan ditemukan: {karcis[0]} dengan nomorplat {karcis[1]}")

                    # Memastikan apakah kendaraan melewati palang?
                    tutup_palang()
                    deteksi = cek_deteksi_kendaraan()
                    if deteksi == 1:
                        # Hapus kendaraan dari daftar
                        del banyak[i]
                        b -= 1
                    else:
                        print()

                    print("==========================================")
                    print("JUMLAH KENDARAAN TERPARKIR SAAT INI: ", b)
                    print("==========================================")
                    break
    elif menu == 3:
        print("Menutup program portal...")
        break
    else:
        print("Pilihan tidak valid!")
        print()