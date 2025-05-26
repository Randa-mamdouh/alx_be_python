monthly_income=float(input("Enter your monthly income:"))
monthly_expenses=float(input("Enter your total monthly expenses: "))
monthly_savings=monthly_income-monthly_expenses
rate=0.05
Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * rate)
print("Your monthly savings are ",str(monthly_saving))

print("Projected savings after one year, with interest, is: ",str(Projected_Savings))