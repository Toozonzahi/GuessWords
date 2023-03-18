# Description of the game --> It's a guessing game.
# The player needs to guess the words to win the game.
import random

def get_player_name():
   name = input(' What Is Your Name : ')   # The player need to enter his name
   print(' Starting The Game', name)   # Message of starting the game + player name

print(get_player_name())

guess_words = [
    ['always', 'be', 'yourself'],
    ['keep', 'it', 'cool'],
    ['act', 'as', 'if'],
    ['all', 'is', 'well'],
    ['be', 'here', 'now'],
    ['be', 'the', 'change'],
    ['cash', 'is', 'king'],
    ['do', 'it', 'now'],
    ['go', 'for', 'it'],
    ['let', 'it', 'go']
]   # List of guessing words

phrase = random.choice(guess_words)  # Random from the list
underscores = ['_ ' * len(word) for word in phrase]     # Build a parallel list with underscores
display = '_ '.join(underscores)      # Join the underscores for display
guessed_letters = set()     # Keep of guessed letters
score = 0       # Scoring

while True:
    letter = input("Guess a letter: ").lower()      # Ask the player for guessing a letter, the letter be lower
    guessed_letters.add(letter)     # Add the letter to the guessed set
    found = False       # Check if the letter is in the phrase
    for i, word in enumerate(phrase):
        for j, char in enumerate(word):
            if char == letter:      # Replace the underscore with the letter
                underscores[i] = underscores[i][:j * 2] + letter + underscores[i][j * 2 + 1:]
                found = True
    if found:
        print(f"Good guess! The phrase is now:\n{''.join(underscores)}\n")
        score += 5  # Add 5 points for correct guess
    else:
        print(f"Sorry, the letter '{letter}' is not in the phrase.\n{''.join(underscores)}\n")
        score -= 1  # Deduct 1 point for wrong guess

    # Check if the player has guessed all the letters
    if ''.join(underscores).replace(' ', '') == ''.join(phrase):
        print("Congratulations, you guessed the phrase!")
        print(f"Your score is {score}")  # Display final score
        break
