# def greet(name, location):
#     print(f"Hello {name}\nHow is {location} today?")
# # name = input("What is your name?: ")
# # location = input("Where are you from?: ")
#
# # print("\n")
# greet(name = "Stevo", location = "NYC")
# greet( location = "NYC",name = "Stevo")
# import math
#
# h = int(input("Height of wall: "))
# w = int(input("Width of wall: "))
# coverage  = 5
#
# def paint_cal(h, w, c):
#     num_of_cans = (h * w) / c
#     print(f"You need of buy {math.ceil(num_of_cans)} cans of Paints")
#
# paint_cal(h, w, coverage)

import math

# number = int(input("Please input a number: "))

def primeNumberChecker(num):
    if num <= 1 or num % 2 == 0 or num % 3 == 0:
        print(f"{num} it's not a prime number")
    else:
        print(f"{num} it's a prime number")
    if num == 2 or num == 3:
        print(f"{num} it's  a prime number")

# primeNumberChecker(num = number)
def prime_checker(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    if is_prime:
        print(f"{num} it's a prime number")
    else:
        print(f"{num} it's a prime number")


# prime_checker(num = number)



# Ceasar Cyper
alphabets  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
  'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
  's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd',
  'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
  's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Typer 'encode' to encrypt or 'decode' to decrypt:\n")
text = input("Type the message text:\n").lower()
shift = int(input("Type the shift number:\n"))



def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    non_text = ""
    pure_text = ""
    shift_amount = shift_amount % len(alphabets)
    for letter in start_text:
        # non_text_position = ""
        if letter not in alphabets:
            non_text += letter
            # non_text_position.append(start_text.index(letter))
        else:
            pure_text += letter
        # print(non_text_position)
    for letter in pure_text:
        position = 0
        if cipher_direction == 'encode':
            position = alphabets.index(letter) + shift_amount
        elif cipher_direction == 'decode':
            position = alphabets.index(letter) - shift_amount
        else:
            print("Wrong input, Please type 'encode' or 'decode' in the direction field.")
        end_text += alphabets[position]

    print(f"The {cipher_direction}d text is {end_text}{non_text}")


caesar(text, shift, direction)

restart = input("Do still want to continue encryption or decrypt? 'yes' or 'no'\n").lower()
while restart == 'yes':
    direction = input("Typer 'encode' to encrypt or 'decode' to decrypt:\n")
    text = input("Type the message text:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    restart = input("Do still want to continue encryption or decrypt? 'yes' or 'no'\n").lower()
if restart == 'no':
    print("See later")


def encrypt(plain_text, shift_number):
    cipher = ""
    for letter in plain_text:
        position = alphabets.index(letter) + shift_number
        cipher += alphabets[position]
    print(f"The encoded text is {cipher}")


def decrypt(cipher_input, shift_number):
    cipher = ""
    for letter in cipher_input:
        position = alphabets.index(letter) - shift_number
        cipher += alphabets[position]
    print(f"The decoded text is {cipher}")


def encrypt_v1(plain_text, shift_number):
    cipher = ""
    for letter in plain_text:
        for index in range(len(alphabets)):
            if letter == alphabets[index]:
                cipher += alphabets[index + shift_number]
    print(f"The encoded test is {cipher}")









