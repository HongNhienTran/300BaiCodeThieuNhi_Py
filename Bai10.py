def is_valid_sin(sin_str):
    sin_str = sin_str.replace(" ", "").replace("-", "")
    
    if len(sin_str) != 9 or not sin_str.isdigit():
        return False
        
    check_digit = int(sin_str[-1])
    
    remaining_digits = sin_str[:-1] 
    
    s1 = 0  
    s2 = 0  
    
    for index, char in enumerate(remaining_digits, start=1):
        digit = int(char)
        
        if index % 2 != 0:
            s1 += digit
        else:
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


#dữ liệu test
#Hợp lệ
# 130 692 544
# 704 690 918

#Không hợp lệ
# 19345678
# 193 456 788
# 123 456 789
# 000 000 001