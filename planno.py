from kivy.lang import Builder
from kivymd.app import MDApp
import psycopg2
import psycopg2.extras
import datetime
from datetime import *
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.picker import MDDatePicker
from kivy.uix.tabbedpanel import TabbedPanel
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineListItem
from kivy.uix.checkbox import CheckBox
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore



events = []
todos = []

store = JsonStore('account.json')


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
        
        curr_day = datetime.today()
        dateID = datetime.today().strftime("%m%d%Y")
        print(dateID)

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
        #self.ids.currMonth.text = str(months[date.today().month - 1])

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
        return "main_sc"
    
    def todo_press(self, root):
        print(self.ids.ToDoList.text)
        label1 = OneLineListItem(
            text = self.ids.ToDoList.text,
            pos_hint = {'center_x': self.ids.ToDoButt.pos_hint['center_x'] + 0.45, 
            'center_y': self.ids.ToDoButt.pos_hint['center_y'] - 0.15}
            )
        self.ids.float.add_widget(label1)  


    def event_add(self, root):
        global events
        index=6
		
        if self.ids.contentEvent.text.strip():
            if  not '\n' in self.ids.contentEvent.text:
                self.ids.contentEvent.text += '\n'
            events.append(self.ids.contentEvent.text)
			
            for e in range(len(events)):
                if len(events) == 1:
                    self.ids.contentEventMain.text = str(index) + ' AM - ' + events[e]
                elif not events[e] in self.ids.contentEventMain.text:
                    self.ids.contentEventMain.text +=  str(index) + ' AM - ' + events[e]
   #     self.ids.contentEvent.text = ''



    def event_addsevenAM(self, root):
        global events
        index = 7
        if self.ids.sevenAM.text.strip():
            if  not '\n' in self.ids.sevenAM.text:
                self.ids.sevenAM.text += '\n'
            events.append(self.ids.sevenAM.text)
            for e in range(len(events)):
                if len(events) == 1:
                    self.ids.contentEventMain.text = str(index) + ' AM - ' + events[e]
                elif not events[e] in self.ids.contentEventMain.text:
                    self.ids.contentEventMain.text +=  str(index) + ' AM - ' + events[e]
     #   self.ids.sevenAM.text = ''

    def event_addeightAM(self, root):
        global events
        index = 8
        if self.ids.eightAM.text.strip():
            if  not '\n' in self.ids.eightAM.text:
                self.ids.eightAM.text += '\n'
            events.append(self.ids.eightAM.text)
            for e in range(len(events)):
                if len(events) == 1:
                    self.ids.contentEventMain.text = str(index) + ' AM - ' + events[e]
                elif not events[e] in self.ids.contentEventMain.text:
                    self.ids.contentEventMain.text +=  str(index) + ' AM - ' + events[e]
   #     self.ids.eightAM.text = ''
		
    def event_addnineAM(self, root):
        global events
        index = 9
        if self.ids.nineAM.text.strip():
            if  not '\n' in self.ids.nineAM.text:
                self.ids.nineAM.text += '\n'
            events.append(self.ids.nineAM.text)
            for e in range(len(events)):
                if len(events) == 1:
                    self.ids.contentEventMain.text = str(index) + ' AM - ' + events[e]
                elif not events[e] in self.ids.contentEventMain.text:
                    self.ids.contentEventMain.text +=  str(index) + ' AM - ' + events[e]
        #self.ids.nineAM.text = ''

    def event_addtenAM(self, root):
        global events
        index = 10
        if self.ids.tenAM.text.strip():
            if  not '\n' in self.ids.tenAM.text:
                self.ids.tenAM.text += '\n'
            events.append(self.ids.tenAM.text)
            for e in range(len(events)):
                if len(events) == 1:
                    self.ids.contentEventMain.text =str(index) + ' AM - ' + events[e]
                elif not events[e] in self.ids.contentEventMain.text:
                    self.ids.contentEventMain.text +=  str(index) + ' AM - ' + events[e]
        #self.ids.tenAM.text = ''

    def event_addelevenAM(self, root):
        global events
        index = 11
        if self.ids.elevenAM.text.strip():
            if  not '\n' in self.ids.elevenAM.text:
                self.ids.elevenAM.text += '\n'
            events.append(self.ids.elevenAM.text)
            for e in range(len(events)):
                if len(events) == 1:
                    self.ids.contentEventMain.text =str(index) + ' AM - ' + events[e]
                elif not events[e] in self.ids.contentEventMain.text:
                    self.ids.contentEventMain.text +=  str(index) + ' AM - ' + events[e]
        #self.ids.elevenAM.text = ''

    def event_addNoon(self, root):
        global events
        index = 12
        if self.ids.noon.text.strip():
            if  not '\n' in self.ids.noon.text:
                self.ids.noon.text += ' - 12 PM\n'
            events.append(self.ids.noon.text)
            for e in range(len(events)):
                if len(events) == 1:
                    self.ids.contentEventMain.text =str(index) + ' PM - ' + events[e]
                elif not events[e] in self.ids.contentEventMain.text:
                    self.ids.contentEventMain.text +=  str(index) + ' PM - ' + events[e]
      #  self.ids.noon.text = ''

    def event_addonePM(self, root):
        global events
        index = 13
        if self.ids.onePM.text.strip():
            if  not '\n' in self.ids.onePM.text:
                self.ids.onePM.text += '\n'
            events.append(self.ids.onePM.text)
            for e in range(len(events)):
                if len(events) == 1:
                    self.ids.contentEventMain.text = str((index-12)) + ' PM - ' +events[e]
                elif not events[e] in self.ids.contentEventMain.text:
                    self.ids.contentEventMain.text +=  str((index-12)) + ' PM - ' + events[e]
      #  self.ids.onePM.text = ''

