# Creating the hangman game

import random
from hangman_art import stages, logo
from hangman_words import word_list

lives = 6
chosen_word = random.choice(word_list)

print(logo)

placeholder = ""
word_length = len(chosen_word)

for i in range(word_length):
    placeholder += "_"

print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"************{lives}/6 LIVES LEFT************")
    chosen_letter = input("Guess a letter: ").lower()

    if chosen_letter in correct_letters:
        print(f"You've already guessed {chosen_letter}")

    display = ""

    for i in chosen_word:
        if i == chosen_letter:
            display += i
            correct_letters.append(chosen_letter)
        elif i in correct_letters:
            display += i
        else:
            display += "_"

    print(display)
    
    if chosen_letter not in chosen_word:
        lives -= 1
        print(f"You guessed {chosen_letter}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f'''************THE WORD WAS "{chosen_word}" YOU LOSE.************''')

    if "_" not in display:
        game_over = True
        print("************YOU WIN!************")

    print(stages[lives])