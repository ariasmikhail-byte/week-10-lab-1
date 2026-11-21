# Mikhail Arias
# CMP 131
# Week: 10
# Lab: 1
# Program: Rock Paper Scissors
# November 20, 2026

import random

def computer_choice():
    c_choice = random.randint(1, 3)
    if c_choice == 1:
        return "Rock"
    elif c_choice == 2:
        return "Paper"
    else:
        return "Scissors"

def user_choice():
    u_choice = int(input("Press 1 for Rock, 2 for Paper or 3 for Scissors"))
    if u_choice == 1:
        return "Rock"
    elif u_choice == 2:
        return "Paper"
    else:
        return "Scissors"

def determine_winner(c, u):
    if c == u:
        return "tie"
    elif (c == "Rock" and u == "Paper") or (c == "Paper" and u == "Scissors") or (c == "Scissors" and u == "Rock"):
        return "User"
    else:
        return "PC"

def results(winner):
    if winner == "tie":
        print("It's a tie. Play again.")
    elif winner == "User":
        print("You win!")
    else:
        print("The computer wins!")

def main():
    while True:
        c_choice = computer_choice()
        u_choice = user_choice()

        print("You chose:", u_choice)
        print("The computer chose:", c_choice)

        winner = determine_winner(c_choice, u_choice)
        results(winner)

        if winner != "tie":
            break

main()