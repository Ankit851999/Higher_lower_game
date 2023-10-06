from art import logo, vs
from game_data import data
from random import choice
from replit import clear
import os

def result(a_follower, b_follower, selection):
    """returns win True False"""

    if a_follower > b_follower:
        return selection == "a"
    elif a_follower > b_follower:
        return selection == "b"


data2 = choice(data)
score = 0
game_over = False
while not game_over:
    data1 = data2
    while data1 == data2:
        data2 = choice(data)
    print(logo)
    print(f'Compare A: {data1["name"]}, a {data1["description"]}, from {data1["country"]}.')
    print(vs)
    print(f'Compare B: {data2["name"]}, a {data2["description"]}, from {data2["country"]}.')
    choices = input("Who has more followers? Type 'A' or 'B': ").lower()
    clear()
    os.system("clear")
    winner = result(data1['follower_count'], data2['follower_count'], choices)
    if winner:
        score += 1
        print("Correct")
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True
