# Name:     Matthew Stasinowsky
# Student Number:  10471721

# This file is provided to you as a starting point for the "word_game.py" program of Assignment 1
# of Programming Principles in Semester 1, 2021.  It mainly provides you with a suitable list of words.
# Please use this file as the basis for your assignment work.  You are not required to reference it.



# Import the random module to allow us to select the word list and password at random.
import random



# This function receives two words as parameters and returns the number of matching letters between them.
# See the assignment brief for details of this function's requirements.
def compare_words(word_1, word_2):
    letters = 0
    for index in range(len(word_1)):
        # Compare each letter one by one using index (position).
        if word_1[index] == word_2[index]:
            # Increase 'letters' everytime there's a match.
            letters += 1
    return letters



# This function receives a promt (the users guess) and checks to see if it is valid (an integer and inbetween the guess range).
# An error message is printed with the reason for rejection. 
def input_int(prompt, minValue = 1, maxValue = None):
    while True:
        # Prompt the user for their guess.
        guess = input(prompt)
        
        # Try make the user's guess an integar
        try:
            int_guess = int(guess)

        # If it is NOT an integer then display error message.
        except ValueError:
            print('Invalid input - Try again with an integer.')
            continue

        # If the guess is outside of the word_list's range display error message.
        if int_guess > maxValue or int_guess < minValue:
            print('Invalid input - Try again, must be between 1 and', str(len(word_list)),'.')
            continue

        return int_guess



# Create a list of 100 words that are similar enough to work well for this game.
candidate_words = ['AETHER', 'BADGED', 'BALDER', 'BANDED', 'BANTER', 'BARBER', 'BASHER', 'BATHED', 'BATHER', 'BEAMED', 'BEANED', 'BEAVER', 'BECKET', 'BEDDER', 'BEDELL', 'BEDRID', 'BEEPER', 'BEGGAR', 'BEGGED', 'BELIES', 'BELLES', 'BENDED', 'BENDEE', 'BETTER', 'BLAMER', 'BLOWER', 'BOBBER', 'BOLDER', 'BOLTER', 'BOMBER', 'BOOKER', 'BOPPER', 'BORDER', 'BOSKER', 'BOTHER', 'BOWYER', 'BRACER', 'BUDGER', 'BUMPER', 'BUSHER', 'BUSIER', 'CEILER', 'DEADEN', 'DEAFER', 'DEARER', 'DELVER', 'DENSER', 'DEXTER', 'EVADER', 'GELDED', 'GELDER', 'HEARER', 'HEIFER', 'HERDER', 'HIDDEN', 'JESTER', 'JUDDER', 'KIDDED', 'KIDDER', 'LEANER', 'LEAPER', 'LEASER', 'LEVIED', 'LEVIER', 'LEVIES', 'LIDDED', 'MADDER', 'MEANER', 'MENDER', 'MINDER', 'NEATER', 'NEEDED', 'NESTER', 'PENNER', 'PERTER', 'PEWTER', 'PODDED', 'PONDER', 'RADDED', 'REALER', 'REAVER', 'REEDED', 'REIVER', 'RELIER', 'RENDER', 'SEARER', 'SEDGES', 'SEEDED', 'SEISER', 'SETTER', 'SIDDUR', 'TENNER', 'TEMPER', 'TENDER', 'TERMER', 'VENDER', 'WEDDED', 'WEEDED', 'WELDED', 'YONDER']



# Print Welcoming message
print('Welcome to the guessing password game!\n')


# Loop through until a valid 'difficulty' has been inputed.
# 'word_list' length and the 'remaining_guesses' amount change respectivley. 
while True:
    # Get 'difficulty'
    difficulty = input('Choose [e]asy, [m]edium or [h]ard: ')

    if difficulty == 'e':
        print('Easy difficulty selected.')
        num_words = 7
        word_list = random.sample(candidate_words, num_words)
        guesses_remaining = 5
        break

    elif difficulty == 'm':
        print('Medium difficulty selected.')
        num_words = 8
        word_list = random.sample(candidate_words, num_words)
        guesses_remaining = 4
        break

    elif difficulty == 'h':
        print('Hard difficulty selected.')
        num_words = 9
        word_list = random.sample(candidate_words, num_words)       
        guesses_remaining = 3
        break

    else:
        print('\nInvlaid choice, enter "e", "m" or "h".')



# Declare and set 'won' bool to False
won = False

# Set the password to a random word in the list
password = random.choice(word_list)

# Set the original guesses amount
# (Used to see if the user guessed correctly on their first attempt)
guesses_amount = guesses_remaining


while guesses_remaining > 0 and won == False:
    # Inform the player that one of the words is the password.
    print('\nThe Password is one of these words: ')

    # Print each item (word) in the list, and its index in the list.
    for index, word in enumerate(word_list): 
        print(index + 1,')',word)

    # Show remaining guesses.
    print('\nGuesses remaining: ', str(guesses_remaining))

    # Prompts user for their guess and
    # runs it through the 'input_int' function to make sure it is valid (an integer and inbetween the guess range)
    guess = input_int(('Guess (enter 1-' + str(len(word_list)) + '): '), 1, len(word_list))

    # Convert to string and display corresponding word to user's guess.
    guessed_word = (str(word_list[guess - 1]))
    print('\n',guessed_word)

    # If the user DIDNT guess the password.
    if guessed_word != password:
        print('Incorrect password.')

        # Compare words (password and guessed word).
        letters_in_common = compare_words(password, guessed_word)
        
        # Display letters in common
        print (letters_in_common,'/',len(password),'letter(s) correct')

        # Redeuce remaining guesses by 1.
        guesses_remaining = guesses_remaining - 1


    # Otherwise if the user guessed correctly 'won' is set to true.
    else:
        won = True



# If the user won.
if won == True:
    print('Password correct!')
    print('\nCongrats! You guessed the password! You win!')
    wait = input("Press Enter to close.")
    
    # If the user guessed correctly on their first go.
    if guesses_remaining == guesses_amount:
        print('Lucky guess!')
        wait = input("Press Enter to close.")


# If the user lost.
else:
    print('You lose...')
    print('The Password was: ',password)
    wait = input("Press Enter to close.")


    



    




