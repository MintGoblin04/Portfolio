'''
Module : Dice Game
Description: The players roll two 6-sided dice each and gets points depending on what tehy roll.
There are 3 rounds in a game. In each round, each playyer rolls two dice.
Date: 06/02/2022
Version: 1.1
'''
import random

end = False

#Introduction to the users
print("Dice Game \n")
print("Rules:")
print("1. Two player allowed in each game.")
print("2. 3 rounds in each game.")
print("3. Two dices to be rolled each round by each player.")
print("4. These dice numbers will be assigned points including the value of the roll.")
print("4.2 Extra points are acheived when the number can be divide by 2 or 5.")
print("    2 points will be added if divided by 2, 5 if it can be divided by 5.")
print("    These extra points will be added to the total.")
print("5. The player with the highest total over the 3 rounds score wins.")
print("6. If the game is ended with the Players having an equal score. A dice will be rolled by each player until the highest wins \n.")
print("Enjoy. \n")


def diceSides():
    if dice1 == 1:
        print("-------")
        print("|     |")
        print("|  x  |")
        print("|     |")
        print("-------")

    elif dice1 == 2:
        print("-------")
        print("|x    |")
        print("|     |")
        print("|    x|")
        print("-------")

    elif dice1 == 3:
        print("-------")
        print("|x    |")
        print("|  x  |")
        print("|    x|")
        print("-------")

    elif dice1 == 4:
        print("-------")
        print("|x   x|")
        print("|     |")
        print("|x   x|")
        print("-------")

    elif dice1 == 5:
        print("-------")
        print("|x   x|")
        print("|  x  |")
        print("|x   x|")
        print("-------")

    elif dice1 == 6:
        print("-------")
        print("|x   x|")
        print("|x   x|")
        print("|x   x|")
        print("-------")


def diceSides2():

    if dice2 == 1:
        print("-------")
        print("|     |")
        print("|  x  |")
        print("|     |")
        print("-------")

    elif dice2 == 2:
        print("-------")
        print("|x    |")
        print("|     |")
        print("|    x|")
        print("-------")

    elif dice2 == 3:
        print("-------")
        print("|x    |")
        print("|  x  |")
        print("|    x|")
        print("-------")

    elif dice2 == 4:
        print("-------")
        print("|x   x|")
        print("|     |")
        print("|x   x|")
        print("-------")

    elif dice2 == 5:
        print("-------")
        print("|x   x|")
        print("|  x  |")
        print("|x   x|")
        print("-------")

    elif dice2 == 6:
        print("-------")
        print("|x   x|")
        print("|x   x|")
        print("|x   x|")
        print("-------")


def winner():
    global winner
    if player1Total > player2Total:
        winner = "Player 1"

    elif player1Total < player2Total:
        winner = "Player 2"

    else:
        winner = "nobody it's a draw"


    print()
    print
    print("The winner is", winner)
        

player1Total = 0
player2Total = 0

while end == False:
    #startup of the game
    start = str(input("Do you want to start the game? (Yes or No). \n"))
    if start == "yes" or start == "Yes":
        end = True

        #Usernames
        player1 = str(input("Enter Player 1 name. "))
        print("Player 1 is", player1 , ".\n")
        player2 = str(input("Enter Player 2 name. "))
        print("Player 2 is", player2, ". \n")

        #Players score
        player1Score = 0
        player2Score = 0

        #set rounds to 3. Can be changed if needed
        rounds = 3

        #start of rounds
        while rounds != 0:
            rounds = rounds - 1
            roundStart = input("Do you want to start the round. \n")
            if roundStart == "yes" or roundStart == "Yes":
                #roll of player 1 dice
                roll = input("Player 1 turn. (Roll). ")
                if roll == "roll" or roll == "Roll":
                    dice1 = random.randint(1,6)
                    dice2 = random.randint(1,6)
                    #adds dice to total
                    player1Total = player1Total + dice1
                    player1Total = player1Total + dice2
                    diceTotal = dice1 + dice2
                    diceSides()
                    print(dice1)
                    diceSides2()
                    print(dice2)
                    if diceTotal % 2 == 0 and diceTotal != 0:
                        print("2 extra points because total can be divided by 2")
                        player1Total = player1Total + 2 #need to test
                        print("Player 1 Overal Total so far", player1Total ,"\n")
                    elif diceTotal % 5 == 0 and diceTotal != 0:
                        print("5 extra points because total can be divided by 5")
                        player1Total = player1Total + 5 #need to test
                        print("Player 1 Overal Total so far", player1Total ,"\n")
                    else:
                        print("Player 1 Overal Total so far", player1Total ,"\n")

                roll2 = input("Player 2 turn. (Roll). ")
                if roll == "roll" or roll == "Roll":
                    dice1 = random.randint(1,6)
                    dice2 = random.randint(1,6)
                    #adds dice to total
                    player2Total = player2Total + dice1
                    player2Total = player2Total + dice2
                    diceTotal = dice1 + dice2
                    diceSides()
                    print(dice1)
                    diceSides2()
                    print(dice2)
                    if diceTotal % 2 == 0 and diceTotal != 0:
                        print("2 extra points because total can be divided by 2")
                        player2Total = player2Total + 2 #need to test
                        print("Player 2 Overal Total so far is", player2Total,"\n")
                    elif diceTotal % 5 == 0 and diceTotal != 0:
                        print("5 extra points because total can be divided by 5")
                        player2Total = player2Total + 5 #need to test
                        print("Player 2 Overal Total so far is", player2Total,"\n")
                    else:
                        print("Player 2 Overal Total so far is", player2Total,"\n")


                
                    
                else:
                    print("Error")
            else:
                pass
            
            
   
    elif start == "no" or start == "No":
        end = True
        print("Game ended. See you later. \n")
    else:
        print("Incorrect input. Repeat of input is required. \n")



winner()    
        
    

