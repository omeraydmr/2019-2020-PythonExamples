#Largest Common Divisor Finder 29.05.2020 written by omeraydmr

def lcd_finder(number1 , number2):
    exact_divisors = list()

    for i in range(1 , (number1 + number2)):
        if (number1 % i == 0 and number2 % i == 0):
            exact_divisors.append(i)
    return exact_divisors[-1]
while True:
    number1= int(input("Enter your first number: "))
    number2= int(input("Enter your second number: "))
    print(lcd_finder(number1 , number2))
