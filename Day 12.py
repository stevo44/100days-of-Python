# Scoping in Python

#Global Scope
# player_health = 10

# def drink_potion():
#     portion_strength = 2
#     print(player_health)

# drink_potion()

# game_level = 3
# enemies = ['skeleton', 'Zombie', 'Alien']

# def increase_enemies():
#     global enemies
#     enemies.append("Poison")
#     print(enemies)
# increase_enemies()
# print(enemies)

# Global Constants

# PI = 3.14159


#Coding Challenge: Guessing a Number
import random as rnd
random_number = rnd.randint(1,100)

print("Welcome to the Number Guessing Game")
print("I am thinking of a number between 1 and 100.")

def guess_checker (live_number):
    def get_clue(guess_number):
        if guess_number > random_number:
            return "Too high"
        if guess_number < random_number:
            return "Too low"

    first_guess = int(input("Make a guess: "))
    if first_guess == random_number:
        print("You guessed the number!, You win")
    else:
        print(f"You have {live_number} attempts to guess the number. ")
        print(get_clue(first_guess))
    while live_number> 0:
        guess = int(input("Guess again!: "))
        live_number -= 1
        if live_number != 0 and guess != random_number:
            print(f"You have {live_number} attempts to guess the number. ")
            print(get_clue(guess))
        if guess == random_number:
            print(f"\nYou guessed the number! which is {random_number}, You win")
            break
        if live_number == 0: print("\nYou are out of guesses, you lose.")

def choice_to_pay():
    choice = input("Would you like to play again? (y/n): ").lower().strip()
    return choice

def play_around(level):
    if level == "easy":
        live = 9
        guess_checker(live)
    elif level == "hard":
        live = 4
        guess_checker(live)

def play_game():
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()
    play_around(difficulty_level)
    while choice_to_pay() == "y":
        difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()
        play_around(difficulty_level)
    print("\nThank you for playing my Guessing Game!")

play_game()