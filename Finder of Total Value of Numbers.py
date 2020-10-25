#Finder of Total Value of Numbers 25.05.2020 written by omeraydmr

print ("Enter your numbers what you want, if you finish your number enter 'q'.")
sum = 0

while True:
    a = input("Please enter your number which want to find of sum: ")

    if a == 'q':
        print("Total Value: " , sum)
        break
    
    else:
        sum = sum + int(a)
