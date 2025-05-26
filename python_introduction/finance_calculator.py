income=int(input("Enter your monthly income:"))
expenses=int(input("Enter your total monthly expenses: "))
saving=income-expenses
rate=0.05
Projected_Savings = saving * 12 + (saving * 12 * rate)
print("Your monthly savings are ",str(saving))
print("Projected savings after one year, with interest, is: ",str(Projected_Savings))