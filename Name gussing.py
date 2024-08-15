import random

name = input("What is your name? ")

print("Good Luck, ", name, "!")

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

print("Guess the characters")

guesses = ''
turns = 12

while turns > 0:
    failed = 0
    display_word = ""

    for char in word:
        if char in guesses:
            display_word += char + " "
        else:
            display_word += "_ "
            failed += 1

    print(display_word.strip())

    if failed == 0:
        print("You Win!")
        print("The word is:", word)
        break

    guess = input("Guess a character: ").lower()

    # Check if the input is a single alphabetical character
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetic character.")
        continue

    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong guess.")
        print(f"You have {turns} more guesses.")

        if turns == 0:
            print("You Lose.")
            print(f"The word was: {word}")
