def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:  
        return 29 if is_leap_year(year) else 28

def get_first_day_of_year(year):
    day = 1
    month = 1
    a = (14 - month) // 12
    y = year - a
    m = month + 12 * a - 2

    return (day + y + y // 4 - y // 100 + y // 400 + (31 * m) // 12) % 7


def print_calendar(year):
    current_first_day = get_first_day_of_year(year)

    for month in range(1, 13):
        print(f"Tháng {month}")
        print("  S  M  T  W  T  F  S") 

        print("   " * current_first_day, end="")

        days_in_month = get_days_in_month(month, year)
        day_of_week_counter = current_first_day

        for day in range(1, days_in_month + 1):
            print(f"{day:3d}", end="")
            day_of_week_counter += 1

            if day_of_week_counter % 7 == 0:
                print()

        current_first_day = (current_first_day + days_in_month) % 7

        if day_of_week_counter % 7 != 0:
            print()
            
        print()  

try:
    year = int(input("Nhập năm: "))
    if year > 1582:
        print_calendar(year)
    else:
        print("Vui lòng nhập năm lớn hơn 1582!")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ!")