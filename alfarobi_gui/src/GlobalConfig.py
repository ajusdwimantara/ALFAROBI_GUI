import pyrebase
import rospy
from connectionCheck import *

class Config:
    def __init__(self) -> None:
        self.firebaseConfig = {
        "apiKey": "AIzaSyDzM2uN5ZfHXe7aeivzgYud67NQHHG62tk",
        "authDomain": "globalconfig-13.firebaseapp.com",
        "projectId": "globalconfig-13",
        "storageBucket": "globalconfig-13.appspot.com",
        "messagingSenderId": "443673025165",
        "appId": "1:443673025165:web:68e69d66a84d63786720c4",
        "measurementId": "G-X02B65KJLS".capitalize,
        "databaseURL": "https://globalconfig-13-default-rtdb.firebaseio.com/",
        "serviceAccount": "/home/ajus/Desktop/alfarobi_ws/src/alfarobi_gui/config/globalconfig-13-firebase-adminsdk-utz1p-f392606d39.json"
        }

        self.firebase = pyrebase.initialize_app(self.firebaseConfig)
        self.db = self.firebase.database()

        self.init_pose = False

    
    def push_data():
        pass
