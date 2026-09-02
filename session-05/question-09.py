'''برنامه ایی بنویسید و یک سیستم Login طراحی کنید که user و password از کاربر بگیرد . کاربر حداکثر 3 بار
فرصت ورود دارد .
اگر username یا password اشتباه بود پیام زیر را مطابق مثال زیر بدهد به همراه تعداد تلاش ناموفق
Wrong username or password
Atempts remaining: 2
اگر درست بود پیام زیر را بدهد
Login successful'''

# mafroozat

username = 'jtk999'           #username farzi
password = 'fanavari.co.THR'  #pass farzi

#shomarande ha

attemtscounter = 0

#functions and conditional statements

while attemtscounter < 3 :
    
    mainusername = input ('username ra vared konid : ')
    mainpassword = input ('password ra vared konid : ')
    
    if mainusername == username and password == mainpassword:
        
        print('login succsesful')
        print('wellcome !')
        break
    
    else:
        attemtscounter = attemtscounter + 1
        y = 3 - attemtscounter
        print(f'Wrong username or password  2')
        print(f'remaining attemts --> {y}')