#Task 4: Closure Practice

#Declare a function called make_hangman() that has one argument called secret_word
def make_hangman(secret_word):

    #Declare an empty array called guesses
    guesses = []

    #Declare a function called hangman_closure() that takes one argument, which should be a letter
    def hangman_closure(letter):
        #each time it is called, the letter should be appended to the guesses array
        guesses.append(letter)

        #The word should be printed out, with underscores substituted for the letters that haven't been guessed
        print_guess = ''.join([char if char in guesses else '_' for char in secret_word])
        print(print_guess)

        #The function should return True if all the letters have been guessed, and False otherwise
        return all(char in guesses for char in secret_word)

    #make_hangman() should return hangman_closure
    return hangman_closure


#Hangman game that uses make_hangman()
if __name__ == "__main__":
    #Use the input() function to prompt for the secret word
    secret = input("Type the secret word: ").lower()

    # Clear the screen by printing newlines (just a simple way to 'hide' the word)
    print("\n" * 50)

    # Create the hangman game function using the closure
    play = make_hangman(secret)

    #Loop while the game is going
    while True:
        #Use the input() function to prompt for each of the guesses, until the full word is guessed
        guess = input("Enter your guess (single letter): ").lower()

        #Guess one letter at a time
        if len(guess) != 1 or not guess.isalpha():
            print("Only enter one letter!")
            continue

        #Check to see if the whole word has been guessed
        complete_guess = play(guess)

        #Break out of the loop if the guess is complete
        if complete_guess:
            print(f"\nYay! The word was '{secret}'. You win!")
            break
