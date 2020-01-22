from tkinter import *
import random

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Design Your Movie:").grid(row = 0, column = 0, columnspan = 5)
        Label(self, text = "Name:").grid(row = 1, column = 0, sticky = W)
        Label(self, text = "Genre:").grid(row = 2, column = 0, sticky = W)
        Label(self, text = "Rating:").grid(row = 3, column = 0, sticky = W)
        Label(self, text = "Budget: $").grid(row = 4, column = 1, sticky = E)       
        Label(self, text = "Actors:").grid(row = 5, column = 0, sticky = W)

        self.genre = StringVar()
        self.genre.set("action movie")
        Radiobutton(self, text="Action", value="action movie", variable=self.genre).grid(row=2, column=1, sticky=W)
        Radiobutton(self, text="Comedy", value="ingenious comedy", variable=self.genre).grid(row=2, column=2, sticky=W)
        Radiobutton(self, text="Documentary", value="interesting documentary", variable=self.genre).grid(row=2, column=3, sticky=W)
        Radiobutton(self, text="Drama", value="inspiring drama", variable=self.genre).grid(row=2, column=4, sticky=W)
        
        self.rating = StringVar()
        self.rating.set("G")
        Radiobutton(self, text="G", value="G", variable=self.rating).grid(row=3, column=1, sticky=W)
        Radiobutton(self, text="PG", value="PG", variable=self.rating).grid(row=3, column=2, sticky=W)
        Radiobutton(self, text="PG-13", value="PG-13", variable=self.rating).grid(row=3, column=3, sticky=W)
        Radiobutton(self, text="R", value="R", variable=self.rating).grid(row=3, column=4, sticky=W)

        self.name = Entry(self, width=85)
        self.name.grid(row=1, column=1, columnspan = 4, sticky=W)

        self.budget = Entry(self, width=40)
        self.budget.grid(row=4, column=2, columnspan = 2, sticky=W)
        
        self.rdjr = BooleanVar()
        Checkbutton(self, text = "Robert Downey Jr.", variable = self.rdjr).grid(row = 5, column = 1, sticky = W)
        self.ch = BooleanVar()
        Checkbutton(self, text = "Chris Hemsworth", variable = self.ch).grid(row = 5, column = 2, sticky = W)
        self.dj = BooleanVar()
        Checkbutton(self, text = "Dwayne Johnson", variable = self.dj).grid(row = 5, column = 3, sticky = W)

        self.aj = BooleanVar()
        Checkbutton(self, text = "Angelina Jolie", variable = self.aj).grid(row = 6, column = 1, sticky = W)
        self.mk = BooleanVar()
        Checkbutton(self, text = "Mila Kunis", variable = self.mk).grid(row = 6, column = 2, sticky = W)
        self.jr = BooleanVar()
        Checkbutton(self, text = "Julia Roberts", variable = self.jr).grid(row = 6, column = 3, sticky = W)

        self.chair = PhotoImage(file="chair.gif")
        Button(self, image=self.chair, command=self.pitch).grid(row = 4, column = 4, rowspan = 3)

        self.results = Text(self, width=70, height=4, wrap = WORD)
        self.results.grid(row = 8, column = 0, columnspan = 5)

    def pitch(self):
        message = self.name.get() + ", an " + self.genre.get() + " rated " + self.rating.get() + ", and"
        message += " costing $" + self.budget.get() + ", stars "

        stars = []

        if self.rdjr.get():
            stars.append("Robert Downey Jr.")
        if self.ch.get():
            stars.append("Chris Hemsworth")
        if self.dj.get():
            stars.append("Dwayne Johnson")
        if self.aj.get():
            stars.append("Angelina Jolie")
        if self.mk.get():
            stars.append("Mila Kunis")
        if self.jr.get():
            stars.append("Julia Roberts")

        stars = (", ").join(stars)

        if not stars:
            stars = "no one you've heard of"

        message += stars + "."

        result = random.randrange(100) + 1

        if result > int(self.budget.get()) / 1000:
            message += "\nIt got approved!"
        else:
            message += "\nThe studio passed on this one..."

        self.results.delete(0.0, END)
        self.results.insert(0.0, message)


# main
root = Tk()
root.title("Pitch a Movie!")
root.geometry("565x280")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
