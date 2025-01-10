print("=========== Anggota Kelompok ==================")
print("1. Nama: Ahmad Alfarizi - NIM: 24241185")
print("2. Nama: Egi Ferdiansyah - NIM: 24241176")
print("3. Nama: Ihja Nurhidayat - NIM: 24241183")
print("4. Nama: M. Adel Fitrah - NIM: 24241153")
print("5. Nama: Kezia Ardia Sasaki - NIM: 24241169")
print("=== Program Menentukan Kelulusan Dengan Nilai Rata-Rata======")


nama = input("\nMasukkan nama mahasiswa: ")
nilai_1 = float(input("Masukkan nilai Matematika (1/100): "))
nilai_2 = float(input("Masukkan nilai Nilai Bahasa (1/100): "))
nilai_3 = float(input("Masukkan nilai Agama (1/100): "))

cek_input_valid = nilai_1 or nilai_2 or nilai_3
input_valid = True
tidak_valid = "Input Tidak Sesuai"

if cek_input_valid < 0 or cek_input_valid> 100:
    input_valid = False
    print(tidak_valid)


rata_rata = (nilai_1 + nilai_2 + nilai_3) / 3
nilai_akhir = rata_rata
status = ""

if input_valid == True and nilai_akhir >= 75 and nilai_akhir <= 100:
    status = "Lulus"
    print(f"\nMahasiswa {nama} dengan nilai {nilai_akhir} dinyatakan: {status}")
elif  input_valid == False:
    print(tidak_valid)

elif input_valid == True:
    status = "Tidak Lulus"
    print(f"\nMahasiswa {nama} dengan nilai {nilai_akhir} dinyatakan: {status}")