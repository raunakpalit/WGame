
import random
from word_exists import WordLibrary
# from word_refinement import WordRefine as word_refine

# word_library = ['Abuse', 'Anger', 'Beach', 'Birth', 'Chief', 'Maker', 'Lynch', 'Snake', 'Evade']

class SelectWord(WordLibrary):
    def __init__(self):
        self.word_library = WordLibrary()
        # WordLibrary.open_file(self)
        # self.word_library = ['Abuse', 'Anger', 'Beach', 'Birth', 'Chief', 'Maker', 'Lynch', 'Snake', 'Evade']
        
    def selected_word(self):
        # open_the_file = self.word_library.open_file()
        random_word = self.word_library.select_a_random_word()
        # print("Word is: {}".format(random_word))
        # return random_word
        return "treat"
        
        # return self.select_a_random_word()
        # return random.choice(self.word_library)
    

class InputWord(SelectWord):
    def __init__(self):
        super().__init__()
        # self.input_word = input_word
        self.input_word = None
        self.sel_word = self.selected_word()
        self.attempts = 6

        self.letter_list = ['?', '?', '?', '?', '?']
        self.matched_characters = []
        self.unmatched_characters = []
        self.indexmatchdict = {}
        self.gcharacter = None
        self.gcharacter_index = None
        self.character_index = None
        
    def split_and_check_each_character(self):
        print("Input word is: {}".format(self.input_word))
        # print("Selected word is: {}".format(self.sel_word))
        
        #Wrap the code for indices=============
        selected_word = self.sel_word
        input_word = self.input_word
        
        
        # =====================================
        for character in self.input_word:
            if character in self.sel_word:
                character_index = self.input_word.index(character)
                if character_index == self.sel_word.index(character):
                    print("Indexing of character {} is correct in {} position".format(character, self.sel_word.index(character)))
                    self.gcharacter = character
                    self.gcharacter_index = self.sel_word.index(character)
                    self.indexmatchdict[character] = self.sel_word.index(character)
                    # self.print_the_word(character, character_index)
                else:
                    print("Character found. Indexing of character {} incorrect".format(character))
                if character not in self.matched_characters:
                    self.matched_characters.append(character)
            else:
                if character not in self.unmatched_characters:
                    self.unmatched_characters.append(character)
        self.print_the_word(self.gcharacter, self.gcharacter_index)
        print("Matched Characters: {}".format(self.matched_characters))
        print("Unmatched Characters: {}".format(self.unmatched_characters))
        
        
    def print_the_word(self, letter, letter_index):
        # print("Dict: {}".format(self.indexmatchdict))
        # print("letter: {}".format(letter))
        # print("letter_index: {}".format(letter_index))
        for chars in self.indexmatchdict:
            self.letter_list[self.indexmatchdict[chars]] = chars
        guessed_word = "".join(self.letter_list)
        print("The word guessed so far: {}".format(guessed_word))
 
        
    def check_word_length(func):
        def wrapper(self):
            length_of_iword = len(self.input_word)
            if length_of_iword != 5:
                print("The length of input word is incorrect. Kindly input a 5 character word")
            else:
                print("Length correct for the input word")
                return func(self)
        return wrapper
   
            
    def check_word_valid(func):
        def wrapper(self):
            word_library = WordLibrary()
            if word_library.validate_word(self.input_word):
                print("Valid Word. Go ahead")
                return func(self)
            else:
                print("Invalid word in decorator")
        return wrapper


    
    @check_word_length
    @check_word_valid
    def check_word_match(self):
        self.input_word = self.input_word.lower()
        self.sel_word = self.sel_word.lower()
        print("Iword is: {}".format(self.input_word))
        # print("Sword is: {}".format(self.sel_word))
        if self.input_word == self.sel_word:
            print("Bingo! Word Matched. Word is {}".format(self.sel_word))
            return "Matched"
        else:
            print("Word did not match")
            self.split_and_check_each_character()
            # refinement = word_refine(iword, sword)
            # refinement.split_and_check_each_character()
            return "Nomatch"

    
    def tries(self):
        while self.attempts != 0:
            uinput = self.user_input_for_word()
            self.input_word = uinput
            tryme = self.check_word_match()
            if tryme == "Matched":
                break
            elif tryme == "Nomatch":
                self.attempts -= 1
                print("Attempts left: {}".format(self.attempts))
                print("=" * 80)
            else:
                print("Current attempt retained.")
                print("Attempts left: {}".format(self.attempts))
                print("=" * 80)
            if self.attempts == 0:
                print("Oops! You lost the game.\nAll 6 attempts exhausted")
                print("The five letter word was: {}".format(self.sel_word))


    def user_input_for_word(self):
        user_input = input("Guess the five letter word: \n")
        return user_input
            

a = InputWord()
a.tries()
