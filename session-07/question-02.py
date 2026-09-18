'''تحلیل سفارش
تابعی به نام process_order(customer, *products, **options) بنویسید.
مثال:
process_order("Ali","Laptop","Mouse","Keyboard",discount=10,tax=9,shipping=200000)
تابعی بنویسید که سفارش را تحلیل کند.
خروجی:
{"customer": "Ali","products": [...],"discount": 10,"tax": 9,"shipping": 200000,"final_price": ...}
چالش:
اگر discount یا tax ارسال نشد، مقدار پیش‌فرض داشته 
باشد.'''

def procces_order(customer,*products,**options):
    discount = options.get('discount',0)
    tax = options.get('tax',9)
    shiping = options.get('shipping',0)
    price = 1000000
    discount_amount = price*discount/100
    price_after_discount = price - discount_amount
    tax_amount = price_after_discount * tax / 100
    final_price=price_after_discount+tax_amount+shiping
    dict_result ={'customer':customer,'products':list(products),'discount':discount,'tax':tax,'shipping':shiping,'final price':final_price}
    return dict_result


print(procces_order('ali','laptop','iphone 13','airpod',discount = 10 , tax = 20 , shipping = 0))