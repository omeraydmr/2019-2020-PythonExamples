#Perfect Number Finder 25.05.2020 written by omeraydmr
#Definition : In number theory, a perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. 
#For instance, 6 has divisors 1, 2 and 3, and 1 + 2 + 3 = 6, so 6 is a perfect number.

number = int(input("Please enter your number which want to find perfect= "))
b = 1
c = list()
summ = 0

while True:
    if(number > b):
        if (number % b == 0):
            c.append(b)
            b += 1
        
        else:
            b += 1
    else:
        break

for i in c:
    summ += i

print("Exact divisors of the number you entered is " , c)

if (summ == number):
    print("The number you entered is PERFECT.")
else:
    print("The number you entered is NOT PERFECT.")
