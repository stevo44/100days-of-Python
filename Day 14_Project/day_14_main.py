# HIGHER LOWER GAME CHALLENGE

import os
import random as rnd
from data import data
import arts

# random_data = rnd.choice(data)
# print(random_data)

print(arts.logo)
# print(arts.vs)



def compare_string():
    random_data = rnd.choice(data)
    display_string = f"{random_data["name"]}, {random_data["description"]} from {random_data["country"]}"
    number_follower = random_data["follower_count"]
    return display_string, number_follower
def get_data():
    compare_A = compare_string()
    against_B = compare_string()
    return compare_A, against_B

def get_players_answer():
    player_answer = input("who has more followers? Type 'A' or 'B': ").upper().strip()
    return player_answer
def followers_checker(A,B):
        if A > B:
            return "A"
        return "B"

def play_game():
     data = get_data()
     question_A = data[0][0]
     question_B = data[1][0]
     answer_A = data[0][1]
     answer_B = data[1][1]
     print(question_A)
     print(arts.vs)
     print(question_B)
     players_answer = get_players_answer()
     print(players_answer)
     print(f"The answer is {followers_checker(answer_A, answer_B)}")
     print(data)

    # while followers_checker() == player_answer:


play_game()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')