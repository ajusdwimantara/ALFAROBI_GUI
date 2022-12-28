#--------masih pake yaml--------#
# from yaml import *
# with open('GlobalConfig.yaml') as file:
#         docs = safe_load_all(file)

#         for doc in docs:
#             Torso_X = float(doc["kicking_v10"]["Torso_X"])
#             Torso_Y = float(doc["kicking_v10"]["Torso_Y"])
#             Torso_Z = float(doc["kicking_v10"]["Torso_Z"])
#             L_Shift_X = float(doc["kicking_v10"]["L_Shift_X"])
#             L_Shift_Y = float(doc["kicking_v10"]["L_Shift_Y"])
#             L_Shift_Z = float(doc["kicking_v10"]["L_Shift_Z"])
#             R_Shift_X = float(doc["kicking_v10"]["R_Shift_X"])
#             R_Shift_Y = float(doc["kicking_v10"]["R_Shift_Y"])
#             R_Shift_Z = float(doc["kicking_v10"]["R_Shift_Z"])
#             L_Lift_X = float(doc["kicking_v10"]["L_Lift_X"])
#             L_Lift_Y = float(doc["kicking_v10"]["L_Lift_Y"])
#             L_Lift_Z = float(doc["kicking_v10"]["L_Lift_Z"])
#             R_Lift_X = float(doc["kicking_v10"]["R_Lift_X"])
#             R_Lift_Y = float(doc["kicking_v10"]["R_Lift_Y"])
#             R_Lift_Z = float(doc["kicking_v10"]["R_Lift_Z"])
#             L_Swing_X = float(doc["kicking_v10"]["L_Swing_X"])
#             L_Swing_Y = float(doc["kicking_v10"]["L_Swing_Y"])
#             L_Swing_Z = float(doc["kicking_v10"]["L_Swing_Z"])
#             R_Swing_X = float(doc["kicking_v10"]["R_Swing_X"])
#             R_Swing_Y = float(doc["kicking_v10"]["R_Swing_Y"])
#             R_Swing_Z = float(doc["kicking_v10"]["R_Swing_Z"])
#             L_Retract_X = float(doc["kicking_v10"]["L_Retract_X"])
#             L_Retract_Y = float(doc["kicking_v10"]["L_Retract_Y"])
#             L_Retract_Z = float(doc["kicking_v10"]["L_Retract_Z"])
#             R_Retract_X = float(doc["kicking_v10"]["R_Retract_X"])
#             R_Retract_Y = float(doc["kicking_v10"]["R_Retract_Y"])
#             R_Retract_Z = float(doc["kicking_v10"]["R_Retract_Z"])

#             #-------Angle----------#
#             Torso_Pitch = float(doc["kicking_v10"]["Torso_Pitch"])
#             Shift_Roll = float(doc["kicking_v10"]["Shift_Roll"])
#             Lift_Roll = float(doc["kicking_v10"]["Lift_Roll"])
#             Lift_Pitch = float(doc["kicking_v10"]["Lift_Pitch"])
#             Swing_Roll = float(doc["kicking_v10"]["Swing_Roll"])
#             Swing_Pitch = float(doc["kicking_v10"]["Swing_Pitch"])
#             Retract_Roll = float(doc["kicking_v10"]["Retract_Roll"])
#             Retract_Pitch = float(doc["kicking_v10"]["Retract_Pitch"])

#             #----------Time-----------#
#             Shift_Time = float(doc["kicking_v10"]["SHIFT_TIME"])
#             Lift_Time = float(doc["kicking_v10"]["LIFT_TIME"])
#             Swing_Time = float(doc["kicking_v10"]["SWING_TIME"])
#             Retract_Time = float(doc["kicking_v10"]["RETRACT_TIME"])
#             Landing_Time = float(doc["kicking_v10"]["LANDING_TIME"])
#             Finished_Time = float(doc["kicking_v10"]["FINISHED_TIME"])

import json
import pyrebase
from GlobalConfig import *

#------------Retrieve Data From JSON------_#

# Opening JSON file
with open('/home/ajus/Desktop/alfarobi_ws/src/alfarobi_gui/config/GlobalConfig.json', 'r') as openfile:

	# Reading from json file
	json_object = json.load(openfile)

kicking_data = json_object["kicking_v10"]

