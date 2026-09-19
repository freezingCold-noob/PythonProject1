from HelloWord import calculate_balance


def test_balance():
    records = [
        {"amount": 200.0, "type": "income"},
        {"amount": 50.0, "type": "expense"},
    ]
    income, expense, balance = calculate_balance(records)
    assert balance == 150.0


# ============================================================
# 下面三个测试的框架已搭好，把每个 ______ 换成你算出来的期望值
# ============================================================


def test_empty_records():
    records = []
    income, expense, balance = calculate_balance(records)
    assert income == 0.0
    assert expense == 0.0
    assert balance == 0.0


def test_only_income():
    records = [
        {"amount": 100.0, "type": "income"},
    ]
    income, expense, balance = calculate_balance(records)
    assert income == 100.0
    assert expense == 0.0
    assert balance == 100.0


def test_negative_balance():
    records = [
        {"amount": 100.0, "type": "income"},
        {"amount": 250.0, "type": "expense"},
    ]
    income, expense, balance = calculate_balance(records)
    assert balance == -150.0
