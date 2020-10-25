#Armstrong Number Finder 25.05.2020 written by Masware

number = int(input("Please enter your number which want to find armstrong= "))
digit = list()
sum = 0

for i in str(number):
    digit.append(i)
    
for j in str(number):
    sum += int(j) ** len(digit)
    print("Exponent Number:" , len(digit) , "Sum of Each Number's Exponential" , sum)

if (number == sum):
    print("The number you entered is ARMSTRONG NUMBER.")

else:
    print("The number you entered is NOT ARMSTRONG NUMBER.")



