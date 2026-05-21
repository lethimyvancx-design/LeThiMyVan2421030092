# Nhập số lượng phần tử n
n = int(input("Nhập số lượng phần tử n (0 < n < 100): "))

# Nhập dãy số thực
day_so = []
for i in range(n):
    x = float(input(f"Nhập phần tử thứ {i+1}: "))
    day_so.append(x)

# Lọc các phần tử dương nằm trong khoảng (0, 1000)
cac_so_thoa_man = [x for x in day_so if 0 < x < 1000]

# Tính trung bình cộng
if len(cac_so_thoa_man) > 0:
    tbc = sum(cac_so_thoa_man) / len(cac_so_thoa_man)
    print(f"Trung bình cộng các phần tử thỏa mãn là: {tbc:.2f}")
else:
    print("Không có phần tử nào thỏa mãn điều kiện (0 < x < 1000).")