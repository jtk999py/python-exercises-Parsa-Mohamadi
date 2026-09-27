def count_sucessful_logins():
    sucessful_login_counter = 0
    file = open('logs.txt','r')
    for line in file:
        data = line.strip().split(',')
        if data[1] == 'LOGIN' and data[2] == '200':
            sucessful_login_counter += 1
    file.close()   
    print('sucessful logins : ',sucessful_login_counter)
def count_failed_logins():
    failed_login_counter = 0
    file = open('logs.txt','r')
    for line in file:
        data = line.strip().split(',')
        if data[1] == 'LOGIN' and data[2] == '403' or data[2] == '500':
            failed_login_counter += 1
    file.close()
    print('failed logins :',failed_login_counter)   
def find_suspicious_users():
    error_403_counter = {}
    file = open ('logs.txt','r')
    for line in file:
        data = line.strip().split(',')
        if data[2] == '403':
            username = data[0]
            if username in error_403_counter:
                error_403_counter[username]+=1
            else:
                error_403_counter[username] = 1
    file.close()
    
    suspicious_users = []
    for username in error_403_counter:
        if error_403_counter[username] >= 3:
            suspicious_users.append(username)
    print('suspicious person is :',suspicious_users)
def generate_report():
    operations = {}
    file = open ('logs.txt','r')
    for line in file:
        data = line.strip().split()
        username = data[0]
        if username in operations:
            operations[username] += 1
        else:
            operations[username] = 1
    file.close()
    print('operations of each person :')
    for username in operations:
        print(username,':',operations[username])
#Farakhan tavabe :
count_sucessful_logins()
count_failed_logins()
find_suspicious_users()
generate_report()