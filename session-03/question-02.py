'''برنامه ای که 10 بار نقش سامانه ی ثبت رکورد های پرش از ارتفاع یک ورزشکار را ثبت میکند.'''
m=0
for i in range(10):
    h=int(input('enter height of jump per cm :'))
    if i==0:
        m=i
        print('new record till yet',m)
    else:
        if h>m:
            m=h
            print('new record till yet',m)
        else:
            print('recorded in past')