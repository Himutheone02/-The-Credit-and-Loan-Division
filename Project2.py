# Himanshu Ladole 031901569

# Project 2 - Function call

import math  # importing the math library

userName = input("\nWhat is your name ?\n").upper()  # user input
MAX_INTEREST_RATE = 18.5  # Pre-assigned value
choice = ' '

def main():     # DEFINE THE MAIN FUNCTION

    while True:   # while loop

        choice = displayMenu()  # calling the display menu function

        if choice == '1':# Verifying user input

            credit_card_approval = ApplyForCard()

            if credit_card_approval == 0:
                print(f"Sorry {userName} you are not approved for a credit card.")
                print()   # adding a extra line
            else:
                print(f"\nCongralulations!! You are approved for a credit card.")
                print("\nCard Type is:", getCardType(credit_card_approval))
                print()   # adding a extra line

        elif choice == '2':

            monthlyPayment = getMonthlyLoanPayment()
            print(f"\nMonthly Loan Payment due: ${monthlyPayment:.2f}")
            print()   # adding a extra line

        elif choice == '3':

            maturity_value = getIRAMaturity()
            if maturity_value is not None:
                print(f"\nIRA Maturity Value is: ${maturity_value:.2f}")
                print()
            else:
                print("\nInvalid age")
                print()  # adding a extra line

        elif choice == 'Q':

            print(f"\nThank you for using our services {userName}.")
            print(f"\nHave a Good Day {userName}.")
            print()
            break   # ends the loop 

        else:
            print("\nINVALID CHOICE. Please try again.")
            print()  # adding a extra line
                       
def displayMenu():   # DEFINE THE displaying Menu FUNCTION

    print(f"Welcome to the Credit and Loan division {userName}.")
    print("\n======================================================\n")
    print("\t1. Apply for a Credit Card.")
    print("\t2. Calculate Monthly Loan Payments.")
    print("\t3. Calculate Maturity Value of an IRA.")
    print("\tQ. Quit")
    print("\n======================================================")
    return input("\n\tPlease Pick a desired course of action: ")  # gering desired input from the user
    
def ApplyForCard():  # DEFINE THE Applying For Card FUNCTION

    global userName
    balance = float(input(f"\n{userName} please enter your account balance: $")) # users account balance
        
    if balance < 0:
        print("\nInsufficent Balance.")
        return 0
    elif balance >= 15000:
        return 1
    elif balance >= 10000:
        return 2
    elif balance >= 5000:
        return 3
    else:
        return 0
    
def getCardType(cardApprovalcode):

    card_type = {1: "Platinum",
                 2: "Gold",
                 3: "Silver",
                 0: "NOT APPROVED"}   # list of credit cards
    return card_type.get(cardApprovalcode)
     
def getMonthlyLoanPayment():  # DEFINE THE monthly loan payment FUNCTION

    global MAX_INTEREST_RATE

    N = input("\nEnter the years until loan maturity: ")  # user input
    if N == '':
        years = 30  # default value of year
    else:
        years = int(N)
        if years < 0:
            print("INVALID ENTRY!! \nYears cannot be negative.")
            return

    P = float(input("\nEnter the loan amount (Principle): $")) # user input
    if P < 0:
        print("INVALID ENTRY!! \nPrinciple amount must be greater than zero. ")
        return
                  
    R = float(input("\nEnter the Annual interest rate (%): ")) # user input
    if R < 0 or R > MAX_INTEREST_RATE:
        print(f"INVALID ENTRY!! \nAccording to State law the interest rate must be between 0 and {MAX_INTEREST_RATE}.")
        return

    return calcMonthlyLoanPayment(P, R, years)  # assigning values

def calcMonthlyLoanPayment(LoanAmt, InterestRate, numYears): # DEFINE THE calculating monthly loan payment FUNCTION

    InterestRate = InterestRate / 100
    monthlyRate = InterestRate / 12
    monthlyPayment = (LoanAmt * monthlyRate) / (1 - math.pow((1 + monthlyRate),(-12 * numYears))) # calculating monthly payment
    return monthlyPayment

def getIRAMaturity():  # DEFINE THE IRA maturity FUNCTION

    global userName

    currentAge = int(input(f"\n{userName} enter your current age: "))  # user input
    if currentAge >= 65 or currentAge < 0:
            print("INVALID AGE!! \nAge must be less that 65 and not a negative number")
            return None

    years_until_maturity = 65 - currentAge

    annualDeposit = float(input(f"\n{userName} enter the annual deposit amount to the IRA: $"))  # user input

    if annualDeposit > 2000 or annualDeposit <= 0:
                          print("INVALID AMOUNT!! \nAnnual deposit must be between $0 and $2000. ")
                          return 
                        
    annual_interest_rate = float(input("\nEnter annual interest rate (%): "))  # user input

    if annual_interest_rate < 0 or annual_interest_rate > MAX_INTEREST_RATE:
            print(f"INVALID ENTRY!! \nAccording to State law the interest rate must be between 0 and {MAX_INTEREST_RATE}.")
            return

    return calcIRAMaturity(years_until_maturity , annualDeposit, annual_interest_rate)  # assigning values
        

def calcIRAMaturity(YearsUntilMaturity , AnnualDepositAmt, InterestRate):  # DEFINE THE calculating IRA maturity FUNCTION

    InterestRate = InterestRate / 100
    maturity_value = AnnualDepositAmt * ((math.pow((1 + InterestRate), YearsUntilMaturity)- 1) / InterestRate)  # calculating maturity value
    return maturity_value


main() # CALL (Execute) THE MAIN FUNCTION
    
               

                

        
        
        
        
                        
                
                        
                
                        
                    
