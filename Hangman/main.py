# imports
import random

from past.builtins import raw_input

import hangman_art
import hangman_words

# declarations
lives = 6
display = []
chosen_word = random.choice(hangman_words.word_list)
print(hangman_art.logo)
# for every letter in the chosen word add a "_" to the display array.
for letter in chosen_word:
    display += "_"

end_of_game = False
# while loop that iterates through all the user attempts and the user guesses until the end of the game.
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(len(chosen_word)):

        if guess == chosen_word[position]:
            display[position] = guess
        if "_" not in display:
            end_of_game = True
            print("You win!")
            break

        elif lives == 0:
            end_of_game = True
            print("You Lose!")
            break
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            end_of_game = True
    # The ASCII art imported from hangman_art.
    print(hangman_art.stages[lives])
    # joining the array into a String
    print(f"{' '.join(display)}")
print(f"The word is {chosen_word}")
raw_input()
