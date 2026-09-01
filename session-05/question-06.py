'''برنامه ایی بنویسید که یک متن دریافت نمایید .
اگر متن شامل هرکدام از کلمات زیر بود:
["hack", "fraud", "scam", "password", "atack"]
آن کلمه را پیدا و تعداد مقدار آن را نمایش دهید.
'''
 
#input

x = input('enter your sentence : ')

#list and null counter
texts = ['hack', 'fraud', 'scam', 'password', 'atack']
y = x.lower().split()
counter = 0
twords = []

#functions
for i in y:
    if i in texts:
        counter = counter + 1
        twords.append(i)

#conditional statements
if counter > 0:
    print(f'moshtaak ha : {twords}')
    print(f'tedad tekrar: {counter}')
else:
    print('No matching words found')