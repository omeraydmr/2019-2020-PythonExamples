#ATM Machine 05.04.2020 written by omeraydmr

budget = int(input("Enter Your First Budget: "))

print("""If you enter 'q', you will exit from ATM machine. 
    \nIf you want to balance inquiry, you will write 'Balance Inquiry' 
    \nIf you want to deposit money to your budget, you will write 'Deposit Money' 
    \nIf you want to withdraw your money, you will write 'Withdraw Money""")

while True:
    

    operation = input("Choose your opertion that you want: ")

    if (operation.lower() == 'q'):
        print("We will wait again...")
        break

    elif(operation.lower() =="balance inquiry"):
        print("Your Budget: " , budget)
   
    elif (operation.lower() == "deposit money"):
        amount = int(input("Enter amount you want to deposit: "))
        budget += amount

    elif (operation.lower() == "withdraw money"):
        amount = int(input("Enter amount you want to withdraw:"))
        budget = budget - amount

        if(budget - amount < 0):
            print("Your balance is insufficient ...")
            continue

    else:
        print("Invalid Transaction... \n\nPlease check your answer.")

