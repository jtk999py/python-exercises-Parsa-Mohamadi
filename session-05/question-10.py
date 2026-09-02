'''برنامه ایی بنویسید که دو جمله از کاربر بگیرد و مشخص کند  چه کلماتی در هر دو جمله وجود دارند'''

#inputs

x = input ('enter first sentence : ')
y = input ('enter second sentence : ')

#lists

m = x.split()
n = y.split()
ze = []

#functions

for i in m:
    if i in n and i not in ze:
        ze.append(i)
        
        
#output

print(f'the simultaneous words are --> {ze}')
