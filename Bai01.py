import math

S = float(input("Nhập vào diện tích S của mặt cầu: "))
r = math.sqrt(S / (4 * math.pi))
print("Bán kính của mặt cầu là:", r)
V = (4/3) * math.pi * r**3
print("Thể tích của mặt cầu là:", V)