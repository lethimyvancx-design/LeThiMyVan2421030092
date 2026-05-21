# Hàm kiểm tra số nguyên tố
def la_so_nguyen_to(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True


# Nhập số phần tử
n = int(input("Nhap n: "))

# Nhập dãy số
tong = 0

for i in range(n):
    x = int(input(f"Nhap x{i+1}: "))
    
    if la_so_nguyen_to(x):
        tong += x

print("Tong cac so nguyen to =", tong)

# Kiểm tra điều kiện
if tong % 2 != 0 and tong > 50:
    print("Tong la so le va lon hon 50")
else:
    print("Tong khong thoa man dieu kien")