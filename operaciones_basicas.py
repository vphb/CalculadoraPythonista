from tkinter import *

root = Tk()
root.title("Scientific Calculator")
root.configure(background = 'white')
root.resizable(width=False, height=False)
root.geometry("480x568+450+90")

calc = Frame(root)
calc.grid()

txtDisplay = Entry(calc,
                   font=('Helvetica', 20,
                         'bold'),
                   bg='black',
                   fg='white',
                   bd=30,
                   width=28,
                   justify=RIGHT)
  
txtDisplay.grid(row=0,
                column=0,
                columnspan=4,
                pady=1)
  
txtDisplay.insert(0, "0")

calc = Frame(root)
calc.grid()
class Calc():
    def __init__(self):
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False
  
    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum+secondnum
        self.display(self.current)
  
    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())
  
    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)
  
    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)
  
    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False
  
    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True
  
    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0