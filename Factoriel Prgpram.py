#Factoriel Program With Integer 16.08.2020 Written by omeraydmr

while True:
    integer = input("Enter a value or press 'e' for exit please: ")    
    if integer.lower() == 'e':
        print("Quiting from the program...")
        break
    else:
        integer = int(integer)
        factoriel = 1
        n = 1    
        for i in range(2,integer+1):
            print("Step:",n ,"Factoriel",factoriel , "i:", i)
            factoriel *=i
            n += 1
        print("The result is: ",factoriel)
