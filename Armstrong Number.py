#Armstrong Number Finder 25.05.2020 written by omeraydmr
#Definition : An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself.
#For example, 371 is an Armstrong number since 3**3 + 7**3 + 1**3 = 371.

number = int(input("Please enter your number which want to find armstrong or not= "))
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



