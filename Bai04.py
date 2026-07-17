import math

# def check_triangle(a, b, c):
#     if a + b > c and a + c > b and b + c > a:
#         return True
#     else: 
#         return False

def check_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def get_triangle_type(a, b, c):
    a2, b2, c2 = round(a**2, 2), round(b**2, 2), round(c**2, 2)
    is_right_triangle = (a2 + b2 == c2) or (a2 + c2 == b2) or (b2 + c2 == a2)
    is_isosceles_triangle = (a == b) or (a == c) or (b == c)

    if a == b == c:
        return "đều"
    elif is_right_triangle and is_isosceles_triangle:
        return "vuông cân"
    elif is_right_triangle:
        return "vuông"
    elif is_isosceles_triangle:
        return "cân"
    else:
        return "thường"

def calc_area(a, b, c):
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area

try:
    a, b, c = map(float, input("Nhập 3 cạnh của tam giác: ").split())

    if a<=0 or b<=0 or c<=0:
        print("Các cạnh phải là số dương.")
    elif check_triangle(a, b, c):
        triangle_type = get_triangle_type(a, b, c)
        area = calc_area(a, b, c)
        print(f"Tam giác {triangle_type} có diện tích là: {area:.2f}")
    else:
        print("Không phải là tam giác.")
except ValueError:
    print("Vui lòng nhập các cạnh hợp lệ.")




