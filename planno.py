from kivy.lang import Builder
from kivymd.app import MDApp
import psycopg2
import psycopg2.extras
import datetime
from datetime import *
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.picker import MDDatePicker
from kivy.uix.tabbedpanel import TabbedPanel

class StartingDates:
    def __init__(self, day1, day2, day3, day4, day5, day6, day7):
        self._day1 = day1
        self._day2 = day2
        self._day3 = day3
        self._day4 = day4
        self._day5 = day5
        self._day6 = day6
        self._day7 = day7
    
    @property
    def day1(self):
        return self._day1

    @day1.setter
    def day1(self, val):
        self._day1 = val
    
    @property
    def day2(self):
        return self._day2

    @day2.setter
    def day2(self, val):
        self._day2 = val
    
    @property
    def day3(self):
        return self._day3

    @day3.setter
    def day3(self, val):
        self._day3 = val

    @property
    def day4(self):
        return self._day4

    @day4.setter
    def day4(self, val):
        self._day4 = val

    @property
    def day5(self):
        return self._day5

    @day5.setter
    def day5(self, val):
        self._day5 = val
    
    @property
    def day6(self):
        return self._day6

    @day6.setter
    def day6(self, val):
        self._day6 = val

    @property
    def day7(self):
        return self._day7

    @day7.setter
    def day7(self, val):
        self._day7 = val


