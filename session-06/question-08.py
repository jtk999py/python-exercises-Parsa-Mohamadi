'''گروه‌بندی کاربران بر اساس زبان برنامه‌نویسی
اطلاعات کاربران:
users = [(“Ali”, 25, “Python”),(“Sara”, 30, “Java”),(“Reza”, 22, “Python”),(“Mina”, 28, “C++”),(“John”, 35, “Python”),(“David”, 30, “Java”)]
برنامه‌ای بنویسید که:
کاربران را بر اساس زبان برنامه‌نویسی گروه‌بندی کند.
خروجی گروه‌بندی:
{“Python”: [“Ali”, “Reza”, “John”],
“Java”: [“Sara”, “David”],
“C++”: [“Mina”] }
میانگین سن کاربران هر زبان را حساب کند.
مسن‌ترین کاربر هر زبان را پیدا کند.
زبان دارای بیشترین کاربر را پیدا کند.
تمام زبان‌های برنامه‌نویسی موجود را استخراج کند.'''


users = [('Ali', 25, 'Python'),('Sara', 30, 'Java'),('Reza', 22, 'Python'),('Mina', 28, 'C++'),('John', 35, 'Python'),('David', 30, 'Java')]

group = {}
ages = {}
average_ages = {}
olds = {}
lan_use = ''

for name,age,lan in users:
    if lan not in group:
        group[lan]=[]
    group[lan].append(name)
    if lan not in olds or age > olds[lan][1]:
       olds[lan] = (name, age)
    
for name,age,lan in users:
    if lan not in ages:
        ages[lan] = []
    ages[lan].append(age)
        
for lan in ages:
    average = sum(ages[lan])/len(ages[lan])
    average_ages[lan] = average

for lan in group:
    most_used = ''

for lan in group:
    if lan_use == '' or len(group[lan]) > len(group[lan_use]):
        lan_use = lan

languages = list(group.keys())

print('groups --->',group)
print('average of ages --->',average_ages)
print('most language that used --->',lan_use)
print('languages that used--->',languages)

        
    

