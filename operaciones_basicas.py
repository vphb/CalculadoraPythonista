from interfaz_grafica import Calc

def numberEnter(Calc, num):
        Calc.result=False
        firstnum=Calc.txtDisplay.get()
        secondnum=str(num)
        if Calc.input_value:
            Calc.current = secondnum
            Calc.input_value=False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            Calc.current = firstnum+secondnum
        Calc.display(Calc.current)
  
def sum_of_total(Calc):
    Calc.result=True
    Calc.current=float(Calc.current)
    if Calc.check_sum==True:
        Calc.valid_function()
    else:
        Calc.total=float(Calc.txtDisplay.get())
  
    def display(Calc, value):
        Calc.txtDisplay.delete(0, Calc.END)
        Calc.txtDisplay.insert(0, value)
  
