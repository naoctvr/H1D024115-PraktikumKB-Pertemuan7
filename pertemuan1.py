import random
import datetime

pertanyaan = [
    ("Makanan khas Padang?", "Rendang"),
    ("Makanan dari Jepang?", "Sushi"),
    ("Makanan Italia berbentuk bulat?", "Pizza"),
    ("Makanan pedas dari Korea?", "Kimchi"),
    ("Makanan dari nasi yang digoreng?", "Nasi goreng")
]

random.shuffle(pertanyaan)

score = 0

waktu_mulai = datetime.datetime.now()
print("Kuis dimulai pada:", waktu_mulai)
print("--------------------------")

for soal in pertanyaan:
    q, jawaban_benar = soal

    print("Pertanyaan:", q)
    jawaban = input("Masukan Jawaban: ").strip()

    if jawaban.lower() == jawaban_benar.lower():
        print("Jawaban benar!")
        score += 1
    else:
        print("Jawaban salah!")

    print()

ulang = input("Ingin melihat skor? (y/n): ")
while ulang.lower() not in ["y", "n"]:
    ulang = input("Masukkan hanya y atau n: ")

if ulang.lower() == "y":
    print("Skor kamu:", score, "dari", len(pertanyaan))

print("Terima kasih sudah bermain kuis ini!")