""" This is a word game where there are five blanks to be filled by English charaters to guess a five letter word """

import random

matched_characters = []
unmatched_characters = []
letter_list = ['?', '?', '?', '?', '?']
attempts = 6

word_library = ['Abuse', 'Anger', 'Beach', 'Birth', 'Chief', 'Maker', 'Lynch', 'Snake', 'Evade']

def selected_word():
    # Selects a word from the word library and positions the characters
    result = random.choice(word_library)
    return "treat"

def check_letter_index(ch_index, ch_word):
    pass

def print_the_word(letter, letter_index):
    letter_list[letter_index] = letter
    guessed_word = "".join(letter_list)
    print("The word guessed so far: {}".format(guessed_word))


def split_and_check_each_letter(word, chosen_word):
    # word = word.lower()
    # chosen_word = chosen_word.lower()
    # chosen_word_list = list(chosen_word)
    for character in word:
        if character in chosen_word:
            character_index = word.index(character)
            if character_index == chosen_word.index(character):
                print("Indexing of character {} is correct in {} position".format(character, chosen_word.index(character)))
                print_the_word(character, character_index)
            else:
                print("Character found. Indexing of character {} incorrect".format(character))
            # check_letter_index(character_index, chosen_word)
            if character not in matched_characters:
                matched_characters.append(character)
        else:
            if character not in unmatched_characters:
                unmatched_characters.append(character)
    return matched_characters, unmatched_characters

def check_valid_word():
    pass

def check_word_length(func):
    def wrapper(*args):
        length_of_word = len(*args)
        if length_of_word != 5:
            print("Error in length")
            return "Error in length"
        else:
            print("Length correct")
            return func(*args)
    return wrapper

@check_word_length
def check_word_match(word):
    # This will check if the entered word by user is the matched word or not from the word library. It will return to the user the matched letters and its position
    chosen_word = selected_word()
    word = word.lower()
    chosen_word = chosen_word.lower()
    if word == chosen_word:
        print("Bingo! You got the word: {}".format(chosen_word))
        return "Word Matched" 
    else:
        matched_characters, unmatched_characters = split_and_check_each_letter(word, chosen_word)
        print("Matched Chracters are: {}". format(matched_characters))
        print("Unmatched characters are: {}".format(unmatched_characters))
        return matched_characters


def main():
    # print("You have six attempts to guess a five letter word....")
    # user_input = input("First Attempt: Guess the five letter word: \n") # Chore
    # check_alphabets = check_word_match(user_input)
    attempts = 6
    while attempts != 0:
        user_input = input("Guess the five letter word: \n") # Chore
        check_alphabets = check_word_match(user_input)
        if check_alphabets == "Word Matched":
            break
        elif check_alphabets == "Error in length":
            print("Wrong length of word. Try a word with 5 characters in it")
            print("Attempts left: {}".format(attempts))
        else:
            attempts -= 1
            print("Attempts left: {}".format(attempts))
            
    # user_input2 = input("Second Attempt: ") # Maker
    # check_word_match(user_input2)
    # user_input3 = input("Third Attempt: ") # Lakes
    # check_word_match(user_input3)
    # user_input4 = input("Fourth Attempt: ") # Snake
    # check_word_match(user_input4)
    # user_input5 = input("Fifth Attempt: ") # Moves
    # check_word_match(user_input5)
    # user_input6 = input("Sixth Attempt: ") # Evade
    # check_word_match(user_input6)
    # print("You lost. All six attempts done! :(")
    
if __name__ == '__main__':
    main()
    
    