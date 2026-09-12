'''گروه‌بندی سفارش‌ها
لیست زیر اطلاعات سفارش‌هاست:
orders = [(“Ali”, “Laptop”),(“Sara”, “Phone”),(“Ali”, “Phone”),(“Reza”, “Laptop”),(“Sara”, “Laptop”),(“Ali”, “Tablet”),(“Reza”, “Phone”)]
Dictionaryای ایجاد کنید که مشخص کند هر مشتری چه محصولاتی سفارش داده است.
خروجی:
{“Ali”: [“Laptop”, “Phone”, “Tablet”],
“Sara”: [“Phone”, “Laptop”],
“Reza”: [“Laptop”, “Phone”]}'''

orders = [('Ali', 'Laptop'),('Sara', 'Phone'),('Ali', 'Phone'),('Reza', 'Laptop'),('Sara', 'Laptop'),('Ali', 'Tablet'),('Reza', 'Phone')]


r = {}

for i , j in orders:
    if i not in r:
        r[i] = []
    r[i].append(j)
        
print('customers ---> products',r)