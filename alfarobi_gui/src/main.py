#!/usr/bin/python3.9
from AlfarobiWorkspace import *
from MainMenu import *
from tkinter import *

if __name__ == "__main__":
    try:
        rospy.init_node('alfarobi_gui_node', anonymous=True)
        root = Page1()

        root.start()
    except Exception as err:
        print("error occurs :", err)
    
    