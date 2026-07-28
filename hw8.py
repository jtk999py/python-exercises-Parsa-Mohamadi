#برنامه ای که از کاربر ساعت دریافت میکند و زمان روز را چاپ میکند
import time
hour=int(input('ساعت را انتخاب کنید بین 0 تا 23 :'))
if hour < 0 and hour>23:
    print('ساعت باید بین بازه زمانی تعیین شده باشد')
else:
    if 0 <= hour <= 5:
        print('early morning')
    elif 6 <= hour <= 12:
        print('morning')
    elif 13 <= hour <= 16:
        print('midday')
    elif 17 <= hour <= 21:
        print('evening')
    elif 22 <= hour <= 23:
        print('night')
