from ssl import Options
from tkinter import *
from tkinter.ttk import *
from AlfarobiWorkspace import *

class Page1:
    def __init__(self):
        #---Window Initialization--------#
        self.window1 = Tk()
        self.window1.geometry("640x480")
        self.window1.title("ALFAROBI GUI")
        self.window1.config(bg="#3399FF")
        self.window1.resizable(width=FALSE, height=FALSE)

        #----------Page Title----------------#

        # Frame
        self.frame1 = Frame(
            master=self.window1,
            width=640,
            height=480,
            bg="black",
            borderwidth=10,
        )
        self.frame1.pack(
            anchor=CENTER,
        )
        # self.frame1.place(
        #     x=0,
        #     y=0
        # )

        # Comment
        self.page_title = Label(
            master=self.frame1,
            text="MAIN MENU",
            font=("Times", 60),
            foreground="white",
            background="black",
            height=2,
            width=17
        )

        self.page_title.pack(anchor=CENTER)
        # self.page_title.place(
        #     x=80,
        #     y=50,
        # )

        self.page_subtitle = Label(
            master=self.frame1,
            text="SELECT ROBOT:",
            font=('Times', 20),
            foreground="white",
            background="black",
        )

        self.page_subtitle.pack(anchor=CENTER)
        # self.page_subtitle.place(
        #     x=125,
        #     y=150,
        # )
        #--------Option Menu---------------#

        # Frame
        self.optionFrame = Frame(
            master=self.window1,
            width=640,
            height=150,
            bg="#3399FF",
        )
        self.optionFrame.pack(anchor=CENTER, pady = 20)
        # self.optionFrame.place(
        #     x=240,
        #     y=260,
        # )

        # datatype of menu text
        self.clicked = StringVar()

        # Dropdown menu options
        self.options = [
            "Alfa",
            "Robi",
            "Abi",
            "Faro",
        ]

        # initial menu text
        self.clicked.set( "-choose robot-" )

        # Create Dropdown menu
        self.drop = OptionMenu(
            self.optionFrame,
            self.clicked ,
            *self.options)
        self.drop.pack(anchor=CENTER)
        

        #---------------Error label--------------------#
        
        # Frame
        self.errorFrame = Frame(
            master=self.window1,
            width=640,
            height=150,
            bg="#3399FF"
        )
        self.errorFrame.pack(anchor=CENTER)
        # self.errorFrame.place(
        #     x=220,
        #     y=230
        # )

        # Label
        self.error_lbl = Label(
            master=self.errorFrame,
            text=" ",
            fg="#3399FF",
            bg="#3399FF"
        )
        self.error_lbl.pack()

        #--------Enter Button------------------#
        
        # Frame
        self.enterFrame = Frame(
            master=self.window1,
            width=640,
            height=100,
            bg="#3399FF",
            relief="raised"
        )
        self.enterFrame.pack(anchor=CENTER, pady=15)
        # self.enterFrame.place(
        #     x=273,
        #     y=300
        # )

        # Button
        self.enter_button = Button( 
            master=self.enterFrame,
            text = "ENTER",
            command=lambda:self.show(),
            font=('MODERN', 10),
            width=7,
            height=1,
            bg="black",
            fg="white",
            )
        self.enter_button.pack()

        #---------Exit Button------------#

        # Frame
        self.exitFrame = Frame(
            master=self.window1,
            width=640,
            height=100,
            bg="black",
            relief="raised"
        )
        self.exitFrame.pack()
        self.exitFrame.place(
            x=10,
            y=440
        )

        # Button
        self.exit_btn = Button(
            master=self.exitFrame,
            text = "EXIT",
            command=lambda:self.exit(),
            font=('MODERN', 10),
            width=7,
            height=1,
            bg="black",
            fg="white",
            
        )
        self.exit_btn.pack()

        #-----------Next Button------------#

        # Frame
        self.nextFrame = Frame(
            master=self.window1,
            width=640,
            height=100,
            bg="black",
            relief="raised"
        )
        self.nextFrame.pack()
        self.nextFrame.place(
            x=550,
            y=440
        )

        # Button
        self.next_btn = Button(
            master=self.nextFrame,
            text = "NEXT",
            command=lambda:self.next(Page2),
            font=('MODERN', 10),
            width=7,
            height=1,
            bg="black",
            fg="white",
            
        )
        self.next_btn.pack()

        #---------Robot Information----------#

        # Variable that will store robot information
        self.id = int()
        self.name = str()

        # Frame
        self.robotInfoFrame = Frame(
            master=self.window1,
            width=640,
            height=100,
            bg="#3399FF"
        )
        self.robotInfoFrame.pack(anchor=CENTER, pady=10)
        # self.robotInfoFrame.place(
        #     x=265,
        #     y=350
        # )

        # Create Label
        self.robot_name = Label(
            master=self.robotInfoFrame,
            text = "ROBOT: - ",
            bg="black",
            fg="white",
            width=12,
            height=2
            )
        self.robot_name.pack()

        self.robot_id = Label(
            master=self.robotInfoFrame,
            text = "ID: - ",
            bg="black",
            fg="white",
            width=12,
            height=2
            )
        self.robot_id.pack()

        #----End of constructor-----------#
    

    # Change the label text and get robot information
    def show(self):
        if self.clicked.get()=="Alfa":
            self.id = 1
            self.name = "Alfa"
            self.robot_name.config(text = "ROBOT: " + self.clicked.get())
            self.robot_id.config(text="ID: " + str(self.id) )
            self.error_lbl.destroy()
        elif self.clicked.get()=="Robi":
            self.id = 2
            self.name = "Robi"
            self.robot_name.config(text = "ROBOT: " + self.clicked.get())
            self.robot_id.config(text="ID: " + str(self.id) )
            self.error_lbl.destroy()
        elif self.clicked.get()=="Abi":
            self.id = 3
            self.name = "Abi"
            self.robot_name.config(text = "ROBOT: " + self.clicked.get())
            self.robot_id.config(text="ID: " + str(self.id) )
            self.error_lbl.destroy()
        elif self.clicked.get()=="Faro":
            self.id = 4
            self.name = "Faro"
            self.robot_name.config(text = "ROBOT: " + self.clicked.get())
            self.robot_id.config(text="ID: " + str(self.id) )
            self.error_lbl.destroy()
        else:
            self.error_lbl.config(text="Please choose a robot first!", fg="purple")
            
        

    # Run the window
    def start(self):
        self.window1.mainloop()
    
    # Exit the window
    def exit(self):
        self.window1.destroy()
    
    # window will changed to the next page
    def next(self, Page2):
        if self.name not in self.options:
            self.error_lbl.config(text="Please choose a robot first!", fg="purple")
        else:
            Page2.id = self.id
            Page2.name = self.name
            self.window1.destroy()
            Page2().start(Page2.name, Page2.id)
    