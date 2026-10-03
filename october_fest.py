print("Hello, world!, today is 03 October")
import math
import datetime

what_is_today = datetime.datetime.today()
today_is= what_is_today.strftime("%Y-%m-%d")
print(what_is_today)
print(today_is)
what_time_is_it_now = datetime.datetime.now()
time_now_is= what_time_is_it_now.strftime("%H:%M:%S")
print(what_time_is_it_now)
print(time_now_is)

