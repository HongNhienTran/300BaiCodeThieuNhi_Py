import math

def process_angele(total_min):
    normalized_min = total_min % 21600

    if normalized_min < 0:
        normalized_min += 21600

    quadrant_index = int(normalized_min // 5400) + 1

    radian_angle = (normalized_min / 21600) * 2 * math.pi
    degree_angle = (normalized_min / 21600) * 360

    cosine_value = math.cos(radian_angle)
    sine_value = math.sin(radian_angle)
    
    return {
        "normalized_min": normalized_min,
        "quadrant_index": quadrant_index,
        "radian_angle": radian_angle,
        "degree_angle": degree_angle,
        "cosine_value": cosine_value,
        "sine_value": sine_value
    }

try:
    total_min = float(input("Nhập tổng số phút (có thể âm): "))
    result = process_angele(total_min)
    
    print(f"Giá trị phút chuẩn hóa: {result['normalized_min']}")
    print(f"Chỉ số góc phần tư: {result['quadrant_index']}")
    print(f"Góc theo radian: {result['radian_angle']}")
    print(f"Góc theo độ: {result['degree_angle']}")
    print(f"Giá trị cosin: {result['cosine_value']}")
    print(f"Giá trị sin: {result['sine_value']}")
except ValueError:
    print("Vui lòng nhập một số thực hợp lệ.")