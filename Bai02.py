import math

xA, yA = map(float, input("Nhập vào tọa độ điểm A(xA, yA): ").split())
xB, yB = map(float, input("Nhập vào tọa độ điểm B(xB, yB): ").split())
distance = math.sqrt((xB - xA)**2 + (yB - yA)**2)

print("Khoảng cách giữa hai điểm A và B là:", distance)