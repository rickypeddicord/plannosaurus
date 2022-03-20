from kivy.lang import Builder
from kivymd.app import MDApp
import psycopg2
import psycopg2.extras
import datetime
from datetime import *
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.picker import MDDatePicker, MDThemePicker
from colorpicker import MDColorPicker
from kivy.uix.tabbedpanel import TabbedPanel
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineListItem
from kivy.uix.checkbox import CheckBox
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.list import TwoLineAvatarIconListItem, OneLineAvatarIconListItem, ILeftBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.dialog import MDDialog
from kivy.utils import get_color_from_hex
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage, Image


events= []
todos = []
userid = -1
dateID = datetime.today().strftime("%m%d%Y")

img_1 = Image(
    source = 'basicwitch-removebg-preview.png',
    pos_hint = {"x": .71, "y": .45},
    size_hint = [.35, .35]
    )

img_2 = Image(
    source = 'crystals-removebg-preview.png',
    pos_hint = {"x": 0, "y": .05},
    size_hint = [.35, .35]
    )
    
citrusIMG1 = Image(
    source = 'orangeflow-removebg-preview.png',
    pos_hint = {"x": .71, "y": .45},
    size_hint = [.32, .32]
    )

citrusIMG2 = Image(
    source = 'yellowflow-removebg-preview.png',
    pos_hint = {"x": 0, "y": .05},
    size_hint = [.32, .32]
    )
    
origIMG1 = Image(
    source = 'dino2-removebg-preview.png',
    pos_hint = {"x": .71, "y": .45},
    size_hint = [.32, .32]
    )

