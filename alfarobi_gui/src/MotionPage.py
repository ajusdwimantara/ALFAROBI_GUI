from tkinter import *
from KickingPage import *

class MotionPg:
    def __init__(self):
        # ----Window Initialization---- #
        self.window = Tk(
    
        )
    
        self.window.geometry("640x480")
        self.window.title("ALFAROBI GUI")
        self.window.config(bg= "#0000FF")
        self.window.resizable(width=FALSE, height=FALSE)

        #--------Subscriber-------#
        self.motion_page_pub = rospy.Publisher('/motion_page', String, queue_size=5) # to activate the topic, we are not publishing anything in this page
        self.motion_page_sub = rospy.Subscriber('/motion_page', String, self.motion_page_cb)

        #-------Page Title---------#
        self.PageTitleFrame = Frame(
            master = self.window,
            height=200,
            width=640,
            bg="blue"
        )
        self.PageTitleFrame.pack()
        
        self.titleLabel = Label(
            master=self.PageTitleFrame,
            text="MOTION MENU",
            font=("Modern", 60),
            bg="black",
            fg="white",
            width=400,
            height=2
        )
        self.titleLabel.pack()

        # ----Robot Information-----------#
         # Variable that will store robot information given in page 1
        self.name = str()
        self.id = int()
        # Frame
        self.robotInfoFrame  = Frame(
            master=self.window,
            width=640,
            height=100,
            bg="black",
            borderwidth=10,
        )
        self.robotInfoFrame.pack()
        self.robotInfoFrame.place(
            x = 20,
            y = 380
        )

        # Name
        self.robot_name = Label(
            master=self.robotInfoFrame,
            text="ROBOT: ",
            font=('MODERN', 15),
            foreground="white",
            background="black",
        )
        self.robot_name.pack()

        # ID
        self.robot_id = Label(
            master=self.robotInfoFrame,
            text="ID: ",
            font=('MODERN', 15),
            foreground="white",
            background="black",
        )
        self.robot_id.pack()

        #----Exit button-----------#
        self.exitFrame = Frame(
            master=self.window,
            width=640,
            height=100,
            bg="#0000FF",
        )
        self.exitFrame.pack(anchor=CENTER, side=BOTTOM, pady=10)
        # self.exitFrame.place(
        #     x = 250,
        #     y = 400
        # )
        self.exit_button = Button(
            master=self.exitFrame,
            text="EXIT",
            font=('Modern', 20),
            command=exit,
            foreground="white",
            background="black",
            width=7,
            height=1
            )
        self.exit_button.pack()

        #-------Quintic Walk----------#
        self.quinticWalkFrame = Frame(
            master=self.window,
            width=640,
            height=100,
            bg="black"
        )
        self.quinticWalkFrame.pack(anchor=CENTER, pady=20)
        # self.quinticWalkFrame.place(
        #     x = 241,
        #     y = 170
        # )

        self.quinticWalkButton = Button(
            master = self.quinticWalkFrame,
            text = "Quintic Walk",
            bg = "black",
            fg = "white",
            font = ("Modern", 15),
            width=11,
            height=1
        )
        self.quinticWalkButton.pack()

        #--------Kicking-----------#
        self.kickingFrame = Frame(
            master=self.window,
            width=640,
            height=100,
            bg="black"
        )
        self.kickingFrame.pack(anchor=CENTER, pady=0)
        # self.kickingFrame.place(
        #     x = 241,
        #     y = 220
        # )

        self.kickingButton = Button(
            master = self.kickingFrame,
            text = "Kicking",
            bg = "black",
            fg = "white",
            font = ("Modern", 15),
            width=11,
            height=1,
            command=lambda:self.kicking_pressed(KickingPg)
        )
        self.kickingButton.pack()

        #--------Initial Pose--------#
        self.initPoseFrame = Frame(
            master=self.window,
            width=640,
            height=100,
            bg="black"
        )
        self.initPoseFrame.pack(anchor=CENTER, pady=20)
        # self.initPoseFrame.place(
        #     x = 241,
        #     y = 270
        # )

        self.initPoseButton = Button(
            master = self.initPoseFrame,
            text = "Initial Pose",
            bg = "black",
            fg = "white",
            font = ("Modern", 15),
            width=11,
            height=1
        )
        self.initPoseButton.pack()

    # # Variable that will store robot information given in page 1
    # name = str()
    # id = int()
    # Start the window
    def start(self, name, id):
        self.robot_name.config(text = "ROBOT: " + name)
        self.name = name
        self.robot_id.config(text="ID: " + str(id))
        self.id = id
        self.window.mainloop()
        
    # Exit the window
    def exit(self):
        self.window.destroy()

    def kicking_pressed(self, KickingPg):
        KickingPg.id = self.id
        KickingPg.name = self.name
        
        KickingPg().start(self.name, self.id)
    
    
    # Subcsriber callback
    def motion_page_cb(self, msg):
        page = msg.data

        # grey out the button when one of the command is running
        if(page=="kicking" or page=="quintic_walk" or page=="initial_pose"):
            for child in self.quinticWalkFrame.winfo_children():
                child.configure(state="disabled")
            for child in self.kickingFrame.winfo_children():
                child.configure(state="disabled")
            for child in self.initPoseFrame.winfo_children():
                child.configure(state="disabled")
            for child in self.exitFrame.winfo_children():
                child.configure(state="disabled")
        # enable the button again when the command is closed
        elif(page=="none"):
            for child in self.quinticWalkFrame.winfo_children():
                child.configure(state="normal")
            for child in self.kickingFrame.winfo_children():
                child.configure(state="normal")
            for child in self.initPoseFrame.winfo_children():
                child.configure(state="normal")
            for child in self.exitFrame.winfo_children():
                child.configure(state="normal")