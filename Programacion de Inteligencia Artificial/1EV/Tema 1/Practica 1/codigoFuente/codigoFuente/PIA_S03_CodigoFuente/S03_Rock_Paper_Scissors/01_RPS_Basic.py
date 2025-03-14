#!/usr/bin/python3

import random


ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'


def assess_game(user_action, computer_action):
    if user_action == computer_action:
        print(f"User and computer picked {user_action}. Draw game!")

    # You picked Rock
    elif user_action == ROCK:
        if computer_action == SCISSORS:
            print("Rock smashes scissors. You won!")
        else:
            print("Paper covers rock. You lost!")

    # You picked Paper
    elif user_action == PAPER:
        if computer_action == ROCK:
            print("Paper covers rock. You won!")
        else:
            print("Scissors cuts paper. You lost!")

    # You picked Scissors
    elif user_action == SCISSORS:
        if computer_action == ROCK:
            print("Rock smashes scissors. You lost!")
        else:
            print("Scissors cuts paper. You won!")
        


def main():
    game_actions = [ROCK, PAPER, SCISSORS]g

    while True:
        user_action = input("\nPick a choice: rock, paper or scissors: ")
        computer_action = random.choice(game_actions)

        print(f"\nYou picked {user_action}. The computer picked {computer_action}\n")
        assess_game(user_action, computer_action)


if __name__ == "__main__":
    main()
