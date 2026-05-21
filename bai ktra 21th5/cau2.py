# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))

# Tính tổng các chữ số bằng cách chuyển n thành chuỗi ký tự
tong_chu_so = sum(int(chu_so) for chu_so in str(n))

print(f"Tổng các chữ số của n là: {tong_chu_so}")

# Kiểm tra chia hết cho 3
if tong_chu_so % 3 == 0:
    print(f"Tổng các chữ số ({tong_chu_so}) CHIA HẾT cho 3.")
else:
    print(f"Tổng các chữ số ({tong_chu_so}) KHÔNG chia hết cho 3.")