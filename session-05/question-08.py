'''برنامه ایی بنویسید که یک متن از کاربر دریافت نماید و گزارش زیر را تولید کنید:
    
Total characters:تعداد کل کارکتر ها
Total words:تعداد کل کلمات
Total leters:تعداد کل حروف
Total digits:تعداد کل اعداد
Total spaces:تعداد فاصله ها
Total upperasce:تعداد حروف بزرگ
Total lowercase:تعداد حروف کوچک
Longest word:بزرگترین کلمه جمله
Shortest word:کوتاه ترین کلمه جمله
Most repeated character:پر تگرار ترین کارکتر
Most repeated word:پر تکرار ترین کلمه'''

#input

x = input('enter sentence : ')

#counters

nums = 0                   #numbers
alfs = 0                   #alphabet
spc = 0                    #spaces
ups = 0                    #upper words
lows = 0                   #lower words
lword = x.split()[0]       #longest word
shword = x.split()[0]      #shortest word
mrc = 0                    #most reapeted character
mrw = 0                    #most reapeted word
mrw2  = ''
mrc2 = ''
#functions

totalcharac = len(x)
totalwords = len(x.split())

for i in x:           #for statements part 1
    if i.isalpha():
        alfs += 1
    if i.isdigit():
        nums += 1
    if i.isspace():
        spc += 1
    if i.islower():
        lows += 1
    if i.isupper():
        ups += 1
    if x.count(i)>mrc:
        mrc = x.count(i)
        mrc2 = i
        
for i in x.split():   #for statements part 2
    if len(i)>len(lword):
        lword = i
    if len(i)<len(shword):
        shword = i
    if x.split().count(i)>mrw:
        mrw = x.split().count(i)
        mrw2 = i
        
#output

print('**------------------**')
print(f'total characters -->{totalcharac}')
print(f'total words -->{totalwords}')        
print(f'total letters -->{alfs}')
print(f'total digits -->{nums}')    
print(f'total spaces -->{spc}')
print(f'total upercases -->{ups}')
print(f'total lowecases -->{lows}')
print(f'longest word -->{lword}')
print(f'shortest word -->{shword}')
print(f'most repeated character -->{mrc2}')
print(f'most repeated word -->{mrw2}')
print('**------------------**')

#end