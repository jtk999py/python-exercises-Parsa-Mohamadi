'''برنامه اي بنویسید که کاراکترهاي متوالی یکسان را فشرده کند .
مثال:
 وزودي : aaabbccccd
a3b2c4d1 : خروج'''
#input

x = input ('enter string : ')

#zarf haye shomarande

r = ''
c = 1

#for statements

for i in range(1,len(x)):
    if x[i] == x[i-1]:
        c = c + 1
    else:
        r = r + x[i-1] + str(c)
        c = 1

#output

print(f'*{r}*')        