class WindowManager(ScreenManager):
    def init_load(self, root):
        # fix date issue here
        # dates are resetting to first of the month for every day after the current...
        root.current = "main_sc"
        
        curr_day = datetime.today()

        if curr_day.weekday() == 6:
            first_day = curr_day
            second_day = (curr_day + timedelta(days = 1))
            third_day = (curr_day + timedelta(days = 2))
            fourth_day = (curr_day + timedelta(days = 3))
            fifth_day = (curr_day + timedelta(days = 4))
            sixth_day = (curr_day + timedelta(days = 5))
            seventh_day = (curr_day + timedelta(days = 6))

        elif curr_day.weekday() == 0:
            second_day = curr_day
            first_day = (curr_day - timedelta(days = 1))
            third_day = (curr_day + timedelta(days = 1))
            fourth_day = (curr_day + timedelta(days = 2))
            fifth_day = (curr_day + timedelta(days = 3))
            sixth_day = (curr_day + timedelta(days = 4))
            seventh_day = (curr_day + timedelta(days = 5))

        elif curr_day.weekday() == 1:
            third_day = curr_day
            second_day = (curr_day - timedelta(days = 1))
            first_day = (curr_day - timedelta(days = 2))
            fourth_day = (curr_day + timedelta(days = 1))
            fifth_day = (curr_day + timedelta(days = 2))
            sixth_day = (curr_day + timedelta(days = 3))
            seventh_day = (curr_day + timedelta(days = 4))

        elif curr_day.weekday() == 2:
            fourth_day = curr_day
            third_day = (curr_day - timedelta(days = 1))
            second_day = (curr_day - timedelta(days = 2))
            first_day = (curr_day - timedelta(days = 3))
            fifth_day = (curr_day + timedelta(days = 1))
            sixth_day = (curr_day + timedelta(days = 2))
            seventh_day = (curr_day + timedelta(days = 3))

        elif curr_day.weekday() == 3:
            fifth_day = curr_day
            fourth_day = (curr_day - timedelta(days = 1))
            third_day = (curr_day - timedelta(days = 2))
            second_day = (curr_day - timedelta(days = 3))
            first_day = (curr_day - timedelta(days = 4))
            sixth_day = (curr_day + timedelta(days = 1))
            seventh_day = (curr_day + timedelta(days = 2))

        elif curr_day.weekday() == 4:
            sixth_day = curr_day
            fifth_day = (curr_day - timedelta(days = 1))
            fourth_day = (curr_day - timedelta(days = 2))
            third_day = (curr_day - timedelta(days = 3))
            second_day = (curr_day - timedelta(days = 4))
            first_day = (curr_day - timedelta(days = 5))
            seventh_day = (curr_day + timedelta(days = 1))

        else:
            seventh_day = curr_day
            sixth_day = (curr_day - timedelta(days = 1))
            fifth_day = (curr_day - timedelta(days = 2))
            fourth_day = (curr_day - timedelta(days = 3))
            third_day = (curr_day - timedelta(days = 4))
            second_day = (curr_day - timedelta(days = 5))
            first_day = (curr_day - timedelta(days = 6))

        theDays = StartingDates(first_day, second_day, third_day, fourth_day, fifth_day, sixth_day, seventh_day)
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.ids.currMonth.text = str(months[date.today().month - 1])

        # highlight the current day

        if first_day == datetime.today():
            self.ids.day1.text = "[color=#42f58d]"+ theDays.day1.strftime("%d") +"[/color]"
            self.ids.day2.text = theDays.day2.strftime("%d")
            self.ids.day3.text = theDays.day3.strftime("%d")
            self.ids.day4.text = theDays.day4.strftime("%d")
            self.ids.day5.text = theDays.day5.strftime("%d")
            self.ids.day6.text = theDays.day6.strftime("%d")
            self.ids.day7.text = theDays.day7.strftime("%d")

        elif second_day == datetime.today():
            self.ids.day1.text = theDays.day1.strftime("%d")
            self.ids.day2.text = "[color=#42f58d]"+ theDays.day2.strftime("%d") +"[/color]"
            self.ids.day3.text = theDays.day3.strftime("%d")
            self.ids.day4.text = theDays.day4.strftime("%d")
            self.ids.day5.text = theDays.day5.strftime("%d")
            self.ids.day6.text = theDays.day6.strftime("%d")
            self.ids.day7.text = theDays.day7.strftime("%d")

        elif third_day == datetime.today():
            self.ids.day1.text = theDays.day1.strftime("%d")
            self.ids.day2.text = theDays.day2.strftime("%d")
            self.ids.day3.text = "[color=#42f58d]"+ theDays.day3.strftime("%d") +"[/color]"
            self.ids.day4.text = theDays.day4.strftime("%d")
            self.ids.day5.text = theDays.day5.strftime("%d")
            self.ids.day6.text = theDays.day6.strftime("%d")
            self.ids.day7.text = theDays.day7.strftime("%d")

        elif fourth_day == datetime.today():
            self.ids.day1.text = theDays.day1.strftime("%d")
            self.ids.day2.text = theDays.day2.strftime("%d")
            self.ids.day3.text = theDays.day3.strftime("%d")
            self.ids.day4.text = "[color=#42f58d]"+ theDays.day4.strftime("%d") +"[/color]"
            self.ids.day5.text = theDays.day5.strftime("%d")
            self.ids.day6.text = theDays.day6.strftime("%d")
            self.ids.day7.text = theDays.day7.strftime("%d")

        elif fifth_day == datetime.today():
            self.ids.day1.text = theDays.day1.strftime("%d")
            self.ids.day2.text = theDays.day2.strftime("%d")
            self.ids.day3.text = theDays.day3.strftime("%d")
            self.ids.day4.text = theDays.day4.strftime("%d")
            self.ids.day5.text = "[color=#42f58d]"+ theDays.day5.strftime("%d") +"[/color]"
            self.ids.day6.text = theDays.day6.strftime("%d")
            self.ids.day7.text = theDays.day7.strftime("%d")

        elif sixth_day == datetime.today():
            self.ids.day1.text = theDays.day1.strftime("%d")
            self.ids.day2.text = theDays.day2.strftime("%d")
            self.ids.day3.text = theDays.day3.strftime("%d")
            self.ids.day4.text = theDays.day4.strftime("%d")
            self.ids.day5.text = theDays.day5.strftime("%d")
            self.ids.day6.text = "[color=#42f58d]"+ theDays.day6.strftime("%d") +"[/color]"
            self.ids.day7.text = theDays.day7.strftime("%d")

        else:
            self.ids.day1.text = theDays.day1.strftime("%d")
            self.ids.day2.text = theDays.day2.strftime("%d")
            self.ids.day3.text = theDays.day3.strftime("%d")
            self.ids.day4.text = theDays.day4.strftime("%d")
            self.ids.day5.text = theDays.day5.strftime("%d")
            self.ids.day6.text = theDays.day6.strftime("%d")
            self.ids.day7.text = "[color=#42f58d]"+ theDays.day7.strftime("%d") +"[/color]"
    
        

