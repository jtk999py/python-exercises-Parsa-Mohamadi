''' برنامه اي بنویسید که یک رمز عبور از کاربر دریافت کند و موارد زیر را بررسی نماید:
• حداقل 8 کاراکتر باشد .
• حداقل یک حرف بزرگ داشته باشد .
• حداقل یک حرف کوچک داشته باشد .
• حداقل یک عدد داشته باشد .
• حداقل یک کاراکتر خاص مثل % $ # @داشته باشد .
• اگر رمز معتبر نبود، دلیل یا دلایل نامعتبر بودن را نمایش دهد.
'''
#input


Pass = input('enter new password : ')


#zarf shomarande ha


l = len(Pass)
up = 0
list1 = 0
low = 0
num = 0
ch = ['!','#','$','&','*','@','%']


#for statements


for i in Pass:
    if i.isupper():
        up = 1
    if i.islower():
        low = 1
    if i.isdigit():
        num = 1
    if i in ch:
        list1 = 1
        
        
#conditional statements 1


if l<8:
    print('password must contain 8 characters !')
elif up < 1:
    print('password must have at least one uppercase letter')
elif low < 1:
    print('password must have at least one lowercase letter')
elif num < 1:
    print('password must have at least one number')
elif list1 < 1:
    print('password must have at least one special character (! # $ & * @ %)')
else:
    print('your password is valid')