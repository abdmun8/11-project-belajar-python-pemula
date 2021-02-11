# biografi info chalenge 3 dari 11
# tanya user tentang biodata
nama = ""
umur = -1
alamat = ""

# ambil nama
while len(nama) < 3 or type(nama) == int:
    try:
        print("Catatan: Nama harus lebih dari 2 huruf dan tidak boleh angka!")
        nama = input("Siapa nama anda?\n").capitalize()
    except:
        nama = ""

# ambil umur
while umur < 0:
    try:
        umur = int(input("Berapakah umur anda?\n"))
    except:
        umur = 0

# ambil alamat
while len(alamat.split(" ")) < 3 or type(alamat) == int:
    try:
        print("Catatan: Alamat harus lebih dari 2 kata!").capitalize()
        alamat = input("Dimana alamat anda?\n")
    except:
        alamat = ""

print("Biodata:")
print("- nama: {}".format(nama))
print("- Umur: {} tahun".format(umur))
print("- Alamat: {}".format(alamat))

"nama".capitalize()
