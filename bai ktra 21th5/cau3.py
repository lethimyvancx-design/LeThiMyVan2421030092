# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))

# Tính tích các chữ số
tich_chu_so = 1
for chu_so in str(n):
    tich_chu_so *= int(chu_so)

print(f"Tích các chữ số của n là: {tich_chu_so}")

# Kiểm tra điều kiện: chẵn (chia hết cho 2) VÀ lớn hơn 20
if tich_chu_so % 2 == 0 and tich_chu_so > 20:
    print("Tích thỏa mãn điều kiện: là số chẵn và lớn hơn 20.")
else:
    print("Tích KHÔNG thỏa mãn điều kiện.")