from tkinter import *
from alfarobi_gui.msg import KickingParam
from std_msgs.msg import String
from KickingConfig import *

class KickingPg:
    def __init__(self) -> None:
        # ----kick_window Initialization---- #
        self.kick_window = Tk(
    
        )
    
        self.kick_window.geometry("1280x860")
        self.kick_window.title("ALFAROBI GUI")
        self.kick_window.config(bg= "#C0C0C0")
        self.kick_window.resizable(width=FALSE, height=FALSE)
        #----------Publisher---------#
        self.kick_param_pub = rospy.Publisher('/kick_param', KickingParam, queue_size=5)
        self.kick_button_pub = rospy.Publisher('/kick_button', String, queue_size=5)
        self.kicking_page_pub = rospy.Publisher('/motion_page', String, queue_size=5)

        self.Param = KickingParam()
        self.button = String()
        self.kicking_page = "kicking"
        self.kicking_page_pub.publish(self.kicking_page)
        
        #-------Page Title---------#
        self.PageTitleFrame = Frame(
            master = self.kick_window,
            height=100,
            width=640,
            bg="blue"
        )
        self.PageTitleFrame.pack()
        
        self.titleLabel = Label(
            master=self.PageTitleFrame,
            text="KICKING",
            font=("Modern", 60),
            fg="black",
            bg="#C0C0C0"
        )
        self.titleLabel.pack()

        # ----Robot Information-----------#
        # Variable that will store robot information given in page 1
        self.name = str()
        self.id = int()
        # Frame
        self.robotInfoFrame  = Frame(
            master=self.kick_window,
            width=640,
            height=100,
            bg="black",
            borderwidth=10,
        )
        self.robotInfoFrame.pack()
        self.robotInfoFrame.place(
            x = 20,
            y = 15
        )

        # Name
        self.robot_name = Label(
            master=self.robotInfoFrame,
            text="ROBOT: ",
            font=('MODERN', 10),
            foreground="white",
            background="black",
        )
        self.robot_name.pack()

        # ID
        self.robot_id = Label(
            master=self.robotInfoFrame,
            text="ID: ",
            font=('MODERN', 10),
            foreground="white",
            background="black",
        )
        self.robot_id.pack()

        #------------KICKING PARAMETERS---------#

        #-------------TORSO----------#
        self.torsoFrame = Frame(
            master = self.kick_window,
            bg="black",
            width=450,
            height=800,
            borderwidth=10,
        )
        self.torsoFrame.pack()
        self.torsoFrame.place(
            x = 900,
            y = 50,
        )
        self.Torso_X_Temp = float(Torso_X)
        self.TORSO_X = Label(
            master=self.torsoFrame,
            width=19,
            height=1,
            bg="white",
            fg = "black",
            text= "TORSO_X: " + str(self.Torso_X_Temp),
            font=("Modern", 12),
            
        )
        self.TORSO_X.pack(pady=4)

        self.Torso_Y_Temp = float(Torso_Y)
        self.TORSO_Y = Label(
            master=self.torsoFrame,
            width=19,
            height=1,
            bg="white",
            fg = "black",
            text= "TORSO_Y: " + str(self.Torso_Y_Temp),
            font=("Modern", 12),
            
        )
        self.TORSO_Y.pack(pady=4)

        self.Torso_Z_Temp = float(Torso_Z)
        self.TORSO_Z = Label(
            master=self.torsoFrame,
            width=19,
            height=1,
            bg="white",
            fg = "black",
            text= "TORSO_Y: " + str(self.Torso_Z_Temp),
            font=("Modern", 12),
            
        )
        self.TORSO_Z.pack(pady=4)

        # button
        self.TORSO_X_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.TORSO_X_UP_CB()
        )
        self.TORSO_X_UP.pack()
        self.TORSO_X_UP.place(
            x = 1135,
            y = 62
        )
        self.TORSO_X_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.TORSO_X_DOWN_CB()
        )
        self.TORSO_X_DOWN.pack()
        self.TORSO_X_DOWN.place(
            x = 1175,
            y = 62
        )

        self.TORSO_Y_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.TORSO_Y_UP_CB()
        )
        self.TORSO_Y_UP.pack()
        self.TORSO_Y_UP.place(
            x = 1135,
            y = 92
        )
        self.TORSO_Y_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.TORSO_Y_DOWN_CB()
        )
        self.TORSO_Y_DOWN.pack()
        self.TORSO_Y_DOWN.place(
            x = 1175,
            y = 92
        )

        self.TORSO_Z_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.TORSO_Z_UP_CB()
        )
        self.TORSO_Z_UP.pack()
        self.TORSO_Z_UP.place(
            x = 1135,
            y = 126
        )
        self.TORSO_Z_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.TORSO_Z_DOWN_CB()
        )
        self.TORSO_Z_DOWN.pack()
        self.TORSO_Z_DOWN.place(
            x = 1175,
            y = 126
        )

        #-------Leg Movement--------------#

        # Label
        # left
        self.leftLegFrame = Frame(
            master = self.kick_window,
            bg="black",
            width=450,
            height=800,
            borderwidth=10,
        )
        self.leftLegFrame.pack()
        self.leftLegFrame.place(
            x = 20,
            y = 220,
        )
        self.L_Shift_X_Temp = float(L_Shift_X)
        self.L_SHIFT_X = Label(
            master=self.leftLegFrame,
            width=19,
            height=1,
            bg="white",
            fg = "black",
            text= "L_SHIFT_X: " + str(L_Shift_X),
            font=("Modern", 12),
            
        )
        self.L_SHIFT_X.pack(pady=4)

        self.L_Shift_Y_Temp = float(L_Shift_Y)
        self.L_SHIFT_Y = Label(
            master=self.leftLegFrame,
            width=19,
            height=1,
            bg="white",
            fg = "black",
            text= "L_SHIFT_Y: "+str(L_Shift_Y),
            font=("Modern", 12)
        )
        self.L_SHIFT_Y.pack(pady=4)

        self.L_Shift_Z_Temp = float(L_Shift_Z)
        self.L_SHIFT_Z = Label(
            master=self.leftLegFrame,
            width=19,
            height=1,
            bg="white",
            fg = "black",
            text= "L_SHIFT_Z: "+str(L_Shift_Z),
            font=("Modern", 12)
        )
        self.L_SHIFT_Z.pack(pady=4)

        self.L_Lift_X_Temp = float(L_Lift_X)
        self.L_LIFT_X = Label(
            master=self.leftLegFrame,
            width=19,
            height=1,
            bg="white",
            fg = "black",
            text= "L_LIFT_X: "+str(L_Lift_X),
            font=("Modern", 12)
        )
        self.L_LIFT_X.pack(pady=4)

        self.L_Lift_Y_Temp = float(L_Lift_Y)
        self.L_LIFT_Y = Label(
            master=self.leftLegFrame,
            width=19,
            height=1,
            bg="white",
            fg = "black",
            text= "L_LIFT_Y: "+str(L_Lift_Y),
            font=("Modern", 12)
        )
        self.L_LIFT_Y.pack(pady=4)

        self.L_Lift_Z_Temp = float(L_Lift_Z)
        self.L_LIFT_Z = Label(
            master=self.leftLegFrame,
            width=19,
            height=1,
            bg="white",
            fg = "black",
            text= "L_LIFT_Z: "+str(L_Lift_Z),
            font=("Modern", 12)
        )
        self.L_LIFT_Z.pack(pady=4)

        self.L_Swing_X_Temp = float(L_Swing_X)
        self.L_SWING_X = Label(
            master=self.leftLegFrame,
            width=19,
            height=1,
            bg="white",
            fg = "black",
            text= "L_SWING_X: "+str(L_Swing_X),
            font=("Modern", 12)
        )
        self.L_SWING_X.pack(pady=4)

        self.L_Swing_Y_Temp = float(L_Swing_Y)
        self.L_SWING_Y = Label(
            master=self.leftLegFrame,
            width=19,
            height=1,
            bg="white",
            fg = "black",
            text= "L_SWING_Y: "+str(L_Swing_Y),
            font=("Modern", 12)
        )
        self.L_SWING_Y.pack(pady=4)

        self.L_Swing_Z_Temp = float(L_Swing_Z)
        self.L_SWING_Z = Label(
            master=self.leftLegFrame,
            width=19,
            height=1,
            bg="white",
            fg = "black",
            text= "L_SWING_Z: "+str(L_Swing_Z),
            font=("Modern", 12)
        )
        self.L_SWING_Z.pack(pady=4)

        self.L_Retract_X_Temp = float(L_Retract_X)
        self.L_RETRACT_X = Label(
            master=self.leftLegFrame,
            width=19,
            height=1,
            bg="white",
            fg = "black",
            text= "L_RETRACT_X: "+str(L_Retract_X),
            font=("Modern", 12)
        )
        self.L_RETRACT_X.pack(pady=4)

        self.L_Retract_Y_Temp = float(L_Retract_Y)
        self.L_RETRACT_Y = Label(
            master=self.leftLegFrame,
            width=19,
            height=1,
            bg="white",
            fg = "black",
            text= "L_RETRACT_Y: "+str(L_Retract_Y),
            font=("Modern", 12)
        )
        self.L_RETRACT_Y.pack(pady=4)

        self.L_Retract_Z_Temp = float(L_Retract_Z)
        self.L_RETRACT_Z = Label(
            master=self.leftLegFrame,
            width=19,
            height=1,
            bg="white",
            fg = "black",
            text= "L_RETRACT_Z: "+str(L_Retract_Z),
            font=("Modern", 12)
        )
        self.L_RETRACT_Z.pack(pady=4)

        # right
        self.rightLegFrame = Frame(
            master = self.kick_window,
            bg="black",
            width=450,
            height=800,
            borderwidth=10,
        )
        self.rightLegFrame.pack()
        self.rightLegFrame.place(
            x = 900,
            y = 220,
        )
        self.R_Shift_X_Temp = float(R_Shift_X)
        self.R_SHIFT_X = Label(
            master=self.rightLegFrame,
            width=19,
            height=1,
            bg="white",
            fg = "black",
            text= "R_SHIFT_X: " + str(R_Shift_X),
            font=("Modern", 12),
            
        )
        self.R_SHIFT_X.pack(pady=4)

        self.R_Shift_Y_Temp = float(R_Shift_Y)
        self.R_SHIFT_Y = Label(
            master=self.rightLegFrame,
            width=19,
            height=1,
            bg="white",
            fg = "black",
            text= "R_SHIFT_Y: "+str(R_Shift_Y),
            font=("Modern", 12)
        )
        self.R_SHIFT_Y.pack(pady=4)

        self.R_Shift_Z_Temp = float(R_Shift_Z)
        self.R_SHIFT_Z = Label(
            master=self.rightLegFrame,
            width=19,
            height=1,
            bg="white",
            fg = "black",
            text= "R_SHIFT_Z: "+str(R_Shift_Z),
            font=("Modern", 12)
        )
        self.R_SHIFT_Z.pack(pady=4)

        self.R_Lift_X_Temp = float(R_Lift_X)
        self.R_LIFT_X = Label(
            master=self.rightLegFrame,
            width=19,
            height=1,
            bg="white",
            fg = "black",
            text= "R_LIFT_X: "+str(R_Lift_X),
            font=("Modern", 12)
        )
        self.R_LIFT_X.pack(pady=4)

        self.R_Lift_Y_Temp = float(R_Lift_Y)
        self.R_LIFT_Y = Label(
            master=self.rightLegFrame,
            width=19,
            height=1,
            bg="white",
            fg = "black",
            text= "R_LIFT_Y: "+str(R_Lift_Y),
            font=("Modern", 12)
        )
        self.R_LIFT_Y.pack(pady=4)

        self.R_Lift_Z_Temp = float(R_Lift_Z)
        self.R_LIFT_Z = Label(
            master=self.rightLegFrame,
            width=19,
            height=1,
            bg="white",
            fg = "black",
            text= "R_LIFT_Z: "+str(R_Lift_Z),
            font=("Modern", 12)
        )
        self.R_LIFT_Z.pack(pady=4)

        self.R_Swing_X_Temp = float(R_Swing_X)
        self.R_SWING_X = Label(
            master=self.rightLegFrame,
            width=19,
            height=1,
            bg="white",
            fg = "black",
            text= "R_SWING_X: "+str(R_Swing_X),
            font=("Modern", 12)
        )
        self.R_SWING_X.pack(pady=4)

        self.R_Swing_Y_Temp = float(R_Swing_Y)
        self.R_SWING_Y = Label(
            master=self.rightLegFrame,
            width=19,
            height=1,
            bg="white",
            fg = "black",
            text= "R_SWING_Y: "+str(R_Swing_Y),
            font=("Modern", 12)
        )
        self.R_SWING_Y.pack(pady=4)

        self.R_Swing_Z_Temp = float(R_Swing_Z)
        self.R_SWING_Z = Label(
            master=self.rightLegFrame,
            width=19,
            height=1,
            bg="white",
            fg = "black",
            text= "R_SWING_Z: "+str(R_Swing_Z),
            font=("Modern", 12)
        )
        self.R_SWING_Z.pack(pady=4)

        self.R_Retract_X_Temp = float(R_Retract_X)
        self.R_RETRACT_X = Label(
            master=self.rightLegFrame,
            width=19,
            height=1,
            bg="white",
            fg = "black",
            text= "R_RETRACT_X: "+str(R_Retract_X),
            font=("Modern", 12)
        )
        self.R_RETRACT_X.pack(pady=4)

        self.R_Retract_Y_Temp = float(R_Retract_Y)
        self.R_RETRACT_Y = Label(
            master=self.rightLegFrame,
            width=19,
            height=1,
            bg="white",
            fg = "black",
            text= "R_RETRACT_Y: "+str(R_Retract_Y),
            font=("Modern", 12)
        )
        self.R_RETRACT_Y.pack(pady=4)

        self.R_Retract_Z_Temp = float(R_Retract_Z)
        self.R_RETRACT_Z = Label(
            master=self.rightLegFrame,
            width=19,
            height=1,
            bg="white",
            fg = "black",
            text= "R_RETRACT_Z: "+str(R_Retract_Z),
            font=("Modern", 12)
        )
        self.R_RETRACT_Z.pack(pady=4)

        # Button
        # left 
        self.L_SHIFT_X_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.L_SHIFT_X_UP_CB()
        )
        self.L_SHIFT_X_UP.pack()
        self.L_SHIFT_X_UP.place(
            x = 255,
            y = 233
        )
        self.L_SHIFT_X_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.L_SHIFT_X_DOWN_CB()
        )
        self.L_SHIFT_X_DOWN.pack()
        self.L_SHIFT_X_DOWN.place(
            x = 295,
            y = 233
        )

        self.L_SHIFT_Y_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.L_SHIFT_Y_UP_CB()
        )
        self.L_SHIFT_Y_UP.pack()
        self.L_SHIFT_Y_UP.place(
            x = 255,
            y = 265
        )
        self.L_SHIFT_Y_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.L_SHIFT_Y_DOWN_CB()
        )
        self.L_SHIFT_Y_DOWN.pack()
        self.L_SHIFT_Y_DOWN.place(
            x = 295,
            y = 265
        )

        
        self.L_SHIFT_Z_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.L_SHIFT_Z_UP_CB()
        )
        self.L_SHIFT_Z_UP.pack()
        self.L_SHIFT_Z_UP.place(
            x = 255,
            y = 295
        )
        self.L_SHIFT_Z_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.L_SHIFT_Z_DOWN_CB()
        )
        self.L_SHIFT_Z_DOWN.pack()
        self.L_SHIFT_Z_DOWN.place(
            x = 295,
            y = 295
        )

        
        self.L_LIFT_X_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.L_LIFT_X_UP_CB()
        )
        self.L_LIFT_X_UP.pack()
        self.L_LIFT_X_UP.place(
            x = 255,
            y = 327
        )
        self.L_LIFT_X_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.L_LIFT_X_DOWN_CB()
        )
        self.L_LIFT_X_DOWN.pack()
        self.L_LIFT_X_DOWN.place(
            x = 295,
            y = 327
        )
        
        self.L_LIFT_Y_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.L_LIFT_Y_UP_CB()
        )
        self.L_LIFT_Y_UP.pack()
        self.L_LIFT_Y_UP.place(
            x = 255,
            y = 357
        )
        self.L_LIFT_Y_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.L_LIFT_Y_DOWN_CB()
        )
        self.L_LIFT_Y_DOWN.pack()
        self.L_LIFT_Y_DOWN.place(
            x = 295,
            y = 357
        )
        
        self.L_LIFT_Z_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.L_LIFT_Z_UP_CB()
        )
        self.L_LIFT_Z_UP.pack()
        self.L_LIFT_Z_UP.place(
            x = 255,
            y = 388
        )
        self.L_LIFT_Z_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.L_LIFT_Z_DOWN_CB()
        )
        self.L_LIFT_Z_DOWN.pack()
        self.L_LIFT_Z_DOWN.place(
            x = 295,
            y = 388
        )
        
        self.L_SWING_X_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.L_SWING_X_UP_CB()
        )
        self.L_SWING_X_UP.pack()
        self.L_SWING_X_UP.place(
            x = 255,
            y = 419
        )
        self.L_SWING_X_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.L_SWING_X_DOWN_CB()
        )
        self.L_SWING_X_DOWN.pack()
        self.L_SWING_X_DOWN.place(
            x = 295,
            y = 419
        )

        self.L_SWING_Y_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.L_SWING_Y_UP_CB()
        )
        self.L_SWING_Y_UP.pack()
        self.L_SWING_Y_UP.place(
            x = 255,
            y = 449
        )
        self.L_SWING_Y_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.L_SWING_Y_DOWN_CB()
        )
        self.L_SWING_Y_DOWN.pack()
        self.L_SWING_Y_DOWN.place(
            x = 295,
            y = 449
        )

        self.L_SWING_Z_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.L_SWING_Z_UP_CB()
        )
        self.L_SWING_Z_UP.pack()
        self.L_SWING_Z_UP.place(
            x = 255,
            y = 482
        )
        self.L_SWING_Z_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.L_SWING_Z_DOWN_CB()
        )
        self.L_SWING_Z_DOWN.pack()
        self.L_SWING_Z_DOWN.place(
            x = 295,
            y = 482
        )
        
        self.L_RETRACT_X_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.L_RETRACT_X_UP_CB()
        )
        self.L_RETRACT_X_UP.pack()
        self.L_RETRACT_X_UP.place(
            x = 255,
            y = 513
        )
        self.L_RETRACT_X_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.L_RETRACT_X_DOWN_CB()
        )
        self.L_RETRACT_X_DOWN.pack()
        self.L_RETRACT_X_DOWN.place(
            x = 295,
            y = 513
        )

        self.L_RETRACT_Y_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.L_RETRACT_Y_UP_CB()
        )
        self.L_RETRACT_Y_UP.pack()
        self.L_RETRACT_Y_UP.place(
            x = 255,
            y = 544
        )
        self.L_RETRACT_Y_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.L_RETRACT_Y_DOWN_CB()
        )
        self.L_RETRACT_Y_DOWN.pack()
        self.L_RETRACT_Y_DOWN.place(
            x = 295,
            y = 544
        )

        self.L_RETRACT_Z_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.L_RETRACT_Z_UP_CB()
        )
        self.L_RETRACT_Z_UP.pack()
        self.L_RETRACT_Z_UP.place(
            x = 255,
            y = 575
        )
        self.L_RETRACT_Z_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.L_RETRACT_Z_DOWN_CB()
        )
        self.L_RETRACT_Z_DOWN.pack()
        self.L_RETRACT_Z_DOWN.place(
            x = 295,
            y = 575
        )

        # right
        self.R_SHIFT_X_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.R_SHIFT_X_UP_CB()
        )
        self.R_SHIFT_X_UP.pack()
        self.R_SHIFT_X_UP.place(
            x = 1135,
            y = 233
        )
        self.R_SHIFT_X_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.R_SHIFT_X_DOWN_CB()
        )
        self.R_SHIFT_X_DOWN.pack()
        self.R_SHIFT_X_DOWN.place(
            x = 1175,
            y = 233
        )

        self.R_SHIFT_Y_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.R_SHIFT_Y_UP_CB()
        )
        self.R_SHIFT_Y_UP.pack()
        self.R_SHIFT_Y_UP.place(
            x = 1135,
            y = 265
        )
        self.R_SHIFT_Y_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.R_SHIFT_Y_DOWN_CB()
        )
        self.R_SHIFT_Y_DOWN.pack()
        self.R_SHIFT_Y_DOWN.place(
            x = 1175,
            y = 265
        )

        
        self.R_SHIFT_Z_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.R_SHIFT_Z_UP_CB()
        )
        self.R_SHIFT_Z_UP.pack()
        self.R_SHIFT_Z_UP.place(
            x = 1135,
            y = 295
        )
        self.R_SHIFT_Z_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.R_SHIFT_Z_DOWN_CB()
        )
        self.R_SHIFT_Z_DOWN.pack()
        self.R_SHIFT_Z_DOWN.place(
            x = 1175,
            y = 295
        )

        
        self.R_LIFT_X_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.R_LIFT_X_UP_CB()
        )
        self.R_LIFT_X_UP.pack()
        self.R_LIFT_X_UP.place(
            x = 1135,
            y = 327
        )
        self.R_LIFT_X_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.R_LIFT_X_DOWN_CB()
        )
        self.R_LIFT_X_DOWN.pack()
        self.R_LIFT_X_DOWN.place(
            x = 1175,
            y = 327
        )
        
        self.R_LIFT_Y_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.R_LIFT_Y_UP_CB()
        )
        self.R_LIFT_Y_UP.pack()
        self.R_LIFT_Y_UP.place(
            x = 1135,
            y = 357
        )
        self.R_LIFT_Y_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.R_LIFT_Y_DOWN_CB()
        )
        self.R_LIFT_Y_DOWN.pack()
        self.R_LIFT_Y_DOWN.place(
            x = 1175,
            y = 357
        )
        
        self.R_LIFT_Z_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.R_LIFT_Z_UP_CB()
        )
        self.R_LIFT_Z_UP.pack()
        self.R_LIFT_Z_UP.place(
            x = 1135,
            y = 388
        )
        self.R_LIFT_Z_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.R_LIFT_Z_DOWN_CB()
        )
        self.R_LIFT_Z_DOWN.pack()
        self.R_LIFT_Z_DOWN.place(
            x = 1175,
            y = 388
        )
        
        self.R_SWING_X_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.R_SWING_X_UP_CB()
        )
        self.R_SWING_X_UP.pack()
        self.R_SWING_X_UP.place(
            x = 1135,
            y = 419
        )
        self.R_SWING_X_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.R_SWING_X_DOWN_CB()
        )
        self.R_SWING_X_DOWN.pack()
        self.R_SWING_X_DOWN.place(
            x = 1175,
            y = 419
        )

        self.R_SWING_Y_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.R_SWING_Y_UP_CB()
        )
        self.R_SWING_Y_UP.pack()
        self.R_SWING_Y_UP.place(
            x = 1135,
            y = 449
        )
        self.R_SWING_Y_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.R_SWING_Y_DOWN_CB()
        )
        self.R_SWING_Y_DOWN.pack()
        self.R_SWING_Y_DOWN.place(
            x = 1175,
            y = 449
        )

        self.R_SWING_Z_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.R_SWING_Z_UP_CB()
        )
        self.R_SWING_Z_UP.pack()
        self.R_SWING_Z_UP.place(
            x = 1135,
            y = 482
        )
        self.R_SWING_Z_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.R_SWING_Z_DOWN_CB()
        )
        self.R_SWING_Z_DOWN.pack()
        self.R_SWING_Z_DOWN.place(
            x = 1175,
            y = 482
        )
        
        self.R_RETRACT_X_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.R_RETRACT_X_UP_CB()
        )
        self.R_RETRACT_X_UP.pack()
        self.R_RETRACT_X_UP.place(
            x = 1135,
            y = 513
        )
        self.R_RETRACT_X_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.R_RETRACT_X_DOWN_CB()
        )
        self.R_RETRACT_X_DOWN.pack()
        self.R_RETRACT_X_DOWN.place(
            x = 1175,
            y = 513
        )

        self.R_RETRACT_Y_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.R_RETRACT_Y_UP_CB()
        )
        self.R_RETRACT_Y_UP.pack()
        self.R_RETRACT_Y_UP.place(
            x = 1135,
            y = 544
        )
        self.R_RETRACT_Y_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.R_RETRACT_Y_DOWN_CB()
        )
        self.R_RETRACT_Y_DOWN.pack()
        self.R_RETRACT_Y_DOWN.place(
            x = 1175,
            y = 544
        )

        self.R_RETRACT_Z_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.R_RETRACT_Z_UP_CB()
        )
        self.R_RETRACT_Z_UP.pack()
        self.R_RETRACT_Z_UP.place(
            x = 1135,
            y = 575
        )
        self.R_RETRACT_Z_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.R_RETRACT_Z_DOWN_CB()
        )
        self.R_RETRACT_Z_DOWN.pack()
        self.R_RETRACT_Z_DOWN.place(
            x = 1175,
            y = 575
        )

        # kick
        self.R_KICK = Button(
            master=self.kick_window,
            width=9,
            height=1,
            text='RIGHT KICK',
            bg='black',
            fg='white',
            font=("Modern", 12),
            command=lambda:self.RIGHT_KICK_CB()
        )
        self.R_KICK.pack()
        self.R_KICK.place(
            x = 950,
            y = 620
        )

        self.L_KICK = Button(
            master=self.kick_window,
            width=9,
            height=1,
            text='LEFT KICK',
            bg='black',
            fg='white',
            font=("Modern", 12),
            command=lambda:self.LEFT_KICK_CB()
        )
        self.L_KICK.pack()
        self.L_KICK.place(
            x = 70,
            y = 620
        )

        #-------ANGLE------------#
        self.angleFrame = Frame(
            master = self.kick_window,
            bg="black",
            width=450,
            height=800,
            borderwidth=10,
        )
        self.angleFrame.pack(anchor=CENTER, side=BOTTOM, pady = 20)
    
        self.Torso_Pitch_Temp = float(Torso_Pitch)
        self.TORSO_PITCH = Label(
            master=self.angleFrame,
            width=21,
            height=1,
            bg="white",
            fg = "black",
            text= "TORSO_PITCH: " + str(self.Torso_Pitch_Temp),
            font=("Modern", 12),
        )
        self.TORSO_PITCH.pack(pady=4)

        self.Shift_Roll_Temp = float(Shift_Roll)
        self.SHIFT_ROLL = Label(
            master=self.angleFrame,
            width=21,
            height=1,
            bg="white",
            fg = "black",
            text= "SHIFT_ROLL: " + str(self.Shift_Roll_Temp),
            font=("Modern", 12),
        )
        self.SHIFT_ROLL.pack(pady=4)

        self.Lift_Roll_Temp = float(Lift_Roll)
        self.LIFT_ROLL = Label(
            master=self.angleFrame,
            width=21,
            height=1,
            bg="white",
            fg = "black",
            text= "LIFT_ROLL: " + str(self.Lift_Roll_Temp),
            font=("Modern", 12),
        )
        self.LIFT_ROLL.pack(pady=4)

        self.Lift_Pitch_Temp = float(Lift_Pitch)
        self.LIFT_PITCH = Label(
            master=self.angleFrame,
            width=21,
            height=1,
            bg="white",
            fg = "black",
            text= "LIFT_PITCH: " + str(self.Lift_Pitch_Temp),
            font=("Modern", 12),
        )
        self.LIFT_PITCH.pack(pady=4)

        self.Swing_Roll_Temp = float(Swing_Roll)
        self.SWING_ROLL = Label(
            master=self.angleFrame,
            width=21,
            height=1,
            bg="white",
            fg = "black",
            text= "SWING_ROLL: " + str(self.Swing_Roll_Temp),
            font=("Modern", 12),
        )
        self.SWING_ROLL.pack(pady=4)

        self.Swing_Pitch_Temp = float(Swing_Pitch)
        self.SWING_PITCH = Label(
            master=self.angleFrame,
            width=21,
            height=1,
            bg="white",
            fg = "black",
            text= "SWING_PITCH: " + str(self.Swing_Pitch_Temp),
            font=("Modern", 12),
        )
        self.SWING_PITCH.pack(pady=4)

        self.Retract_Roll_Temp = float(Retract_Roll)
        self.RETRACT_ROLL = Label(
            master=self.angleFrame,
            width=21,
            height=1,
            bg="white",
            fg = "black",
            text= "RETRACT_ROLL: " + str(self.Retract_Roll_Temp),
            font=("Modern", 12),
        )
        self.RETRACT_ROLL.pack(pady=4)

        self.Retract_Pitch_Temp = float(Retract_Pitch)
        self.RETRACT_PITCH = Label(
            master=self.angleFrame,
            width=21,
            height=1,
            bg="white",
            fg = "black",
            text= "RETRACT_PITCH: " + str(self.Retract_Pitch_Temp),
            font=("Modern", 12),
        )
        self.RETRACT_PITCH.pack(pady=4)

        # button
        self.TORSO_PITCH_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.TORSO_PITCH_UP_CB()
        )
        self.TORSO_PITCH_UP.pack()
        self.TORSO_PITCH_UP.place(
            x = 776,
            y = 585
        )
        self.TORSO_PITCH_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.TORSO_PITCH_DOWN_CB()
        )
        self.TORSO_PITCH_DOWN.pack()
        self.TORSO_PITCH_DOWN.place(
            x = 816,
            y = 585
        )

        self.SHIFT_ROLL_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.SHIFT_ROLL_UP_CB()
        )
        self.SHIFT_ROLL_UP.pack()
        self.SHIFT_ROLL_UP.place(
            x = 776,
            y = 616
        )
        self.SHIFT_ROLL_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.SHIFT_ROLL_DOWN_CB()
        )
        self.SHIFT_ROLL_DOWN.pack()
        self.SHIFT_ROLL_DOWN.place(
            x = 816,
            y = 616
        )

        self.LIFT_ROLL_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.LIFT_ROLL_UP_CB()
        )
        self.LIFT_ROLL_UP.pack()
        self.LIFT_ROLL_UP.place(
            x = 776,
            y = 646
        )
        self.LIFT_ROLL_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.LIFT_ROLL_DOWN_CB()
        )
        self.LIFT_ROLL_DOWN.pack()
        self.LIFT_ROLL_DOWN.place(
            x = 816,
            y = 646
        )

        self.LIFT_PITCH_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.LIFT_PITCH_UP_CB()
        )
        self.LIFT_PITCH_UP.pack()
        self.LIFT_PITCH_UP.place(
            x = 776,
            y = 678
        )
        self.LIFT_PITCH_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.LIFT_PITCH_DOWN_CB()
        )
        self.LIFT_PITCH_DOWN.pack()
        self.LIFT_PITCH_DOWN.place(
            x = 816,
            y = 678
        )

        self.SWING_ROLL_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.SWING_ROLL_UP_CB()
        )
        self.SWING_ROLL_UP.pack()
        self.SWING_ROLL_UP.place(
            x = 776,
            y = 710
        )
        self.SWING_ROLL_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.SWING_ROLL_DOWN_CB()
        )
        self.SWING_ROLL_DOWN.pack()
        self.SWING_ROLL_DOWN.place(
            x = 816,
            y = 710
        )

        self.SWING_PITCH_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.SWING_PITCH_UP_CB()
        )
        self.SWING_PITCH_UP.pack()
        self.SWING_PITCH_UP.place(
            x = 776,
            y = 741
        )
        self.SWING_PITCH_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.SWING_PITCH_DOWN_CB()
        )
        self.SWING_PITCH_DOWN.pack()
        self.SWING_PITCH_DOWN.place(
            x = 816,
            y = 741
        )

        self.RETRACT_ROLL_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.RETRACT_ROLL_UP_CB()
        )
        self.RETRACT_ROLL_UP.pack()
        self.RETRACT_ROLL_UP.place(
            x = 776,
            y = 772
        )
        self.RETRACT_ROLL_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.RETRACT_ROLL_DOWN_CB()
        )
        self.RETRACT_ROLL_DOWN.pack()
        self.RETRACT_ROLL_DOWN.place(
            x = 816,
            y = 772
        )

        self.RETRACT_PITCH_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.RETRACT_PITCH_UP_CB()
        )
        self.RETRACT_PITCH_UP.pack()
        self.RETRACT_PITCH_UP.place(
            x = 776,
            y = 802
        )
        self.RETRACT_PITCH_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.RETRACT_PITCH_DOWN_CB()
        )
        self.RETRACT_PITCH_DOWN.pack()
        self.RETRACT_PITCH_DOWN.place(
            x = 816,
            y = 802
        )

        #--------TIME--------------#
        self.timeFrame = Frame(
            master = self.kick_window,
            bg="black",
            width=450,
            height=800,
            borderwidth=10,
        )
        self.timeFrame.pack(anchor=CENTER, side=BOTTOM, pady = 20)
    
        self.Shift_Time_Temp = float(Shift_Time)
        self.SHIFT_TIME = Label(
            master=self.timeFrame,
            width=21,
            height=1,
            bg="white",
            fg = "black",
            text= "SHIFT_TIME: " + str(self.Shift_Time_Temp),
            font=("Modern", 12),
        )
        self.SHIFT_TIME.pack(pady=4)

        self.Lift_Time_Temp = float(Lift_Time)
        self.LIFT_TIME = Label(
            master=self.timeFrame,
            width=21,
            height=1,
            bg="white",
            fg = "black",
            text= "LIFT_TIME: " + str(self.Lift_Time_Temp),
            font=("Modern", 12),
        )
        self.LIFT_TIME.pack(pady=4)

        self.Swing_Time_Temp = float(Swing_Time)
        self.SWING_TIME = Label(
            master=self.timeFrame,
            width=21,
            height=1,
            bg="white",
            fg = "black",
            text= "SWING_TIME: " + str(self.Swing_Time_Temp),
            font=("Modern", 12),
        )
        self.SWING_TIME.pack(pady=4)

        self.Retract_Time_Temp = float(Retract_Time)
        self.RETRACT_TIME = Label(
            master=self.timeFrame,
            width=21,
            height=1,
            bg="white",
            fg = "black",
            text= "RETRACT_TIME: " + str(self.Retract_Time_Temp),
            font=("Modern", 12),
        )
        self.RETRACT_TIME.pack(pady=4)

        self.Landing_Time_Temp = float(Landing_Time)
        self.LANDING_TIME = Label(
            master=self.timeFrame,
            width=21,
            height=1,
            bg="white",
            fg = "black",
            text= "LANDING_TIME: " + str(self.Landing_Time_Temp),
            font=("Modern", 12),
        )
        self.LANDING_TIME.pack(pady=4)

        self.Finished_Time_Temp = float(Finished_Time)
        self.FINISHED_TIME = Label(
            master=self.timeFrame,
            width=21,
            height=1,
            bg="white",
            fg = "black",
            text= "FINISHED_TIME: " + str(self.Finished_Time_Temp),
            font=("Modern", 12),
        )
        self.FINISHED_TIME.pack(pady=4)

        # button
        self.SHIFT_TIME_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.SHIFT_TIME_UP_CB()
        )
        self.SHIFT_TIME_UP.pack()
        self.SHIFT_TIME_UP.place(
            x = 776,
            y = 339
        )
        self.SHIFT_TIME_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.SHIFT_TIME_DOWN_CB()
        )
        self.SHIFT_TIME_DOWN.pack()
        self.SHIFT_TIME_DOWN.place(
            x = 816,
            y = 339
        )

        self.LIFT_TIME_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.LIFT_TIME_UP_CB()
        )
        self.LIFT_TIME_UP.pack()
        self.LIFT_TIME_UP.place(
            x = 776,
            y = 369
        )
        self.LIFT_TIME_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.LIFT_TIME_DOWN_CB()
        )
        self.LIFT_TIME_DOWN.pack()
        self.LIFT_TIME_DOWN.place(
            x = 816,
            y = 369
        )

        self.SWING_TIME_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.SWING_TIME_UP_CB()
        )
        self.SWING_TIME_UP.pack()
        self.SWING_TIME_UP.place(
            x = 776,
            y = 400
        )
        self.SWING_TIME_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.SWING_TIME_DOWN_CB()
        )
        self.SWING_TIME_DOWN.pack()
        self.SWING_TIME_DOWN.place(
            x = 816,
            y = 400
        )

        self.RETRACT_TIME_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.RETRACT_TIME_UP_CB()
        )
        self.RETRACT_TIME_UP.pack()
        self.RETRACT_TIME_UP.place(
            x = 776,
            y = 432
        )
        self.RETRACT_TIME_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.RETRACT_TIME_DOWN_CB()
        )
        self.RETRACT_TIME_DOWN.pack()
        self.RETRACT_TIME_DOWN.place(
            x = 816,
            y = 432
        )

        self.LANDING_TIME_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.LANDING_TIME_UP_CB()
        )
        self.LANDING_TIME_UP.pack()
        self.LANDING_TIME_UP.place(
            x = 776,
            y = 463
        )
        self.LANDING_TIME_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.LANDING_TIME_DOWN_CB()
        )
        self.LANDING_TIME_DOWN.pack()
        self.LANDING_TIME_DOWN.place(
            x = 816,
            y = 463
        )

        self.FINISHED_TIME_UP = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='+',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.FINISHED_TIME_UP_CB()
        )
        self.FINISHED_TIME_UP.pack()
        self.FINISHED_TIME_UP.place(
            x = 776,
            y = 495
        )
        self.FINISHED_TIME_DOWN = Button(
            master=self.kick_window,
            width=1,
            height=1,
            text='-',
            bg='black',
            fg='white',
            font=("Modern", 10),
            command=lambda:self.FINISHED_TIME_DOWN_CB()
        )
        self.FINISHED_TIME_DOWN.pack()
        self.FINISHED_TIME_DOWN.place(
            x = 816,
            y = 495
        )
        #-------KICKING MODE----------#
        self.kickModeFrame = Frame(
            master = self.kick_window,
            background= "#C0C0C0",
            relief="raised"
        )
        self.kickModeFrame.pack(anchor=CENTER,side = TOP, padx = 10)

        self.kickModeButton = Button(
            master=self.kickModeFrame,
            text="KICKING MODE",
            font=('Modern', 15),
            width=12,
            height=1,
            bg="black",
            fg="white"
        )
        self.kickModeButton.pack()

        #----------SAVE----------#
        self.saveFrame = Frame(
            master = self.kick_window,
            background= "#C0C0C0",
            relief="raised"
        )
        self.saveFrame.pack(anchor=CENTER,side=TOP, pady =10)

        self.saveButton = Button(
            master=self.saveFrame,
            text="SAVE",
            font=('Modern', 15),
            width=8,
            height=1,
            bg="black",
            fg="white",
            command=lambda:self.SAVE_CB()
        )
        self.saveButton.pack()

        #-------ENTER--------#
        self.enterFrame = Frame(
            master = self.kick_window,
            background= "#C0C0C0",
            relief="raised"
        )
        self.enterFrame.pack(anchor=CENTER)

        self.enterButton = Button(
            master=self.enterFrame,
            text="ENTER",
            font=('Modern', 15),
            width=8,
            height=1,
            bg="black",
            fg="white",
            command=lambda:self.ENTER_CB()
        )
        self.enterButton.pack()

        #----------EXIT-------#
        self.exitFrame = Frame(
            master = self.kick_window,
            background= "#C0C0C0",
            relief="raised"
        )
        self.exitFrame.pack(anchor=CENTER, side = BOTTOM, pady=10)

        self.exitButton = Button(
            master=self.exitFrame,
            text="EXIT",
            font=('Modern', 15),
            width=7,
            height=1,
            bg="black",
            fg="white",
            command=lambda:self.exit_kick()
        )
        self.exitButton.pack()
        
        
    
    # Start the kick_window
    def start(self, name, id):
        self.robot_name.config(text = "ROBOT: " + name)
        self.name = name
        self.robot_id.config(text="ID: " + str(id))
        self.id = id
        self.kick_window.mainloop()
    def exit_kick(self):
        # publish that the page no longer used
        self.kicking_page = "none"
        self.kicking_page_pub.publish(self.kicking_page)
        self.kick_window.destroy()
    # + and - button callback
    # torso
    def TORSO_X_UP_CB(self):
        self.Torso_X_Temp = round(self.Torso_X_Temp + 0.005, 5) 
        self.TORSO_X.config(text="TORSO_X: " + str(self.Torso_X_Temp))
    def TORSO_X_DOWN_CB(self):
        self.Torso_X_Temp = round(self.Torso_X_Temp - 0.005, 5) 
        self.TORSO_X.config(text="TORSO_X: " + str(self.Torso_X_Temp))
    
    def TORSO_Y_UP_CB(self):
        self.Torso_Y_Temp = round(self.Torso_Y_Temp + 0.005, 5) 
        self.TORSO_Y.config(text="TORSO_Y: " + str(self.Torso_Y_Temp))
    def TORSO_Y_DOWN_CB(self):
        self.Torso_Y_Temp = round(self.Torso_Y_Temp - 0.005, 5) 
        self.TORSO_Y.config(text="TORSO_Y: " + str(self.Torso_Y_Temp))
    
    def TORSO_Z_UP_CB(self):
        self.Torso_Z_Temp = round(self.Torso_Z_Temp + 0.005, 5) 
        self.TORSO_Z.config(text="TORSO_Z: " + str(self.Torso_Z_Temp))
    def TORSO_Z_DOWN_CB(self):
        self.Torso_Z_Temp = round(self.Torso_Z_Temp - 0.005, 5) 
        self.TORSO_Z.config(text="TORSO_Z: " + str(self.Torso_Z_Temp))

    # left
    def L_SHIFT_X_UP_CB(self):
        self.L_Shift_X_Temp = round(self.L_Shift_X_Temp + 0.005, 5) 
        self.L_SHIFT_X.config(text="L_SHIFT_X: " + str(self.L_Shift_X_Temp))
    def L_SHIFT_X_DOWN_CB(self):
        self.L_Shift_X_Temp = round(self.L_Shift_X_Temp - 0.005, 5) 
        self.L_SHIFT_X.config(text="L_SHIFT_X: " + str(self.L_Shift_X_Temp))

    def L_SHIFT_Y_UP_CB(self):
        self.L_Shift_Y_Temp = round(self.L_Shift_Y_Temp + 0.005, 5) 
        self.L_SHIFT_Y.config(text="L_SHIFT_Y: " + str(self.L_Shift_Y_Temp))
    def L_SHIFT_Y_DOWN_CB(self):
        self.L_Shift_Y_Temp = round(self.L_Shift_Y_Temp - 0.005, 5) 
        self.L_SHIFT_Y.config(text="L_SHIFT_Y: " + str(self.L_Shift_Y_Temp))
    
    def L_SHIFT_Z_UP_CB(self):
        self.L_Shift_Z_Temp = round(self.L_Shift_Z_Temp + 0.005, 5) 
        self.L_SHIFT_Z.config(text="L_SHIFT_Z: " + str(self.L_Shift_Z_Temp))
    def L_SHIFT_Z_DOWN_CB(self):
        self.L_Shift_Z_Temp = round(self.L_Shift_Z_Temp - 0.005, 5) 
        self.L_SHIFT_Z.config(text="L_SHIFT_Z: " + str(self.L_Shift_Z_Temp))

    def L_LIFT_X_UP_CB(self):
        self.L_Lift_X_Temp = round(self.L_Lift_X_Temp + 0.005, 5) 
        self.L_LIFT_X.config(text="L_LIFT_X: " + str(self.L_Lift_X_Temp))
    def L_LIFT_X_DOWN_CB(self):
        self.L_Lift_X_Temp = round(self.L_Lift_X_Temp - 0.005, 5) 
        self.L_LIFT_X.config(text="L_LIFT_X: " + str(self.L_Lift_X_Temp))

    def L_LIFT_Y_UP_CB(self):
        self.L_Lift_Y_Temp = round(self.L_Lift_Y_Temp + 0.005, 5) 
        self.L_LIFT_Y.config(text="L_LIFT_Y: " + str(self.L_Lift_Y_Temp))
    def L_LIFT_Y_DOWN_CB(self):
        self.L_Lift_Y_Temp = round(self.L_Lift_Y_Temp - 0.005, 5) 
        self.L_LIFT_Y.config(text="L_LIFT_Y: " + str(self.L_Lift_Y_Temp))

    def L_LIFT_Z_UP_CB(self):
        self.L_Lift_Z_Temp = round(self.L_Lift_Z_Temp + 0.005, 5) 
        self.L_LIFT_Z.config(text="L_LIFT_Z: " + str(self.L_Lift_Z_Temp))
    def L_LIFT_Z_DOWN_CB(self):
        self.L_Lift_Z_Temp = round(self.L_Lift_Z_Temp - 0.005, 5) 
        self.L_LIFT_Z.config(text="L_LIFT_Z: " + str(self.L_Lift_Z_Temp))

    def L_SWING_X_UP_CB(self):
        self.L_Swing_X_Temp = round(self.L_Swing_X_Temp + 0.005, 5) 
        self.L_SWING_X.config(text="L_SWING_X: " + str(self.L_Swing_X_Temp))
    def L_SWING_X_DOWN_CB(self):
        self.L_Swing_X_Temp = round(self.L_Swing_X_Temp - 0.005, 5) 
        self.L_SWING_X.config(text="L_SWING_X: " + str(self.L_Swing_X_Temp))

    def L_SWING_Y_UP_CB(self):
        self.L_Swing_Y_Temp = round(self.L_Swing_Y_Temp + 0.005, 5) 
        self.L_SWING_Y.config(text="L_SWING_Y: " + str(self.L_Swing_Y_Temp))
    def L_SWING_Y_DOWN_CB(self):
        self.L_Swing_Y_Temp = round(self.L_Swing_Y_Temp - 0.005, 5) 
        self.L_SWING_Y.config(text="L_SWING_Y: " + str(self.L_Swing_Y_Temp))

    def L_SWING_Z_UP_CB(self):
        self.L_Swing_Z_Temp = round(self.L_Swing_Z_Temp + 0.005, 5) 
        self.L_SWING_Z.config(text="L_SWING_Z: " + str(self.L_Swing_Z_Temp))
    def L_SWING_Z_DOWN_CB(self):
        self.L_Swing_Z_Temp = round(self.L_Swing_Z_Temp - 0.005, 5) 
        self.L_SWING_Z.config(text="L_SWING_Z: " + str(self.L_Swing_Z_Temp))

    def L_RETRACT_X_UP_CB(self):
        self.L_Retract_X_Temp = round(self.L_Retract_X_Temp + 0.005, 5) 
        self.L_RETRACT_X.config(text="L_RETRACT_X: " + str(self.L_Retract_X_Temp))
    def L_RETRACT_X_DOWN_CB(self):
        self.L_Retract_X_Temp = round(self.L_Retract_X_Temp - 0.005, 5) 
        self.L_RETRACT_X.config(text="L_RETRACT_X: " + str(self.L_Retract_X_Temp))

    def L_RETRACT_Y_UP_CB(self):
        self.L_Retract_Y_Temp = round(self.L_Retract_Y_Temp + 0.005, 5) 
        self.L_RETRACT_Y.config(text="L_RETRACT_Y: " + str(self.L_Retract_Y_Temp))
    def L_RETRACT_Y_DOWN_CB(self):
        self.L_Retract_Y_Temp = round(self.L_Retract_Y_Temp - 0.005, 5) 
        self.L_RETRACT_Y.config(text="L_RETRACT_Y: " + str(self.L_Retract_Y_Temp))

    def L_RETRACT_Z_UP_CB(self):
        self.L_Retract_Z_Temp = round(self.L_Retract_Z_Temp + 0.005, 5) 
        self.L_RETRACT_Z.config(text="L_RETRACT_Z: " + str(self.L_Retract_Z_Temp))
    def L_RETRACT_Z_DOWN_CB(self):
        self.L_Retract_Z_Temp = round(self.L_Retract_Z_Temp - 0.005, 5) 
        self.L_RETRACT_Z.config(text="L_RETRACT_Z: " + str(self.L_Retract_Z_Temp))
    
    # right
    def R_SHIFT_X_UP_CB(self):
        self.R_Shift_X_Temp = round(self.R_Shift_X_Temp + 0.005, 5) 
        self.R_SHIFT_X.config(text="R_SHIFT_X: " + str(self.R_Shift_X_Temp))
    def R_SHIFT_X_DOWN_CB(self):
        self.R_Shift_X_Temp = round(self.R_Shift_X_Temp - 0.005, 5) 
        self.R_SHIFT_X.config(text="R_SHIFT_X: " + str(self.R_Shift_X_Temp))

    def R_SHIFT_Y_UP_CB(self):
        self.R_Shift_Y_Temp = round(self.R_Shift_Y_Temp + 0.005, 5) 
        self.R_SHIFT_Y.config(text="R_SHIFT_Y: " + str(self.R_Shift_Y_Temp))
    def R_SHIFT_Y_DOWN_CB(self):
        self.R_Shift_Y_Temp = round(self.R_Shift_Y_Temp - 0.005, 5) 
        self.R_SHIFT_Y.config(text="R_SHIFT_Y: " + str(self.R_Shift_Y_Temp))
    
    def R_SHIFT_Z_UP_CB(self):
        self.R_Shift_Z_Temp = round(self.R_Shift_Z_Temp + 0.005, 5) 
        self.R_SHIFT_Z.config(text="R_SHIFT_Z: " + str(self.R_Shift_Z_Temp))
    def R_SHIFT_Z_DOWN_CB(self):
        self.R_Shift_Z_Temp = round(self.R_Shift_Z_Temp - 0.005, 5) 
        self.R_SHIFT_Z.config(text="R_SHIFT_Z: " + str(self.R_Shift_Z_Temp))

    def R_LIFT_X_UP_CB(self):
        self.R_Lift_X_Temp = round(self.R_Lift_X_Temp + 0.005, 5) 
        self.R_LIFT_X.config(text="R_LIFT_X: " + str(self.R_Lift_X_Temp))
    def R_LIFT_X_DOWN_CB(self):
        self.R_Lift_X_Temp = round(self.R_Lift_X_Temp - 0.005, 5) 
        self.R_LIFT_X.config(text="R_LIFT_X: " + str(self.R_Lift_X_Temp))

    def R_LIFT_Y_UP_CB(self):
        self.R_Lift_Y_Temp = round(self.R_Lift_Y_Temp + 0.005, 5) 
        self.R_LIFT_Y.config(text="R_LIFT_Y: " + str(self.R_Lift_Y_Temp))
    def R_LIFT_Y_DOWN_CB(self):
        self.R_Lift_Y_Temp = round(self.R_Lift_Y_Temp - 0.005, 5) 
        self.R_LIFT_Y.config(text="R_LIFT_Y: " + str(self.R_Lift_Y_Temp))

    def R_LIFT_Z_UP_CB(self):
        self.R_Lift_Z_Temp = round(self.R_Lift_Z_Temp + 0.005, 5) 
        self.R_LIFT_Z.config(text="R_LIFT_Z: " + str(self.R_Lift_Z_Temp))
    def R_LIFT_Z_DOWN_CB(self):
        self.R_Lift_Z_Temp = round(self.R_Lift_Z_Temp - 0.005, 5) 
        self.R_LIFT_Z.config(text="R_LIFT_Z: " + str(self.R_Lift_Z_Temp))

    def R_SWING_X_UP_CB(self):
        self.R_Swing_X_Temp = round(self.R_Swing_X_Temp + 0.005, 5) 
        self.R_SWING_X.config(text="R_SWING_X: " + str(self.R_Swing_X_Temp))
    def R_SWING_X_DOWN_CB(self):
        self.R_Swing_X_Temp = round(self.R_Swing_X_Temp - 0.005, 5) 
        self.R_SWING_X.config(text="R_SWING_X: " + str(self.R_Swing_X_Temp))

    def R_SWING_Y_UP_CB(self):
        self.R_Swing_Y_Temp = round(self.R_Swing_Y_Temp + 0.005, 5) 
        self.R_SWING_Y.config(text="R_SWING_Y: " + str(self.R_Swing_Y_Temp))
    def R_SWING_Y_DOWN_CB(self):
        self.R_Swing_Y_Temp = round(self.R_Swing_Y_Temp - 0.005, 5) 
        self.R_SWING_Y.config(text="R_SWING_Y: " + str(self.R_Swing_Y_Temp))

    def R_SWING_Z_UP_CB(self):
        self.R_Swing_Z_Temp = round(self.R_Swing_Z_Temp + 0.005, 5) 
        self.R_SWING_Z.config(text="R_SWING_Z: " + str(self.R_Swing_Z_Temp))
    def R_SWING_Z_DOWN_CB(self):
        self.R_Swing_Z_Temp = round(self.R_Swing_Z_Temp - 0.005, 5) 
        self.R_SWING_Z.config(text="R_SWING_Z: " + str(self.R_Swing_Z_Temp))

    def R_RETRACT_X_UP_CB(self):
        self.R_Retract_X_Temp = round(self.R_Retract_X_Temp + 0.005, 5) 
        self.R_RETRACT_X.config(text="R_RETRACT_X: " + str(self.R_Retract_X_Temp))
    def R_RETRACT_X_DOWN_CB(self):
        self.R_Retract_X_Temp = round(self.R_Retract_X_Temp - 0.005, 5) 
        self.R_RETRACT_X.config(text="R_RETRACT_X: " + str(self.R_Retract_X_Temp))

    def R_RETRACT_Y_UP_CB(self):
        self.R_Retract_Y_Temp = round(self.R_Retract_Y_Temp + 0.005, 5) 
        self.R_RETRACT_Y.config(text="R_RETRACT_Y: " + str(self.R_Retract_Y_Temp))
    def R_RETRACT_Y_DOWN_CB(self):
        self.R_Retract_Y_Temp = round(self.R_Retract_Y_Temp - 0.005, 5) 
        self.R_RETRACT_Y.config(text="R_RETRACT_Y: " + str(self.R_Retract_Y_Temp))

    def R_RETRACT_Z_UP_CB(self):
        self.R_Retract_Z_Temp = round(self.R_Retract_Z_Temp + 0.005, 5) 
        self.R_RETRACT_Z.config(text="R_RETRACT_Z: " + str(self.R_Retract_Z_Temp))
    def R_RETRACT_Z_DOWN_CB(self):
        self.R_Retract_Z_Temp = round(self.R_Retract_Z_Temp - 0.005, 5) 
        self.R_RETRACT_Z.config(text="R_RETRACT_Z: " + str(self.R_Retract_Z_Temp))
    
    # angle
    def TORSO_PITCH_UP_CB(self):
        self.Torso_Pitch_Temp = round(self.Torso_Pitch_Temp + 0.005, 5) 
        self.TORSO_PITCH.config(text="TORSO_PITCH: " + str(self.Torso_Pitch_Temp))
    def TORSO_PITCH_DOWN_CB(self):
        self.Torso_Pitch_Temp = round(self.Torso_Pitch_Temp - 0.005, 5) 
        self.TORSO_PITCH.config(text="TORSO_PITCH: " + str(self.Torso_Pitch_Temp))

    def SHIFT_ROLL_UP_CB(self):
        self.Shift_Roll_Temp = round(self.Shift_Roll_Temp + 0.005, 5) 
        self.SHIFT_ROLL.config(text="SHIFT_ROLL: " + str(self.Shift_Roll_Temp))
    def SHIFT_ROLL_DOWN_CB(self):
        self.Shift_Roll_Temp = round(self.Shift_Roll_Temp - 0.005, 5) 
        self.SHIFT_ROLL.config(text="SHIFT_ROLL: " + str(self.Shift_Roll_Temp))

    def LIFT_ROLL_UP_CB(self):
        self.Lift_Roll_Temp = round(self.Lift_Roll_Temp + 0.005, 5) 
        self.LIFT_ROLL.config(text="LIFT_ROLL: " + str(self.Lift_Roll_Temp))
    def LIFT_ROLL_DOWN_CB(self):
        self.Lift_Roll_Temp = round(self.Lift_Roll_Temp - 0.005, 5) 
        self.LIFT_ROLL.config(text="LIFT_ROLL: " + str(self.Lift_Roll_Temp))

    def LIFT_PITCH_UP_CB(self):
        self.Lift_Pitch_Temp = round(self.Lift_Pitch_Temp + 0.005, 5) 
        self.LIFT_PITCH.config(text="LIFT_PITCH: " + str(self.Lift_Pitch_Temp))
    def LIFT_PITCH_DOWN_CB(self):
        self.Lift_Pitch_Temp = round(self.Lift_Pitch_Temp - 0.005, 5) 
        self.LIFT_PITCH.config(text="LIFT_PITCH: " + str(self.Lift_Pitch_Temp))
    
    def SWING_ROLL_UP_CB(self):
        self.Swing_Roll_Temp = round(self.Swing_Roll_Temp + 0.005, 5) 
        self.SWING_ROLL.config(text="SWING_ROLL: " + str(self.Swing_Roll_Temp))
    def SWING_ROLL_DOWN_CB(self):
        self.Swing_Roll_Temp = round(self.Swing_Roll_Temp - 0.005, 5) 
        self.SWING_ROLL.config(text="SWING_ROLL: " + str(self.Swing_Roll_Temp))
    
    def SWING_PITCH_UP_CB(self):
        self.Swing_Pitch_Temp = round(self.Swing_Pitch_Temp + 0.005, 5) 
        self.SWING_PITCH.config(text="SWING_PITCH: " + str(self.Swing_Pitch_Temp))
    def SWING_PITCH_DOWN_CB(self):
        self.Swing_Pitch_Temp = round(self.Swing_Pitch_Temp - 0.005, 5) 
        self.SWING_PITCH.config(text="SWING_PITCH: " + str(self.Swing_Pitch_Temp))
    
    def RETRACT_ROLL_UP_CB(self):
        self.Retract_Roll_Temp = round(self.Retract_Roll_Temp + 0.005, 5) 
        self.RETRACT_ROLL.config(text="RETRACT_ROLL: " + str(self.Retract_Roll_Temp))
    def RETRACT_ROLL_DOWN_CB(self):
        self.Retract_Roll_Temp = round(self.Retract_Roll_Temp - 0.005, 5) 
        self.RETRACT_ROLL.config(text="RETRACT_ROLL: " + str(self.Retract_Roll_Temp))
    
    def RETRACT_PITCH_UP_CB(self):
        self.Retract_Pitch_Temp = round(self.Retract_Pitch_Temp + 0.005, 5) 
        self.RETRACT_PITCH.config(text="RETRACT_PITCH: " + str(self.Retract_Pitch_Temp))
    def RETRACT_PITCH_DOWN_CB(self):
        self.Retract_Pitch_Temp = round(self.Retract_Pitch_Temp - 0.005, 5) 
        self.RETRACT_PITCH.config(text="RETRACT_PITCH: " + str(self.Retract_Pitch_Temp))
    
    # time
    def SHIFT_TIME_UP_CB(self):
        self.Shift_Time_Temp = round(self.Shift_Time_Temp + 0.005, 5) 
        self.SHIFT_TIME.config(text="SHIFT_TIME: " + str(self.Shift_Time_Temp))
    def SHIFT_TIME_DOWN_CB(self):
        self.Shift_Time_Temp = round(self.Shift_Time_Temp - 0.005, 5) 
        self.SHIFT_TIME.config(text="SHIFT_TIME: " + str(self.Shift_Time_Temp))

    def LIFT_TIME_UP_CB(self):
        self.Lift_Time_Temp = round(self.Lift_Time_Temp + 0.005, 5) 
        self.LIFT_TIME.config(text="LIFT_TIME: " + str(self.Lift_Time_Temp))
    def LIFT_TIME_DOWN_CB(self):
        self.Lift_Time_Temp = round(self.Lift_Time_Temp - 0.005, 5) 
        self.LIFT_TIME.config(text="LIFT_TIME: " + str(self.Lift_Time_Temp))
    
    def SWING_TIME_UP_CB(self):
        self.Swing_Time_Temp = round(self.Swing_Time_Temp + 0.005, 5) 
        self.SWING_TIME.config(text="SWING_TIME: " + str(self.Swing_Time_Temp))
    def SWING_TIME_DOWN_CB(self):
        self.Swing_Time_Temp = round(self.Swing_Time_Temp - 0.005, 5) 
        self.SWING_TIME.config(text="SWING_TIME: " + str(self.Swing_Time_Temp))
    
    def RETRACT_TIME_UP_CB(self):
        self.Retract_Time_Temp = round(self.Retract_Time_Temp + 0.005, 5) 
        self.RETRACT_TIME.config(text="RETRACT_TIME: " + str(self.Retract_Time_Temp))
    def RETRACT_TIME_DOWN_CB(self):
        self.Retract_Time_Temp = round(self.Retract_Time_Temp - 0.005, 5) 
        self.RETRACT_TIME.config(text="RETRACT_TIME: " + str(self.Retract_Time_Temp))
    
    def LANDING_TIME_UP_CB(self):
        self.Landing_Time_Temp = round(self.Landing_Time_Temp + 0.005, 5) 
        self.LANDING_TIME.config(text="LANDING_TIME: " + str(self.Landing_Time_Temp))
    def LANDING_TIME_DOWN_CB(self):
        self.Landing_Time_Temp = round(self.Landing_Time_Temp - 0.005, 5) 
        self.LANDING_TIME.config(text="LANDING_TIME: " + str(self.Landing_Time_Temp))
    
    def FINISHED_TIME_UP_CB(self):
        self.Finished_Time_Temp = round(self.Finished_Time_Temp + 0.005, 5) 
        self.FINISHED_TIME.config(text="FINISHED_TIME: " + str(self.Finished_Time_Temp))
    def FINISHED_TIME_DOWN_CB(self):
        self.Finished_Time_Temp = round(self.Finished_Time_Temp - 0.005, 5) 
        self.FINISHED_TIME.config(text="FINISHED_TIME: " + str(self.Finished_Time_Temp))

    # save
    def SAVE_CB(self):
        global is_updated
        json_object["kicking_v10"] = {
            "Torso_X": self.Torso_X_Temp, 
            "Torso_Y": self.Torso_Y_Temp,
            "Torso_Z": self.Torso_Z_Temp,
            "L_Shift_X": self.L_Shift_X_Temp,
            "L_Shift_Y": self.L_Shift_Y_Temp, 
            "L_Shift_Z": self.L_Shift_Z_Temp,
            "R_Shift_X": self.R_Shift_X_Temp,
            "R_Shift_Y": self.R_Shift_Y_Temp, 
            "R_Shift_Z": self.R_Shift_Z_Temp,
            "L_Lift_X": self.L_Lift_X_Temp,
            "L_Lift_Y": self.L_Lift_Y_Temp,
            "L_Lift_Z": self.L_Lift_Z_Temp,
            "R_Lift_X": self.R_Lift_X_Temp, 
            "R_Lift_Y": self.R_Lift_Y_Temp,
            "R_Lift_Z": self.R_Lift_Z_Temp,
            "L_Swing_X": self.L_Swing_X_Temp,
            "L_Swing_Y": self.L_Swing_Y_Temp,
            "L_Swing_Z": self.L_Swing_Z_Temp,
            "R_Swing_X": self.R_Swing_X_Temp, 
            "R_Swing_Y": self.R_Swing_Y_Temp,
            "R_Swing_Z": self.R_Swing_Z_Temp,
            "L_Retract_X": self.L_Retract_X_Temp,
            "L_Retract_Y": self.L_Retract_Y_Temp,
            "L_Retract_Z": self.L_Retract_Z_Temp,
            "R_Retract_X": self.R_Retract_X_Temp,
            "R_Retract_Y": self.R_Retract_Y_Temp,
            "R_Retract_Z": self.R_Retract_Z_Temp,
            "Torso_Pitch": self.Torso_Pitch_Temp, 
            "Shift_Roll": self.Shift_Roll_Temp,
            "Lift_Roll": self.Lift_Roll_Temp,
            "Lift_Pitch": self.Lift_Pitch_Temp, 
            "Swing_Roll": self.Swing_Roll_Temp,
            "Swing_Pitch": self.Swing_Pitch_Temp, 
            "Retract_Roll": self.Retract_Roll_Temp,
            "Retract_Pitch": self.Retract_Pitch_Temp, 
            "SHIFT_TIME": self.Shift_Time_Temp,
            "LIFT_TIME": self.Lift_Time_Temp,
            "SWING_TIME": self.Swing_Time_Temp,
            "RETRACT_TIME": self.Retract_Time_Temp, 
            "LANDING_TIME": self.Landing_Time_Temp, 
            "FINISHED_TIME": self.Finished_Time_Temp
        }
        print("Saved succesfully!")

        #------Upload Data To The Firebase--------#
        if(is_updated and internet_status):
            is_updated = False
            data={"general":{"is_updated": is_updated},
            "kicking_v10/0":{
            "Torso_X": self.Torso_X_Temp, 
            "Torso_Y": self.Torso_Y_Temp,
            "Torso_Z": self.Torso_Z_Temp,
            "L_Shift_X": self.L_Shift_X_Temp,
            "L_Shift_Y": self.L_Shift_Y_Temp, 
            "L_Shift_Z": self.L_Shift_Z_Temp,
            "R_Shift_X": self.R_Shift_X_Temp,
            "R_Shift_Y": self.R_Shift_Y_Temp, 
            "R_Shift_Z": self.R_Shift_Z_Temp,
            "L_Lift_X": self.L_Lift_X_Temp,
            "L_Lift_Y": self.L_Lift_Y_Temp,
            "L_Lift_Z": self.L_Lift_Z_Temp,
            "R_Lift_X": self.R_Lift_X_Temp, 
            "R_Lift_Y": self.R_Lift_Y_Temp,
            "R_Lift_Z": self.R_Lift_Z_Temp,
            "L_Swing_X": self.L_Swing_X_Temp,
            "L_Swing_Y": self.L_Swing_Y_Temp,
            "L_Swing_Z": self.L_Swing_Z_Temp,
            "R_Swing_X": self.R_Swing_X_Temp, 
            "R_Swing_Y": self.R_Swing_Y_Temp,
            "R_Swing_Z": self.R_Swing_Z_Temp,
            "L_Retract_X": self.L_Retract_X_Temp,
            "L_Retract_Y": self.L_Retract_Y_Temp,
            "L_Retract_Z": self.L_Retract_Z_Temp,
            "R_Retract_X": self.R_Retract_X_Temp,
            "R_Retract_Y": self.R_Retract_Y_Temp,
            "R_Retract_Z": self.R_Retract_Z_Temp,
            "Torso_Pitch": self.Torso_Pitch_Temp, 
            "Shift_Roll": self.Shift_Roll_Temp,
            "Lift_Roll": self.Lift_Roll_Temp,
            "Lift_Pitch": self.Lift_Pitch_Temp, 
            "Swing_Roll": self.Swing_Roll_Temp,
            "Swing_Pitch": self.Swing_Pitch_Temp, 
            "Retract_Roll": self.Retract_Roll_Temp,
            "Retract_Pitch": self.Retract_Pitch_Temp, 
            "SHIFT_TIME": self.Shift_Time_Temp,
            "LIFT_TIME": self.Lift_Time_Temp,
            "SWING_TIME": self.Swing_Time_Temp,
            "RETRACT_TIME": self.Retract_Time_Temp, 
            "LANDING_TIME": self.Landing_Time_Temp, 
            "FINISHED_TIME": self.Finished_Time_Temp}
            }
            conf.db.update(data)
            json_object["is_updated"] = is_updated

            with open("/home/ajus/Desktop/alfarobi_ws/src/alfarobi_gui/config/GlobalConfig.json", "w") as outfile:
                json.dump(json_object, outfile)
            print("Uploaded to the firebase!")
        
        else:
            json_object["is_updated"] = is_updated

            with open("/home/ajus/Desktop/alfarobi_ws/src/alfarobi_gui/config/GlobalConfig.json", "w") as outfile:
                json.dump(json_object, outfile)
        
    def ENTER_CB(self):
        
        self.Param.torso[0] = self.Torso_X_Temp
        self.Param.torso[1] = self.Torso_Y_Temp
        self.Param.torso[2] = self.Torso_Z_Temp

        self.Param.left_leg[0] = self.L_Shift_X_Temp
        self.Param.left_leg[1] = self.L_Shift_Y_Temp
        self.Param.left_leg[2] = self.L_Shift_Z_Temp
        self.Param.left_leg[3] = self.L_Lift_X_Temp
        self.Param.left_leg[4] = self.L_Lift_Y_Temp
        self.Param.left_leg[5] = self.L_Lift_Z_Temp
        self.Param.left_leg[6] = self.L_Swing_X_Temp
        self.Param.left_leg[7] = self.L_Swing_Y_Temp
        self.Param.left_leg[8] = self.L_Swing_Z_Temp
        self.Param.left_leg[9] = self.L_Retract_X_Temp
        self.Param.left_leg[10] = self.L_Retract_Y_Temp
        self.Param.left_leg[11] = self.L_Retract_Z_Temp
        
        self.Param.right_leg[0] = self.R_Shift_X_Temp
        self.Param.right_leg[1] = self.R_Shift_Y_Temp
        self.Param.right_leg[2] = self.R_Shift_Z_Temp
        self.Param.right_leg[3] = self.R_Lift_X_Temp
        self.Param.right_leg[4] = self.R_Lift_Y_Temp
        self.Param.right_leg[5] = self.R_Lift_Z_Temp
        self.Param.right_leg[6] = self.R_Swing_X_Temp
        self.Param.right_leg[7] = self.R_Swing_Y_Temp
        self.Param.right_leg[8] =  self.R_Swing_Z_Temp
        self.Param.right_leg[9] =  self.R_Retract_X_Temp
        self.Param.right_leg[10] = self.R_Retract_Y_Temp
        self.Param.right_leg[11] = self.R_Retract_Z_Temp

        self.Param.angle[0] = self.Torso_Pitch_Temp
        self.Param.angle[1] = self.Shift_Roll_Temp
        self.Param.angle[2] = self.Lift_Roll_Temp
        self.Param.angle[3] = self.Lift_Pitch_Temp
        self.Param.angle[4] = self.Swing_Roll_Temp
        self.Param.angle[5] = self.Swing_Pitch_Temp
        self.Param.angle[6] = self.Retract_Roll_Temp
        self.Param.angle[7] = self.Retract_Pitch_Temp

        self.Param.time[0] = self.Shift_Time_Temp
        self.Param.time[1] = self.Lift_Time_Temp
        self.Param.time[2] = self.Swing_Time_Temp
        self.Param.time[3] = self.Retract_Time_Temp
        self.Param.time[4] = self.Landing_Time_Temp
        self.Param.time[5] = self.Finished_Time_Temp

        self.kick_param_pub.publish(self.Param)
    
    def LEFT_KICK_CB(self):
        self.button = "left"
        self.kick_button_pub.publish(self.button)
    
    def RIGHT_KICK_CB(self):
        self.button = "right"
        self.kick_button_pub.publish(self.button)