#Day 11: Coding Challenge
# Black Jack Game
import random as rnd
card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# My First Version
# def play_game():
#     should_play = True
#     while should_play:
#         player_card = []
#         computer_card = []
#         player_score = 0
#         computer_score = 0
#
#         def update_score(cards):
#             score = sum(cards)
#
#             while score > 21 and 11 in cards:
#                 cards[cards.index(11)] = 1
#                 score = sum(cards)
#
#             return score
#
#         play = input("Do want to play Black jack? y/n: ").lower()
#         if play == "y":
#             for n in range(0, 2):
#                 player_card.append(rnd.choice(card))
#                 computer_card.append(rnd.choice(card))
#             player_score = update_score(player_card)
#             computer_score = update_score(computer_card)
#
#             def winner_checker():
#                 if player_score > 21:
#                     print("You Lose!")
#                 elif computer_score > 21:
#                     print("You Win!")
#                 elif player_score > computer_score:
#                     print("You win!")
#                 elif computer_score <= 21 and computer_score > player_score:
#                     print("You lose!")
#                 else:
#                     print("Draw!")
#
#             print(f"Your Cards: {player_card}, current score: {player_score}")
#             print(f"Computer's first Card: {computer_card[0]}")
#             another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
#             if another_card == "y":
#                 player_card.append(rnd.choice(card))
#                 player_score = update_score(player_card)
#                 while computer_score < 17 and len(computer_card) < 4:
#                     computer_card.append(rnd.choice(card))
#                     computer_score = update_score(computer_card)
#                 winner_checker()
#                 print(f"Your final hand: {player_card} and final score: {player_score}")
#                 print(f"Computer's final hand: {computer_card} and final score: {computer_score}")
#                 should_play = False
#             else:
#                 while computer_score < 17 and len(computer_card) < 3:
#                     computer_card.append(rnd.choice(card))
#                     computer_score = update_score(computer_card)
#                 winner_checker()
#                 print(f"Your final hand: {player_card} and final score: {player_score}")
#                 print(f"Computer's final hand: {computer_card} and final score: {computer_score}")
#                 should_play = False
#             play_game()
#
#         else:
#             should_play = False

# play_game()

# Code refactoring, make a function perform only on task and one task only (Separation of concerns)

def draw_card():
    card_choice = rnd.choice(card)
    return card_choice

def update_score(card_list):
    score = sum(card_list)
    while score > 21 and 11 in card_list:
        card_list[card_list.index(11)] = 1
        score = sum(card_list)
    return score

def players_turn(players_card, computers_card):
    players_score = update_score(players_card)
    print(f" Your Cards: {players_card} and Your Current Score: {players_score}")
    print(f" Computer's first Cards: {computers_card[0]}")
    while players_score < 21 and len(players_card) < 3:
        choice = input("Type 'y' to Draw another card, type 'n' to pass ").lower().strip()
        if choice == 'n':
           break
        if choice != 'y':
            print("Please enter 'y' or 'n'")
            continue
        players_card.append(draw_card())
        players_score = update_score(players_card)
    return players_score

def computer_turn(computers_card):
    # computers_card.append(draw_card())
    computers_score = update_score(computers_card)

    while (computers_score <= 17 ) and len(computers_card) < 3:
        computers_card.append(draw_card())
        computers_score = update_score(computers_card)
    return computers_score

def get_winner(players_score, computers_score):
    if players_score > 21:
        return "\nYou Bust! you lose!"
    if computers_score > 21:
        return "\nComputer Bust! you win!"
    if players_score > computers_score:
        return "\nYou Win! you win!"
    if computers_score > players_score:
        return "\nComputer Win! you lose!"
    return "\nIt's a draw!"

def play_around():
    players_card = [draw_card(), draw_card()]
    computers_card = [draw_card(), draw_card()]

    players_score = players_turn(players_card, computers_card)
    computers_score = computer_turn(computers_card)
    print(f" Your Cards: {players_card} and Your Current Score: {players_score}")
    print(f" Computer's Cards: {computers_card} and Computer's Score: {computers_score}")

    print(get_winner(players_score, computers_score))
    choice = input("Type 'y' to play again, and 'n' to pass ").lower().strip()
    return choice

def play_game():
     while play_around() == "y":
         # play_around()
         if play_around() == 'n':
             break
     print("\nThank you for playing Black Jack with me, Game Over!")
play_game()