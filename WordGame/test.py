# def my_decorator(func):
#     def wrapper(*args):
#         print(*args)
#         print("Something is happening before the function is called.")
#         func(*args)
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_whee(name):
#     print("Whee!")
#     print(name)

# # say_whee = my_decorator(say_whee)
# say_whee("Raunak")
input_word = "Maker"
sel_word = "Maker"

def check_word_length(func):
    def wrapper():
        length_of_iword = len(input_word)
        if length_of_iword != 5:
            print("The length of input word is incorrect. Kindly input a 5 character word")
        else:
            print("Length correct for the input word")
            return func()
    return wrapper
        

@check_word_length
def check_word_match():
    iword = input_word.lower()
    sword = sel_word.lower()
    print("Iword is: {}".format(iword))
    print("Sword is: {}".format(sword))
    if iword == sword:
        print("Bingo! Word Matched. Word is {}".format(sword))
    else:
        print("Word did not match")
        
check_word_match()