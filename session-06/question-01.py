'''products = {“laptop”: 1200,“phone”: 800,“tablet”: 500,“headphone”: 150,“mouse”: 50}
برنامه‌ای بنویسید که:
گران‌ترین محصول را پیدا کند.
ارزان‌ترین محصول را پیدا کند.
میانگین قیمت محصولات را حساب کند.
محصولاتی که قیمتشان بیشتر از 500 است را نمایش دهد.
مجموع قیمت تمام محصولات را حساب کند.'''

products = {'laptop':1200 ,'phone':800 ,'tablet':500 ,'headphones':150 ,'mouse':50}

max_price = 0
max_product = ''
min_price = products['laptop']
min_product = 'laptop' 
total = 0
more_500 = []

for i in products:
    if products[i] > max_price:
        max_price = products[i]
        max_product = i
        
    if products[i]<min_price:
        min_price = products[i]
        min_product = i
        
for i in products:
    total += products[i]
    
l = len(products)
average = total / l

for i in products:
    if products[i]>500:
        more_500.append(i)
        
print('the most expensive product is:',max_product,':',max_price,'$')
print('the cheapest product is:',min_product,min_price,'$')
print('the averege of products price is:',average,'$')
print('the products that worth more than 500$ :',more_500)

        
    