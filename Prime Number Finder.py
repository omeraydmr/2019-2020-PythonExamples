#Prime Number Finder 26.05.2020 written by omeraydmr

def prime_number(number):
    if (number == 1):
        return False
    elif (number == 2):
        return True
    else:
        for i in range (2 , number):            
            if (number % i == 0):
                return False
        return True

print("If you want to quit press 'q' .")
while True:
    number = input("Please enter your number: ")
    if (number.lower() == "q"):
        print("Goodbye...")
        break
    else:
        number = int(number)
        if (prime_number(number)):
            print (number , "is a prime number.")
        else:
            print (number , "is not a prime number.")
