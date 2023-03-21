# Problem 1
# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

# The following variables contain values as described below:

# balance - the outstanding balance on the credit card

# annualInterestRate - annual interest rate as a decimal

# monthlyPaymentRate - minimum monthly payment rate as a decimal

# For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print

# Remaining balance: 813.41
# instead of

# Remaining balance: 813.4141998135 
# So your program only prints out one thing: the remaining balance at the end of the year in the format:

# Remaining balance: 4784.0
# A summary of the required math is found below:

# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

# We provide sample test cases below. We suggest you develop your code on your own machine, and make sure your code passes the sample test cases, before you paste it into the box below.

YEAR = 12
interest = 0
unpid_balance = balance
for i in range(13):
    balance = unpid_balance + interest
    min_payment = balance * monthlyPaymentRate
    unpid_balance = balance - min_payment
    interest = annualInterestRate/YEAR * unpid_balance
    # print("Month ",i, " Remaining balance: ",balance)
print("Remaining balance:",round(balance,2)) 


# Problem 2 - Paying Debt Off in a Year
# Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

# In this problem, we will not be dealing with a minimum monthly payment rate.

# The following variables contain values as described below:

# balance - the outstanding balance on the credit card

# annualInterestRate - annual interest rate as a decimal

# The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:

# Lowest Payment: 180 
# Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay. A summary of the required math is found below:

# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

# Paste your code into this box
YEAR = 12
monthly_inserest_rate = round(annualInterestRate / YEAR,4)
min_fix_monthly_payment = 10
previous_balance = balance
while previous_balance > 0:
    previous_balance = balance
    min_fix_monthly_payment = min_fix_monthly_payment + 10
    for i in range(12):
        monthly_unpid_balance = previous_balance - min_fix_monthly_payment
        previous_balance = monthly_unpid_balance + monthly_inserest_rate * monthly_unpid_balance
print("Lowest Payment:",min_fix_monthly_payment) 


# Problem 3 - Using Bisection Search to Make the Program Faster
# You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. Why did we make it that way? You can try running your code locally so that the payment can be any dollar and cent amount (in other words, the monthly payment is a multiple of $0.01). Does your code still work? It should, but you may notice that your code runs more slowly, especially in cases with very large balances and interest rates. (Note: when your code is running on our servers, there are limits on the amount of computing time each submission is allowed, so your observations from running this experiment on the grading system might be limited to an error message complaining about too much time taken.)

# Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without running into the problem of slow code? We can make this program run faster using a technique introduced in lecture - bisection search!

# The following variables contain values as described below:

# balance - the outstanding balance on the credit card

# annualInterestRate - annual interest rate as a decimal

# To recap the problem: we are searching for the smallest monthly payment such that we can pay off the entire balance within a year. What is a reasonable lower bound for this payment value? $0 is the obvious answer, but you can do better than that. If there was no interest, the debt can be paid off by monthly payments of one-twelfth of the original balance, so we must pay at least this much every month. One-twelfth of the original balance is a good lower bound.

# What is a good upper bound? Imagine that instead of paying monthly, we paid off the entire balance at the end of the year. What we ultimately pay must be greater than what we would've paid in monthly installments, because the interest was compounded on the balance we didn't pay off each month. So a good upper bound for the monthly payment would be one-twelfth of the balance, after having its interest compounded monthly for an entire year.

# In short:

# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly payment lower bound = Balance / 12
# Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

# Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search) to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year. Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!). Produce the same return value as you did in Problem 2.

# Note that if you do not use bisection search, your code will not run - your code only has 30 seconds to run on our servers.
# Paste your code into this box
YEAR = 12
monthly_inserest_rate = annualInterestRate / YEAR
monthly_payment_lower = balance / YEAR
monthly_payment_upper = (balance * (1 + monthly_inserest_rate)**12) / YEAR
init_balance = balance
epsilon = 0.01

while abs(balance) > epsilon:
    monthly_payment_mid = (monthly_payment_lower + monthly_payment_upper) / 2
    balance = init_balance

    for i in range(12):
        balance = balance - monthly_payment_mid + ((balance - monthly_payment_mid) * monthly_inserest_rate)
    if balance > epsilon:
        monthly_payment_lower = monthly_payment_mid
    elif balance < -epsilon:
        monthly_payment_upper = monthly_payment_mid
    else:
        break

print("Lowest Payment:",round(monthly_payment_mid, 2)) 
