# Get the loan details
money_owed = float(input("How much money do you owe, in dollars?\n"))
apr = float(input("What is the annual percentage rate?\n"))
payment = float(input("What will your monthly payment be, in dollars?\n"))
months = int(input("How many months do you want to see results for?\n"))

# Divide the apr by 100 to make it a percent, then divide by 12 to make it monthly
monthly_rate = apr/100/12

for i in range(months):
    # Add in interest
    interest_paid = money_owed * monthly_rate
    money_owed += interest_paid

    # Make payment
    if money_owed >= payment:
        money_owed -= payment
    else:
        payment = money_owed
        money_owed = 0.0

    # Print the results after this month
    print("Paid", payment, "of which", interest_paid, "was interest.", end=' ')
    print("Now I owe ", money_owed, ".", sep='')
