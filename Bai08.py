import math

def solve_quadratic(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Phương trình có vô số nghiệm."
            else:
                return "Phương trình vô nghiệm."
        else:
            return f"Phương trình có nghiệm duy nhất: x = {-c / b}"
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            return "Phương trình vô nghiệm."
        elif delta == 0:
            x = -b / (2*a)
            return f"Phương trình có nghiệm kép: x1 = x2 = {x}"
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            return f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}"

try:
    a, b, c = map(float, input("Nhâp vào tham số a, b, c của phương trình bậc hai ax^2 + bx + c = 0: ").split())
    print(solve_quadratic(a, b, c))
except ValueError:  
    print("Vui lòng nhập ba số thực hợp lệ.")