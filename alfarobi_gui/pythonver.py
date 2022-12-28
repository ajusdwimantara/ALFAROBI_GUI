#!/usr/bin/env python3
# call_py3.py
# Try to print out the python version
import sys
import platform
import rospy

rospy.init_node("call_py3")
print("\n\nPython Version:\n")
print(sys.version)
print(platform.python_version())
print("\n\n")
rospy.spin()