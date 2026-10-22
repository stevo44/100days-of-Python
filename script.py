import random as rnd
import note
# print("hello world")

# fr = rnd.randint(1,10)
# for i in range(fr):
#   print("Good Day")
# print(note.name)
#
# randomFloat = rnd.random() * 5
# print(randomFloat)

randomDecision = rnd.randint(0, 1)

# is randomDecision == 1 ? print("Heads") : print("Tails")

# if randomDecision == 0:
#     print("Tails")
# else:
#     print("Heads")

print("Heads" if randomDecision == 1 else "Tails")

fruits = ["cherry", "apple", "Pear"]

states_by_admission = [
    "Delaware",         # 1  - Dec 7, 1787
    "Pennsylvania",     # 2  - Dec 12, 1787
    "New Jersey",       # 3  - Dec 18, 1787
    "Georgia",          # 4  - Jan 2, 1788
    "Connecticut",      # 5  - Jan 9, 1788
    "Massachusetts",    # 6  - Feb 6, 1788
    "Maryland",         # 7  - Apr 28, 1788
    "South Carolina",   # 8  - May 23, 1788
    "New Hampshire",    # 9  - Jun 21, 1788
    "Virginia",         # 10 - Jun 25, 1788
    "New York",         # 11 - Jul 26, 1788
    "North Carolina",   # 12 - Nov 21, 1789
    "Rhode Island",     # 13 - May 29, 1790
    "Vermont",          # 14 - Mar 4, 1791
    "Kentucky",         # 15 - Jun 1, 1792
    "Tennessee",        # 16 - Jun 1, 1796
    "Ohio",             # 17 - Mar 1, 1803
    "Louisiana",        # 18 - Apr 30, 1812
    "Indiana",          # 19 - Dec 11, 1816
    "Mississippi",      # 20 - Dec 10, 1817
    "Illinois",         # 21 - Dec 3, 1818
    "Alabama",          # 22 - Dec 14, 1819
    "Maine",            # 23 - Mar 15, 1820
    "Missouri",         # 24 - Aug 10, 1821
    "Arkansas",         # 25 - Jun 15, 1836
    "Michigan",         # 26 - Jan 26, 1837
    "Florida",          # 27 - Mar 3, 1845
    "Texas",            # 28 - Dec 29, 1845
    "Iowa",             # 29 - Dec 28, 1846
    "Wisconsin",        # 30 - May 29, 1848
    "California",       # 31 - Sep 9, 1850
    "Minnesota",        # 32 - May 11, 1858
    "Oregon",           # 33 - Feb 14, 1859
    "Kansas",           # 34 - Jan 29, 1861
    "West Virginia",    # 35 - Jun 20, 1863
    "Nevada",           # 36 - Oct 31, 1864
    "Nebraska",         # 37 - Mar 1, 1867
    "Colorado",         # 38 - Aug 1, 1876
    "North Dakota",     # 39 - Nov 2, 1889
    "South Dakota",     # 40 - Nov 2, 1889
    "Montana",          # 41 - Nov 8, 1889
    "Washington",       # 42 - Nov 11, 1889
    "Idaho",            # 43 - Jul 3, 1890
    "Wyoming",          # 44 - Jul 10, 1890
    "Utah",             # 45 - Jan 4, 1896
    "Oklahoma",         # 46 - Nov 16, 1907
    "New Mexico",       # 47 - Jan 6, 1912
    "Arizona",          # 48 - Feb 14, 1912
    "Alaska",           # 49 - Jan 3, 1959
    "Hawaii",           # 50 - Aug 21, 1959
]

# num = int(input("Enter a number from 1 to 50:\n"))
# # print(f"In the order of entry in the union of the us {states_by_admission[num - 1]} was state number {num} to enter the union")
#
# names = input("Enter the names of your friends( separated by space and comma): ")
# splitName = names.split(", ")
#
# randSelector  = rnd.randint(0, len(splitName) - 1)
# print(f"{splitName[randSelector]} Will Pay for the Food {len(splitName)}")

row1 = ["🎴","🎴","🎴"]
row2 = ["🎴","🎴","🎴"]
row3 = ["🎴","🎴","🎴"]

# maps = [row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("where do you want to put your Treasure?: ")
# splitPosition = [position[0], position[1]]
# print(splitPosition)

# row = int(position[0]) - 1
# column = int(position[1]) - 1
# print(row, column)
# maps[column][row] = "X"
# print(f"{row1}\n{row2}\n{row3}")


# option = int(input("what do you choose? Type 0 for Rock, 1 for Paper 0r 2 for Scissor: "))
# optionList = ["Rock", "Paper", "Scissor"]
# computerOption = rnd.randint(0, 2)
# # computerOption = 2
# print(f"You chose {optionList[option]}\n")
# print(f"The computer chose {optionList[computerOption]}\n")
# if (option == 0 and computerOption == 2) or (option == 1 and computerOption == 0) or (option == 2 and computerOption == 1):
#     print(f"You Win, {optionList[option]} Bits {optionList[computerOption]}")
# elif (computerOption == 0 and option == 2) or (computerOption == 1 and option == 0) or (computerOption == 2 and option == 1):
#     print(f"You lose and Computer wins, {optionList[computerOption]} Bits {optionList[option]}")
# if option == computerOption:
#     print("It's a tie")

