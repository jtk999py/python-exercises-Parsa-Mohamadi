'''برنامه ایی بنویسید که یک جمله دریافت نمایید و مشخص کن ید کدام کلمه بیشترین تعداد تکرار را دارد'''
#input

x = input ('enter your sentence : ')

#functions

wordlist = x.split()

#null lists

ws = []
wt = []

#for statements

for word in wordlist:
    if word in ws:
        iin = ws.index(word)
        wt[iin] = wt[iin]+1
    else:
        ws.append(word)
        wt.append(1)
        
#most word that used

mc = max(wt)
mi = wt.index(mc)
mn = ws[mi]

#output

print('word-->',mn)
print('tekrar-->',mc)