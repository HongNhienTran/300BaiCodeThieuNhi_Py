import math

def solve_system_of_equations(a1, b1, c1, a2, b2, c2):
    D = a1 * b2 - a2 * b1
    Dx = c1 * b2 - c2 * b1
    Dy = a1 * c2 - a2 * c1

    if not math.isclose(D, 0.0, abs_tol=1e-9):
        x = Dx / D
        y = Dy / D
        
        if math.isclose(x, 0.0, abs_tol=1e-9): x = 0.0
        if math.isclose(y, 0.0, abs_tol=1e-9): y = 0.0
        
        return f"x = {x:.4f}\ny = {y:.4f}"
    else:
        if math.isclose(Dx, 0.0, abs_tol=1e-9) and math.isclose(Dy, 0.0, abs_tol=1e-9):
            return "Hệ phương trình có VÔ SỐ NGHIỆM."
        else:
            return "Hệ phương trình VÔ NGHIỆM."

try:
    a1, b1, c1 = map(float, input("Nhap a1, b1, c1: ").split())
    a2, b2, c2 = map(float, input("Nhap a2, b2, c2: ").split())

    result = solve_system_of_equations(a1, b1, c1, a2, b2, c2)
    print(result)

except ValueError:
    print("Vui lòng nhập các hệ số hợp lệ dưới dạng số thực!")