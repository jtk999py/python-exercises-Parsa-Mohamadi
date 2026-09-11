'''تحلیل اطلاعات فروش'''
'''طلاعات فروش به شکل Tuple ذخیره شده است:
sales = ((“Ali”, “Laptop”, 1200),(“Sara”, “Phone”, 800),(“Ali”, “Phone”, 800),(“Reza”, “Laptop”, 1200),(“Sara”, “Laptop”, 1200),(“Ali”, “Mouse”, 50))
هر Tuple شامل موارد زیر است:
(customer, product, price)
برنامه‌ای بنویسید که مشخص کند:
هر مشتری چقدر خرید کرده است.
کدام مشتری بیشترین خرید را داشته است.
هر محصول چند بار فروخته شده است.
مجموع درآمد فروشگاه چقدر است.'''

sales = (('Ali', 'Laptop', 1200),('Sara', 'Phone', 800),('Ali', 'Phone', 800),('Reza', 'Laptop', 1200),('Sara', 'Laptop', 1200),('Ali', 'Mouse', 50))

customers = []
totals = []

for i in sales:
    name = i[0]
    price = i[2]
    if name in customers:
        index = customers.index(name)
        totals[index] += price
    else:
        customers.append(name)
        totals.append(price)

print('Customer purchases:')

for i in range(len(customers)):
    print(customers[i], totals[i])


max_total = max(totals)
index = totals.index(max_total)

print('Customer with the highest purchase:', customers[index])
print('Highest purchase:', max_total)


products = []
product_counts = []

for i in sales:
    product = i[1]

    if product in products:
        index = products.index(product)
        product_counts[index] += 1

    else:
        products.append(product)
        product_counts.append(1)

print('Product sales:')

for i in range(len(products)):
    print(products[i], product_counts[i])


total_income = 0

for i in sales:
    total_income += i[2]

print('Total store income:', total_income)