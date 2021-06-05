from tkinter import *
import sympy as sp


expression = ""

class Calculate:
    def press(num):
    
        global expression

        #get input from button press and add to expression
        expression = expression + str(num)
    
        sp.solve(expression)
 
 
    # Function to evaluate the final expression
    def equalpress():
        # Try and except statement is used
        # for handling the errors like zero
        # division error etc.
    
        # Put that code inside the try block
        # which may generate the error
        try:
    
            global expression
    
            #open and write the expression to a file
            f = open("calculator.txt", "a")
            f.write(expression)
            f.write("=")

            #calculate total
            total = str(eval(expression))

            #print total to console
            print(total)

            #write total to file and close it
            f.write(total)
            f.write("\n")
            f.close()
    
            expression = ""
    
        # handle errors
        except:
    
            print(" error ")
            expression = ""


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master
        self.press = Calculate.press
        self.equalpress = Calculate.equalpress

        # widget can take all window
        self.pack(fill=BOTH, expand=2)
        self.create_buttons()
        self.place_buttons()
    
    def create_buttons(self):
        # create button link it to the press function or equalpress function
        self.Button0 = Button(self, text=" 0         ", background='light green', command=lambda: self.press(0))
        self.Button1 = Button(self, text=" 1 ", background='pink', command=lambda: self.press(1))
        self.Button2 = Button(self, text=" 2 ", background='light green', command=lambda: self.press(2))
        self.Button3 = Button(self, text=" 3 ", background='pink', command=lambda: self.press(3))
        self.Button4 = Button(self, text=" 4 ", background='light green', command=lambda: self.press(4))
        self.Button5 = Button(self, text=" 5 ", background='pink', command=lambda: self.press(5))
        self.Button6 = Button(self, text=" 6 ", background='light green', command=lambda: self.press(6))
        self.Button7 = Button(self, text=" 7 ", background='pink', command=lambda: self.press(7))
        self.Button8 = Button(self, text=" 8 ", background='light green', command=lambda: self.press(8))
        self.Button9 = Button(self, text=" 9 ", background='pink', command=lambda: self.press(9))
        self.equalButton = Button(self, text=" =", background='light blue', command=self.equalpress)
        self.plusButton = Button(self, text=" +", background='light blue', command=lambda: self.press('+'))
        self.minusButton = Button(self, text=" - ", background='light blue', command=lambda: self.press('-'))
        self.multiplyButton = Button(self, text=" x ", background='light blue', command=lambda: self.press('*'))
        self.divideButton = Button(self, text=" / ", background='light blue', command=lambda: self.press('/'))

    def place_buttons(self):
        # place button at (0,0)
        self.Button0.place(x=25, y=170)
        self.equalButton.place(x=75, y=170)
        self.divideButton.place(x=100, y=170)
        self.Button1.place(x=25, y=140)
        self.Button2.place(x=50, y=140)
        self.Button3.place(x=75, y=140)
        self.multiplyButton.place(x=100, y=140)
        self.Button4.place(x=25, y=110)
        self.Button5.place(x=50, y=110)
        self.Button6.place(x=75, y=110)
        self.minusButton.place(x=100, y=110)
        self.Button7.place(x=25, y=80)
        self.Button8.place(x=50, y=80)
        self.Button9.place(x=75, y=80)
        self.plusButton.place(x=100, y=80)

#set up window and tkinter GUI        
root = Tk()
app = Window(root)
root.wm_title("Tkinter button")
root.geometry("150x200")
root.mainloop()
