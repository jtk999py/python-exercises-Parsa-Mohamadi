'''شمارش حروف با دیکشنری'''

s = input ('enter string : ')

n_dic = {}

for i in s:
    if i in n_dic:
        n_dic[i] = n_dic[i]+1
    else:
        n_dic[i] = 1
        
print(n_dic)
        
