# Write your code here
import random

def welcome():
    welcome_message = ''
    while welcome_message not in ('play', 'exit'):
        welcome_message = input('Type "play" to play the game, "exit" to quit: ')
    return welcome_message

def play_game():
    list_of_choices = ['python', 'java', 'kotlin', 'javascript']
    choice = random.choice(list_of_choices)
    output = list("-" * len(choice))
    lives = 8
    already_tried = []

    while output != list(choice):
        if lives == 0:
            print("You lost!")
            break
        else:
            print()
            print("".join(output))
            letter = input("Input a letter:")
            if letter in already_tried:
                print("You've already guessed this letter")
            elif letter in choice:
                already_tried.append(letter)
                for i in range(len(choice)):
                    if choice[i] == letter:
                        output[i] = letter
            elif len(letter) != 1:
                print("You should input a single letter")
            elif letter not in "abcdefghijklmnopqrstuvwxyz":
                print("Please enter a lowercase English letter")
            else:
                print("That letter doesn't appear in the word")
                already_tried.append(letter)
                lives -= 1
    else:
        print("You guessed the word!")
        print("You survived!")

print("H A N G M A N")

while True:
    player_choice = welcome()
    if player_choice == "play":
        play_game()
    else:
        break
