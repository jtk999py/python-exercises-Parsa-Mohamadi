#برنامه ای بنویسید که 10 عدد از کاربر بگیرید و میانگین آن را حساب کند.
sum = 0
for i in range(10):
    num = float(input("Enter number " + str(i+1) + ": "))
    sum = sum + num
average = sum / 10
print("Average:", average)