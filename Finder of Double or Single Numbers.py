#Finder of Double or Single Numbers 1 to 100 25.05.2020 written by omeraydmr

double_number_list = [x for x in range(1, 101) if x % 2 == 0]
single_number_list = [x for x in range(1 , 101) if x % 2 != 0]
print("Double Numbers= " , double_number_list, "\nSingle Numbers= ", single_number_list)
