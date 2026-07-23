def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_day_of_year(day, month, year):
    sum_days = int(30.42 * (month - 1)) + day

    if month == 2 or (is_leap_year(year) and month > 2):
        sum_days += 1

    if 2 < month < 8:
        sum_days -= 1

    return sum_days

try:
    day, month, year = map(int, input("Nhập ngày, tháng, năm: ").split())

    day_number = get_day_of_year(day, month, year)

    print(f"Ngày thứ: {day_number}")

except ValueError:
    print("Vui lòng nhập ngày, tháng, năm hợp lệ!")

from datetime import datetime
try:
    day, month, year = map(int, input("Nhập ngày, tháng, năm: ").split())
    current_date = datetime(year, month, day)

    day_number = int(current_date.strftime('%j'))

    print(f"Ngày thứ: {day_number}")
except ValueError:
    print("Vui lòng nhập ngày, tháng, năm hợp lệ!")