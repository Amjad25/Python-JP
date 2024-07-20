# Write a Python program that uses the date module to print the current date in the format "YYYY-MM-DD".

from datetime import date,timedelta,datetime

today = date.today()
print(today)
print(today.strftime("%Y-%m-%d"))

# Create a program that takes a date in the format "MM/DD/YYYY" as string and converts it to "YYYY-MM-DD".

def convert_date(date_str):
    return date.strftime(date.fromisoformat(date_str), "%Y-%m-%d")

print(convert_date("2024-07-06"))

# Write a program that takes a birth year as input and calculates the age of a person.

def calculate_age(birth_year):
    return date.today().year - birth_year

print(calculate_age(1990))

# Create a program that calculates and prints the number of days remaining until a person's next birthday.
# take users birth date as input

def days_until_next_birthday(birth_date):
    today = date.today()
    next_birthday = date(today.year, birth_date.month, birth_date.day)
    if next_birthday < today:
        next_birthday = date(today.year + 1, birth_date.month, birth_date.day)
    return (next_birthday - today).days

print(days_until_next_birthday(date(1990, 7, 6)))

# Write a program that calculates and displays the number of days between two given dates.

def days_between_dates(date1, date2):
    return (date1 - date2).days

print(days_between_dates(date(2024, 7, 6), date(2024, 7, 1)))


# Create a program that takes a date as string and returns the corresponding day of the week (e.g., Monday, Tuesday, etc.).

def get_day_of_week(date_str):
    return date.fromisoformat(date_str).strftime("%A")

print(get_day_of_week("2024-07-06"))

# Create a program that takes a year and a month as input and prints the number of days in that month.
# without using calender module

def days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if year % 4 == 0:
            return 29
        else:
            return 28
        
print(days_in_month(2024, 2))

# Create a function that takes a starting date and a number of days as input, and then calculates and prints the date that is the specified number of days in the future.

def future_date(start_date, days):
    return start_date + timedelta(days)

print(future_date(date(2024, 7, 6), 5))

# Write a Python program that uses the datetime module to print the current date and time.


now = datetime.now()
print(now)
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# Create a function that takes a datetime in the format "MM/DD/YYYY HH:MM:SS" as string  formats it as "YYYY-MM-DD HH:MM:SS".

def format_datetime(datetime_str):
    return datetime.strptime(datetime_str, "%m/%d/%Y %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")

print(format_datetime("07/06/2024 20:02:20"))

# Write a program that calculates the time difference between two given datetime objects and displays it in hours, minutes, and seconds.

def difference_bw_two_datetime(datetime1:datetime, datetime2:datetime):
    difference_date :timedelta =datetime1.__sub__(datetime2)
    print("datetime1" ,datetime1)
    print("datetime2" ,datetime2)
    print("difference_date", difference_date)

difference_bw_two_datetime(datetime1=datetime(2024,7,19,15,0,0),datetime2=datetime.now())





