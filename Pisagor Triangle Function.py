#Pisagor Triangle Finder 1 to 100 29.05.2020 written by omeraydmr

def pisagor_finder(number):
    first_edge = list()
    second_edge = list()
    third_edge = list()
    for a in range(1 , number+1):
        for b in range(1 , number*4):
            for c in range(1 , number*4):
                if ((a*a) + (b*b) == (c*c)):
                    first_edge.append(a)
                    second_edge.append(b)
                    third_edge.append(c)
    for i in range(len(third_edge)):
        print("Pisagor Triangle's first edge: {} second edge: {} third edge: {}".format(first_edge[i],second_edge[i],third_edge[i]))
while True:
    number= int(input("Enter your end number: "))
    print(pisagor_finder(number))
