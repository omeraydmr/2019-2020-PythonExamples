#Upgraded Admin Enterance 05.04.2020 written by omeraydmr

nickname_saved = "Masware"
password_saved = "123456"
enterance_right = 3

while True:
    nickname = input("Enter Your Nickname :")
    password = input("Enter Your Password :")
    if (nickname != nickname_saved and password == password_saved):
        print("Nickname is Wrong...")
        enterance_right -= 1
    elif (nickname == nickname_saved and password != password_saved):
        print("Password is Wrong...")
        enterance_right -= 1
    elif (nickname != nickname_saved and password != password_saved):
        print("Nickname and Password is not Correct...")
        enterance_right -= 1
    else:
        print("You entered to system succesfuly...")
        break
    
    if(enterance_right == 0):
        print("Your rights done...")
        break