###########
    def event_addtwoPM(self, root):
        global events
        index = 14
        if self.ids.twoPM.text.strip():
            if  not '\n' in self.ids.twoPM.text:
                self.ids.twoPM.text += '\n'
            events.append(self.ids.twoPM.text)
            for e in range(len(events)):
                if len(events) == 1:
                    self.ids.contentEventMain.text =str((index-12)) + ' PM - ' + events[e]
                elif not events[e] in self.ids.contentEventMain.text:
                    self.ids.contentEventMain.text +=  str((index-12)) + ' PM - ' + events[e]
    #    self.ids.twoPM.text = ''


    def event_addthreePM(self, root):
        global events
        index = 15
        if self.ids.threePM.text.strip():
            if  not '\n' in self.ids.threePM.text:
                self.ids.threePM.text += '\n'
            events.append(self.ids.threePM.text)
            for e in range(len(events)):
                if len(events) == 1:
                    self.ids.contentEventMain.text = str((index-12)) + ' PM - ' + events[e]
                elif not events[e] in self.ids.contentEventMain.text:
                    self.ids.contentEventMain.text +=  str((index-12)) + ' PM - ' + events[e]
     #   self.ids.threePM.text = ''

    def event_addfourPM(self, root):
        global events
        index = 16
        if self.ids.fourPM.text.strip():
            if  not '\n' in self.ids.fourPM.text:
                self.ids.fourPM.text += '\n'
            events.append(self.ids.fourPM.text)
            for e in range(len(events)):
                if len(events) == 1:
                    self.ids.contentEventMain.text = str((index-12)) + ' PM - ' + events[e]
                elif not events[e] in self.ids.contentEventMain.text:
                    self.ids.contentEventMain.text +=  str((index-12)) + ' PM - ' + events[e]
      #  self.ids.fourPM.text = ''
		
    def event_addfivePM(self, root):
        global events
        index = 17
        if self.ids.fivePM.text.strip():
            if  not '\n' in self.ids.fivePM.text:
                self.ids.fivePM.text += '\n'
            events.append(self.ids.fivePM.text)
            for e in range(len(events)):
                if len(events) == 1:
                    self.ids.contentEventMain.text = str((index-12)) + ' PM - ' + events[e]
                elif not events[e] in self.ids.contentEventMain.text:
                    self.ids.contentEventMain.text +=  str((index-12)) + ' PM - ' + events[e]
      #  self.ids.fivePM.text = ''

    def event_addsixPM(self, root):
        global events
        index = 18
        if self.ids.sixPM.text.strip():
            if  not '\n' in self.ids.sixPM.text:
                self.ids.sixPM.text += '\n'
            events.append(self.ids.sixPM.text)
            for e in range(len(events)):
                if len(events) == 1:
                    self.ids.contentEventMain.text = str((index-12)) + ' PM - ' + events[e]
                elif not events[e] in self.ids.contentEventMain.text:
                    self.ids.contentEventMain.text +=  str((index-12)) + ' PM - ' + events[e]
      #  self.ids.sixPM.text = ''

    def event_addsevenPM(self, root):
        global events
        index = 19
        if self.ids.sevenPM.text.strip():
            if  not '\n' in self.ids.sevenPM.text:
                self.ids.sevenPM.text += '\n'
            events.append(self.ids.sevenPM.text)
            for e in range(len(events)):
                if len(events) == 1:
                    self.ids.contentEventMain.text = str((index-12)) + ' PM - ' + events[e]
                elif not events[e] in self.ids.contentEventMain.text:
                    self.ids.contentEventMain.text +=  str((index-12)) + ' PM - ' + events[e]
    #    self.ids.sevenPM.text = ''

    def event_addeightPM(self, root):
        global events
        index = 20
        if self.ids.eightPM.text.strip():
            if  not '\n' in self.ids.eightPM.text:
                self.ids.eightPM.text += '\n'
            events.append(self.ids.eightPM.text)
            for e in range(len(events)):
                if len(events) == 1:
                    self.ids.contentEventMain.text =str((index-12)) + ' PM - ' +  events[e]
                elif not events[e] in self.ids.contentEventMain.text:
                    self.ids.contentEventMain.text +=  str((index-12)) + ' PM - ' + events[e]
    #    self.ids.eightPM.text = ''

    def event_addninePM(self, root):
        global events
        index = 21
        if self.ids.ninePM.text.strip():
            if  not '\n' in self.ids.ninePM.text:
                self.ids.ninePM.text += '\n'
            events.append(self.ids.ninePM.text)
            for e in range(len(events)):
                if len(events) == 1:
                    self.ids.contentEventMain.text = str((index-12)) + ' PM - ' + events[e]
                elif not events[e] in self.ids.contentEventMain.text:
                    self.ids.contentEventMain.text +=  str((index-12)) + ' PM - ' + events[e]
   #     self.ids.ninePM.text = ''



		
		
    def event_addToDo(self, root):
        global todos
		
        if self.ids.toDoEntries.text.strip():
            if  not '\n' in self.ids.toDoEntries.text:
                self.ids.toDoEntries.text += '\n'
            todos.append(self.ids.toDoEntries.text)
            for e in range(len(todos)):
                if len(todos) == 1:
                    self.ids.contentTODOMain.text = todos[e]
                elif not todos[e] in self.ids.contentTODOMain.text:
                    self.ids.contentTODOMain.text += todos[e]
        self.ids.toDoEntries.text = ''


