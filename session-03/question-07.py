#برنامه ای که سه رنگ دریافت کمرده و اگر یکسان باشتد تعداد رنگ های یکسان را چاپ می نماید.
rang1=str(input('رنگ اول را وارد کنید : '))
rang2=str(input('رنگ دوم را وارد کنید : '))
rang3=str(input('رنگ سوم را وارد کنید : '))
if rang1==rang2 and rang2==rang3:
    print('سه رنگ یکسان هستند')
elif rang1==rang2 or rang1==rang3 or rang2==rang3:
    print('دو رنگ یکسان هستند')
else:
    print('هیچ رنگی یکسان نیست')