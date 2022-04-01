import config
import psycopg2
import psycopg2.extras

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            host = "ec2-34-205-209-14.compute-1.amazonaws.com",
            database = "d19re7njihace8",
            user = "lveasasuicarlg",
            password = "c372ee6ba2bc15c476bf85a8258fa444d2a51f4323b6903a1963c0c5fb118a08",
            port = "5432",
        )

        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
         # Create users table
        self.cursor.execute("CREATE TABLE if not exists users(userID SERIAL PRIMARY KEY, email VARCHAR(255), password VARCHAR(255), firstName VARCHAR(255), lastName VARCHAR(255))")

        # Create events table
        self.cursor.execute("CREATE TABLE if not exists events(eventID SERIAL PRIMARY KEY, dateID VARCHAR(255), timestamp VARCHAR(255), time VARCHAR(255), messageBody VARCHAR(255), userID int REFERENCES users)")

        # Create todos table
        self.cursor.execute("CREATE TABLE if not exists todos(todoID SERIAL PRIMARY KEY, dateID VARCHAR(255), timestamp VARCHAR(255), todoItem VARCHAR(255), userID int REFERENCES users)")

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

    def close_db(self):
        self.conn.close()
