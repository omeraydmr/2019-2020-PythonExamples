#Perfect Number Finder 25.05.2020 written by Masware

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