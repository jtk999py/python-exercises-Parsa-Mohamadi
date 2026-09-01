'''برنامه ایی بنویسید که یک جمله دریافت کنید و طولانیترین کلمه را پیدا نمایید. اگر چند کلمه طول یکسان داشتند،
اولین کلمه را نمایش بده.'''

#input

x = input ('enter your sentence : ')

#functions

long = ''
r = x.split()
for i in r:
    if len(i)>len(long):
        long=i
  
#output      
  
print(f'the longest word is *{long}* .')
