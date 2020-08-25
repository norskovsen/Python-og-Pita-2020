def calculate_loan(amount, interest_rate, monthly_payment):
    left = amount
    months = 0
    while left > 0:
        if (left * interest_rate) >= monthly_payment:
            return None, None
        left += left * interest_rate
        left -= monthly_payment
        months += 1
    return months, left

print(calculate_loan(2000, 0.01, 200))   # Output: (11, -82.03...)
print(calculate_loan(100, 0.02, 200))    # Output: (1, -98.0)
print(calculate_loan(10000, 0.10, 2000)) # Output: (8, -1435.88...)




