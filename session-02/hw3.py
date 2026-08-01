#برنامه ای که حرف اول نام و کل فامیلی رو جدا میکنه و چاپ میکنه
name=str(input('enter your name : '))
fm=str(input('enter your family name : '))
nameind=(name[0])
fmsl=(fm[0::])
print(f'{nameind}.{fmsl}')