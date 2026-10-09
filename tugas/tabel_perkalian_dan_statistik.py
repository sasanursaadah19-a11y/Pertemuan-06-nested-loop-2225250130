# Tugas 3: Tabel Perkalian dan Statistik

n = int(input("Masukkan n: "))

while n <= 0:
    print("n harus positif.")
    n = int(input("Masukkan n: "))

    
print("\nTabel Perkalian:")
total_semua = 0
jumlah_genap = 0

for i in range(1, n + 1):
    total_baris = 0

    for j in range(1, n + 1):
        hasil = i * j
        print(hasil, end="\t")

        total_semua += hasil
        total_baris += hasil

        if hasil % 2 == 0:
            jumlah_genap += 1

    print(f"| Jumlah baris: {total_baris}")

print("\nTotal semua hasil:", total_semua)
print("Jumlah hasil genap:", jumlah_genap)