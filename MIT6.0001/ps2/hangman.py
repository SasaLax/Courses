# Problem Set 2, hangman.py
# Name: Sasa Lakic
# Collaborators: no one
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for c in secret_word:
      if(c not in letters_guessed):
        return False
    return True




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = ""
    for c in secret_word:
      if(c in letters_guessed):
        guessed_word += c
      else:
        guessed_word += "_ "
    return guessed_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = string.ascii_lowercase
    available_letters = ""
    for c in alphabet:
      if c not in letters_guessed:
          available_letters += c
    return available_letters
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    guessed_letters = []
    num_of_guesses = 6
    warnings = 3
    check_word = False
    
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {warnings} warnings left.")

    while(check_word == False and num_of_guesses != 0):
      available_letters = get_available_letters(guessed_letters)
      print("==============")
      print(f"You have {num_of_guesses} guesses left")
      print(f"Available letters: {available_letters}")
      guessed_letter = input("Please guess a letter: ")
      
      if not(guessed_letter.isalpha()):
        guessed_word = get_guessed_word(secret_word, guessed_letters)
        if(warnings > 0):
          warnings -= 1
          print(f"Oops! That is not a valid letter. You have {warnings} warnings left: {guessed_word}")
        else:
          print(f"Oops! That is not a valid letter. You have no warnings left so you lose one guess: {guessed_word}")
          num_of_guesses -= 1
      elif(guessed_letter in guessed_letters):
        guessed_word = get_guessed_word(secret_word, guessed_letters)
        if(warnings > 0):
          warnings -= 1
          print(f"Oops! You've already guessed that letter. You have {warnings} warnings left: {guessed_word}")
        else:
          print(f"Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {guessed_word}")
          num_of_guesses -= 1
      elif(guessed_letter not in secret_word):
        guessed_letters.append(guessed_letter.lower())
        print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, guessed_letters)}")
        if(guessed_letter in "aeiou"):
          if(num_of_guesses > 1):
            num_of_guesses -= 2
          else:
            num_of_guesses -= 1
        else:
          num_of_guesses -= 1
      elif(guessed_letter in secret_word):
        guessed_letters.append(guessed_letter.lower())
        print(f"Good guess: {get_guessed_word(secret_word, guessed_letters)}")

      check_word = is_word_guessed(secret_word, guessed_letters)

    print("==============")
    if(num_of_guesses == 0):
      print(f"Sorry, you ran out of guesses. The word was {secret_word}\n")
    else:
      set_letters = set()
      for c in secret_word:
        set_letters.add(c)
      num_of_unique = len(set_letters)
      total_score = num_of_guesses * num_of_unique
      print("Congratulations, you won!")
      print(f"Your total score for this game is: {total_score}\n")

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word_without_spaces = my_word.replace(" ", "")
    
    length_my_word = len(my_word_without_spaces)
    length_other_word = len(other_word)
    if(length_my_word != length_other_word):
        return False
    else:
      for i in range(length_other_word):
          if(my_word_without_spaces[i] == "_"):
            for c in my_word_without_spaces:
                if(c == other_word[i]):
                  return False
          elif(my_word_without_spaces[i] != other_word[i]):
            return False
          
    return True
         
        
       



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for word in wordlist:
      if(match_with_gaps(my_word, word)):
         print(f"{word} ", end = "")
    print("")
        



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word = "apple"
    
    guessed_letters = []
    num_of_guesses = 6
    warnings = 3
    check_word = False
    
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {warnings} warnings left.")

    while(check_word == False and num_of_guesses != 0):
      available_letters = get_available_letters(guessed_letters)
      print("==============")
      print(f"You have {num_of_guesses} guesses left")
      print(f"Available letters: {available_letters}")
      guessed_letter = input("Please guess a letter: ")
      
      if(guessed_letter == "*"):
        show_possible_matches(get_guessed_word(secret_word, guessed_letters))
      elif not(guessed_letter.isalpha()):
        guessed_word = get_guessed_word(secret_word, guessed_letters)
        if(warnings > 0):
          warnings -= 1
          print(f"Oops! That is not a valid letter. You have {warnings} warnings left: {guessed_word}")
        else:
          print(f"Oops! That is not a valid letter. You have no warnings left so you lose one guess: {guessed_word}")
          num_of_guesses -= 1
      elif(guessed_letter in guessed_letters):
        guessed_word = get_guessed_word(secret_word, guessed_letters)
        if(warnings > 0):
          warnings -= 1
          print(f"Oops! You've already guessed that letter. You have {warnings} warnings left: {guessed_word}")
        else:
          print(f"Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {guessed_word}")
          num_of_guesses -= 1
      elif(guessed_letter not in secret_word):
        guessed_letters.append(guessed_letter.lower())
        print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, guessed_letters)}")
        if(guessed_letter in "aeiou"):
          if(num_of_guesses > 1):
            num_of_guesses -= 2
          else:
            num_of_guesses -= 1
        else:
          num_of_guesses -= 1
      elif(guessed_letter in secret_word):
        guessed_letters.append(guessed_letter.lower())
        print(f"Good guess: {get_guessed_word(secret_word, guessed_letters)}")

      check_word = is_word_guessed(secret_word, guessed_letters)

    print("==============")
    if(num_of_guesses == 0):
      print(f"Sorry, you ran out of guesses. The word was {secret_word}\n")
    else:
      set_letters = set()
      for c in secret_word:
        set_letters.add(c)
      num_of_unique = len(set_letters)
      total_score = num_of_guesses * num_of_unique
      print("Congratulations, you won!")
      print(f"Your total score for this game is: {total_score}\n")




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
