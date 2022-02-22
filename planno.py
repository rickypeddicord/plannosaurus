from kivy.lang import Builder
from kivymd.app import MDApp
import psycopg2
import psycopg2.extras
from datetime import *
from dateutil.relativedelta import *
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
        
        current_day = date.today()

        first_day = date.today()
        second_day = first_day + relativedelta(days = + 1)
        third_day = second_day + relativedelta(days = + 1)
        fourth_day = third_day + relativedelta(days = + 1)
        fifth_day = fourth_day + relativedelta(days = + 1)
        sixth_day = fifth_day + relativedelta(days = + 1)
        seventh_day = sixth_day + relativedelta(days = + 1)

        if current_day.weekday() == 6:
            first_day = date.today()
            second_day = first_day + relativedelta(days = + 1)
            third_day = second_day + relativedelta(days = + 1)
            fourth_day = third_day + relativedelta(days = + 1)
            fifth_day = fourth_day + relativedelta(days = + 1)
            sixth_day = fifth_day + relativedelta(days = + 1)
            seventh_day = sixth_day + relativedelta(days = + 1)

        elif current_day.weekday() == 0:
            second_day = current_day
            print(date.today() + relativedelta(day = + 1))
            first_day = second_day + relativedelta(days = - 1)
            third_day = second_day + relativedelta(day = + 1) # should be 22.... 
            fourth_day = third_day + relativedelta(day = + 1)
            fifth_day = fourth_day + relativedelta(day = + 1)
            sixth_day = fifth_day + relativedelta(day = + 1)
            seventh_day = sixth_day + relativedelta(day = + 1)

        elif current_day.weekday() == 1:
            third_day = date.today()
            second_day = third_day + relativedelta(day = - 1)
            first_day = second_day + relativedelta(day = - 1)
            fourth_day = third_day + relativedelta(day = + 1)
            fifth_day = fourth_day + relativedelta(day = + 1)
            sixth_day = fifth_day + relativedelta(day = + 1)
            seventh_day = sixth_day + relativedelta(day = + 1)

        elif current_day.weekday() == 2:
            fourth_day = date.today()
            third_day = fourth_day + relativedelta(day = - 1)
            second_day = third_day + relativedelta(day = - 1)
            first_day = second_day + relativedelta(day = - 1)
            fifth_day = fourth_day + relativedelta(day = + 1)
            sixth_day = fifth_day + relativedelta(day = + 1)
            seventh_day = sixth_day + relativedelta(day = + 1)

        elif current_day.weekday() == 3:
            fifth_day = date.today()
            fourth_day = fifth_day + relativedelta(day = - 1)
            third_day = fourth_day + relativedelta(day = - 1)
            second_day = third_day + relativedelta(day = - 1)
            first_day = second_day + relativedelta(day = - 1)
            sixth_day = fifth_day + relativedelta(day = + 1)
            seventh_day = sixth_day + relativedelta(day = + 1)

        elif current_day.weekday() == 4:
            sixth_day = date.today()
            fifth_day = sixth_day + relativedelta(day = - 1)
            fourth_day = fifth_day + relativedelta(day = - 1)
            third_day = fourth_day + relativedelta(day = - 1)
            second_day = third_day + relativedelta(day = - 1)
            first_day = second_day + relativedelta(day = - 1)
            seventh_day = sixth_day + relativedelta(day = + 1)

        else:
            seventh_day = date.today()
            sixth_day = seventh_day + relativedelta(day = - 1)
            fifth_day = sixth_day + relativedelta(day = - 1)
            fourth_day = fifth_day + relativedelta(day = - 1)
            third_day = fourth_day + relativedelta(day = - 1)
            second_day = third_day + relativedelta(day = - 1)
            first_day = second_day + relativedelta(day = - 1)

        theDays = StartingDates(first_day, second_day, third_day, fourth_day, fifth_day, sixth_day, seventh_day)
        theMonth = date.today().month
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.ids.currMonth.text = str(months[theMonth - 1])

        # highlight the current day

        if first_day == date.today():
            self.ids.day1.text = "[color=#42f58d]"+ str(theDays.day1.day) +"[/color]"
            self.ids.day2.text = str(theDays.day2.day)
            self.ids.day3.text = str(theDays.day3.day)
            self.ids.day4.text = str(theDays.day4.day)
            self.ids.day5.text = str(theDays.day5.day)
            self.ids.day6.text = str(theDays.day6.day)
            self.ids.day7.text = str(theDays.day7.day)

        elif second_day == date.today():
            self.ids.day1.text = str(theDays.day1.day)
            self.ids.day2.text = "[color=#42f58d]"+ str(theDays.day2.day) +"[/color]"
            self.ids.day3.text = str(theDays.day3.day)
            self.ids.day4.text = str(theDays.day4.day)
            self.ids.day5.text = str(theDays.day5.day)
            self.ids.day6.text = str(theDays.day6.day)
            self.ids.day7.text = str(theDays.day7.day)

        elif third_day == date.today():
            self.ids.day1.text = str(theDays.day1.day)
            self.ids.day2.text = str(theDays.day2.day)
            self.ids.day3.text = "[color=#42f58d]"+ str(theDays.day3.day) +"[/color]"
            self.ids.day4.text = str(theDays.day4.day)
            self.ids.day5.text = str(theDays.day5.day)
            self.ids.day6.text = str(theDays.day6.day)
            self.ids.day7.text = str(theDays.day7.day)

        elif fourth_day == date.today():
            self.ids.day1.text = str(theDays.day1.day)
            self.ids.day2.text = str(theDays.day2.day)
            self.ids.day3.text = str(theDays.day3.day)
            self.ids.day4.text = "[color=#42f58d]"+ str(theDays.day4.day) +"[/color]"
            self.ids.day5.text = str(theDays.day5.day)
            self.ids.day6.text = str(theDays.day6.day)
            self.ids.day7.text = str(theDays.day7.day)

        elif fifth_day == date.today():
            self.ids.day1.text = str(theDays.day1.day)
            self.ids.day2.text = str(theDays.day2.day)
            self.ids.day3.text = str(theDays.day3.day)
            self.ids.day4.text = str(theDays.day4.day)
            self.ids.day5.text = "[color=#42f58d]"+ str(theDays.day5.day) +"[/color]"
            self.ids.day6.text = str(theDays.day6.day)
            self.ids.day7.text = str(theDays.day7.day)

        elif sixth_day == date.today():
            self.ids.day1.text = str(theDays.day1.day)
            self.ids.day2.text = str(theDays.day2.day)
            self.ids.day3.text = str(theDays.day3.day)
            self.ids.day4.text = str(theDays.day4.day)
            self.ids.day5.text = str(theDays.day5.day)
            self.ids.day6.text = "[color=#42f58d]"+ str(theDays.day6.day) +"[/color]"
            self.ids.day7.text = str(theDays.day7.day)

        else:
            self.ids.day1.text = str(theDays.day1.day)
            self.ids.day2.text = str(theDays.day2.day)
            self.ids.day3.text = str(theDays.day3.day)
            self.ids.day4.text = str(theDays.day4.day)
            self.ids.day5.text = str(theDays.day5.day)
            self.ids.day6.text = str(theDays.day6.day)
            self.ids.day7.text = "[color=#42f58d]"+ str(theDays.day7.day) +"[/color]"
    
        

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

        first_day = date.today()
        second_day = first_day + relativedelta(days = + 1)
        third_day = second_day + relativedelta(days = + 1)
        fourth_day = third_day + relativedelta(days = + 1)
        fifth_day = fourth_day + relativedelta(days = + 1)
        sixth_day = fifth_day + relativedelta(days = + 1)
        seventh_day = sixth_day + relativedelta(days = + 1)
        self.theDays = StartingDates(first_day, second_day, third_day, fourth_day, fifth_day, sixth_day, seventh_day)
    
        return WindowManager()

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
        self.theDays.day1 = self.theDays.day1 + relativedelta(days = - 7)
        self.theDays.day2 = self.theDays.day2 + relativedelta(days = - 7)
        self.theDays.day3 = self.theDays.day3 + relativedelta(days = - 7)
        self.theDays.day4 = self.theDays.day4 + relativedelta(days = - 7)
        self.theDays.day5 = self.theDays.day5 + relativedelta(days = - 7)
        self.theDays.day6 = self.theDays.day6 + relativedelta(days = - 7)
        self.theDays.day7 = self.theDays.day7 + relativedelta(days = - 7)
        day1 = self.theDays.day1
        day2 = self.theDays.day2
        day3 = self.theDays.day3
        day4 = self.theDays.day4
        day5 = self.theDays.day5
        day6 = self.theDays.day6
        day7 = self.theDays.day7
        theMonth = day7.month
        theYear = day7.year
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.root.ids.currMonth.text = str(months[theMonth - 1])
        self.root.ids.currYear.text = str(theYear)
        dayHold = ""
        for key, val in self.root.ids.items():
            if "day" in key:
                if "[" in self.root.ids[key].text:
                    self.root.ids[key].text = self.root.ids[key].text.split(']')[1].split('[')[0]
                    dayHold = self.root.ids[key] # save reference to current day id
        
        self.root.ids.day1.text = str(day1.day)
        self.root.ids.day2.text = str(day2.day)
        self.root.ids.day3.text = str(day3.day)
        self.root.ids.day4.text = str(day4.day)
        self.root.ids.day5.text = str(day5.day)
        self.root.ids.day6.text = str(day6.day)
        self.root.ids.day7.text = str(day7.day)
        dayHold.text = "[color=#42f58d]" + dayHold.text + "[/color]" # change text color of same day of the week when shifted

    def right_cal(self):
        self.theDays.day1 = self.theDays.day1 + relativedelta(days = + 7)
        self.theDays.day2 = self.theDays.day2 + relativedelta(days = + 7)
        self.theDays.day3 = self.theDays.day3 + relativedelta(days = + 7)
        self.theDays.day4 = self.theDays.day4 + relativedelta(days = + 7)
        self.theDays.day5 = self.theDays.day5 + relativedelta(days = + 7)
        self.theDays.day6 = self.theDays.day6 + relativedelta(days = + 7)
        self.theDays.day7 = self.theDays.day7 + relativedelta(days = + 7)
        day1 = self.theDays.day1
        day2 = self.theDays.day2
        day3 = self.theDays.day3
        day4 = self.theDays.day4
        day5 = self.theDays.day5
        day6 = self.theDays.day6
        day7 = self.theDays.day7
        theMonth = day7.month
        theYear = day7.year
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.root.ids.currMonth.text = str(months[theMonth - 1])
        self.root.ids.currYear.text = str(theYear)
        dayHold = ""
        for key, val in self.root.ids.items():
            if "day" in key:
                if "[" in self.root.ids[key].text:
                    self.root.ids[key].text = self.root.ids[key].text.split(']')[1].split('[')[0]
                    dayHold = self.root.ids[key] # save reference to current day id
        self.root.ids.day1.text = str(day1.day)
        self.root.ids.day2.text = str(day2.day)
        self.root.ids.day3.text = str(day3.day)
        self.root.ids.day4.text = str(day4.day)
        self.root.ids.day5.text = str(day5.day)
        self.root.ids.day6.text = str(day6.day)
        self.root.ids.day7.text = str(day7.day)
        dayHold.text = "[color=#42f58d]" + dayHold.text + "[/color]" # change text color of same day of the week when shifted
        
    def current_day(self, instance):
        for key, val in self.root.ids.items():
            if "day" in key:
                if "[" in self.root.ids[key].text:
                    self.root.ids[key].text = self.root.ids[key].text.split(']')[1].split('[')[0]
        instance.text = "[color=#42f58d]" + instance.text + "[/color]"
                

     
    def todo_press(self):
        print(self.root.ids.ToDoList.text)

MainApp().run()