Torso_X = float(kicking_data["Torso_X"])
Torso_Y = float(kicking_data["Torso_Y"])
Torso_Z = float(kicking_data["Torso_Z"])
L_Shift_X = float(kicking_data["L_Shift_X"])
L_Shift_Y = float(kicking_data["L_Shift_Y"])
L_Shift_Z = float(kicking_data["L_Shift_Z"])
R_Shift_X = float(kicking_data["R_Shift_X"])
R_Shift_Y = float(kicking_data["R_Shift_Y"])
R_Shift_Z = float(kicking_data["R_Shift_Z"])
L_Lift_X = float(kicking_data["L_Lift_X"])
L_Lift_Y = float(kicking_data["L_Lift_Y"])
L_Lift_Z = float(kicking_data["L_Lift_Z"])
R_Lift_X = float(kicking_data["R_Lift_X"])
R_Lift_Y = float(kicking_data["R_Lift_Y"])
R_Lift_Z = float(kicking_data["R_Lift_Z"])
L_Swing_X = float(kicking_data["L_Swing_X"])
L_Swing_Y = float(kicking_data["L_Swing_Y"])
L_Swing_Z = float(kicking_data["L_Swing_Z"])
R_Swing_X = float(kicking_data["R_Swing_X"])
R_Swing_Y = float(kicking_data["R_Swing_Y"])
R_Swing_Z = float(kicking_data["R_Swing_Z"])
L_Retract_X = float(kicking_data["L_Retract_X"])
L_Retract_Y = float(kicking_data["L_Retract_Y"])
L_Retract_Z = float(kicking_data["L_Retract_Z"])
R_Retract_X = float(kicking_data["R_Retract_X"])
R_Retract_Y = float(kicking_data["R_Retract_Y"])
R_Retract_Z = float(kicking_data["R_Retract_Z"])

#-------Angle----------#
Torso_Pitch = float(kicking_data["Torso_Pitch"])
Shift_Roll = float(kicking_data["Shift_Roll"])
Lift_Roll = float(kicking_data["Lift_Roll"])
Lift_Pitch = float(kicking_data["Lift_Pitch"])
Swing_Roll = float(kicking_data["Swing_Roll"])
Swing_Pitch = float(kicking_data["Swing_Pitch"])
Retract_Roll = float(kicking_data["Retract_Roll"])
Retract_Pitch = float(kicking_data["Retract_Pitch"])

#----------Time-----------#
Shift_Time = float(kicking_data["SHIFT_TIME"])
Lift_Time = float(kicking_data["LIFT_TIME"])
Swing_Time = float(kicking_data["SWING_TIME"])
Retract_Time = float(kicking_data["RETRACT_TIME"])
Landing_Time = float(kicking_data["LANDING_TIME"])
Finished_Time = float(kicking_data["FINISHED_TIME"])

#---------Upload Data To The Firebase-------#

conf = Config()

if(is_updated==True and internet_status==True):
    data={"kicking_v10/0":{
    "Torso_X": Torso_X, 
    "Torso_Y": Torso_Y,
    "Torso_Z": Torso_Z,
    "L_Shift_X": L_Shift_X,
    "L_Shift_Y": L_Shift_Y, 
    "L_Shift_Z": L_Shift_Z,
    "R_Shift_X": R_Shift_X,
    "R_Shift_Y": R_Shift_Y, 
    "R_Shift_Z": R_Shift_Z,
    "L_Lift_X": L_Lift_X,
    "L_Lift_Y": L_Lift_Y,
    "L_Lift_Z": L_Lift_Z,
    "R_Lift_X": R_Lift_X, 
    "R_Lift_Y": R_Lift_Y,
    "R_Lift_Z": R_Lift_Z,
    "L_Swing_X": L_Swing_X,
    "L_Swing_Y": L_Swing_Y,
    "L_Swing_Z": L_Swing_Z,
    "R_Swing_X": R_Swing_X, 
    "R_Swing_Y": R_Swing_Y,
    "R_Swing_Z": R_Swing_Z,
    "L_Retract_X": L_Retract_X,
    "L_Retract_Y": L_Retract_Y,
    "L_Retract_Z": L_Retract_Z,
    "R_Retract_X": R_Retract_X,
    "R_Retract_Y": R_Retract_Y,
    "R_Retract_Z": R_Retract_Z,
    "Torso_Pitch": Torso_Pitch, 
    "Shift_Roll": Shift_Roll,
    "Lift_Roll": Lift_Roll,
    "Lift_Pitch": Lift_Pitch, 
    "Swing_Roll": Swing_Roll,
    "Swing_Pitch": Swing_Pitch, 
    "Retract_Roll": Retract_Roll,
    "Retract_Pitch": Retract_Pitch, 
    "SHIFT_TIME": Shift_Time,
    "LIFT_TIME": Lift_Time,
    "SWING_TIME": Swing_Time,
    "RETRACT_TIME": Retract_Time, 
    "LANDING_TIME": Landing_Time, 
    "FINISHED_TIME": Finished_Time}
    }
    conf.db.update(data)
    print("Data updated succesfully")
