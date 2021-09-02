import datetime

if 1<2:
    print("1 is smaller than 2")

day = datetime.datetime.now()

now = "{}년 {}월 {}일 {}시 {}분 {}초".format(day.year, day.month, day.day, day.hour, day.minute, day.second)
print(now)

if day.hour<12:
    print("현재 오전입니다(AM)")

if day.hour>=12:
    print("현재 오후입니다(PM)")