import math

try:
    a, b, c = map(int, input("Nhập ba số nguyên a, b, c: ").split())

    if a > b:
        temp = a
        a = b
        b = temp
    if b > c:
        temp = b
        b = c
        c = temp
    if a > b:
        temp = a
        a = b
        b = temp
    
    print("Các số nguyên sau khi sắp xếp theo thứ tự tăng dần là: ", a, b, c)

except ValueError:
    print("Vui lòng nhập ba số nguyên hợp lệ.")

# dùng Tuple Unpacking, sort
try:
    a, b, c = sorted(map(int, input("Nhập ba số nguyên a, b, c: ").split()))
    print("Các số nguyên sau khi sắp xếp theo thứ tự tăng dần là: ", a, b, c)
except ValueError:
    print("Vui lòng nhập ba số nguyên hợp lệ.")

# thự tự giảm dần
try: 
    a, b, c = sorted(map(int, input("Nhập ba số nguyên a, b, c: ").split()), reverse=True)
    print("Các số nguyên sau khi sắp xếp theo thứ tự giảm dần là: ", a, b, c)
except ValueError:
    print("Vui lòng nhập ba số nguyên hợp lệ.")
    