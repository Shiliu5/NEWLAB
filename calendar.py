import calendar

# 输入年份和月份
year = int(input("请输入年份："))
month = int(input("请输入月份："))

# 创建日历对象
cal = calendar.monthcalendar(year, month)

# 打印日历标题
print(calendar.month_name[month], year)
print("一  二  三  四  五  六  日")

# 打印日历内容
for week in cal:
    for day in week:
        if day == 0:
            print("   ", end=" ")
        else:
            print(f"{day:2d}", end=" ")
    print()
