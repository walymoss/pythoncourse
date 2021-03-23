expenses = []
num_expenses = int(input("please enter num of expenses: \n"))
for i in range(0, num_expenses, 1):
    expenses.append(float(input("Enter expense: ")))
print("total expenses: ", sum(expenses), "")
