#Perfect Number Finder 19.05.2020 written by omeraydmr

def perfect_finder(number):
    perfect_numbers = list()
    for i in range(1 , number):
        exact_divisors = list()   
        for j in range(1 , i):     
            if (i % j == 0):
                exact_divisors.append(j)
        if i == sum(exact_divisors):
            perfect_numbers.append(i)
    return perfect_numbers

while True:
    number = int(input("Please enter your end number: "))
    print(perfect_finder(number))