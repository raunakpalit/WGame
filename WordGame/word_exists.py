import os
import random
        
class WordLibrary:
    def __init__(self):
        self.filename = "five_letter_word_list.txt"
        self.filehandle = None
    
    
    def open_file(self):
        if os.path.exists(self.filename):
            self.filehandle = open(self.filename)
            # print("File exists")
            return True
        else:
            print("File does not exist")
            return False
            
    
    def select_a_random_word(self):
        if self.open_file():
            lines = self.filehandle.read().splitlines()
            choice = random.choice(lines)
            return choice
        
    
    def validate_word(self, word):
        if self.open_file():
            contents = self.filehandle.read().lower()
            if word.lower() in contents:
                return True
            else:
                return False
                
# obj = WordLibrary()
# obj.validate_word("Laura")
