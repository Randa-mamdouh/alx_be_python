monthly_income=int(input("Enter your monthly income:"))
expenses=int(input("Enter your total monthly expenses: "))
monthly_saving=monthly_income-expenses
rate=0.05
Projected_Savings = saving * 12 + (monthly_saving * 12 * rate)
print("Your monthly savings are ",str(monthly_saving))

print("Projected savings after one year, with interest, is: ",str(Projected_Savings))