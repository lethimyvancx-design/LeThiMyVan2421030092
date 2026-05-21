# Nhập ba số nguyên dương
x = int(input("Nhap x: "))
y = int(input("Nhap y: "))
z = int(input("Nhap z: "))

# Tính tích
tich = x * y * z

print("Tich =", tich)

# Đếm số chữ số
so_chu_so = len(str(tich))

# Tìm chữ số lớn nhất
max_digit = max(str(tich))

print("So chu so cua tich =", so_chu_so)
print("Chu so lon nhat =", max_digit)