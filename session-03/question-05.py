import math
num=int(input('enter first number :'))
num2=int(input('enter second number :'))
func=str(input('enter your function :'))
functions=['*','/','-','+']
if func=='*':
    j=num*num2
    print('multiply is :',j)
elif func=='/':
    t=num/num2
    print('division is :',t)
elif func=='-':
    sub=num-num2
    print('subtract is :',sub)
elif func=='+':
    jam=num+num2
    print('the plus is :',jam)
    
