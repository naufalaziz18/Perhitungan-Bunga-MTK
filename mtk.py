# Fungsi untuk menghitung bunga majemuk
def hitung_bunga_majemuk(principal, rate, time, n):
    # principal: Modal awal
    # rate: Suku bunga tahunan dalam desimal (misalnya 5% = 0.05)
    # time: Waktu (tahun)
    # n: Jumlah penggabungan bunga per tahun
    amount = principal * (1 + rate/n)**(n*time)
    return amount

# Input dari pengguna
modal_awal = float(input("Masukkan modal awal: "))
suku_bunga = float(input("Masukkan suku bunga tahunan (dalam %): ")) / 100
waktu = int(input("Masukkan waktu (tahun): "))
n = int(input("Masukkan jumlah penggabungan bunga per tahun (misalnya 4 untuk triwulanan): "))

# Menghitung jumlah total
total = hitung_bunga_majemuk(modal_awal, suku_bunga, waktu, n)

# Menampilkan hasil
print(f"Jumlah total setelah {waktu} tahun adalah: Rp{total:.2f}")
