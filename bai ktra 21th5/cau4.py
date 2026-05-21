# Nhập 2 số nguyên dương a và b
a = int(input("Nhập số nguyên dương a: "))
# Sử dụng vòng lặp để đảm bảo b cũng là số nguyên dương tương tự
b = int(input("Nhập số nguyên dương b: "))

# Tính tổng
tong = a + b
print(f"Tổng ({a} + {b}) = {tong}")

# Tìm chữ số lớn nhất trong tổng bằng cách chuyển tổng thành chuỗi
chu_so_lon_nhat = max(str(tong))

print(f"Chữ số lớn nhất trong tổng là: {chu_so_lon_nhat}")