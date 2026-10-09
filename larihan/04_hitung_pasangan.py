# Latihan 4: Menghitung Pasangan
# Loop luar dan loop dalam menghasilkan pasangan i dan j.
# Kondisi memeriksa apakah i + j <= n.
# Counter menghitung pasangan yang memenuhi kondisi.

n = int(input("n: "))

count = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i + j <= n:
            count += 1

print(f"Banyak pasangan = {count}")