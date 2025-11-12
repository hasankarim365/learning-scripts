import datetime

date = datetime.date(2025, 1 , 27)
now = datetime.date.today()
print(f"This is a date: {date}. \n  This is the date now: {now}")

time = datetime.time(9, 5, 0)
time_now = datetime.datetime.now()

print(time)
print(time_now)

now = now.strftime("%d/%m/%Y, %H:%M:%S")
