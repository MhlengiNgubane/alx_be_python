monthly_income = float(input("Enter your monthly income: $"))

monthly_expenses = float(input("Enter your total monthly expenses: $"))

monthly_savings = monthly_income - monthly_expenses

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are: ${monthly_savings}")

print(f"Projected annual savings after one year with 5% annual interest: ${projected_savings}")