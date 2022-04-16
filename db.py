import config
import psycopg2
import psycopg2.extras

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            host = "localhost",
            database = "plannodb",
            user = "postgres",
            password = "postgres",
            port = "5432",
        )

        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
         # Create users table
        self.cursor.execute("CREATE TABLE if not exists users(userID SERIAL PRIMARY KEY, email VARCHAR(255), password VARCHAR(255), firstName VARCHAR(255), lastName VARCHAR(255))")
        
        # Create events table
        self.cursor.execute("CREATE TABLE if not exists events(eventID SERIAL PRIMARY KEY, dateID VARCHAR(255), timestamp VARCHAR(255), time VARCHAR(255), messageBody VARCHAR(255), userID int REFERENCES users, sticker VARCHAR(255), color VARCHAR(255))")

        # Create todos table
        self.cursor.execute("CREATE TABLE if not exists todos(todoID SERIAL PRIMARY KEY, dateID VARCHAR(255), timestamp VARCHAR(255), completed int, todoItem VARCHAR(255), userID int REFERENCES users)")

        # Create colors table
        self.cursor.execute("CREATE TABLE if not exists colors(style VARCHAR(255), userID int REFERENCES users)")

        # Create theme table
        self.cursor.execute("CREATE TABLE if not exists theme(primary_palette VARCHAR(255), accent_palette VARCHAR(255), theme_style VARCHAR(255))")

        self.conn.commit()

    def login(self, userText, passText):
        loginCode = -1

        c = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM users WHERE email = %s"
        c.execute(query, (userText,))
        records = c.fetchone()
        

        if records:
            if records[1] == userText and records[2] == passText:
                loginCode = 1
                config.store.put('account', userid=records[0], email=userText, password=passText)
            else:
                loginCode = -1
        else:
            loginCode = -1

        self.conn.commit()
        return loginCode

    def register(self, firstName, lastName, enterPass, passReEnter, emailPrompt):
        regCode = -1
        c = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        if firstName == "" or lastName == "":
            regCode = -1
            return regCode
        elif enterPass != passReEnter:
            regCode = -2
            return regCode
        elif enterPass == "" or passReEnter == "":
            regCode = -3
            regLabel = "Password fields required."
            return regCode
        else:
            c.execute("SELECT * FROM users")
            records = c.fetchall()
        if records:
            for record in records:
                if record[1] == emailPrompt:
                    regCode = 0
                else:
                    c.execute("INSERT INTO users (email, password, firstName, lastName) VALUES (%s, %s, %s, %s)", (emailPrompt, enterPass, firstName, lastName))
                    regCode = 1
                    config.store.put('account', userid=record[0], email=emailPrompt, password=enterPass)
                    break
        else:
            c.execute("INSERT INTO users (email, password, firstName, lastName) VALUES (%s, %s, %s, %s)", (emailPrompt, enterPass, firstName, lastName))
            regCode = 1
            config.store.put('account', userid=record[0], email=emailPrompt, password=enterPass)
        
        self.conn.commit()
        
        return regCode

    def delete_event(self, deleteItem):
        c = self.conn.cursor()
        query = "SELECT time FROM events WHERE userid = %s AND messageBody = %s"
        c.execute(query, (config.userid, deleteItem,))
        timeofEvent = c.fetchall()

        query = "DELETE FROM events WHERE userid = %s AND messageBody = %s"
        c.execute(query, (config.userid, deleteItem,))
        
        self.conn.commit()

        return timeofEvent

    def update_theme(self, primary, accent, theme):
        c = self.conn.cursor()

        c.execute("SELECT * FROM theme")
        curr_theme = c.fetchall()

        if len(curr_theme) == 0:
            c.execute("INSERT INTO theme (primary_palette, accent_palette, theme_style) VALUES (%s, %s, %s)",
            (primary, accent, theme))
        else:
            c.execute("UPDATE theme SET primary_palette = %s, accent_palette = %s, theme_style = %s", 
            (primary, accent, theme))

        self.conn.commit()

    def update_sticker(self, text, event_text):
        c = self.conn.cursor()
        query = "UPDATE events SET sticker = %s WHERE messageBody = %s"
        c.execute(query, (text, event_text))
        
        self.conn.commit()

    def save_stickerColor(self, color, event_text):
        c = self.conn.cursor()
        query = "UPDATE events SET color = %s WHERE messageBody = %s"
        c.execute(query, (color, event_text))

        self.conn.commit()

    def add_todo(self, task_date, todoMessage):
        c = self.conn.cursor()
        c.execute("INSERT INTO todos(dateID, timestamp, completed, todoItem, userID) VALUES (%s, %s, %s, %s, %s)", (config.dateID, task_date, 0, todoMessage, config.userid))
        
        self.conn.commit()

    def post_todo(self):
        c = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM todos WHERE userID = %s AND dateID = %s"
        c.execute(query, (config.userid, config.dateID,))
        records = c.fetchall()

        return records
        

    def load_theme(self, primary, accent, theme, hue):
        # load theme data
        c = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        c.execute("SELECT * FROM theme")
        curr_theme = c.fetchall()

        self.conn.commit()

        return curr_theme

    def event_add(self):
        pass

    def post_events(self):
        pass

    def load_colors(self):
        pass

    def mark(self):
        pass

    def delete_item(self):
        pass

    def color_changer(self):
        pass

    def close_db(self):
        self.conn.close()
