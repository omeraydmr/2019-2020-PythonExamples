#Class Level Finder 30.03.2020 written by omeraydmr

classes = ["MATH 150", "PSYCH 111", "PSYCH 313", "PSYCH 412", "MATH 300", 
           "MATH 404", "MATH 206", "ENG 100", "ENG 103", "ENG 201", 
           "PSYCH 508", "ENG 220", "ENG 125", "ENG 124"]
upper_classes = list()
lower_classes = list()

for i in classes:
    info_class = i.split(" ")
    if info_class[0] == "MATH":
        if(int(info_class[1]) >= 300):
            upper_classes.append(i)
        else:
            lower_classes.append(i)
    elif info_class[0] == "ENG":
        if(int(info_class[1]) >= 200):
            upper_classes.append(i)
        else:
            lower_classes.append(i)
    elif info_class[0] == "PSYCH":
        if(int(info_class[1]) >= 400):
            upper_classes.append(i)
        else:
            lower_classes.append(i)

print("Upper Level Classes :", upper_classes)
print("Lower Level Classes :", lower_classes)



