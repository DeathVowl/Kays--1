from datetime import datetime

def get_weekday(day, month, year):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[datetime(year, month, day).weekday()]

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_age(day, month, year):
    today = datetime.now()
    age = today.year - year
    if today.month < month or (today.month == month and today.day < day):
        age -= 1
    return age

def print_digital_date(day, month, year):
    digits = {
        '0': ['***', '* *', '* *', '* *', '***'],
        '1': ['  *', '  *', '  *', '  *', '  *'],
        '2': ['***', '  *', '***', '*  ', '***'],
        '3': ['***', '  *', '***', '  *', '***'],
        '4': ['* *', '* *', '***', '  *', '  *'],
        '5': ['***', '*  ', '***', '  *', '***'],
        '6': ['***', '*  ', '***', '* *', '***'],
        '7': ['***', '  *', '  *', '  *', '  *'],
        '8': ['***', '* *', '***', '* *', '***'],
        '9': ['***', '* *', '***', '  *', '***'],
        ' ': ['   ', '   ', '   ', '   ', '   ']
    }
    
    date_str = f"{day:02d} {month:02d} {year}"
    
    for i in range(5):
        line = ""
        for char in date_str:
            line += digits[char][i] + " "
        print(line)

day = int(input("Enter your day birth: "))
month = int(input("Enter your month birth: "))
year = int(input("Enter your year birth: "))

print("Weekday:", get_weekday(day, month, year))
print("Leap year:", "yes" if is_leap_year(year) else "no")
print("Age:", get_age(day, month, year))
print_digital_date(day, month, year)