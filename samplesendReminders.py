import pyrebase
import sys, os
import json
sys.path.append(os.getcwd() + "/../dp_lib/")
sys.path.append(os.getcwd() + "/../")
from Task import *
from config import *

task = Task('medicine', 'Take Aspirin', "Fucking take the aspirin bitch")
task.add_reminder([9, 0], ['MON', 'SAT', 'WED'], end_time=[17, 0], interval=[1, 0])

firebase = pyrebase.initialize_app(config)
db = firebase.database()
task.to_firebase(db)

tasks = db.get()
for stuff in tasks.each():
    task = Task.from_dict(stuff.val())