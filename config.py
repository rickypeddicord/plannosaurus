import datetime
from datetime import *
from kivy.storage.jsonstore import JsonStore

store = JsonStore('account.json')
userid = -1
dateID = datetime.today().strftime("%m%d%Y")
