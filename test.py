class Record:
    def __init__(self, rtype, amount):
        self.rtype = rtype
        self.amount = amount

    def describe(self):
        return f"{self.rtype}：{self.amount}元"

    def is_income(self):
        return self.rtype == "收入"


records = [
    Record("收入", 100),
    Record("支出", 30),
    Record("收入", 50),
    Record("支出", 20),
]

total_income = 0
total_expense = 0

for r in records:
    if r.is_income():
        total_income += r.amount
    else:
        total_expense += r.amount

print(f"收入：{total_income}，支出：{total_expense}，余额：{total_income - total_expense}")
