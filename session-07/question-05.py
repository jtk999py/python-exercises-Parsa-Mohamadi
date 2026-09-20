'''تحلیل لاگ‌های سیستم
داده‌ها به صورت زیر داریم:
logs = [("Ali", "LOGIN", 200),("Ali", "DOWNLOAD", 200),("Sara", "LOGIN", 403),("Reza", "LOGIN", 200),("Sara", "LOGIN", 403),("Sara", "LOGIN", 403),]
سیستمی بسازید که:
تعداد Login موفق را پیدا کند.
تعداد Login ناموفق را پیدا کند.
اگر یک کاربر حداقل ۳ خطای 403 داشت، او را مشکوک اعلام کند
تعداد عملیات هر کاربر را محاسبه کند.
گزارش نهایی تولید کند.
'''


def log_analyz(logs):
    log_counter_succesful = 0
    log_counter_unsuccesful = 0
    eror_403 = {}
    suspicious_person = []
    total_count = {}
    for i in logs:
        if i[1] == 'LOGIN' and i[2] == 200:
            log_counter_succesful +=1
        if i[1] == 'LOGIN' and i[2] == 403:
            log_counter_unsuccesful +=1
    for name,func,status in logs:
        if func == 'LOGIN' and status == 403:
            if name not in eror_403:
                eror_403[name] = 1
            else:
                eror_403[name] += 1
    for name,count in eror_403.items():
        if count >= 3:
            suspicious_person.append(name)

    for name,func,status in logs:
        if name not in total_count:
            total_count[name] =1
        else:
            total_count[name] +=1
    result = {'succsesfull logins':log_counter_succesful , 'unsuccsesful logins ':log_counter_unsuccesful, 'suspicious person ': suspicious_person , 'total count for each person ': total_count}
    return result

print(log_analyz([("Ali", "LOGIN", 200),("Ali", "DOWNLOAD", 200),("Sara", "LOGIN", 403),("Reza", "LOGIN", 200),("Sara", "LOGIN", 403),("Sara", "LOGIN", 403),]))
 