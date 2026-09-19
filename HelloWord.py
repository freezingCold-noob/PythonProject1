import json
from typing import TypedDict

class 记录(TypedDict):
    amount: float
    type: str

def show_menu() -> None:
    # TODO: 打印菜单，例如 print("1. 添加收入")
    print("记账程序--请输入对应数字进入对应功能")
    print("1. 添加收入")
    print("2. 添加支出")
    print("3. 查看记录")
    print("4. 计算余额")
    print("0. 退出")

def add_income(records: list[记录]) -> None:
    while True:
        amount_str = input("请输入收入金额：")
        try:
            amount = float(amount_str)
            if amount <= 0:
                print("金额必须大于 0，请重新输入！")
                continue
            break
        except ValueError:
            print("金额必须是数字，请重新输入！")
    records.append({"amount": amount, "type": "income"})
    print(f"已存入{amount}元")

def add_expense(records: list[记录]) -> None:
    while True:
        amount_str = input("请输入支出金额：")
        try:
            amount = float(amount_str)
            if amount <= 0:
                print("金额必须大于 0，请重新输入！")
                continue
            break
        except ValueError:
            print("金额必须是数字，请重新输入！")
    records.append({"amount": amount, "type": "expense"})
    print(f"已支出{amount}元")


def show_records(records: list[记录]) -> None:
    print("===== 所有记账记录 =====")
    for item in records:
        print(f"类型：{item['type']},金额：{item['amount']}元")
def calculate_balance(records: list[记录]) -> tuple[float,float,float]:
    total_income = 0.0
    total_expense = 0.0
    for item in records:
        if item["type"] == "income":
            total_income += item["amount"]
        else:
            total_expense += item["amount"]
    balance = total_income - total_expense
    return total_income,total_expense,balance

def show_balance(records: list[记录]) -> None:
    total_income, total_expense, balance = calculate_balance(records)
    print(f"总收入：{total_income:.2f} 元,总支出：{total_expense:.2f} 元,当前余额：{balance:.2f} 元")

def save_records(records: list[记录]) -> None:
    # 把列表字典存入json文件
    with open("records.json", "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
    print("✅ 记录已保存到 records.json")

def load_records() -> list[记录]:
    try:
        with open("records.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("警告：records.json 内容损坏")
        return []

def main() -> None:
    records = load_records()
    while True:
        show_menu()
        choice = input("请选择功能：")
        if choice == "0":
            save_records(records)
            print("已退出")
            break
        elif choice == "1":
            add_income(records)
        elif choice == "2":
            add_expense(records)
        elif choice == "3":
            show_records(records)
        elif choice == "4":
            show_balance(records)
        else:
            print("无效选项，请重新输入")

if __name__ == "__main__":
    main()
