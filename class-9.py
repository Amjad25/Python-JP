from datetime import date, datetime


# print the current date
today = date.today()
print(today)
print(today.day)
print(today.month)
print(today.year)


# print the current date and time
now = datetime.now()
print(now)
print(now.hour)
print(now.minute)
print(now.second)


dt = "2024-07-06"
dt = date.fromisoformat(dt)
print(dt,type(dt)) 



# class Task

"""
**Task:**
1. Write a function 'parse_ios_date(iso_str)' that takes a IOS date string and return a datetime object.


"""

def parse_ios_date(iso_str):
    return date.fromisoformat(iso_str)

print(parse_ios_date("2024-07-06"))


"""
Strign to datetime obj on specif format"""

date_str = "06-07-2024"
date_obj = datetime.strptime(date_str, "%d-%m-%Y")

print(date_obj)

# function take strigndate and format and return datetime obj

def convert_to_datetime(date_str, format):
    return datetime.strptime(date_str, format)

print(convert_to_datetime("06-07-2024 20:02:20", "%d-%m-%Y %H:%M:%S"))

def format_datetime(dt, format):
    return dt.strftime(format)

dt = datetime.now()
print(format_datetime(dt, "%d-%m-%Y %H:%M:%S %p"))