# import random as rnd

# CHOICES = ("Rock", "Paper", "Scissors")
#
# try:
#     player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
#     if player not in (0, 1, 2):
#         raise ValueError
# except ValueError:
#     print("Invalid choice. Please enter 0, 1 or 2.")
# else:
#     computer = rnd.randint(0, 2)
#
#     print(f"You chose {CHOICES[player]}")
#     print(f"The computer chose {CHOICES[computer]}\n")
#
#     result = (player - computer) % 3
#
#     if result == 0:
#         print("It's a tie")
#     elif result == 1:
#         print(f"You win! {CHOICES[player]} beats {CHOICES[computer]}")
#     else:
#         print(f"You lose! {CHOICES[computer]} beats {CHOICES[player]}")


# fruits = ["apple", "pear", "mango"]
#
# for i in fruits:
#     print(i)
#     print(f"{i} pie")

# student_heights = input("Enter your student height: ").split()
# sum = 0
# count = 0
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
#     sum += student_heights[n]
#     count += 1
# print(student_heights)
# print(f"The total high of the Students is {sum} with an Average of {round(sum/count)}")
# hightest = 0
# student_score = input("Enter your score: ").split()
# for n in range(0, len(student_score)):
#     student_score[n] = int(student_score[n])
#     if student_score[n] > hightest:
#         hightest = student_score[n]
# print(f"The highest score in class is: {hightest}")

# total = 0
# for n in range(2, 101, 2):
#     total += n
# print(total)
# total = 0
# for n in range(1, 101):
#     if n % 2 == 0:
#       total += n
# print(total)

# for n in range(1, 101):
#     if n % 3 == 0 and n % 5 == 0:
#       print("FIZZ BUZZ")
#     elif n % 3 == 0:
#       print("FIZZ")
#     elif n % 5 == 0:
#       print("BUZZ")
#     else:
#       print(n)

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# numbers = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+']
#
# print("Welcome to pyPassword Generator!")
# num_letters = int(input("How many letters would you like? "))
# num_numbers = int(input("How many numbers would you like? "))
# num_symbols = int(input("How many symbols would you like? "))
#
#
# psd = ""
# password = []
# for n in range(0, num_letters):
#     psd += rnd.choice(letters)
#     password+= rnd.choice(letters)
# for n in range(0, num_numbers):
#     psd += rnd.choice(numbers)
#     password+= rnd.choice(numbers)
# for n in range(0, num_symbols):
#     psd += rnd.choice(symbol)
#     password+= rnd.choice(symbol)
# rnd.shuffle(password)
# print(psd)
# # print(password)
# shufflePassword = ''.join(password)
# print(shufflePassword)


# def my_fuction(year):
#     age = 2026 - int(year)
#     print(f"you are {age} years old")
#
#
# my_fuction(2000 )

HANGMAN_PICS = [r"""
  +--+
  |  |
     |
     |
     |
     |
 =====""",
r"""
  +--+
  |  |
  O  |
     |
     |
     |
 =====""",
r"""
  +--+
  |  |
  O  |
  |  |
     |
     |
 =====""",
 r"""
  +--+
  |  |
  O  |
 /|  |
     |
     |
 =====""",
 r"""
  +--+
  |  |
  O  |
 /|\ |
     |
     |
 =====""",
 r"""
  +--+
  |  |
  O  |
 /|\ |
 /   |
     |
 =====""",
 r"""
  +--+
  |  |
  O  |
 /|\ |
 / \ |
     |
 ====="""]

import hangman_words as hw
import hangman_art as ha

print(ha.logo)
chosen_word = rnd.choice(hw.word_list)

displayDash = []
lives = 6
hang = 0

for n in range(len(chosen_word)):
 displayDash += "_"
 # displayDash.append(chosen_word[n])
# status = " ".join(displayDash)
guess = input("Guess the letter: ").lower()
for n in range(len(chosen_word)):
    if guess == chosen_word[n]:
        displayDash[n] = chosen_word[n]
        print("".join(displayDash))
print(HANGMAN_PICS[hang])

# if guess in displayDash:
#     print(f"You already guessed the letter {guess}!")
if guess not in chosen_word and guess not in displayDash:
    lives -= 1
    hang += 1
    print(f"You guessed the letter {guess}, That's not in the word! You lose a live and you got {lives} more left\n")
    print("".join(displayDash))
    print(HANGMAN_PICS[hang])

end_game = False

while not end_game:
    guess = input("Guess the letter: ").lower()
    for n in range(len(chosen_word)):
        if guess == chosen_word[n]:
            displayDash[n] = chosen_word[n]
    print("".join(displayDash))
    print(HANGMAN_PICS[hang])
    if guess in displayDash:
        print(f"You already guessed the letter {guess}!")
    if guess not in chosen_word and guess not in displayDash:
        lives -= 1
        hang += 1
        print(f"You guessed the letter {guess}, That's not in the word! You lose a live and you got {lives} more left\n")
        print("".join(displayDash))
        print(HANGMAN_PICS[hang])

    if "_" not in displayDash:
      end_game = True
      print("You win!")
    elif "_" in displayDash and lives == 0:
      end_game = True
      print("You lose!")

