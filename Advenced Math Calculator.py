#Advenced Math Calculator 30.05.2020 written by omeraydmr

import math

print(""" *************************************
Calculator Program

Transactions;

1. Factorial Process

2. Collection Process

3. Extraction Process

4. Splitting Process

5. Multiplication Process

6. Getting The Mod Process

7. Largest Common Divisor Finding Process

8. Finding Circumference of The Circle of Diameter

9. Finding The Area of ​​The Circle Given the Diameter

10. Calculating The Logarithmic Value

11. The Process of Taking Force

For exit from process press 'q'

**************************************
""")

while True:
    process = input("\nEnter your process number: ")

    number1 = int(input("\nEnter your first number: "))

    if process == "1":
        print(math.factorial(number1))

    elif process == "2":
        summ = number1
        while True:
            number2 = input("Enter your second number: ")
            if number2 == 'q' :
                break
            else:
                summ += int(number2)
                print("Your Result: " , summ)
            

    elif process == "3":
        ext = number1
        while True:
            number2 = input("Enter your second number: ")
            if number2 == 'q' :
                break
            else:
                ext -= int(number2)
                print("Your Result: " , ext)

    elif process == "4":
        spl = number1
        while True:
            number2 = input("Enter your second number: ")
            if number2 == 'q' :
                break
            else:
                spl /= int(number2)
                print("Your Result: " , spl)

    elif process == "5":
        mlt = number1
        while True:
            number2 = input("Enter your second number: ")
            if number2 == 'q' :
                break
            else:
                mlt *= int(number2)
                print("Your Result: " , mlt)

    elif process == "6":
        number2 = int(input("Enter your second number: "))
        print(math.fmod(number1 , number2))

    elif process == "7":
        number2 = int(input("Enter your second number: "))
        print(math.gcd(number1 , number2))

    elif process == "8":
        circumference = number1 * math.pi
        print("Circumference" , circumference)

    elif process == "9":
        area = ((number1 / 2) ** 2) * math.pi
        print("Area" , area)

    elif process == "10":
        number2 = int(input("Enter your second number: "))
        print("Logarithmic Value is: " , math.log(number1 , number2))

    elif process == "11":
        number2 = int(input("Enter your second number for using force: "))
        print(math.pow(number1 , number2))

