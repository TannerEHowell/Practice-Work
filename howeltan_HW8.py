from tkinter import *
import random

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widget()
        self.number = random.randint(0,9)

    def create_widget(self):

        ##I tried doing a \n but it kept making an unnecessary space, originally these first two lines were just one line
        self.lbl = Label(self, text = "Im thinking of a number 0-9.").grid(row = 0, column = 0, sticky = W)
        self.lbl = Label(self, text = "Take a Guess what it is!").grid(row =1, column = 0, sticky = W)
        self.lbl = Label(self, text = "Your Guess Is: ").grid(row = 2, column = 0, sticky = W)

        ##Entry box for guessing the number
        self.ent = Entry(self, width = 10)
        self.ent.grid(row = 2, column = 1, sticky = W)

        ##Submission Button (I wasn't able to get the .bind to work, but I think this is how it would've gone.
        ##If you could help explain why it just wouldn't wrok that would be greatly appreicated.)
        self.bttn = Button(self, text = "Submit", command = self.guess_answr)
        self.bttn.grid(row = 3, column = 1, sticky = W)
##        self.bttn.bind("<Return>", self.enter_key)
##        self.bttn.focus_set()

        ##Text Box
        self.txt = Text(self, width = 50, height = 5, wrap = WORD)
        self.txt.grid(row = 4, column = 0,columnspan = 3, sticky = W)



    ##Command to run the guess
    def guess_answr(self):
        answr_num = int(self.ent.get())

        if answr_num != self.number:
            response = ""
            if answr_num > self.number:
                response += " That's too high. Guess lower..."
            elif answr_num < self.number:
                response += " That's too low. Guess higher..."

            self.txt.delete(0.0, END)
            self.txt.insert(0.0, response)

            self.ent.delete(0, END)

        ##Was a little confused on how to make a new window so I researched. I ended up using .pack()
        else:
            wind = Tk()
            wind.geometry("400x275")
            wind.title("Woah! A New Window! How Cool!")
            self.lbl = Label(wind, text="You Guessed it Right! You Earned Nothing!")
            self.lbl.grid()
            wind.mainloop()
        
        

    def enter_key(self, event):
        if event.keysym == "Return":
            self.guess_answr()






##Main
root = Tk()
root.title("Guessing Game!")
root.geometry("400x275")

app = Application(root)
root.mainloop()
