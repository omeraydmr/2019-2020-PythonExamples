#Rock Paper Scissors 13.11.2020 written by omeraydmr

right = 0
player_1score=0
player_2score=0



while (right < 5):
    
    
    player_1 = str(input("Player 1 enter your shape: "))
    player_2 = str(input("Player 2 enter your shape: "))
    

    if(player_1.lower() == 'rock' and player_2.lower() == 'scissors'):
        print("Player 1 won.")
        player_1score +=1
        right += 1
        continue

    elif(player_2.lower() == 'rock' and player_1.lower() == 'scissors'):
        print("Player 2 won.")
        player_2score +=1
        right += 1
        continue

    elif((player_2.lower() == 'rock' and player_1.lower() == 'rock') and (player_2.lower() == 'scissors' and player_1.lower() == 'scissors')):
        print("Players are equal.")
        continue

    elif(player_1.lower() == 'paper' and player_2.lower() == 'rock'):
        print("Player 1 won.")
        player_1score +=1
        right += 1
        continue

    elif(player_2.lower() == 'paper' and player_1.lower() == 'rock'):
        print("Player 2 won.")
        player_2score +=1
        right += 1
        continue

    elif((player_1.lower() == 'paper' and player_2.lower() == 'rock') and (player_2.lower() == 'rock' and player_1.lower() == 'rock')):
        print("Players are equal.")
        continue

    elif(player_1.lower() == 'scissors' and player_2.lower() == 'paper'):
        print("Player 1 won.")
        player_1score +=1
        right += 1
        continue

    elif(player_2.lower() == 'scissors' and player_1.lower() == 'paper'):
        print("Player 2 won.")
        player_2score +=1
        right += 1
        continue

    elif((player_1.lower() == 'scissors' and player_2.lower() == 'scissors') and (player_2.lower() == 'scissors' and player_1.lower() == 'scissors')):
        print("Players are equal.")
        continue

    else:
        print("Invalid input! You have not entered rock, paper or scissors, try again.")
        break

if(player_1score > player_2score):
    print("\n ---------PLAYER 1 WIN---------")

else:
    print("\n ---------PLAYER 2 WIN---------")



    
