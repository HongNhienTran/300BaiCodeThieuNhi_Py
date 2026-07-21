def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def is_valid_date(day, month, year):
    if year < 1582 or month < 1 or month > 12 or day < 1:
        return False
    
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31
    elif month in [4, 6, 9, 11]:
        max_days = 30
    else:  
        max_days = 29 if is_leap_year(year) else 28

    return day <= max_days

def calculate_day_of_week(day, month, year):
    a = (14 - month) // 12
    y = year - a
    m = month + 12 * a - 2
    
    day_index = (day + y + y // 4 - y // 100 + y // 400 + (31 * m) // 12) % 7
    
    days_map = {
        0: "Chủ nhật",
        1: "Thứ 2",
        2: "Thứ 3",
        3: "Thứ 4",
        4: "Thứ 5",
        5: "Thứ 6",
        6: "Thứ 7"
    }
    
    return days_map[day_index]

try:
    day, month, year = map(int, input("Nhập ngày, tháng và năm: ").split())

    if is_valid_date(day, month, year):
        print("Hợp lệ")
        day_str = calculate_day_of_week(day, month, year)
        print(day_str)
    else:
        print("Không hợp lệ")

except ValueError:
    print("Vui lòng nhập 3 số nguyên hợp lệ!")