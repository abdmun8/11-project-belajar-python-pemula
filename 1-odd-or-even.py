# ganjil genap challenge 1 dari 11
# user input angka dan beritahu mereka angka yang dimasukan ganjil atau genap
try:
    num = int(input("Angka berapa yang ada di pikiranmu?\n"))
except:
    print("Kamu harus memasukan angka!")
    exit(1)
result = "genap" if num % 2 == 0 else "ganjil"
print("kamu memasukan angka {}!".format(result))
