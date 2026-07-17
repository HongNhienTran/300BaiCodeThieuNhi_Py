import math

def solve_linear_equation(a, b):
    if math.isclose(a, 0.0, abs_tol=1e-5):
        if math.isclose(b, 0.0, abs_tol=1e-5):
            return "Phương trình có vô số nghiệm."
        else:
            return "Phương trình vô nghiệm."
    else:
        return f"Phương trình có nghiệm duy nhất: x = {-b / a}"

try:
    a, b = map(float, input("Nhập hệ số a và b của phương trình ax + b = 0: ").split())
    print(solve_linear_equation(a, b))
except ValueError:
    print("Vui lòng nhập hai số thực hợp lệ.")