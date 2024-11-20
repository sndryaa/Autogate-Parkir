# PROYEK BERPIKIR KOMPUTASIONAL 1
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
        print(f"Palang akan menutup dalam {detik} detik...")
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
    print("Palang parkir telah tertutup.")

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
                print()

                if validasi == 1:
                    # Cetak karcis sebelum deteksi portal
                    print("[]================================================[]")
                    print("         KARCIS PARKIR ITB JATINANGOR            ")
                    print()
                    print(f"     Kendaraan : {kendaraan}                           ")
                    print(f"     Nomor     : {nopol}                        ")
                    print(f"     Waktu     : {waktu_sekarang}      ")
                    print()
                    print("         Kunci kendaraan anda dengan rapat          ")
                    print("[]================================================[]")

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
                    print()
                    break
            else:
                print("Jenis kendaraan tidak valid")
                print()

    elif menu == 2:
        print("- MENU KELUAR -")
        nopol = input("Masukkan nomor plat kendaraan: ")

        if b == 0:
            print("Tidak ada kendaraan terparkir!")
            print()

        else:
            i = 0
            while i < b:
                    karcis = banyak[i]
                    if karcis[1] != nopol:
                        if i < b - 1:
                            i += 1
                        else:
                            print("Kendaraan tidak ditemukan!")
                            print()
                            break

                    elif karcis[1] == nopol:
                        print(f"Kendaraan ditemukan: {karcis[0]} dengan plat nomor {karcis[1]}")
                        # Input data waktu otomatis dari sistem
                        waktu_sekarang = datetime.now()
                        tanggal_keluar = int(waktu_sekarang.day)
                        jam_keluar = int(waktu_sekarang.hour)
                        menit_keluar = int(waktu_sekarang.minute)
                        detik_keluar = int(waktu_sekarang.second)

                        # Hitung durasi parkir
                        total_detik_masuk = jam_masuk * 3600 + menit_masuk * 60 + detik_masuk
                        total_detik_keluar = jam_keluar * 3600 + menit_keluar * 60 + detik_keluar
                        durasi_hari = tanggal_keluar - karcis[2]
                        durasi_detik = total_detik_keluar - total_detik_masuk

                        if durasi_detik < 0:
                            durasi_detik += 24 * 3600 # Tambahkan satu hari dalam detik jika melewati tengah malam

                        total_durasi_menit = durasi_hari * 1440 + (durasi_detik // 60) # Total durasi dalam menit

                        # Pembayaran
                        biaya = 0
                        if karcis[0].lower() == "motor":
                            # Durasi parkir di hari pertama
                            if durasi_hari == 0 :
                                if total_durasi_menit <= 60 :
                                    biaya = 1000  # 1 jam pertama

                                else: # Biaya untuk jam berikutnya
                                    biaya = 1000 + (total_durasi_menit - 60) // 60 * 1000  # setengah jam atau lebih
                            else: # Durasi Hari lebih dari 1 hari
                                biaya = 10000 + durasi_hari * 10000

                        elif karcis[0].lower() == "mobil":
                            # Durasi parkir di hari pertama
                            if durasi_hari == 0 :
                                if total_durasi_menit <= 60:
                                    biaya = 5000  # 1 jam pertama
                                else: # Biaya untuk jam berikutnya
                                    biaya = 5000 + (total_durasi_menit - 60) // 60 * 5000
                            else: # Durasi parkir lebih dari 1 hari
                                biaya = 25000 +  durasi_hari * 25000

                        # Tampilkan rincian
                        durasi_jam = total_durasi_menit // 60
                        sisa_menit = total_durasi_menit % 60

                        print("Biaya parkir untuk kendaraan", nopol, "adalah Rp ",biaya)
                        print("Durasi parkir:", durasi_hari, "hari", durasi_jam, "jam", sisa_menit, "menit")

                        # Pembayaran
                        while True:
                            print("Pilih metode pembayaran: ")
                            print("[1] Cash")
                            print("[2] Kartu elektronik")
                            metode_pembayaran = int(input("Masukkan pilihan: "))

                            if metode_pembayaran == 1 :
                                print("Silakan membayar sebesar Rp", biaya, "secara tunai.")
                                time.sleep(3)
                                print("Terima kasih, hati-hati di jalan!")
                                break

                            elif metode_pembayaran == 2 :
                                print("Silakan tempel kartu anda!")
                                saldo_kartu = int(input("Saldo kartu anda: "))

                                if saldo_kartu >= biaya:
                                    saldo_kartu -= biaya
                                    print("Kartu anda tersisa Rp", saldo_kartu)
                                    print("Terima kasih, hati-hati di jalan!")
                                    break
                                else:
                                    print("Saldo kartu anda tidak mencukupi!")
                                    continue # Kembali ke menu pembayaran

                        # Tambahkan hitung mundur menutup palang portal
                        if karcis[0].lower() == "motor":
                            print()
                            hitung_mundur(7)
                        else:
                            print()
                            hitung_mundur(10)
                        # Memastikan apakah kendaraan melewati palang
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
