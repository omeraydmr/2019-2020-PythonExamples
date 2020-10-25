#Car Rent Program 07.04.2020 written by omeraydmr

brand = ["BMW" , "Mercedes" , "BMW" , "Volkswagen"]
model = ["3.18" , "A180" , "5.20" , "Passat"]
year = ["2018" , "2019" , "2017" , "2014"]
amount = [8 , 4 , 3 , 3]
daily_price = [140 , 120 , 210 , 120]
subtractive=1


print("Our Car Brands: " , set(brand) ,"\n")
print("""If you write 'exit' , you will quit from program. \n """)
print("""If you write 'info' you can see all information about our cars.""")

while True:
    chosen = input("Enter Your Brand Choice :")
    if chosen.lower() == "exit":
        print("Thank You, See You Later...")
        break
    
    elif chosen.lower() == "info":
        for i in range(3 , -1 , -1):
            print("Our Unique Brands : {} Models : {} Amount : {}".format(brand[i] , model[i] , amount[i]))

    elif chosen.lower() == "bmw":
        print("Model : {}  Year : {}  Amount : {}".format(model[0] , year[0] , amount[0]))
        print("Model : {}  Year : {}  Amount : {}".format(model[2] , year[2] , amount[2]))
        
        chosen2 = input("Can You Choose Your Model (Write Model Number):")        
        while True:            
            if chosen2.lower() == "3.18":
                if 0 < amount[0]:
                    day = int(input("How Many Days Your Usage :"))
                    print("Your Choice : {} Year : {}  Amount : {} Daily Price : {}".format(chosen , year[0] , amount[0] , daily_price[0]))
                    print("The Money You Have To Pay : {}".format (day * daily_price[0]))
                    amount[0]-subtractive
                    break
                else:
                    print("This Car Is Not Available!")
                    break
            elif chosen2 == "5.20":
                if 0 < amount[2]:
                    day = int(input("How Many Days Your Usage :"))
                    print("Your Choice : {} Year : {}  Amount : {} Daily Price : {}".format(chosen , year[2] , amount[2] , daily_price[2]))
                    print("The Money You Have To Pay : {}".format (day * daily_price[2]))
                    amount[2]-subtractive
                    break
                else:
                    print("This Car Is Not Available!")
                    break               
            else:
                print("Wrong Model Number!")
                break
        break
    elif chosen.lower() == "volkswagen":
        if 0 < amount[3]:
            day = int(input("How Many Days Your Usage :"))
            print("Your Choice : {} Year : {}  Amount : {} Daily Price : {}".format(chosen , year[3] , amount[3] , daily_price[3]))
            print("The Money You Have To Pay : {}".format (day * daily_price[3]))
            amount[3]-subtractive
            break
        else:
            print("This Car Is Not Available!")             
            break

    elif chosen.lower() == "mercedes":
        if 0 < amount[1]:
            day = int(input("How Many Days Your Usage :"))
            print("Your Choice : {} Year : {}  Amount : {} Daily Price : {}".format(chosen , year[1] , amount[1] , daily_price[1]))
            print("The Money You Have To Pay : {}".format (day * daily_price[1]))
            amount[1]-subtractive
            break
        else:
            print("This Car Is Not Available!")
            break

    else:
        print("You Wrote Wrong Brand!")



