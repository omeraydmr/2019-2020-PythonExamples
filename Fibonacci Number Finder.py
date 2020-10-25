#Fibonacci Number Finder 19.05.2020 written by omeraydmr

a = 1
b = 1
c = int(input("Write your range for fibonacci as an integer: "))

fibonacci = [a , b]
while True:
    if c < 0 :
        print("Error ! Range can not be negative...")
        break
    elif c == 0:
        print("0")
        break
    elif c == 1:
        print(fibonacci [a])
        break
    else:
        for i in range(c-2):
            a , b = b , a+b
            fibonacci.append(b)            
        print("Your fibonacci values are: " , fibonacci)
        break