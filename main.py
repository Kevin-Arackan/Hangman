import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)

correct_guesses = []
incorrect_guesses = []

chosen_word = random.choice(word_list)

display = ""
for char in chosen_word:
    display += "_"
print(display)


while "_" in display and lives > 0:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    
    lose_life = True
    
    print(f"Incorrect guesses: {incorrect_guesses}")

    guess = input("Guess a letter: ").lower()

    placeholder = list(display)

    if guess in correct_guesses or guess in incorrect_guesses:
        lose_life = False
        print("You have already guessed that letter.\nTry a different one.")

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            placeholder[i] = guess
            lose_life = False


    if lose_life:
        print(f"The letter '{guess}' is not in the word. You lose a life.")
        lives -= 1
        incorrect_guesses.append(guess)
    else:
        correct_guesses.append(guess)

    display = "".join(placeholder)

    print(f"{stages[lives]}\n{display}")


if lives == 0:
    print(f"************The correct word was '{chosen_word}'!************")
    print("***********************YOU LOSE**********************")
else:
    print("****************************YOU WIN****************************")