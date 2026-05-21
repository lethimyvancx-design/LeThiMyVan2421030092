import math
def dien_tich_hinh_tron(r):
    return math.pi * r * r
def dien_tich_hinh_chu_nhat(a, b):
    return a * b
def dien_tich_hinh_vuong(a):
    return a**2
def chu_vi_hinh_chu_nhat(a, b):
    return (a + b) * 2
chieu_dai = int(input("chieu dai hinh chu nhat la: "))
chieu_rong = int(input("chieu rong hinh chu nhat la: "))
print("dien tich hinh chu nhat la:", dien_tich_hinh_chu_nhat(chieu_dai, chieu_rong))
print("chu vi hinh chu nhat la:", chu_vi_hinh_chu_nhat(chieu_dai, chieu_rong))


ban_kinh = int(input("ban kinh hinh tron la: "))
print("dien tich hinh tron la:", dien_tich_hinh_tron(ban_kinh))


canh = int(input("nhap canh hinh vuong: "))
print("dien tich hinh vuong la:", dien_tich_hinh_vuong(canh))