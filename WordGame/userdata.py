import sqlite3

class Login:
    pass

class Register:
    pass


class DatabaseEntry:
    def __init__(self):
        self.conn = sqlite3.connect('wgameudata.db')
        self.cursorObj = self.conn.cursor()
        sql = 'CREATE TABLE if not exists ' + 'wgameusers' + ' (firstname text, surname text, username text, totalgames int, won int, lost int)'
        self.cursorObj.execute(sql)
        
    def get_userstat_from_username(self, uname):
        self.cursorObj.execute("SELECT * FROM wgameusers WHERE username" +"=?", (uname,))
        rows = self.cursorObj.fetchall()
        # print("Rows: {}".format(rows))
        return rows
    
    def get_win_loss_stats(self, uname):
        self.cursorObj.execute("SELECT totalgames FROM wgameusers WHERE username" +"=?", (uname,))
        total_games = self.cursorObj.fetchone()[0]

        self.cursorObj.execute("SELECT won FROM wgameusers WHERE username" +"=?", (uname,))
        won = self.cursorObj.fetchone()[0]
        
        self.cursorObj.execute("SELECT lost FROM wgameusers WHERE username" +"=?", (uname,))
        lost = self.cursorObj.fetchone()[0]
        
        
        if not total_games:
            win_percentage = 0
        else:
            win_percentage = (int(won)/int(total_games)) * 100

        return("Total Games Played: {}\nGames Won:          {}\nGames Lost:         {}\nWin %:              {}".format(total_games, won, lost, win_percentage))
    
    def is_user(self, uname):
        self.cursorObj.execute("SELECT * FROM wgameusers WHERE username" +"=?", (uname,))
        rows = self.cursorObj.fetchall()
        return rows
    
    def update_database_result(self, uname, result):
        udata = self.get_userstat_from_username(uname)
        totalgames = int(udata[0][3]) + 1
        won = int(udata[0][4])
        lost = int(udata[0][5])
        if result:
            won += 1
        else:
            lost += 1
        
        self.cursorObj.execute("UPDATE wgameusers SET totalgames=?, won=?, lost=? WHERE username=?", (totalgames, won, lost, uname))
        self.conn.commit()
        self.cursorObj.execute("SELECT * FROM wgameusers WHERE username" +"=?", (uname,))
        rows = self.cursorObj.fetchall()
        return rows
        
    
    # def create_database(self):
    #     self.conn = sqlite3.connect('wgameudata.db')
    #     # cursorObj = conn.cursor()
        
    # def sql_table(self):
    #     self.cursorObj.execute("CREATE TABLE wgameusers (firstname text, surname text, username text, totalgames int, won int, lost int)")
    #     self.conn.commit()
        


class User(DatabaseEntry):
    def __init__(self, firstname, surname, username):
        super().__init__()
        self.firstname = firstname.lower()
        self.surname = surname.lower()
        self.username = username.lower()
        
    def get_fullname(self):
        return "{} {}".format(self.firstname.upper(), self.surname.upper())
    
    def register_user(self):
        pass
    
    def create_database_entry(self):
        # self.cursorObj.execute("INSERT INTO wgameusers (firstname, surname, username, totalgames, won, lost) VALUES (test1, test1, test1, 0, 0, 0)")
        # self.cursorObj.execute("INSERT INTO wgameusers (firstname, surname, username, totalgames, won, lost) VALUES ({}, {}, {}, 0, 0, 0)".format(self.firstname, self.surname, self.username))
        self.cursorObj.execute("INSERT INTO wgameusers (firstname, surname, username, totalgames, won, lost) \
                               VALUES (?, ?, ?, 0, 0, 0)", (self.firstname, self.surname, self.username))
        # print("Before commit")
        # self.cursorObj.execute("SELECT * FROM wgameusers")
        self.conn.commit()
        # print("After commit")
        # self.cursorObj.execute("SELECT * FROM wgameusers")
        
    def get_details(self):
        self.cursorObj.execute("SELECT * FROM wgameusers WHERE username" +"=?", (self.username,))
        rows = self.cursorObj.fetchall()
        return rows
        # print("Rows: {}".format(rows))
        