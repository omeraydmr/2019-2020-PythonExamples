#Basic Calculator 27.03.2020 written by omeraydmr

print(""" *************************************
Calculator Program

Transactions;

1. Collection Process

2. Extraction Process

3. Splitting Process

4. Multiplication Process

**************************************
""")

operation = input("Transaction Number You Want To Do: ")

a = int(input("First number: "))
b = int(input("Second number: "))

if operation == "1":
    print("{} + {} = {}" .format(a,b,a+b))
elif operation == "2":
    print("{} - {} = {}" .format(a,b,a-b))
elif operation == "3":
    print("{} / {} = {}" .format(a,b,a/b))
elif operation == "4":
    print("{} x {} = {}" .format(a,b,a*b))
else:
    print("Wrong Transaction!")


