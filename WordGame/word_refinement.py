


class WordRefine:
    def __init__(self, iword, sword):
        self.input_word = iword
        self.selected_word = sword
        self.letter_list = ['?', '?', '?', '?', '?']
        self.matched_characters = []
        self.unmatched_characters = []
        self.indexmatchdict = {}
        self.gcharacter = None
        self.gcharacter_index = None
        self.character_index = None
        
    
    def split_and_check_each_character(self):
        for character in self.input_word:
            if character in self.selected_word:
                character_index = self.input_word.index(character)
                if character_index == self.selected_word.index(character):
                    print("Indexing of character {} is correct in {} position".format(character, self.selected_word.index(character)))
                    self.gcharacter = character
                    self.gcharacter_index = self.gcharacter_index
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


    def indexing_character(self):
        pass
    
    
    def print_the_word(self, letter, letter_index):
        if letter is not None:
            self.letter_list[letter_index] = letter
        guessed_word = "".join(self.letter_list)
        print("The word guessed so far: {}".format(guessed_word))
    