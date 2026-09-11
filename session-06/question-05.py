'''اطلاعات دانش آموزان'''
'''برنامه‌ای بنویسید که برای هر دانش‌آموز:

میانگین را محاسبه کند.
وضعیت قبولی را مشخص کند.
بالاترین نمره او را پیدا کند.
قانون:
Average >= 15 → Passed
Average < 15 → Failed'''


std = {'Ali': [18, 17, 20],'Sara': [15, 19, 18],'Reza':[12, 14, 10],'Mina':[20, 20, 19] }

high_avg = 0
best_std = ''

for i in std:
    
    scores = std[i]
    
    average = sum(scores) / len(scores)
    
    high = 0
    if average > high_avg:
       high_avg = average
       best_std = i
    
    print('student',i)
    
    if average >= 15:
        print('status : passed')
        
    else:
        print('status : failed')
        
    for score in scores:
        
        if score > high:
            high = score
        print('average of numbers :',average)
        print('the highest number is :',high)
        print('<--------------->')
        
print(f'{best_std} is the best student')
print(f'{high_avg} is the highest average')

