year = 400
is_leap_year = True if year % 4 == 0 and year % 100 != 0 or year % 100 == 0 else False
if is_leap_year:
    print("Year", year, "is a leap year.")
else:
    print("Year", year, "is not a leap year.")