def get_values():
    values = []
    count = int(input('How many quantities do you want to enter?'))
    for i in range(count):
        value = input('enter the value :')
        values.append(value)
    return values
def add_unique(value, position, unique_values, positions):
    if value == '':
        return 'empty'
    for i in range(len(unique_values)):
        if value.lower() == unique_values[i].lower():
            return positions[i]
    unique_values.append(value)
    positions.append(position)
    return "added"
def process_values(values):
    unique_values = []
    positions = []
    duplicate_count = 0
    for i in range(len(values)):
        value = values[i]
        result=add_unique(value,i+1,unique_values,positions)
        if result == 'empty':
            print('error --> value is empty !')
        elif result == 'added':
            print('value added : ',value)
        else:
            duplicate_count += 1
            print('A duplicate value has been entered first time in :',result)
    return unique_values, positions, duplicate_count
def show_report(unique_values, positions, duplicate_count):
    print('<-----REPORT----->')
    print('special values :', unique_values)
    print('duplicate values :', duplicate_count)
    print('number of special values :', len(unique_values))
    print('Initial entry position')
    for i in range(len(unique_values)):
        print(unique_values[i],'-->',positions[i])
values = get_values()
unique_values,positions,duplicate_count = process_values(values)
show_report(unique_values, positions, duplicate_count)