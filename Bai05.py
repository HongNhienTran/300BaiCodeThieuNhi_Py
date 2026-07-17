import math

def calc_triangle_area(a, b, c):
    return 0.5 * abs(a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]))

try:
    a = tuple(map(float, input("Nhập tọa độ điểm A(x, y): ").split()))
    b = tuple(map(float, input("Nhập tọa độ điểm B(x, y): ").split()))
    c = tuple(map(float, input("Nhập tọa độ điểm C(x, y): ").split()))
    M = tuple(map(float, input("Nhập tọa độ điểm M(x, y): ").split()))

    area_ABC = calc_triangle_area(a, b, c)
    area_ABM = calc_triangle_area(a, b, M)
    area_ACM = calc_triangle_area(a, c, M)
    area_BCM = calc_triangle_area(b, c, M)

    sum_of_areas = area_ABM + area_ACM + area_BCM

    if math.isclose(sum_of_areas, area_ABC, abs_tol=1e-5):
        
        if math.isclose(area_ABM, 0.0, abs_tol=1e-5) or \
           math.isclose(area_ACM, 0.0, abs_tol=1e-5) or \
           math.isclose(area_BCM, 0.0, abs_tol=1e-5):
            print("Điểm M nằm trên cạnh của tam giác ABC.")
        else:
            print("Điểm M nằm trong tam giác ABC.")
            
    else:
        print("Điểm M nằm ngoài tam giác ABC.")

except ValueError:
    print("Vui lòng nhập các tọa độ hợp lệ dưới dạng số thực ngăn cách bởi khoảng trắng (ví dụ: 3 4).")