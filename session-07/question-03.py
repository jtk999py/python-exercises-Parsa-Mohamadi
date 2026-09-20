'''تحلیل تراکنش‌های مالی
داده‌های زیر را در نظر بگیرید:
transactions = [("Ali", "deposit", 5000000),("Ali", "withdraw", 1000000),("Sara", "deposit", 8000000),("Ali", "withdraw", 500000),("Sara", "withdraw", 2000000),("Reza", "deposit", 10000000)]
تابع زیر را بنویسید:
analyze_transactions(transactions)
باید برای هر کاربر مشخص کند:
Total Deposits
Total Withdrawals
Balance Change
Number of Transactions
{"Ali": {"deposits": 5000000,"withdrawals": 1500000,"balance_change": 3500000,"transactions": 3}}
سپس موارد زیر را حساب نمایید:
بیشترین واریز
بیشترین برداشت
فعال‌ترین کاربر
'''
def analyze_transactions(transactions):
    result = {}

    for transaction in transactions:
        user_name, transaction_type, amount = transaction

        if user_name not in result:
            result[user_name] = {
                'deposits': 0,
                'withdrawals': 0,
                'balance_change': 0,
                'transactions': 0
            }

        if transaction_type == 'deposit':
            result[user_name]['deposits'] += amount
            result[user_name]['balance_change'] += amount

        elif transaction_type == 'withdraw':
            result[user_name]['withdrawals'] += amount
            result[user_name]['balance_change'] -= amount

        result[user_name]['transactions'] += 1

    highest_deposit = 0
    highest_withdrawal = 0
    most_active = 0

    highest_deposit_user = ""
    highest_withdrawal_user = ""
    most_active_user = ""

    for user in result:
        if result[user]["deposits"] > highest_deposit:
            highest_deposit = result[user]["deposits"]
            highest_deposit_user = user

        if result[user]["withdrawals"] > highest_withdrawal:
            highest_withdrawal = result[user]["withdrawals"]
            highest_withdrawal_user = user

        if result[user]["transactions"] > most_active:
            most_active = result[user]["transactions"]
            most_active_user = user
        
        return result,highest_deposit_user,highest_withdrawal_user,most_active_user
    
    

print(analyze_transactions(transactions=[("Ali", "deposit", 5000000),("Ali", "withdraw", 1000000),("Sara", "deposit", 8000000),("Ali", "withdraw", 500000),("Sara", "withdraw", 2000000),("Reza", "deposit", 10000000)]))
        
        
        
        
        
        
        