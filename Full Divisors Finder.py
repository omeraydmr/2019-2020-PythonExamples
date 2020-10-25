#Full Divisors Finder 26.05.2020 written by omeraydmr

def full_divisor(number):
    full_divisors = list()
    for i in range (2 , number):
        if (number % i == 0):
            full_divisors.append(i)
    full_divisors.append(number)
    return full_divisors
print("If you want to quit press 'q' .")

while True:
    number = input ("Please enter your number: ")
    if (number == 'q'):
        print("You're exiting...")
        break
    else:
        number = int(number)
        print("The Full Divisors List of" , number , "is" , full_divisor(number))
