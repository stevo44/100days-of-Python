######################DEBUGGING###########################

#Describe the Problem
def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it!")
my_function()

#Solution
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it!")
# my_function()

# Reproduce the Bug
from random import randint
dice_image = ["😊", "😂", "🤣", "😍", "😒", "😘"]
# dice_num = randint(1, 6)
# print(dice_image[dice_num])

#Solution
dice_num = randint(0, 5)
# print(dice_image[dice_num])

#Playing Computer
# year = int(input("Enter your birth year?: "))
# if year > 1988 and year < 1994:
#     print("You're a millennial")
# elif year > 1994:
#     print("You're a Gen-Z.")

#Correction
# if year > 1988 and year <= 1994:
#     print("You're a millennial")
# elif year > 1994:
#     print("You're a Gen-Z.")

#debugging from error throw the console
# age = input("How old are you? ")
# if age > 18:
#     print(f"You can drive at age {age}")

#soluton
# age = int(input("How old are you? "))
# if age > 18:
#     print(f"You can drive at age {age}")

#Debugging with print
pages = 0
word_per_page = 0
# pages = int(input("Number of pages: ? "))
# word_per_page == int(input("Word per page: ? "))
# total_pages = pages * word_per_page
# print(total_pages)

#solution
# ages = int(input("Number of pages: ? "))
# word_per_page = int(input("Word per page: ? "))
# total_pages = pages * word_per_page
# print(f"pages: {pages}, words: {word_per_page}")
# print(total_pages)

#use the Debugger

# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)
#
# mutate([1,2,3,5,8,13])

#Debugging Challenge
# number = int(input("Enter a number: "))
#
# if number % 2 == 0:
#     print("You enter an even number!")
# else:
#     print("You enter an odd number!")

# year = int(input("which year do you wanna check?: "))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("leap year")
#         else:
#             print("not a leap year")
#     else:
#         print("leap year")
# else:
#     print("not a leap year")


for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)