import tkinter as tk

class Mycalculator:
    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("300x300")
        self.root.title("My Calculator")

        self.label = tk.Label(self.root, text="Hello DIP01", font=('Arial', 18))
        self.label.pack()

        self.button = tk.Button(self.root, text="AC", height=4 , width=8)
        # self.button.place(x=20 , y=50)
        self.button.place(x=20, y=50)

        self.button = tk.Button(self.root, text="+/-", height=4 , width=8)
        self.button.place(x=90, y=50)

        self.button = tk.Button(self.root, text="%", height=4 , width=8)
        self.button.place(x=160, y=50)

        self.button = tk.Button(self.root, text="/", height=4 , width=8)
        self.button.place(x=230, y=50)

        self.button = tk.Button(self.root, text="7", height=4 , width=8)
        self.button.place(x=20, y=130)

        self.button = tk.Button(self.root, text="8", height=4 , width=8)
        self.button.place(x=90, y=130)

        self.button = tk.Button(self.root, text="9", height=4 , width=8)
        self.button.place(x=160, y=130)

        self.button = tk.Button(self.root, text="x", height=4 , width=8)
        self.button.place(x=230, y=130)

        self.button = tk.Button(self.root, text="4", height=4 , width=8)
        self.button.place(x=20, y=210)

        self.button = tk.Button(self.root, text="5", height=4 , width=8)
        self.button.place(x=90, y=210)

        self.button = tk.Button(self.root, text="6", height=4 , width=8)
        self.button.place(x=160, y=210)

        self.button = tk.Button(self.root, text="-", height=4 , width=8)
        self.button.place(x=230, y=210)

        self.button = tk.Button(self.root, text="1", height=4 , width=8)
        self.button.place(x=20, y=290)

        self.button = tk.Button(self.root, text="2", height=4 , width=8)
        self.button.place(x=90, y=290)

        self.button = tk.Button(self.root, text="3", height=4 , width=8)
        self.button.place(x=160, y=290)

        self.button = tk.Button(self.root, text="+", height=4 , width=8)
        self.button.place(x=230, y=290)

        self.button = tk.Button(self.root, text="0", height=4 , width=18)
        self.button.place(x=20, y=370)







        self.root.mainloop()

Mycalculator()        

