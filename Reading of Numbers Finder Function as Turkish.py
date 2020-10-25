#Reading of Numbers Finder as Turksih 29.05.2020 written by omeraydmr

def ron_finder(number):
    tenth = ["On" , "Yirmi" , "Otuz" , "Kırk" , "Elli" , "Altmış" , "Yetmiş" , "Seksen" , "Doksan"]
    oneth = ["" , "Bir" , "İki" , "Üç" , "Dört" , "Beş" , "Altı" , "Yedi" , "Sekiz" , "Dokuz"]
    ynumber = list()

    for i in number:
        ynumber.append(i)
    if int(number) < 100 and 9 < int(number): 
        return "{} {}" .format ((tenth[int(ynumber[0]) - 1]) , (oneth[int(ynumber[1])]))
    else: 
        return "Number is not avaliable."

while True:
    number= input("Enter your two digit number: ")
    print(ron_finder(number))
