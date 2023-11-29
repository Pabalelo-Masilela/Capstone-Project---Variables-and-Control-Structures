'''This program is designed for the user to access 2 different financial 
calculators, an investment calculator and a bond repayment calculator.'''
import math

print('''investment - to calculate the amount of interest\
you'll earn on your investment.\n
bond - to calculate the amount you'll have to pay on a home loan.\n
      ''')
calculator_type = input('''Enter either 'investment' or 'bond'\
from the menu above to proceed: \n''')
calculator_type = calculator_type.lower()
if calculator_type == "bond" or calculator_type == "investment":
    print("Thank you.Lets begin calculating!")

#Investment calculator
if calculator_type == "investment":
    deposit_amount = float(input("Enter deposit amount(R): \n"))
    interest_rate = float(input("Enter interest rate without '%' sign: \n"))
    investment_years = float(input("Enter estimated investment years:\n"))
    transaction_type =input("Enter interest type as 'compound' or 'simple':\n")
    transaction_type = transaction_type.lower()
    if transaction_type == "simple":
        investment_return = deposit_amount*(1 + (interest_rate/100)\
        * investment_years)
        investment_return = round(investment_return,2)
        print(str(f'''Based on the following data:\n
        Deposit amount: {deposit_amount}\n
        Interest rate: {interest_rate}%\n
        Investment years: {investment_years}\n
        The investment payout will be: R{investment_return}'''))
    elif transaction_type == "compound":
        investment_return = deposit_amount *\
        math.pow(1 + (interest_rate/100),investment_years)
        investment_return = round(investment_return,2)
        print(str(f'''Based on the following data:\n
        Deposit amount: {deposit_amount}\n
        Interest rate: {interest_rate}%\n
        Investment years: {investment_years}\n
        The investment payout will be: R{investment_return}'''))

#Bond repayment calculator
elif calculator_type == "bond":
    house_value = float(input("Enter house value (R): \n"))
    house_interest_rate = float(input("Enter interest rate,\
without the '%' sign: \n"))
    repayment_months = float(input("Enter number of repayment months: \n"))
    i = (house_interest_rate/100)/12
    repayment = (i * house_value)/(1-(1 + i)**(-repayment_months))
    repayment = round(repayment,2)
    print(str(f'''Based on the following data:\n
    House value: {house_value}\n
    Interest rate: {house_interest_rate}%\n
    Repayment months: {repayment_months}\n
    The monthly repayment will be: R{repayment}'''))
else:
    print("You have not chosen a valid option.")