elif(is_updated==False and internet_status==True):
    print("Data already up to date")
elif(is_updated==True and internet_status==False):
    print("Updating data requires internet connection")

#----------Retrieve Data From The Firebase---------#

# kicking_data = conf.db.child("kicking_v10").child("0").get()

# Torso_X = float(kicking_data.val()["Torso_X"])
# Torso_Y = float(kicking_data.val()["Torso_Y"])
# Torso_Z = float(kicking_data.val()["Torso_Z"])
# L_Shift_X = float(kicking_data.val()["L_Shift_X"])
# L_Shift_Y = float(kicking_data.val()["L_Shift_Y"])
# L_Shift_Z = float(kicking_data.val()["L_Shift_Z"])
# R_Shift_X = float(kicking_data.val()["R_Shift_X"])
# R_Shift_Y = float(kicking_data.val()["R_Shift_Y"])
# R_Shift_Z = float(kicking_data.val()["R_Shift_Z"])
# L_Lift_X = float(kicking_data.val()["L_Lift_X"])
# L_Lift_Y = float(kicking_data.val()["L_Lift_Y"])
# L_Lift_Z = float(kicking_data.val()["L_Lift_Z"])
# R_Lift_X = float(kicking_data.val()["R_Lift_X"])
# R_Lift_Y = float(kicking_data.val()["R_Lift_Y"])
# R_Lift_Z = float(kicking_data.val()["R_Lift_Z"])
# L_Swing_X = float(kicking_data.val()["L_Swing_X"])
# L_Swing_Y = float(kicking_data.val()["L_Swing_Y"])
# L_Swing_Z = float(kicking_data.val()["L_Swing_Z"])
# R_Swing_X = float(kicking_data.val()["R_Swing_X"])
# R_Swing_Y = float(kicking_data.val()["R_Swing_Y"])
# R_Swing_Z = float(kicking_data.val()["R_Swing_Z"])
# L_Retract_X = float(kicking_data.val()["L_Retract_X"])
# L_Retract_Y = float(kicking_data.val()["L_Retract_Y"])
# L_Retract_Z = float(kicking_data.val()["L_Retract_Z"])
# R_Retract_X = float(kicking_data.val()["R_Retract_X"])
# R_Retract_Y = float(kicking_data.val()["R_Retract_Y"])
# R_Retract_Z = float(kicking_data.val()["R_Retract_Z"])

# #-------Angle----------#
# Torso_Pitch = float(kicking_data.val()["Torso_Pitch"])
# Shift_Roll = float(kicking_data.val()["Shift_Roll"])
# Lift_Roll = float(kicking_data.val()["Lift_Roll"])
# Lift_Pitch = float(kicking_data.val()["Lift_Pitch"])
# Swing_Roll = float(kicking_data.val()["Swing_Roll"])
# Swing_Pitch = float(kicking_data.val()["Swing_Pitch"])
# Retract_Roll = float(kicking_data.val()["Retract_Roll"])
# Retract_Pitch = float(kicking_data.val()["Retract_Pitch"])

# #----------Time-----------#
# Shift_Time = float(kicking_data.val()["SHIFT_TIME"])
# Lift_Time = float(kicking_data.val()["LIFT_TIME"])
# Swing_Time = float(kicking_data.val()["SWING_TIME"])
# Retract_Time = float(kicking_data.val()["RETRACT_TIME"])
# Landing_Time = float(kicking_data.val()["LANDING_TIME"])
# Finished_Time = float(kicking_data.val()["FINISHED_TIME"])
