'''برنامه ایی بنویسید که رشته اي از کاربر بگیرید و تعداد موارد زیر را محاسبه نماید :
• حروف انگلیسی
• حروف بزرگ
• حروف کوچک
• اعداد
• فاصله
• کاراکترهاي خاص
'''
# input 

x = input ('enter string : ')

#zarf shomarande ha

alf = 0
up = 0
low = 0
nums = 0
spc = 0
ss = 0
ch = ['!','#','$','&','*','@','%']

#for statements

for i in x:
    if i.isalpha():
        alf = alf+1
    if i.isupper():
        up = up+1
    if i.islower():
        low = low+1
    if i.isdigit():
        nums = nums+1
    if i.isspace():
        spc = spc+1
    if i in ch:
        ss = ss+1
        
#prints

print(f'english words--> {alf} # upper words--> {up} # lower words--> {low} # numbers--> {nums} # spaces--> {spc} # characters--> {ss} ')