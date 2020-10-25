#Finder of Can Divide by 3 Numbers 1 to 100 25.05.2020 written by omeraydmr

numbers = list()

for i in range(1 , 101):
    if i % 3 != 0:
        continue
    else: 
        numbers.append(i)

print("The numbers that can divide by 3: " , numbers)
