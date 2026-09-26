def add_user(username,password,status):
    file = open('users.txt','r')
    for line in file:
        data = line.strip().split(',')
        if data[0]== username:
            print('username allready exists !')
            file.close()
            return
    file.close()
    
    file = open('users.txt','a')
    file.write(username+','+password+','+status+'\n')
    file.close()
    print('username added succsesfully !')
def find_user(username):
    file = open('users.txt','r')
    for line in file:
        data = line.strip().split(',')
        if data[0] == username:
            print('username',data[0])
            print('password',data[1])
            print('status',data[2])
            file.close()
            return
    file.close()
    print('user not found !')
def delete_user(username):
    file = open ('users.txt','r')
    users = []
    for line in file:
        data = line.strip().split(',')
        if data[0] != username:
            users.append(line)
    file.close()
    file = open('users.txt', 'w')

    for user in users:
        file.write(user)

    file.close()

    print('User deleted')
def generate_report():
    file = open ('users.txt','r')
    actives = 0
    blocks = 0
    for line in file:
        data = line.strip().split(',')
        if data[2] == 'active':
            actives += 1
        elif data[2] == 'blocked':
            blocks += 1
    file.close()
    
    print('active users --> ',actives)
    print('blocked users --> ',blocks)
    
# test tavabe va farakhan anha:
    
add_user('parsa','game57039','active')
find_user('Sara')
delete_user('Reza')
generate_report()
