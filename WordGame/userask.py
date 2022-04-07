from userdata import User, DatabaseEntry
from wordgame import InputWord

def register():
    fname = input("Enter your first name: ")
    sname = input("Enter your surname: ")
    uname = input("Enter a username of your choice: ")
    # To-CODE
    # If username already present, do not create
    database = DatabaseEntry()
    user = database.get_userstat_from_username(uname)
    if user:
        print("Already a user. Kindly login with this username")
    else:
        print("Create user")
        create_user = User(fname, sname, uname)
        print(create_user.get_fullname())
        create_user.create_database_entry()
        login()
        # create_user.get_details()

    
def login():
    auname = input("Enter your username: ")
    login_user = DatabaseEntry()
    udata = login_user.get_userstat_from_username(auname)
    if not udata:
        print("Not a user. Please register yourself first")
        return
    else:
        # print(udata)
        userlogin = User(udata[0][0], udata[0][1], udata[0][2])
        welcome_name = userlogin.get_fullname()
        print("WELCOME {}".format(welcome_name))
        print(userlogin.get_win_loss_stats(auname))
        game = InputWord()
        gameresult = game.tries()
        login_user.update_database_result(auname, gameresult)
        print(userlogin.get_win_loss_stats(auname))
        # res = login_user.update_database_result(auname, gameresult)
        # print("Updated data is: {}".format(res))
        
        
        
        # To-CODE
        # Play the game with the user
        # After completion of one game, update the game details to database
        
        

details_input = input("For Login, press 1. To Register, press 2: ")

if int(details_input) == 2:
    register()
elif int(details_input) == 1:
    login()
else:
    print("Not a valid input")
    
