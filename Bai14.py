from datetime import datetime, timedelta

try:
    day, month, year = map(int, input("Nhập ngày, tháng, năm: ").split())

    current_date = datetime(year, month, day)

    next_date = current_date + timedelta(days=1)

    previous_date = current_date - timedelta(days=1)

    print(f"Ngày mai: {next_date.strftime('%d/%m/%Y')}")
    print(f"Hôm qua: {previous_date.strftime('%d/%m/%Y')}")

except ValueError:
    print("Vui lòng nhập ngày, tháng, năm hợp lệ!")

# dùng if else
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def get_days_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:  
        return 29 if is_leap_year(year) else 28

def get_next_day(day, month, year):
    max_days = get_days_in_month(month, year)
    if day < max_days:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    return day, month, year

def get_previous_day(day, month, year):
    if day > 1:
        day -= 1
    else:
        if month == 1:
            month = 12
            year -= 1
        else:
            month -= 1
        day = get_days_in_month(month, year)
    return day, month, year

try:
    d, m, y = map(int, input("Nhập ngày, tháng, năm: ").split())

    next_d, next_m, next_y = get_next_day(d, m, y)
    prev_d, prev_m, prev_y = get_previous_day(d, m, y)

    print(f"Ngày mai: {next_d:02d}/{next_m:02d}/{next_y}")
    print(f"Hôm qua: {prev_d:02d}/{prev_m:02d}/{prev_y}")

except ValueError:
    print("Vui lòng nhập ngày, tháng, năm hợp lệ!")