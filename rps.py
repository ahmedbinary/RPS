import random

choices = ["rock", "paper", "scissors"]


class Choices:
    ROCK = "rock"
    SCISSORS = "scissors"
    PAPER = "paper"


def print_player_choices(player_choice, computer_choice):
    print("computer_choice: " + computer_choice)
    print("player_choice : " + player_choice)


def get_computer_choice():
    return random.choice(choices)


while True:
    computer_choice = get_computer_choice()
    player_choice = None
    while player_choice not in choices:

        player_choice = input("rock , paper or scissors?: ").lower()
    if player_choice == computer_choice:
        print("computer_choice: "+ computer_choice)
        print("player_choice : "+ player_choice)
        print("Tie!")
    elif player_choice == Choices.ROCK:
        if computer_choice =="paper":
            print("computer_choice: " + computer_choice)
            print("player_choice : " + player_choice)
            print("You Lose Bozo!")
        elif computer_choice == "scissors":
            print("computer_choice: " + computer_choice)
            print("player_choice : " + player_choice)
            print("You deafeted a computer_choice GJ!!")
    elif player_choice == "paper":
        if computer_choice == "scissors":
            print_player_choices(player_choice, computer_choice)
            print("You Lose Bozo!")
        elif computer_choice == "rock":
            print_player_choices(player_choice, computer_choice)
            print("You deafeted a computer_choice GJ!!")

    elif player_choice =="scissors":
        if computer_choice == "rock":
            print_player_choices(player_choice, computer_choice)
            print("You lose Bozo!")
        elif computer_choice == "paper":
            print_player_choices(player_choice, computer_choice)
            print("You deafeted a computer_choice GJ!!")
    playAgain = input("Press 'y' to play again or press any key to get out of here ").lower()
    if playAgain !="y":
        break

print("Bye!")





