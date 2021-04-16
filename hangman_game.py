import random, os

# Words database list
words_db = []

# call the functions 
from functions import get_database
from functions import normalize_character

# call the ascii
from ascii_art import *

def main():
    os.system("clear")
    print(welcome)
    score = 100
    score_flag = 1
    words_db = get_database() # words database read

    #  Random word selection based on the database length
    word_number = random.randint(1, len(words_db))
    word_select = words_db[word_number]
    word_select = word_select[:-1] # Remove the last character "\n"
    word_select_list = [i_letter for i_letter in word_select] # Word selected as list mode
    word_select_list_orig = [i_letter for i_letter in word_select] # Word selected as list mode without normalize

    # Normalize each character, remove the accents
    n = 0
    for i_character in word_select_list:
        if i_character != "ñ":
            word_select_list[n] = normalize_character(i_character)
        else:
            word_select_list[n] = i_character
        n += 1

    # Word to user complete "_ _ _ _ _ _ _"
    word_building = []
    for j in range(1, len(word_select)+1):
        word_building.insert(j, "_")

    print(*word_building)    # First print

    while True:
        n_input = input("Enter a letter: ")
        assert len(n_input) == 1, "Press just one character."
        os.system("clear")
        i = 0
        
        for n_letter in range(0, len(word_select)):
            if n_input == word_select_list[n_letter]:
                word_building[n_letter] = word_select_list_orig[n_letter]
                score_flag = 0
            
        if score_flag:
            score -= 1 
        
        if word_building.count("_") == 0:
            break
        
        print(welcome)
        print(*word_building)
        print("Score: ", score)
        i += 1
        score_flag = 1
    print(welcome)
    print(won)
    print("The word was: ", word_select)
    print("Your score is: ", score)


if __name__ == "__main__":
    main()