class MainApp(MDApp):
    def build(self):
        Builder.load_file("app.kv")
        self.theme_cls.theme_style = "Light"
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

        # Create users table
        c.execute("CREATE TABLE if not exists users(userID SERIAL PRIMARY KEY, email VARCHAR(255), password VARCHAR(255), firstName VARCHAR(255), lastName VARCHAR(255))")

        # Create events table
        c.execute("CREATE TABLE if not exists events(eventID SERIAL PRIMARY KEY, dateID VARCHAR(255), messageBody VARCHAR(255), userID int REFERENCES users)")

        # save reference to userid via select
        # create dateid from currently selected date
        # messgagebody will contain event information
        # eventid needed for editing or deleting an event?
        # probably separate table needed for todos
        
        
        conn.commit()
        conn.close()

        self.gen_cal(date.today())

        

        return WindowManager()

    def on_start(self):
        Clock.schedule_once(self.set_screen, 0)

    def set_screen(self, dt):
        global store

        if store.exists('account'):
            self.root.current = "main_sc"
            self.root.init_load(self.root)
        else:
            self.root.current = "login_sc"

    def gen_cal(self, date):
        curr_day = date

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
        #self.root.ids.currMonth.text = str(months[value.month - 1])
        #self.root.ids.currYear.text = str(value.year)
        self.gen_cal(value)

        
        if self.theDays.day1 == value:
            self.root.ids.day1.text = "[color=#42f58d]"+ self.theDays.day1.strftime("%d") +"[/color]"
            self.root.ids.day2.text = self.theDays.day2.strftime("%d")
            self.root.ids.day3.text = self.theDays.day3.strftime("%d")
            self.root.ids.day4.text = self.theDays.day4.strftime("%d")
            self.root.ids.day5.text = self.theDays.day5.strftime("%d")
            self.root.ids.day6.text = self.theDays.day6.strftime("%d")
            self.root.ids.day7.text = self.theDays.day7.strftime("%d")

        elif self.theDays.day2 == value:
            self.root.ids.day1.text = self.theDays.day1.strftime("%d")
            self.root.ids.day2.text = "[color=#42f58d]"+ self.theDays.day2.strftime("%d") +"[/color]"
            self.root.ids.day3.text = self.theDays.day3.strftime("%d")
            self.root.ids.day4.text = self.theDays.day4.strftime("%d")
            self.root.ids.day5.text = self.theDays.day5.strftime("%d")
            self.root.ids.day6.text = self.theDays.day6.strftime("%d")
            self.root.ids.day7.text = self.theDays.day7.strftime("%d")

        elif self.theDays.day3 == value:
            self.root.ids.day1.text = self.theDays.day1.strftime("%d")
            self.root.ids.day2.text = self.theDays.day2.strftime("%d")
            self.root.ids.day3.text = "[color=#42f58d]"+ self.theDays.day3.strftime("%d") +"[/color]"
            self.root.ids.day4.text = self.theDays.day4.strftime("%d")
            self.root.ids.day5.text = self.theDays.day5.strftime("%d")
            self.root.ids.day6.text = self.theDays.day6.strftime("%d")
            self.root.ids.day7.text = self.theDays.day7.strftime("%d")

        elif self.theDays.day4 == value:
            self.root.ids.day1.text = self.theDays.day1.strftime("%d")
            self.root.ids.day2.text = self.theDays.day2.strftime("%d")
            self.root.ids.day3.text = self.theDays.day3.strftime("%d")
            self.root.ids.day4.text = "[color=#42f58d]"+ self.theDays.day4.strftime("%d") +"[/color]"
            self.root.ids.day5.text = self.theDays.day5.strftime("%d")
            self.root.ids.day6.text = self.theDays.day6.strftime("%d")
            self.root.ids.day7.text = self.theDays.day7.strftime("%d")

        elif self.theDays.day5 == value:
            self.root.ids.day1.text = self.theDays.day1.strftime("%d")
            self.root.ids.day2.text = self.theDays.day2.strftime("%d")
            self.root.ids.day3.text = self.theDays.day3.strftime("%d")
            self.root.ids.day4.text = self.theDays.day4.strftime("%d")
            self.root.ids.day5.text = "[color=#42f58d]"+ self.theDays.day5.strftime("%d") +"[/color]"
            self.root.ids.day6.text = self.theDays.day6.strftime("%d")
            self.root.ids.day7.text = self.theDays.day7.strftime("%d")

        elif self.theDays.day6 == value:
            self.root.ids.day1.text = self.theDays.day1.strftime("%d")
            self.root.ids.day2.text = self.theDays.day2.strftime("%d")
            self.root.ids.day3.text = self.theDays.day3.strftime("%d")
            self.root.ids.day4.text = self.theDays.day4.strftime("%d")
            self.root.ids.day5.text = self.theDays.day5.strftime("%d")
            self.root.ids.day6.text = "[color=#42f58d]"+ self.theDays.day6.strftime("%d") +"[/color]"
            self.root.ids.day7.text = self.theDays.day7.strftime("%d")

        else:
            self.root.ids.day1.text = self.theDays.day1.strftime("%d")
            self.root.ids.day2.text = self.theDays.day2.strftime("%d")
            self.root.ids.day3.text = self.theDays.day3.strftime("%d")
            self.root.ids.day4.text = self.theDays.day4.strftime("%d")
            self.root.ids.day5.text = self.theDays.day5.strftime("%d")
            self.root.ids.day6.text = self.theDays.day6.strftime("%d")
            self.root.ids.day7.text = "[color=#42f58d]"+ self.theDays.day7.strftime("%d") +"[/color]"
        

        
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
        query = "SELECT * FROM users WHERE email = %s"
        c.execute(query, (self.root.ids.user.text,))
        records = c.fetchone()
        print(records)
        

        if records:
            if records[1] == self.root.ids.user.text and records[2] == self.root.ids.password.text:
                self.root.ids.welcome_label.text = "Logged in successfully"
                loginCode = 1
                store.put('account', email=self.root.ids.user.text, password=self.root.ids.password.text)
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

    def register(self):
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
                if record[1] == self.root.ids.emailPrompt.text:
                    self.root.ids.welcome_label.text = "An account with these credentials already exists"
                else:
                    c.execute("INSERT INTO users (email, password, firstName, lastName) VALUES (%s, %s, %s, %s)", (self.root.ids.emailPrompt.text, self.root.ids.enterPass.text, self.root.ids.firstName.text, self.root.ids.lastName.text))
                    self.root.ids.welcome_label.text = "Account created successfully"
                    break
        else:
            c.execute("INSERT INTO users (email, password, firstName, lastName) VALUES (%s, %s, %s, %s)", (self.root.ids.emailPrompt.text, self.root.ids.enterPass.text, self.root.ids.firstName.text, self.root.ids.lastName.text))
            self.root.ids.welcome_label.text = "Account created successfully"
        conn.commit()
        conn.close()
        # redirect
        self.root.current = "login_sc"

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
        
        theYear = int(day7.strftime("%Y"))
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        #self.root.ids.currMonth.text = str(months[theMonth - 1])
        #self.root.ids.currYear.text = str(theYear)
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
        
        theYear = int(day7.strftime("%Y"))
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        #self.root.ids.currMonth.text = str(months[theMonth - 1])
        #self.root.ids.currYear.text = str(theYear)

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
                
    def current_day(self, instance):
        for key, val in self.root.ids.items():
            if "day" in key:
                if "[" in self.root.ids[key].text:
                    self.root.ids[key].text = self.root.ids[key].text.split(']')[1].split('[')[0]
        instance.text = "[color=#42f58d]" + instance.text + "[/color]"
    
    def taskFun_press(self, contentEvent):
		#int timeArray[24] = {0}
		#for i in range 24:
		#	if i = 0:
		#		i=i+12
		#		self.add_widget(Label(text=i))
		#	elif i > 12:
		#		i=i-12
		#		self.add_widget(Label(text=i))
		#	else:
		#		self.add_widget(Label(text=i))
		#timeArray[time] = contentEvent
        print(self.contentEvent)
		

MainApp().run()
