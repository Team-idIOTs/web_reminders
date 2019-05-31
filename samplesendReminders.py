import pyrebase
import sys, os
import json
sys.path.append(os.getcwd() + "/../reminders_lib/")
sys.path.append(os.getcwd() + "/../")
from Task import *
from config import *

task = Task('medicine', 'Eat your medicine', "Come on let's get it done")
task.add_reminder([4, 00], ['FRI', 'SAT', 'WED'], end_time=[5, 0], interval=[0, 1])

firebase = pyrebase.initialize_app(config)
db = firebase.database()
storage = firebase.storage()
task.to_firebase(db)
task.make_audio(storage)

#task.add_reminder([7, 30], ['THU'], end_time=[17, 0], interval=[0, 30])
#task.to_firebase(db)


#task.update_reminder(1, days=['THU', 'SUN'])
#task.to_firebase(db)
#tasks = db.get()
#for curr_task in tasks.each():
#    task = Task.from_dict(curr_task.val())