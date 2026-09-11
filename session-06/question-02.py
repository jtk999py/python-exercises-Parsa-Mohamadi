'''برنامه‌ای بنویسید که محصولات زیر را را به دو دسته زیر تقسیم کند:
inventory = {'apple':20 , 'banana':5 , 'orange':0 , 'milk':12 , 'bread':0}
Available: apple , banana , milk 
Out of stock: orange , bread
سپس تعداد محصولات موجود و ناموجود را نیز نمایش دهید.'''


iv={'apple':20,'banana':5,'orange':0,'milk':12,'bread':0}

avail = []
unavails = []

for i in iv:
    if iv[i]>0:
        avail.append(i)
    if iv[i]==0:
        unavails.append(i)
        
for i in avail:
    print(i,':',iv[i],end=' ')
    
print('available products:', avail)
print('available products:', len(avail))
print('unavailable products:', len(unavails))


        