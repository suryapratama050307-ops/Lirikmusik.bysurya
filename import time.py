import time
import sys

lirik = [
    "Mengertiii,   mengertilah",
    "Banyak haaaaal yang tak kupahami",
    "Kendati kau kusuka",
    "Kita dua hati yang salah",
    "Bodoh pada waktu",
    "Itulah kenapa jatuh cinta dikatakan jatuh",
    "Karena sebagaimana kita jatuh",
    "Kita tidak punya kuasa",
    "Pilih jatuh pada hati yang",
    
]

waktu_Jeda = 0.85

print("Memulai lagu 3 detik...")

for i in range(3, 0, -1):
    print("...")
    time.sleep(3)

print("\n==Dunia Yang Nanti==\n")


for baris in lirik:
    for huruf in baris :
        sys.stdout.write(huruf)
        sys.stdout.flush()
        time.sleep(0.20)      
    print()
    time.sleep(waktu_Jeda)

print("\nHatur nuhun tos BUCAT!!!\n")