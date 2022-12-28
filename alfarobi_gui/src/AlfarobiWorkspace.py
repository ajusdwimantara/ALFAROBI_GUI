from tkinter import *
from MotionPage import *

class Page2:
    def __init__(self):
        # ----Window Initialization---- #
        self.window = Tk(
    
        )
    
        self.window.geometry("640x480")
        self.window.title("ALFAROBI GUI")
        self.window.config(bg= "#0000FF")
        self.window.resizable(width=FALSE, height=FALSE)

        # ----Page Title---- #

        # Frame
        self.pageTitleFrame = Frame(
            master=self.window,
            width=640,
            height=480,
            bg="black",
            borderwidth=10,
        )
        self.pageTitleFrame.pack(anchor=CENTER)
        # self.pageTitleFrame.place(
        #     x=70,
        #     y=40
        # )

        # Comment
        self.comment1 = Label(
            master=self.pageTitleFrame,
            text="ALFAROBI",
            font=('MODERN', 70),
            foreground="black",
            background="white",
        )
        self.comment1.pack()
    
        self.comment2 = Label(
            master=self.pageTitleFrame,
            text="WORKSPACE",
            font=('MODERN', 30),
            foreground="white",
            background="black",
        )
        self.comment2.pack()

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

        #----------Button----------------#

        # Frame
        self.buttonFrame = Frame(
            master=self.window,
            width=640,
            height=100,
            bg="#0000FF",
        )
        self.buttonFrame.pack(anchor=CENTER, pady = 30)
        # self.buttonFrame.place(
        #     x = 250,
        #     y = 250
        # )

        # Tune
        self.tune = Button(
            master=self.buttonFrame,
            command=lambda:self.tune_pressed(),
            text="TUNE",
            font=('Modern', 20),
            foreground="white",
            background="black",
            width=7,
            height=1
        )
        self.tune.pack()
        
        # Motion and vision button will be packed when tune button is clicked
        self.motion = Button(
                master=self.buttonFrame,
                text="MOTION",
                font=('Modern', 20),
                command=lambda:self.motion_pressed(MotionPg),
                foreground="white",
                background="black",
                width=7,
                height=1
                )
        self.vision = Button(
            master=self.buttonFrame,
            text="VISION",
            font=('Modern', 20),
            command=lambda:self.vision_pressed(),
            foreground="white",
            background="black",
            width=7,
            height=1
            )
        
        #----Exit button-----------#
        self.exitFrame = Frame(
            master=self.window,
            width=640,
            height=100,
            bg="black",
        )
        self.exitFrame.pack(side=BOTTOM, anchor=CENTER, pady = 20)
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
        
        #----End of constructor----#
        
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
    
    # Method that will change tune button into vision and motion
    def tune_pressed(self):
        self.tune.destroy()
        self.motion.pack(anchor=CENTER, pady = 10)
        self.vision.pack(anchor=CENTER, pady = 10)
        self.window.update()

    # Method that will executed when motion is chosen
    def motion_pressed(self, MotionPg):
        MotionPg.id = self.id
        MotionPg.name = self.name
        self.window.destroy()
        MotionPg().start(self.name, self.id)

    # Method that will executed when vision is chosen
    def vision_pressed(self):
        pass   
