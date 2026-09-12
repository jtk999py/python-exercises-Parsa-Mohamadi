'''تحلیل موجودی محصولات
ساختار هر محصول:
(Product Name, Price, Stock)
برنامه‌ای بنویسید که:
محصولات موجود را نمایش دهد.
محصولات ناموجود را نمایش دهد.
ارزش کل موجودی هر محصول را محاسبه کند.
Price × Stock
محصول دارای بیشترین ارزش موجودی را پیدا کند.
ارزش کل انبار را محاسبه کند.'''


products = {'P01': ('Laptop', 1200, 5),'P02': ('Phone', 800, 0),'P03': ('Tablet', 500, 12),'P04': ('Mouse', 50, 25),'P05': ('Keyboard', 100, 0)}

avails = []
noavails = []
most = 0
all_pd = 0

for i in products:
     if products[i][2] > 0:
         avails.append(products[i][0])
     else:
         noavails.append(products[i][0])   
     price = products[i][1]
     stock = products[i][2]
     tot_price = price*stock
     all_pd = all_pd + tot_price
     if tot_price > most:
        most = tot_price
        most_product = products[i][0]

print('Available products:', avails)
print('Unavailable products:', noavails)
print('Product with the highest inventory value:', most_product)
print('Highest inventory value:', most)
print('Total value:', all_pd)