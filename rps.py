import random

choices = ["rock","paper","scissors"]
while True:
    computer = random.choice(choices)
    player = None
    while player not in choices:

        player = input("rock , paper or scissors?: ").lower()
    if player == computer:
        print("computer: "+ computer)
        print("player : "+ player)
        print("Tie!")
    elif player == "rock":
        if computer =="paper":
            print("computer: "+ computer)
            print("player : "+ player)
            print("You Lose Bozo!")
        elif computer == "scissors":
            print("computer: "+ computer)
            print("player : "+ player)
            print("You deafeted a computer GJ!!")
    elif player =="paper":
        if computer == "scissors":
            print("computer: "+ computer)
            print("player : "+ player)
            print("You Lose Bozo!")
        elif computer == "rock":
            print("computer: "+ computer)
            print("player : "+ player)
            print("You deafeted a computer GJ!!")

    elif player =="scissors":
        if computer == "rock":
            print("computer: "+ computer)
            print("player : "+ player)
            print("You lose Bozo!")
        elif computer == "paper":
            print("computer: "+ computer)
            print("player : "+ player)
            print("You deafeted a computer GJ!!")
    playAgain = input("Press 'y' to play again or press any key to get out of here ").lower()
    if playAgain !="y":
        break

print("Bye!")





