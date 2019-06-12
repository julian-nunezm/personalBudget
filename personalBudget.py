from tkinter import Tk, Label, Button

class personalBudgetGUI:
    def __init__(self, master):
        self.master = master
        master.title("Julian's Personal Budget")

        self.label = Label(master, text="You got this!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.destroy)
        self.close_button.pack()

    def greet(self):
        print("Greetings! Welcome to this awesome tool.")

root = Tk()
pb_gui = personalBudgetGUI(root)
root.mainloop()
