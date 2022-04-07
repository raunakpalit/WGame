from userdata import User, DatabaseEntry
from wordgame import InputWord

class RegLog:
    def __init__(self):
        self.fstname = None
        self.lstname = None
        self.usrname = None
        self.databaseinit = DatabaseEntry()
        self.userclassobj = None
    
    def register(self):
        self.fstname = input("Enter your first name: ")
        self.lstname = input("Enter your surname: ")
        self.usrname = input("Enter a username of your choice: ")

        # database = DatabaseEntry()
        # user = database.get_userstat_from_username(uname)
        user = self.databaseinit.get_userstat_from_username(self.usrname)
        if user:
            print("Already a user. Kindly login with this username")
        else:
            print("Creating user...")
            self.userclassobj = User(self.fstname, self.lstname, self.usrname)
            print(self.userclassobj.get_fullname())
            self.userclassobj.create_database_entry()
            self.login()
            
    def login(self):
        self.usrname = input("Enter your username: ")
        self.usrname = self.usrname.lower()
        # login_user = DatabaseEntry()
        udata = self.databaseinit.get_userstat_from_username(self.usrname)
        if not udata:
            print("Not a user. Please register yourself first")
            return
        else:
            self.userclassobj = User(udata[0][0], udata[0][1], udata[0][2])
            welcome_name = self.userclassobj.get_fullname()
            print("WELCOME {}".format(welcome_name))
            userinputforplayorstatcheck = input("To play the game, press 1. To check player statistics, press 2: ")
            if int(userinputforplayorstatcheck) == 1:
                choice = 'y'
                while choice == 'y':
                    self.play_the_wordgame(choice)
                    userinputplayagain = input("Hey {}, would you like to give another try(Y/N): ".format(welcome_name))
                    if userinputplayagain.lower() == 'y':
                        choice = 'y'
                    elif userinputplayagain.lower() == 'n':
                        choice = 'n'
                    else:
                        print("Invalid input")
                        return
            elif int(userinputforplayorstatcheck) == 2:
                print(self.databaseinit.get_win_loss_stats(self.usrname))
            else:
                print("Incorrect input")
                
    def play_the_wordgame(self, choice='y'):
        if choice == 'y':
            game = InputWord()
            gameresult = game.tries()
            self.databaseinit.update_database_result(self.usrname, gameresult)
            print(self.databaseinit.get_win_loss_stats(self.usrname))
            

playclass = RegLog()
details_input = input("For Login, press 1. To Register, press 2: ")

if int(details_input) == 2:
    playclass.register()
elif int(details_input) == 1:
    playclass.login()
else:
    print("Not a valid input")