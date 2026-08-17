import random
print('سلام به بازی سنگ کاغذ قیچی خوش آمدید')
print('exitبرای خروج بنویسید')
while True: 
    x = str(input('سنگ یا کاغذ یا قیچی ؟'))
    if x == 'exit':
        print('خدا نگهدار')
        break
    elif x not in ['قیچی','کاغذ','سنگ','gheychi','kaghaz','sang']:
        print('نا معتبر لطفا درست وارد کنید')
    else:
        b = random.choice(['sang','kaghaz','gheychi'])
    print('computer:',b)
    if x == b:
        print('مساوی شدید')
    elif x == 'sang' or x == 'سنگ' and b == 'kaghaz' or b == 'کاغذ':
        print('شما باختید')
    elif x == 'sang' or x == 'سنگ' and b == 'gheychi' or b == 'قیچی':
        print('شما بردید')
    elif x == 'kaghaz' or x == 'کاغذ' and b == 'gheychi' or b == 'قیچی':
        print('شما باختید')
    elif x == 'gheychi' or x == 'قیچی' and b == 'sang' or b == 'سنگ':
        print('شما باختید')
    elif x == 'gheychi' or x == 'قیچی' and b == 'kaghaz' or b == 'کاغذ':
        print('شما بردید')