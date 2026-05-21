# Nhập 2 số nguyên dương m và n
m = int(input("Nhập số nguyên dương m: "))
n = int(input("Nhập số nguyên dương n: "))

# Tính tổng các chữ số của n
tong_chu_so_n = sum(int(chu_so) for chu_so in str(n))

print(f"Tổng các chữ số của n ({n}) là: {tong_chu_so_n}")

# Kiểm tra xem m có chia hết cho tổng đó không
if m % tong_chu_so_n == 0:
    print(f"Kết quả: {m} CHIA HẾT cho {tong_chu_so_n}.")
else:
    print(f"Kết quả: {m} KHÔNG chia hết cho {tong_chu_so_n}.")