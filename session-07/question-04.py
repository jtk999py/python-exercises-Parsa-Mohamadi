'''تشخیص تراکنش‌های مشکوک
تابعی به نام detect_fraud(transactions) بنویسید.
تراکنش‌ها:
transactions = [("Ali", "deposit", 50000000, 10),("Ali", "withdraw", 2000000, 11),("Ali", "withdraw", 3000000, 12),("Ali", "withdraw", 4000000, 13),("Ali", "withdraw", 5000000, 14),("Ali", "withdraw", 6000000, 15),("Sara", "deposit", 50000000, 20),("Sara", "withdraw", 60000000, 21),("Reza", "deposit", 150000000, 30)]
ساختار هر تراکنش:
(username, type, amount, time)
یک تراکنش مشکوک است اگر:
مبلغ بیشتر از 100 میلیون باشد.
بیش از ۳ برداشت پشت سر هم انجام شده باشد.
مبلغ برداشت بیشتر از موجودی باشد.
تابع باید تراکنش‌های مشکوک را برگرداند.
چالش بسیار مهم:
تابع detect_fraud() نباید خودش همه کارها را انجام دهد.
آن را به چند تابع کوچک‌تر تقسیم کنید:
check_large_transaction()
check_repeated_withdrawals()
check_balance()
generate_fraud_report()
در نهایت گزارشی از تراکنش‌ها را در تابع آخر برگردانید.'''































