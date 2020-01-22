from tkinter import *
import random

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.canvas = Canvas(self, height = 310, width = 500)
        self.canvas.grid(row = 1, column = 0, rowspan = 4)

        ##Labels for the GUI
        Label(self, text="Roman Numeral Canvas").grid(row=0, column=0, sticky = E)
        Label(self, text="Number: ").grid(row=1, column=2)
        Label(self, text="Line Width: ").grid(row=2, column=2)
        Label(self, text="Line Color: ").grid(row=3, column=2)

        ##Title for entry box
        self.numch = BooleanVar()
        Checkbutton(self, text = "Numbers", variable = self.numch).grid(row=1, column=5, sticky = W)

        ##Line Width line with radio buttonw
        self.linewidth = StringVar()
        self.linewidth.set("1")
        Radiobutton(self, text="1", value="1", variable = self.linewidth).grid(row=2, column=3)
        Radiobutton(self, text="3", value="3", variable = self.linewidth).grid(row=2, column=4)
        Radiobutton(self, text="5", value="5", variable = self.linewidth).grid(row=2, column=5)

        ##Line Color Line with Radio Buttons 
        self.linecolor = StringVar()
        self.linecolor.set("Black")
        Radiobutton(self, text="Black", value="Black", variable = self.linecolor).grid(row=3, column=3)
        Radiobutton(self, text="Red", value="Red", variable = self.linecolor).grid(row=3, column=4, sticky = W)
        Radiobutton(self, text="Blue", value="Blue", variable = self.linecolor).grid(row=3, column=5)

        ##Entry Box
        self.nument = Entry(self, width = 25)
        self.nument.grid(row=1, column=3)

        ##Roman button
        self.roman = PhotoImage(file="roman.gif")
        Button(self, image=self.roman, command = self.romanize).grid(row=4, column=3, sticky = W)

        ##I had to rename the image to silly.gif as it wouldn't find the gif for some reason
        self.randpic = PhotoImage(file="silly.gif")
        Button(self, image=self.randpic, command = self.sillify).grid(row=4, column=4,columnspan = 2, sticky = E)

        ##Starting coordinates for the canvas
        self.x, self.y = 20,20
    
    ##I wasn't sure how to go about writing these exact characters, so I thought of making them a combination
    ##of the up, down, left and right commands from class. Is this how it was suppose to be done?
    ##Probably not. But I really couldn't think of another way. (My plumbing at my house busted so I couldn't make it to class Thursday so I'm paying for it) 
    def up(self):
        self.canvas.create_line(slef.x, self.y, self.x, self.y - 20)
        self.y -= 20

    def down(self):
        self.canvas.create_line(slef.x, self.y, self.x, self.y + 20)
        self.y += 20

    def left(self):
        self.canvas.create_line(slef.x, self.y, self.x - 20, self.y)
        self.x -= 20

    def right(self):
        self.canvas.create_line(slef.x, self.y, self.x + 20, self.y)
        self.x += 20

    def sillify(self):
        pass


    def romanize(self):
        commands = self.numch.get()

        for char in commands:
            if char == "M":
                self.m()
            elif char == "D":
                self.d()
            elif char == "C":
                self.c()
            elif char == "L":
                self.l()
            elif char == "X":
                self.x()
            elif char == "V":
                self.v()
            elif char == "I":
                self.i()

    def m(self):
        right()
        right()
        left()
        down()
        down()
        down()
        down()
        left()
        right()
        right()
        left()
        up()
        up()
        up()
        up()
        right()
        down()
        right()
        down()
        down()
        right()
        down()
        right()
        down()
        right()
        down()
        down()
        down()
        right()
        up()
        up()
        up()
        right()
        up()
        right()
        up()
        right()
        up()
        up()
        right()
        up()
        right()
        up()
        left()
        right()
        right()
        left()
        down()
        down()
        down()
        down()
        left()
        right()
        right()

##At this point in time there is 5 minutes left and I'm just not able to really finish this one off.
##I really struggled getting the GUI to look the way it's suppose to, so I know to study further into reading columns as that's what
##was getting to me. As far as wat the rest of step 2 would've been like, I would've used the same method that I used for M just to make
##the other letters. Again I don't know if that's correct but I feel as if it could have worked so I'm happy with getting some of it in there.
##But ultimately I'm sorry for not finishing this. If there's any way you could give me feedback on step 2 that would be super helpful.
##Im' going to be practicing a lot of python over break because I'm pretty dumb at this so I should prep for the next class yikes.

##okay that was a really long comment i sound like I'm going through a crisis and class is over oops I gotta go thx for grading my poor lil code lol have a good break!!
        
        




##Main

root = Tk()
root.title("Roman Numerals")
root.geometry("900x350")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