origIMG2 = Image(
    source = 'dinog-removebg-preview.png',
    pos_hint = {"x": 0, "y": .05},
    size_hint = [.32, .32]
    )
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



    def event_add(self, root, time):
        global events
        global userid
        global dateID

        timesArr = ["6 AM", "7 AM", "8 AM", "9 AM", "10 AM", "11 AM", "12 PM", "1 PM", "2 PM", "3 PM", "4 PM", "5 PM", "6 PM", "7 PM", "8 PM", "9 PM"]
        militaryArr = ["06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"]
        index = timesArr.index(time)
        timeObj = datetime.strptime(militaryArr[index], '%H:%M').strftime("%H:%M")

        if index == 0:
            messageText = self.ids.contentEvent.text
        elif index == 1:
            messageText = self.ids.sevenAM.text
        elif index == 2:
            messageText = self.ids.eightAM.text
        elif index == 3:
            messageText = self.ids.nineAM.text
        elif index == 4:
            messageText = self.ids.tenAM.text
        elif index == 5:
            messageText = self.ids.elevenAM.text
        elif index == 6:
            messageText = self.ids.noon.text
        elif index == 7:
            messageText = self.ids.onePM.text
        elif index == 8:
            messageText = self.ids.twoPM.text
        elif index == 9:
            messageText = self.ids.threePM.text
        elif index == 10:
            messageText = self.ids.fourPM.text
        elif index == 11:
            messageText = self.ids.fivePM.text
        elif index == 12:
            messageText = self.ids.sixPM.text
        elif index == 13:
            messageText = self.ids.sevenPM.text
        elif index == 14:
            messageText = self.ids.eightPM.text
        elif index == 15:
            messageText = self.ids.ninePM.text
        

        conn = psycopg2.connect(
            host = "ec2-34-205-209-14.compute-1.amazonaws.com",
            database = "d19re7njihace8",
            user = "lveasasuicarlg",
            password = "c372ee6ba2bc15c476bf85a8258fa444d2a51f4323b6903a1963c0c5fb118a08",
            port = "5432",
        )

        # Create a cursor
        c = conn.cursor()

        if store.exists('account'):
            userid = store.get('account')['userid']
        
        c.execute("INSERT INTO events(dateID, timestamp, time, messageBody, userID) VALUES (%s, %s, %s, %s, %s)", (dateID, timeObj, time, time + " - " + messageText, userid))
        conn.commit()
        conn.close()
        
        self.ids.contentEvent.text = ''
        self.ids.sevenAM.text = ''
        self.ids.eightAM.text = ''
        self.ids.nineAM.text = ''
        self.ids.tenAM.text = ''
        self.ids.elevenAM.text = ''
        self.ids.noon.text = ''
        self.ids.onePM.text = ''
        self.ids.twoPM.text = ''
        self.ids.threePM.text = ''
        self.ids.fourPM.text = ''
        self.ids.fivePM.text = ''
        self.ids.sixPM.text = ''
        self.ids.sevenPM.text = ''
        self.ids.eightPM.text = ''
        self.ids.ninePM.text = ''


    def overview_images(self, root, image1, image2):
        global img_1
        global img_2
        global citrusIMG1
        global citrusIMG2
        global origIMG1
        global origIMG2
        
        self.ids.float.remove_widget(img_1)
        self.ids.float.remove_widget(img_2)
        self.ids.float.remove_widget(citrusIMG1)
        self.ids.float.remove_widget(citrusIMG2)
        self.ids.float.remove_widget(origIMG1)
        self.ids.float.remove_widget(origIMG2)
        
        self.ids.float.add_widget(image1)
        self.ids.float.add_widget(image2)

    def postEvents(self, root):
        global userid
        global events
        global dateID
        global origIMG1
        global origIMG2

        if store.exists('account'):
            userid = store.get('account')['userid']

     #   self.ids.contentEventMain.text = '' # reset textfield to be blank

        conn = psycopg2.connect(
            host = "ec2-34-205-209-14.compute-1.amazonaws.com",
            database = "d19re7njihace8",
            user = "lveasasuicarlg",
            password = "c372ee6ba2bc15c476bf85a8258fa444d2a51f4323b6903a1963c0c5fb118a08",
            port = "5432",
        )

        c = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM events WHERE userID = %s AND dateID = %s"
        c.execute(query, (userid, dateID,))
        records = c.fetchall()
        records.sort(key = lambda date: datetime.strptime(date[2], "%H:%M"))

        # query = "DELETE FROM events"
        # c.execute(query)

        
        self.ids['eventContainer'].clear_widgets()
        if records:
            for items in records:
                self.ids['eventContainer'].add_widget(EventItemWithCheckbox(text= '[b]' + items[4] + '[/b]'))

        conn.commit()
        conn.close()
        
        self.overview_images(root, origIMG1, origIMG2)
        
    
    def delete_eventFromAdd(self, root, time, the_event_item):
        global userid
        deleteItem = ''
        
        if the_event_item.text[0:3] == '[b]':
            deleteItem = the_event_item.text.split('[b]')[1].split('[/b]')[0]
        else:
            deleteItem = the_event_item.text.split('[s][b]')[1].split('[/b][/s]')[0]

        conn = psycopg2.connect(
            host = "ec2-34-205-209-14.compute-1.amazonaws.com",
            database = "d19re7njihace8",
            user = "lveasasuicarlg",
            password = "c372ee6ba2bc15c476bf85a8258fa444d2a51f4323b6903a1963c0c5fb118a08",
            port = "5432",
        )

        # Create a cursor
        c = conn.cursor()
        query = "DELETE FROM events WHERE userid = %s AND messageBody = %s"
        c.execute(query, (userid, deleteItem,))
        
        conn.commit()
        conn.close()
        
        # if records:
        #     for items in records:
        #         self.parent.remove_widget(the_event_item)
                
        
        
        
        #self.parent.remove_widget(the_event_item)
        if time == "6 AM":
            self.ids.contentEvent.disabled = False
            self.ids.contentEvent.text = ''
        elif time == "7 AM":
            self.ids.sevenAM.disabled = False
            self.ids.sevenAM.text = ''
    


