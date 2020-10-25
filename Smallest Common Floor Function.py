#Smallest Common Floor Finder 29.05.2020 written by omeraydmr

def scf_finder(number1 , number2):
    exact_divisors = list()
    for i in range(1 , (number1 * number2) + 1):
        if i % number1 == 0 and i % number2 == 0:
            exact_divisors.append(i)      
    return exact_divisors[0]

while True:
    number1= int(input("Enter your first number: "))
    number2= int(input("Enter your second number: "))
    print(scf_finder(number1 , number2))
