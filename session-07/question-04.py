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

transactions = [
    ("Ali", "deposit", 50000000, 10),
    ("Ali", "withdraw", 2000000, 11),
    ("Ali", "withdraw", 3000000, 12),
    ("Ali", "withdraw", 4000000, 13),
    ("Ali", "withdraw", 5000000, 14),
    ("Ali", "withdraw", 6000000, 15),
    ("Sara", "deposit", 50000000, 20),
    ("Sara", "withdraw", 60000000, 21),
    ("Reza", "deposit", 150000000, 30)
]


def check_large_transaction(transaction):
    username, transaction_type, amount, time = transaction

    if amount > 100000000:
        return True

    return False


def check_repeated_withdrawals(transactions, index):
    username = transactions[index][0]

    if transactions[index][1] != "withdraw":
        return False

    count = 1
    i = index - 1

    while i >= 0 and transactions[i][0] == username and transactions[i][1] == "withdraw":
        count += 1
        i -= 1

    i = index + 1

    while i < len(transactions) and transactions[i][0] == username and transactions[i][1] == "withdraw":
        count += 1
        i += 1

    if count > 3:
        return True

    return False


def check_balance(transactions, index):
    username = transactions[index][0]
    balance = 0

    for i in range(index + 1):
        if transactions[i][0] == username:

            if transactions[i][1] == "deposit":
                balance += transactions[i][2]

            elif transactions[i][1] == "withdraw":
                balance -= transactions[i][2]

    if balance < 0:
        return True

    return False


def generate_fraud_report(transactions):
    report = []

    for i in range(len(transactions)):

        transaction = transactions[i]
        reasons = []

        if check_large_transaction(transaction):
            reasons.append("large transaction")

        if check_repeated_withdrawals(transactions, i):
            reasons.append("repeated withdrawals")

        if check_balance(transactions, i):
            reasons.append("insufficient balance")

        if len(reasons) > 0:
            report.append({
                "transaction": transaction,
                "reasons": reasons
            })

    return report


def detect_fraud(transactions):
    return generate_fraud_report(transactions)


result = detect_fraud(transactions)

for item in result:
    print(item)
