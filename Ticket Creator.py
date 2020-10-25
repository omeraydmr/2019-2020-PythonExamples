#Ticket Creator As 2 Digits Letter and 2 Digits Number 16.08.2020 written by omeraydmr

small_letter = "abcdefghijklmnopqrstuvwxyz"
digit = "0123456789"
ticket_number = list()

for i in small_letter:
    for j in small_letter:
        for k in digit:
            for l in digit:
                ticket_number.append(i+j+k+l)
print("Ticket Number List: " , ticket_number)

