xC, yC = map(float, input("Nhập vào tạo độ điểm C(xC, yC): ").split())
r = float(input("Nhập vào bán kính r: "))
xM, yM = map(float, input("Nhập vào tọa độ điểm M(xM, yM): ").split())

distance = (xM - xC)**2 + (yM - yC)**2 

print("Khoảng cách từ điểm M đến tâm C là: ", distance)

if distance < r**2:
    print("Điểm M nằm trong đường tròn.")
elif distance == r**2:
    print("Điểm M nằm trên đường tròn.")
else:
    print("Điểm M nằm ngoài đường tròn.")


