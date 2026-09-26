from HelloWord import calculate_balance, load_records,add_income,add_expense,save_records
from fastapi import FastAPI

app = FastAPI()


# TODO: 下面这行的括号里，填「查看余额」的网址
@app.get("/balance")
def get_balance():
    total_income, total_expense, balance = calculate_balance(load_records())
    return {"balance": balance,"total_income":total_income,"total_expense":total_expense}

@app.post("/add_income")
def add_income_api(amount: float):
    records = load_records()
    add_income(records, amount)
    save_records(records)
    return {"ok": True}