class MainApp(MDApp):
    task_list_dialog = None
    customize_dialog = None
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
        c.execute("CREATE TABLE if not exists events(eventID SERIAL PRIMARY KEY, dateID VARCHAR(255), timestamp VARCHAR(255), time VARCHAR(255), messageBody VARCHAR(255), userID int REFERENCES users)")

        c.execute("CREATE TABLE if not exists todos(todoID SERIAL PRIMARY KEY, dateID VARCHAR(255), timestamp VARCHAR(255), todoItem VARCHAR(255), userID int REFERENCES users)")
        
        conn.commit()
        conn.close()

        self.gen_cal(date.today())

        

        return WindowManager()

    def on_start(self):
        Clock.schedule_once(self.set_screen, 0)

    def set_screen(self, dt):
        global store

        if store.exists('account'):
            self.root.init_load(self.root)
            self.root.postEvents(self.root)
            self.postTodo()
            self.root.current = "main_sc"
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
        global dateID
        init_date = datetime.strptime(dateID, "%m%d%Y")
        init_day = init_date.strftime("%#d")
        init_month = init_date.strftime("%#m")
        init_year = init_date.strftime("%Y")
        date_dialog = MDDatePicker(year=int(init_year), month=int(init_month), day=int(init_day))
        date_dialog.bind(on_save = self.on_save)
        date_dialog.open()
        

    def on_save(self, instance, value, date_range):
        global dateID
        dateID = value.strftime("%m%d%Y")
        self.gen_cal(value)
        self.root.postEvents(self.root)
        self.postTodo()

        
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
        

        if records:
            if records[1] == self.root.ids.user.text and records[2] == self.root.ids.password.text:
                self.root.ids.welcome_label.text = "Logged in successfully"
                loginCode = 1
                store.put('account', userid=records[0], email=self.root.ids.user.text, password=self.root.ids.password.text)
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
            self.root.ids.regLabel.text = "Fields cannot be empty"
            return
        elif self.root.ids.enterPass.text != self.root.ids.passReEnter.text:
            self.root.ids.enterPass.text = ''
            self.root.ids.passReEnter.text = ''
            self.root.ids.regLabel.text = 'Passwords must match.'
            return
        elif self.root.ids.enterPass.text == "" or self.root.ids.passReEnter.text == "":
            self.root.ids.regLabel.text = "Password fields required."
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
                    store.put('account', userid=record[0], email=self.root.ids.emailPrompt.text, password=self.root.ids.enterPass.text)
                    break
        else:
            c.execute("INSERT INTO users (email, password, firstName, lastName) VALUES (%s, %s, %s, %s)", (self.root.ids.emailPrompt.text, self.root.ids.enterPass.text, self.root.ids.firstName.text, self.root.ids.lastName.text))
            self.root.ids.welcome_label.text = "Account created successfully"
            store.put('account', userid=1, email=self.root.ids.emailPrompt.text, password=self.root.ids.enterPass.text)

        conn.commit()
        conn.close()
        # redirect
        self.root.current = "login_sc"
    
   

    def left_cal(self):
        global dateID
        newDate = ""
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
        
        dayHold = ""
        currMonth = ""
        currYear = ""
        for key, val in self.root.ids.items():
            if "day" in key:
                if "[" in self.root.ids[key].text:
                    self.root.ids[key].text = self.root.ids[key].text.split(']')[1].split('[')[0]
                    dayHold = self.root.ids[key] # save reference to current day id
        
        if dayHold.text == self.root.ids.day1.text:
            currMonth = day1.strftime("%#m")
            currYear = day1.strftime("%Y")
            currDay = day1.strftime("%#d")
        elif dayHold.text == self.root.ids.day2.text:
            currMonth = day2.strftime("%#m")
            currYear = day2.strftime("%Y")
            currDay = day2.strftime("%#d")
        elif dayHold.text == self.root.ids.day3.text:
            currMonth = day3.strftime("%#m")
            currYear = day3.strftime("%Y")
            currDay = day3.strftime("%#d")
        elif dayHold.text == self.root.ids.day4.text:
            currMonth = day4.strftime("%#m")
            currYear = day4.strftime("%Y")
            currDay = day4.strftime("%#d")
        elif dayHold.text == self.root.ids.day5.text:
            currMonth = day5.strftime("%#m")
            currYear = day5.strftime("%Y")
            currDay = day5.strftime("%#d")
        elif dayHold.text == self.root.ids.day6.text:
            currMonth = day6.strftime("%#m")
            currYear = day6.strftime("%Y")
            currDay = day6.strftime("%#d")
        else:
            currMonth = day7.strftime("%#m")
            currYear = day7.strftime("%Y")
            currDay = day7.strftime("%#d")

        
        self.root.ids.day1.text = day1.strftime("%d")
        self.root.ids.day2.text = day2.strftime("%d")
        self.root.ids.day3.text = day3.strftime("%d")
        self.root.ids.day4.text = day4.strftime("%d")
        self.root.ids.day5.text = day5.strftime("%d")
        self.root.ids.day6.text = day6.strftime("%d")
        self.root.ids.day7.text = day7.strftime("%d")

        newDate = currMonth + currDay + currYear
        
        dateID = datetime.strptime(newDate, '%m%d%Y').strftime("%m%d%Y")

        dayHold.text = "[color=#42f58d]" + dayHold.text + "[/color]" # change text color of same day of the week when shifted
        self.root.postEvents(self.root)

    def right_cal(self):
        global dateID

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

        dayHold = ""
        for key, val in self.root.ids.items():
            if "day" in key:
                if "[" in self.root.ids[key].text:
                    self.root.ids[key].text = self.root.ids[key].text.split(']')[1].split('[')[0]
                    dayHold = self.root.ids[key] # save reference to current day id

        if dayHold.text == self.root.ids.day1.text:
            currMonth = day1.strftime("%#m")
            currYear = day1.strftime("%Y")
            currDay = day1.strftime("%#d")
        elif dayHold.text == self.root.ids.day2.text:
            currMonth = day2.strftime("%#m")
            currYear = day2.strftime("%Y")
            currDay = day2.strftime("%#d")
        elif dayHold.text == self.root.ids.day3.text:
            currMonth = day3.strftime("%#m")
            currYear = day3.strftime("%Y")
            currDay = day3.strftime("%#d")
        elif dayHold.text == self.root.ids.day4.text:
            currMonth = day4.strftime("%#m")
            currYear = day4.strftime("%Y")
            currDay = day4.strftime("%#d")
        elif dayHold.text == self.root.ids.day5.text:
            currMonth = day5.strftime("%#m")
            currYear = day5.strftime("%Y")
            currDay = day5.strftime("%#d")
        elif dayHold.text == self.root.ids.day6.text:
            currMonth = day6.strftime("%#m")
            currYear = day6.strftime("%Y")
            currDay = day6.strftime("%#d")
        else:
            currMonth = day7.strftime("%#m")
            currYear = day7.strftime("%Y")
            currDay = day7.strftime("%#d")
        
        self.root.ids.day1.text = day1.strftime("%d")
        self.root.ids.day2.text = day2.strftime("%d")
        self.root.ids.day3.text = day3.strftime("%d")
        self.root.ids.day4.text = day4.strftime("%d")
        self.root.ids.day5.text = day5.strftime("%d")
        self.root.ids.day6.text = day6.strftime("%d")
        self.root.ids.day7.text = day7.strftime("%d")

        newDate = currMonth + currDay + currYear
        dateID = datetime.strptime(newDate, '%m%d%Y').strftime("%m%d%Y")

        dayHold.text = "[color=#42f58d]" + dayHold.text + "[/color]" # change text color of same day of the week when shifted
        self.root.postEvents(self.root)
                
    def current_day(self, instance):
        global dateID
        newDate = ''
        for key, val in self.root.ids.items():
            if "day" in key:
                if "[" in self.root.ids[key].text:
                    self.root.ids[key].text = self.root.ids[key].text.split(']')[1].split('[')[0]
        newDate = list(dateID)
        newDate[2] = instance.text[0]
        newDate[3] = instance.text[1]
        newDate = ''.join(newDate)
        dateID = datetime.strptime(newDate, '%m%d%Y').strftime("%m%d%Y")
        instance.text = "[color=#42f58d]" + instance.text + "[/color]"
        self.root.postEvents(self.root)

    def changeIt(self, rect_color):
        self.rect_color=1,0,0,1
        return
        
    def colorChangerPink(self, root):
        self.root.ids.contentEventMain.fill_color = [1, 0, .1, .5]
        self.root.ids.contentEventMain._set_fill_color([1, 0, .1, .5])
        
        self.root.ids.contentTODOMain.fill_color = [.8, 0, .5, .5]
        self.root.ids.contentTODOMain._set_fill_color([.8, 0, .5, .5])
        
        self.root.ids.addToDo.md_bg_color = [1, 0, 0, .8]
        self.root.ids.addTask.md_bg_color = [1, 0, 0, .8]
        
    def colorChangerCitrus(self, root):
        self.root.ids.contentEventMain.fill_color = [1, 1, 0, .5]
        self.root.ids.contentEventMain._set_fill_color([1, 1, 0, .5])
        
        self.root.ids.contentTODOMain.fill_color = [1, .5, 0, .5]
        self.root.ids.contentTODOMain._set_fill_color([1, .5, 0, .5])
        
        self.root.ids.addToDo.md_bg_color = [1, .5, 0, .8]
        self.root.ids.addTask.md_bg_color = [1, .5, 0, .8]
        global citrusIMG1
        global citrusIMG2
        self.root.overview_images(root, citrusIMG1, citrusIMG2)

    def colorChangerSpooky(self, root):
        self.root.ids.contentEventMain.fill_color = [.8,0,.8,0.6]
        self.root.ids.contentEventMain._set_fill_color([.8,0,.8,0.6])
        
        self.root.ids.contentTODOMain.fill_color = [.8,.7,.8,0.3]
        self.root.ids.contentTODOMain._set_fill_color([.8,.7,.8,0.3])
        
        self.root.ids.addToDo.md_bg_color = [0, 1, 0, .5]
        self.root.ids.addTask.md_bg_color = [0, 1, 0, .5]
        global img_1
        global img_2
        self.root.overview_images(root, img_1, img_2)

        
    def colorChangerOG(self, root):
        self.root.ids.contentEventMain.fill_color = [.5,1,.5,0.6]
        self.root.ids.contentEventMain._set_fill_color([.5,1,.5,0.6])
        
        self.root.ids.contentTODOMain.fill_color = [.5,.5,.8,0.6]
        self.root.ids.contentTODOMain._set_fill_color([.5,.5,.8,0.6])
        
        self.root.ids.addToDo.md_bg_color = [0, 1, 0, .5]
        self.root.ids.addTask.md_bg_color = [0, 1, 0, .5]
        global origIMG1
        global origIMG2
        self.root.overview_images(root, origIMG1, origIMG2)
        
        
    def show_customize_dialog(self):
        if not self.customize_dialog:
            self.customize_dialog=MDDialog(
                title="Customize",
                type="custom",
                content_cls=CustomizeDialog(),
            )
        self.customize_dialog.open()
    
    
    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()
        
    
    def customizeColor(self, root):
        
        self.root.ids.contentEventMain.fill_color = .5, 0, 0, .5
    
    def close_customize_dialog(self):
        self.customize_dialog.dismiss()
    
    def show_todolist_dialog(self):
        if not self.task_list_dialog:
            self.task_list_dialog=MDDialog(
                title="Create To-Do",
                type="custom",
                content_cls=DialogContent(),
            )
        self.task_list_dialog.content_cls.update_date()
        self.task_list_dialog.open()
    
    def close_todolist_dialog(self):
        self.task_list_dialog.dismiss()
    
    def add_todo(self, task, task_date):
        global userid
        global dateID
        global todos

        conn = psycopg2.connect(
            host = "ec2-34-205-209-14.compute-1.amazonaws.com",
            database = "d19re7njihace8",
            user = "lveasasuicarlg",
            password = "c372ee6ba2bc15c476bf85a8258fa444d2a51f4323b6903a1963c0c5fb118a08",
            port = "5432",
        )

        # Create a cursor
        c = conn.cursor()
        
        if store.exists('account'):
            userid = store.get('account')['userid']
            
        todoMessage = task.text
        
        c.execute("INSERT INTO todos(dateID, timestamp, todoItem, userID) VALUES (%s, %s, %s, %s)", (dateID, task_date, todoMessage, userid))
        
        self.root.ids['container'].add_widget(ListItemWithCheckbox(text='[b]'+task.text+'[/b]', secondary_text='[size=12]'+'have done by: '+ task_date+'[/size]'))

       
        conn.commit()
        conn.close()


    def postTodo(self):
        global userid
        global todos
        global dateID

        if store.exists('account'):
            userid = store.get('account')['userid']

        #self.root.ids.contentTODOMain.text = '' # reset textfield to be blank

        conn = psycopg2.connect(
            host = "ec2-34-205-209-14.compute-1.amazonaws.com",
            database = "d19re7njihace8",
            user = "lveasasuicarlg",
            password = "c372ee6ba2bc15c476bf85a8258fa444d2a51f4323b6903a1963c0c5fb118a08",
            port = "5432",
        )

        c = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM todos WHERE userID = %s AND dateID = %s"
        c.execute(query, (userid, dateID,))
        records = c.fetchall()
        print(records)
        
      #  self.root.ids['container'].add_widget(ListItemWithCheckbox(text='[b]'+task.text+'[/b]', secondary_text='[size=12]'+'have done by: '+ task_date+'[/size]'))
        self.root.ids['container'].clear_widgets()
        if records:
            for items in records:
                self.root.ids['container'].add_widget(ListItemWithCheckbox(text= '[b]' + items[3] + '[/b]', secondary_text='[size=12]'+'have done by: '+ items[2] +'[/size]'))
        
        
        conn.commit()
        
        conn.close()
        #task.text = ''


