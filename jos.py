def binary_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


angka = [10, 23, 35, 47, 59, 62, 78, 90]
print("Daftar angka:", angka)

# Nangkep input dari terminal dan ubah jadi angka bulat
dicari = int(input("Masukkan angka yang mau dicari: "))

hasil = binary_search(angka, dicari)

if hasil != -1:
    print(f"Angka {dicari} ketemu di indeks ke-{hasil}")
else:
    print(f"Angka {dicari} nggak ada di dalam list")