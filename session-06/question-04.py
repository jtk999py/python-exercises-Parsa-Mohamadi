'''اطلاعات کارمندان'''
''' بر نامه ای بنویسید که کارمندی که بیشترین حقوق را دارد پیدا کند.
میانگین حقوق را محاسبه کند.
کارمندان با حقوق بیشتر از 3000 را نمایش دهد.
نام کارمندی که کمترین حقوق را دارد نمایش دهد.'''

karmands = {'E01': {'name': 'Ali', 'age': 28, 'salary': 3000}, 'E02': {'name': 'Sara', 'age': 32, 'salary': 4500}, 'E03': {'name': 'Reza', 'age': 25, 'salary': 2800}}

max_salary = 0
max_employ = ''
total_salary = 0
count = 0
min_salary = 10000000000000000000000000000000000
min_employ = ''

for i in karmands:
    s = karmands[i]['salary']
    if s > max_salary:
        max_salary = s
        max_employ = karmands[i]['name']
    total_salary = total_salary + s
    count = count + 1
    if s > 3000:
       r =  karmands[i]['name']
    if s < min_salary:
        min_salary = s
        min_employ = karmands[i]['name']

average = total_salary // count

print('daray bishtarin foroosh :',max_employ,':',max_salary,'$')
print('average of salaryes : ',average,'$')
print('karmandan ba hoghoogh bishtar az 3000 :',r)
print('daray kamtarin hoghoogh : ',min_employ,':',min_salary,'$')
        