class CustomizeDialog(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
       # self.ids.date_text.text = str(datetime.now().strftime('%A %d %B %Y'))

class DialogContent(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global dateID
        formatedDate = datetime.strptime(dateID, "%m%d%Y")
        self.ids.date_text.text = str(formatedDate.strftime("%A %d %B %Y"))
        

    def update_date(self):
        global dateID
        formatedDate = datetime.strptime(dateID, "%m%d%Y")
        self.ids.date_text.text = str(formatedDate.strftime("%A %d %B %Y"))


    def show_date_picker(self):
        global dateID
        init_date = datetime.strptime(dateID, "%m%d%Y")
        init_day = init_date.strftime("%#d")
        init_month = init_date.strftime("%#m")
        init_year = init_date.strftime("%Y")
        date_dialog = MDDatePicker(year=int(init_year), month=int(init_month), day=int(init_day))
        date_dialog.bind(on_save = self.on_save)
        date_dialog.open()

    def on_save(self, instance, value, date_range):


        date = value.strftime('%A %d %B %Y')
        self.ids.date_text.text = str(date)
#class StickerClass():
 #   icon = StringProperty()
    
  #  def pickSticker(self):
   #     pass

     
class EventItemWithCheckbox(OneLineAvatarIconListItem):

    def __init__(self, pk=None, **kwargs):
        super().__init__(**kwargs)
        self.pk = pk


    def markEvent(self, check, the_event_item):
        if check.active == True:
            the_event_item.text = '[s]'+the_event_item.text+'[/s]'
        else:
            the_event_item.text = the_event_item.text.split('[s]')[1].split('[/s]')[0]

    def delete_event(self, the_event_item):
        global userid
        deleteItem = ''
        
        if the_event_item.text[0:3] == '[b]':
            deleteItem = the_event_item.text.split('[b]')[1].split('[/b]')[0]
        else:
            deleteItem = the_event_item.text.split('[s][b]')[1].split('[/b][/s]')[0]
        

        conn = psycopg2.connect(
            host = "ec2-34-205-209-14.compute-1.amazonaws.com",
            database = "d19re7njihace8",
            user = "lveasasuicarlg",
            password = "c372ee6ba2bc15c476bf85a8258fa444d2a51f4323b6903a1963c0c5fb118a08",
            port = "5432",
        )

        # Create a cursor
        c = conn.cursor()
        query = "DELETE FROM events WHERE userid = %s AND messageBody = %s"
        c.execute(query, (userid, deleteItem,))
        
        conn.commit()
        conn.close()
        
        self.parent.remove_widget(the_event_item)

# below class for Todos
class ListItemWithCheckbox(TwoLineAvatarIconListItem):


    def __init__(self, pk=None, **kwargs):
        super().__init__(**kwargs)
        self.pk = pk


    def mark(self, check, the_list_item):
        if check.active == True:
            the_list_item.text = '[s]'+the_list_item.text+'[/s]'
        else:
            the_list_item.text = the_list_item.text.split('[s]')[1].split('[/s]')[0]

    def delete_item(self, the_list_item):
        global userid
        deleteItem = ''

        if the_list_item.text[0:3] == '[b]':
            deleteItem = the_list_item.text.split('[b]')[1].split('[/b]')[0]
        else:
            deleteItem = the_list_item.text.split('[s][b]')[1].split('[/b][/s]')[0]
        

        conn = psycopg2.connect(
            host = "ec2-34-205-209-14.compute-1.amazonaws.com",
            database = "d19re7njihace8",
            user = "lveasasuicarlg",
            password = "c372ee6ba2bc15c476bf85a8258fa444d2a51f4323b6903a1963c0c5fb118a08",
            port = "5432",
        )

        # Create a cursor
        c = conn.cursor()
        query = "DELETE FROM todos WHERE userid = %s AND todoItem = %s"
        c.execute(query, (userid, deleteItem,))
        
        conn.commit()
        conn.close()
        self.parent.remove_widget(the_list_item)

#class RootWidget(BoxLayout):
 #   def __init__(self, **kwargs):
  #      super().__init__(**kwargs)
   # def colorChanger(self):
    #    rect_color=(1, 0, 0, 1)


class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    """creates checkbox for task"""

MainApp().run()