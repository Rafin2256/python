import random  # Import random to pick a word randomly

# Step 1: Pick a random word
def get_word():
    """
    Chooses a random word from a list.
    """
    words = ['python', 'programming', 'developer', 'algorithm', 'variable', 'debugging']
    return random.choice(words)  # Randomly pick one word from the list

# Step 2: Show the player's remaining lives
def display_lives(lives):
    """
    Shows lives as stars (*) for lives left and underscores (_) for lives lost.
    """
    max_lives = 6  # Total lives
    life_display = "* " * lives + "_ " * (max_lives - lives)  # Visual for lives
    print(f"Lives Remaining: {life_display}")  # Print the visual

# Step 3: Play the game
def play_game(word, guessed_letters=None, lives=6):
    """
    The main game logic. Keeps running until the player wins or loses.
    """
    if guessed_letters is None:  # If no guesses yet, start with an empty set
        guessed_letters = set()

    # Show lives and the word with blanks
    display_lives(lives)
    word_display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print(f"\nWord: {word_display}")  # Show the word progress
    print(f"Guessed letters: {sorted(guessed_letters)}")  # Show guessed letters

    # Step 4: Check if the game is over
    if word_display == word:  # All letters guessed correctly
        print(f"\nCongratulations! You won with {lives} lives left!")
        return
    if lives == 0:  # No lives left
        print("\nGame Over! No more lives remaining.")
        print(f"The word was: {word}")
        return

    # Step 5: Ask the player for a guess
    guess = input("\nEnter a letter: ").lower()  # Get input and make it lowercase

    # Step 6: Check if the guess is valid
    if len(guess) != 1 or not guess.isalpha():  # Input should be one letter
        print("\nPlease enter a single letter!")
        return play_game(word, guessed_letters, lives)  # Retry
    if guess in guessed_letters:  # Check if letter was already guessed
        print("\nYou already guessed that letter!")
        return play_game(word, guessed_letters, lives)  # Retry

    # Add the guessed letter to the set
    guessed_letters.add(guess)

    # Step 7: Check if the guess is correct
    if guess in word:
        print("\nCorrect guess!")  # If correct, continue the game
        return play_game(word, guessed_letters, lives)
    else:
        print("\nIncorrect guess! You lost a life!")  # If wrong, lose a life
        return play_game(word, guessed_letters, lives - 1)

# Step 8: Start the game
print("Welcome to the Word Guessing Game!")
print("Save your lives by guessing the word correctly!")
word = get_word()  # Pick a random word
play_game(word)  # Start the game