class MainApp(MDApp):
    def build(self):
        Builder.load_file("app.kv")
        #self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"

        # Create database table if it doesn't exist
        conn = psycopg2.connect(
            host = "ec2-34-205-209-14.compute-1.amazonaws.com",
            database = "d19re7njihace8",
            user = "lveasasuicarlg",
            password = "c372ee6ba2bc15c476bf85a8258fa444d2a51f4323b6903a1963c0c5fb118a08",
            port = "5432",
        )

        # Create a cursor
        c = conn.cursor()

        # Create a table
        c.execute("CREATE TABLE if not exists users(id SERIAL PRIMARY KEY, username VARCHAR(255), password VARCHAR(255), firstName VARCHAR(255), lastName VARCHAR(255), emailPrompt VARCHAR(255))")
        
        
        conn.commit()
        conn.close()

        self.gen_cal()

        
    
        return WindowManager()

    def gen_cal(self):
        curr_day = datetime.today()

        if curr_day.weekday() == 6:
            first_day = curr_day
            second_day = (curr_day + timedelta(days = 1))
            third_day = (curr_day + timedelta(days = 2))
            fourth_day = (curr_day + timedelta(days = 3))
            fifth_day = (curr_day + timedelta(days = 4))
            sixth_day = (curr_day + timedelta(days = 5))
            seventh_day = (curr_day + timedelta(days = 6))

        elif curr_day.weekday() == 0:
            second_day = curr_day
            first_day = (curr_day - timedelta(days = 1))
            third_day = (curr_day + timedelta(days = 1))
            fourth_day = (curr_day + timedelta(days = 2))
            fifth_day = (curr_day + timedelta(days = 3))
            sixth_day = (curr_day + timedelta(days = 4))
            seventh_day = (curr_day + timedelta(days = 5))

        elif curr_day.weekday() == 1:
            third_day = curr_day
            second_day = (curr_day - timedelta(days = 1))
            first_day = (curr_day - timedelta(days = 2))
            fourth_day = (curr_day + timedelta(days = 1))
            fifth_day = (curr_day + timedelta(days = 2))
            sixth_day = (curr_day + timedelta(days = 3))
            seventh_day = (curr_day + timedelta(days = 4))

        elif curr_day.weekday() == 2:
            fourth_day = curr_day
            third_day = (curr_day - timedelta(days = 1))
            second_day = (curr_day - timedelta(days = 2))
            first_day = (curr_day - timedelta(days = 3))
            fifth_day = (curr_day + timedelta(days = 1))
            sixth_day = (curr_day + timedelta(days = 2))
            seventh_day = (curr_day + timedelta(days = 3))

        elif curr_day.weekday() == 3:
            fifth_day = curr_day
            fourth_day = (curr_day - timedelta(days = 1))
            third_day = (curr_day - timedelta(days = 2))
            second_day = (curr_day - timedelta(days = 3))
            first_day = (curr_day - timedelta(days = 4))
            sixth_day = (curr_day + timedelta(days = 1))
            seventh_day = (curr_day + timedelta(days = 2))

        elif curr_day.weekday() == 4:
            sixth_day = curr_day
            fifth_day = (curr_day - timedelta(days = 1))
            fourth_day = (curr_day - timedelta(days = 2))
            third_day = (curr_day - timedelta(days = 3))
            second_day = (curr_day - timedelta(days = 4))
            first_day = (curr_day - timedelta(days = 5))
            seventh_day = (curr_day + timedelta(days = 1))

        else:
            seventh_day = curr_day
            sixth_day = (curr_day - timedelta(days = 1))
            fifth_day = (curr_day - timedelta(days = 2))
            fourth_day = (curr_day - timedelta(days = 3))
            third_day = (curr_day - timedelta(days = 4))
            second_day = (curr_day - timedelta(days = 5))
            first_day = (curr_day - timedelta(days = 6))

        self.theDays = StartingDates(first_day, second_day, third_day, fourth_day, fifth_day, sixth_day, seventh_day)

    def pick_date(self):
        date_dialog = MDDatePicker() 
        date_dialog.bind(on_save = self.on_save)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.root.ids.currMonth.text = str(months[value.month - 1])
        self.root.ids.currYear.text = str(value.year)

        
    def login(self):
        loginCode = -1
        conn = psycopg2.connect(
            host = "ec2-34-205-209-14.compute-1.amazonaws.com",
            database = "d19re7njihace8",
            user = "lveasasuicarlg",
            password = "c372ee6ba2bc15c476bf85a8258fa444d2a51f4323b6903a1963c0c5fb118a08",
            port = "5432",
        )

        c = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM users WHERE username = %s"
        c.execute(query, (self.root.ids.user.text,))
        records = c.fetchone()
        
        if records:
            if records[1] == self.root.ids.user.text and records[2] == self.root.ids.password.text:
                self.root.ids.welcome_label.text = "Logged in successfully"
                loginCode = 1
            else:
                self.root.ids.welcome_label.text = "User doesn't exist or incorrect password entered"
                loginCode = -1
        else:
            self.root.ids.welcome_label.text = "User doesn't exist or incorrect password entered"
            loginCode = -1

        conn.commit()
        conn.close()
        return loginCode
    
    def clear(self):
        self.root.ids.welcome_label.text = "Please Login or Register"
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""

    def register(self, root):
        conn = psycopg2.connect(
            host = "ec2-34-205-209-14.compute-1.amazonaws.com",
            database = "d19re7njihace8",
            user = "lveasasuicarlg",
            password = "c372ee6ba2bc15c476bf85a8258fa444d2a51f4323b6903a1963c0c5fb118a08",
            port = "5432",
        )

        c = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        if self.root.ids.firstName.text == "" or self.root.ids.lastName.text == "":
            self.root.ids.welcome_label.text = "Fields cannot be empty"
            return
        else:
            c.execute("SELECT * FROM users")
            records = c.fetchall()
        if records:
            for record in records:
                if record[1] == self.root.ids.user.text:
                    self.root.ids.welcome_label.text = "An account with these credentials already exists"
                else:
                    c.execute("INSERT INTO users (username, password, firstName, lastName, emailPrompt) VALUES (%s, %s, %s, %s, %s)", (self.root.ids.user.text, self.root.ids.password.text, self.root.ids.firstName.text, self.root.ids.lastName.text, self.root.ids.emailPrompt.text))
                    self.root.ids.welcome_label.text = "Account created successfully"
                    root.current="login_sc"
                    break
        else:
            c.execute("INSERT INTO users (username, password, firstName, lastName, emailPrompt) VALUES (%s, %s, %s, %s, %s)", (self.root.ids.user.text, self.root.ids.password.text, self.root.ids.firstName.text, self.root.ids.lastName.text, self.root.ids.emailPrompt.text))
            self.root.ids.welcome_label.text = "Account created successfully"
            root.current="login_sc"
        conn.commit()
        conn.close()

    def left_cal(self):
        self.theDays.day1 = (self.theDays.day1 - timedelta(days = 7))
        self.theDays.day2 = (self.theDays.day2 - timedelta(days = 7))
        self.theDays.day3 = (self.theDays.day3 - timedelta(days = 7))
        self.theDays.day4 = (self.theDays.day4 - timedelta(days = 7))
        self.theDays.day5 = (self.theDays.day5 - timedelta(days = 7))
        self.theDays.day6 = (self.theDays.day6 - timedelta(days = 7))
        self.theDays.day7 = (self.theDays.day7 - timedelta(days = 7))

        day1 = self.theDays.day1
        day2 = self.theDays.day2
        day3 = self.theDays.day3
        day4 = self.theDays.day4
        day5 = self.theDays.day5
        day6 = self.theDays.day6
        day7 = self.theDays.day7
        
        if day7.strftime("%m") != "10":  
            theMonth = int(day7.strftime("%m").strip("0"))
        else:
            theMonth = int(day7.strftime("%m"))
        
        theYear = int(day7.strftime("%y"))
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.root.ids.currMonth.text = str(months[theMonth - 1])
        self.root.ids.currYear.text = str(theYear)
        dayHold = ""
        for key, val in self.root.ids.items():
            if "day" in key:
                if "[" in self.root.ids[key].text:
                    self.root.ids[key].text = self.root.ids[key].text.split(']')[1].split('[')[0]
                    dayHold = self.root.ids[key] # save reference to current day id
        
        self.root.ids.day1.text = day1.strftime("%d")
        self.root.ids.day2.text = day2.strftime("%d")
        self.root.ids.day3.text = day3.strftime("%d")
        self.root.ids.day4.text = day4.strftime("%d")
        self.root.ids.day5.text = day5.strftime("%d")
        self.root.ids.day6.text = day6.strftime("%d")
        self.root.ids.day7.text = day7.strftime("%d")
        dayHold.text = "[color=#42f58d]" + dayHold.text + "[/color]" # change text color of same day of the week when shifted

    def right_cal(self):
        self.theDays.day1 = (self.theDays.day1 + timedelta(days = 7))
        self.theDays.day2 = (self.theDays.day2 + timedelta(days = 7))
        self.theDays.day3 = (self.theDays.day3 + timedelta(days = 7))
        self.theDays.day4 = (self.theDays.day4 + timedelta(days = 7))
        self.theDays.day5 = (self.theDays.day5 + timedelta(days = 7))
        self.theDays.day6 = (self.theDays.day6 + timedelta(days = 7))
        self.theDays.day7 = (self.theDays.day7 + timedelta(days = 7))

        day1 = self.theDays.day1
        day2 = self.theDays.day2
        day3 = self.theDays.day3
        day4 = self.theDays.day4
        day5 = self.theDays.day5
        day6 = self.theDays.day6
        day7 = self.theDays.day7
        
        if day7.strftime("%m") != "10":  
            theMonth = int(day7.strftime("%m").strip("0"))
        else:
            theMonth = int(day7.strftime("%m"))
        
        theYear = int(day7.strftime("%y"))
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.root.ids.currMonth.text = str(months[theMonth - 1])
        self.root.ids.currYear.text = str(theYear)

        dayHold = ""
        for key, val in self.root.ids.items():
            if "day" in key:
                if "[" in self.root.ids[key].text:
                    self.root.ids[key].text = self.root.ids[key].text.split(']')[1].split('[')[0]
                    dayHold = self.root.ids[key] # save reference to current day id
        
        self.root.ids.day1.text = day1.strftime("%d")
        self.root.ids.day2.text = day2.strftime("%d")
        self.root.ids.day3.text = day3.strftime("%d")
        self.root.ids.day4.text = day4.strftime("%d")
        self.root.ids.day5.text = day5.strftime("%d")
        self.root.ids.day6.text = day6.strftime("%d")
        self.root.ids.day7.text = day7.strftime("%d")
        dayHold.text = "[color=#42f58d]" + dayHold.text + "[/color]" # change text color of same day of the week when shifted
                

     
    def todo_press(self):
        print(self.root.ids.ToDoList.text)

MainApp().run()
