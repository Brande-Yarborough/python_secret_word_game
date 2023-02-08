import random

print("Let's play Hangman!")

words = ["javascript", "html", "css", "bootstrap", "react", "python"]
secretWord = random.choice(words)
lettersGuessed = ""
# number of guesses before player loses
guesses = 6

# loop until player has made too many failed attempts
# will break loop if they succeed instead
while guesses > 0:

    guess = input("Enter a letter: ")

    if guess in secretWord:
        print(f"Correct! There is one or more {guess}'s in the word.")
    else:
        guesses -= 1
        print(
            f"Wrong guess! There are no {guess}'s in the word. {guesses} attempt(s) left.")

    # maintain list of all letters guessed
    lettersGuessed = lettersGuessed + guess
    wrongLetterCount = 0

    # iterate through each letter in secret word
    for letter in secretWord:
        if letter in lettersGuessed:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            # increment wrong letter count by 1 each time guessed wrong
            wrongLetterCount += 1
    # space out print statement so enter a letter is on next line
    print("")

    if wrongLetterCount == 0:
        print(f"Congratulations, You Win! :) The word was: {secretWord}.")
        break

else:
    print("Sorry, you did not win. Try again. :(")
