# Nhập ba số nguyên dương
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))

# Tính tổng
tong = a + b + c

print("Tong =", tong)

# Đếm chữ số chẵn
dem = 0

for ch in str(tong):
    if int(ch) % 2 == 0:
        dem += 1

print("So chu so chan trong tong =", dem)