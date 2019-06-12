from tkinter import Tk, Label, Button, Entry, StringVar#, LEFT, RIGHT

class personalBudgetGUI:
    def __init__(self, master):
        self.master = master
        master.title("Julian's Personal Budget")

        #geometry managers: Pack, Grid (complex interfaces) and Place (absolute position)
        self.label = Label(master, text="You got this!")
        #self.label.pack()
        self.label.grid(row=1, column=1, columnspan=2)

        self.labelNameText = StringVar()
        self.labelNameText.set("Type your name")
        self.labelName = Label(master, textvariable=self.labelNameText)
        #self.labelName.pack(side=LEFT)
        self.labelName.grid(row=2, column=1)
        
        self.name = Entry(master, textvariable=self.labelName)
        #self.name.pack(side=RIGHT)
        self.name.grid(row=2, column=2)

        self.greet_button = Button(master, text="Greet", command=self.greet)
        #self.greet_button.pack()
        self.greet_button.grid(row=3, column=1)

        self.close_button = Button(master, text="Close", command=master.destroy)
        #self.close_button.pack()
        self.close_button.grid(row=3, column=2)

    def greet(self):
        print(f"Greetings! Welcome to this awesome tool {self.name.get()}.")

app = Tk()
pb_gui = personalBudgetGUI(app)
app.mainloop()
