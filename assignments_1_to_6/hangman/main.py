import random
stages = ["""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
 =========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
 =========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
 =========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
 =========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
 =========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
 =========
""",]
word = ["mango","apple","banana","orange","grapes", "pineapple", "watermelon"]
random_word = random.choice(word)
word_display = ['_']
guess_letters = []
lives = len(stages)-1
print("Welcome to hangman game")
print("Guess the word")

while True:
    print("".join(word_display))
    guess = input("Guess a letter: ").lower()
    if not guess.isalpha() or len(guess) != 1:
        print("Invalid input. Please enter a single letter.\n")
        continue
    if guess in guess_letters:
        print("You already guessed that letter. Try again")
        continue
    guess_letters.append(guess)
    if guess in random_word:
        print(f"Good guess! {guess} is in the word.")
    for index, letter in enumerate(random_word):
        if letter == guess_letters:
                word_display[index] = guess_letters
    else:
        print(f"Sorry, {guess} is not in the word.")
        lives -= 1
    if lives == 0:
            print("You lost! The word was:", random_word)
            break
        