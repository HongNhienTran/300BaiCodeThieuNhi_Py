def is_valid_sin(sin_str):
    sin_str = sin_str.replace(" ", "").replace("-", "")
    
    if len(sin_str) != 9 or not sin_str.isdigit():
        return False
        
    check_digit = int(sin_str[-1])
    
    # SỬA TẠI ĐÂY: Giữ nguyên thứ tự từ trái sang giống như ví dụ mẫu tính toán
    remaining_digits = sin_str[:-1] 
    
    s1 = 0  
    s2 = 0  
    
    # Duyệt từ trái sang phải của chuỗi 8 số còn lại
    for index, char in enumerate(remaining_digits, start=1):
        digit = int(char)
        
        if index % 2 != 0:
            # Vị trí lẻ (1, 3, 5, 7 từ trái sang): 1, 3, 5, 7 -> Tổng = 16
            s1 += digit
        else:
            # Vị trí chẵn (2, 4, 6, 8 từ trái sang): 9, 4, 6, 8 -> Nhân đôi
            doubled = digit * 2
            if doubled > 9:
                s2 += (doubled // 10) + (doubled % 10)
            else:
                s2 += doubled
                
    total_sum = s1 + s2 + check_digit
    
    return total_sum % 10 == 0

while True:
    user_input = input("Nhập số SIN cần kiểm tra (Nhập 0 để thoát): ").strip()
    if user_input == "0":
        print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
        break
    if is_valid_sin(user_input):
        print(f"-> Kết quả: Số SIN {user_input} HỢP LỆ.\n")
    else:
        print(f"-> Kết quả: Số SIN {user_input} KHÔNG hợp lệ. Vui lòng kiểm tra lại.\n")