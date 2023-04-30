#导入所需的模块
import time
import datetime
import pytz
#定义一个函数来显示本地时间
def show_local_time():
    local_time = time.localtime()
    time_string = time.strftime("%H:%M:%S", local_time)
    print("Local time:", time_string)
#显示不同时区的时间
def show_timezone_time(timezone):
    tz = pytz.timezone(timezone)
    tz_time = datetime.datetime.now(tz)
    time_string = tz_time.strftime("%H:%M:%S")
    print(timezone, "time:", time_string)
#显示一个菜单
def main():
    while True:
print("\nChoose an option:")
print("1. Show local time")
print("2. Show time in a different timezone")
print("3. Start stopwatch")
print("4. Exit")

choice = input("> ")

if choice == "1":
    show_local_time()
elif choice == "2":
    timezone = input("Enter timezone (e.g. America/New_York): ")
    show_timezone_time(timezone)
elif choice == "3":
    start_time = time.time()
    input("Press Enter to stop")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Elapsed time:", elapsed_time, "seconds")
elif choice == "4":
    break
else:
    print("Invalid choice. Please try again.")
