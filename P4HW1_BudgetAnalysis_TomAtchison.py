# Input monthly budget. Use loop to enter expenses to keep running total.
# Display total amount budget is over or under.
# 26 October 2018
# CTI-110 P4HW1 - Budget Analysis
# Tom Atchison


# Input the budget amount.
budget = float(input("Enter the amount of this months budget: $"))
expense = "y"
totalexpense = 0
# Input expenses using while loop
while expense == "y":
    todaysexpense = float(input("Enter an expense: $"))
    totalexpense += todaysexpense
    expense = input("Do you have more expenses to add? Type y for yes or " \
                    "n for no: " )
# Output the budget and whether on, over or under.
if totalexpense > budget:
    print("You are over the budget of $",format(budget, ",.2f" ), \
          "by $", format(totalexpense - budget, ",.2f"))
elif budget > totalexpense:
    print("You are under the budget of $",format(budget, ",.2f" ), \
         "by $", format(budget - totalexpense, ",.2f"))
else:
    print("You are at your budget of $",format(budget, ",.2f" ))



