'''برنامه ای بنویسید که یک رشته دریافت کند و تمام کارکتر هایی که بیشتر از یکبار تکرار شده اند را حذف کند به طوری که فقط اولین مقدار باقی بماند'''
#input

x = input ('enter string : ')

#list

mainlist = []

#for statement

for i in x:
    if i not in mainlist:
        mainlist.append(i)
        
#end

end = ''.join(mainlist)

print(mainlist)