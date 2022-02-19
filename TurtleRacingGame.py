'''
Module: Turtle Game
Description: There are two turtles that are racing against each other.
You will have to pick one and see if it wins.
Date: 19/02/2022
Version: 1
'''

import turtle
import random

print("Turtle Game")
print("There are two Turtles racing against each other. Only one will win. ")
snakeChoose = input("Enter the snake you think will win. (1 or 2). ")


import turtle
import random

#window + pen
wn = turtle.Screen()
wn.title("Turtles Racing")
wn.setup(width = 500, height =500)
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.goto(50, 300)
pen.write("~ Turtles Racing ~", align="center",
		font=("candara", 24, "bold"))

#turtle one
turtleOne = turtle.Turtle()
turtleOne.hideturtle()
turtleOne.color("blue")
turtleOne.shape("turtle")
turtleOne.penup()
turtleOne.goto(-200, 100)


#turtle two
turtleTwo = turtleOne.clone()
turtleTwo.hideturtle()
turtleTwo.color("purple")
turtleTwo.penup()
turtleTwo.goto(-200,-100)

#turtle box
box = turtleOne.clone()
box.hideturtle()
box.color("green")
box.goto(-260,250)

#box
box.pendown()
box.goto(-260,-250)
box.goto(350,-250)
box.goto(350,250)
box.goto(-260,250)


#start line
line = turtle.Turtle()
line.hideturtle()
line.penup()
line.color("black")
line.goto(-180, 200)
line.right(90)
line.pendown()
line.goto(-180,-200)
line.right(90)
line.goto(-210, -200)
line.right(90)
line.goto(-210, 200)
line.right(90)
line.goto(-180, 200)
line.penup()



#triangle 1
turtleOne.goto(300,60)
turtleOne.pendown()
turtleOne.left(90)
turtleOne.forward(100)
turtleOne.left(120)
turtleOne.forward(100)
turtleOne.left(120)
turtleOne.forward(100)
turtleOne.left(30)
turtleOne.penup()
turtleOne.goto(-200,110)

#triangle 2
turtleTwo.goto(300,-140)
turtleTwo.pendown()
turtleTwo.left(90)
turtleTwo.forward(100)
turtleTwo.left(120)
turtleTwo.forward(100)
turtleTwo.left(120)
turtleTwo.forward(100)
turtleTwo.left(30)
turtleTwo.penup()
turtleTwo.goto(-200,-90)


turtleOne.showturtle()
turtleTwo.showturtle()

x = "false"
y = "false"
#main program
while x != "true":
    start = input("Do you want to start the game. (Yes). ")
    if start == "Yes" or start == "yes":
        #add game mechanics
        x = "true"

        while y != "true":
            if turtleOne.pos() >= (300, 100):
                winner = "1"
                y = "true"
                print("1")
            
            elif turtleTwo.pos() >= (300, -100):
                winner = "2"
                y = "true"
                print("2")

            #need to randomise first time
            else:
                dice = random.randint(0,6)
                dice2 = random.randint(0,6)
                run = dice * 20
                run2 = dice2 * 20
                turtleOne.forward(run)
                turtleTwo.forward(run2)
        
    else:
        print("Input isn't accepted. Enter Yes. ")
    


if winner == "1" and snakeChoose == "1":
    pen.color("dark red")
    pen.goto(50, 275)
    pen.write(">> Turtle 1 is the winner <<", align="center",
                    font=("candara", 18, "bold"))
    pen.goto(50,255)
    pen.write(">> You won!!! <<", align="center",
                    font=("candara", 18, "bold"))

    print("Turtle 1 is the winner")
    print("You won!!!")

elif winner == "1" and snakeChoose == "2":
    pen.color("dark red")
    pen.goto(50, 275)
    pen.write(">> Turtle 1 is the winner <<", align="center",
                    font=("candara", 18, "bold"))
    pen.goto(50,255)
    pen.write(">> You lost :( <<", align="center",
                    font=("candara", 18, "bold"))

    print("Turtle 1 is the winner")
    print("You lost :(")

elif winner == "2" and snakeChoose == "2":
    pen.color("dark red")
    pen.goto(50, 275)
    pen.write(">> Turtle 2 is the winner <<", align="center",
                    font=("candara", 18, "bold"))
    pen.goto(50,255)
    pen.write(">> You won!!! <<", align="center",
                    font=("candara", 18, "bold"))

    print("Turtle 2 is the winner")
    print("You won!!!")
    
elif winner == "2" and snakeChoose == "1":
    pen.color("dark red")
    pen.goto(50, 275)
    pen.write(">> Turtle 2 is the winner <<", align="center",
                    font=("candara", 18, "bold"))
    pen.goto(50,255)
    pen.write(">> You lost :( <<", align="center",
                    font=("candara", 18, "bold"))

    print("Turtle 2 is the winner")
    print("You lost :(")


