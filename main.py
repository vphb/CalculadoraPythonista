# Importa las bibliotecas necesarias para la interfaz gráfica y las operaciones matemáticas.
from tkinter import *
import math
import tkinter.messagebox

# Crea una ventana principal de la aplicación.
root = Tk()

# Configura el título de la ventana.
root.title("Calculadora Pythonista")

# Configura el color de fondo de la ventana.
root.configure(background='white')

# Hace que la ventana no sea redimensionable en anchura y altura.
root.resizable(width=False, height=False)

# Establece la geometría de la ventana con un tamaño y una posición específicos.
root.geometry("480x568+450+90")

# Crea un contenedor para los componentes de la calculadora.
calc = Frame(root)

# Organiza el contenedor en la ventana.
calc.grid()

class Calc():
    def __init__(self):
        """
        Inicializa una instancia de la calculadora.
        """
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False

    def numberEnter(self, num):
        """
        Registra un número en la calculadora.

        Args:
            num (str or float): El número que se va a registrar.
        """
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
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        """
        Realiza la suma total de la calculadora y muestra el resultado.
        """
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
        """
        Muestra el valor especificado en la pantalla de la calculadora.

        Args:
            value (str or float): El valor a mostrar en la pantalla.
        """
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        """
        Realiza la operación matemática actual y muestra el resultado.
        """
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
        if self.op == "potencia":
            self.total **= self.current
        if self.op == "cociente":
            self.total //= self.current

        self.input_value = True
        self.check_sum = False

        self.display(self.total)

    def operation(self, op):
        """
        Establece la operación matemática actual.

        Args:
            op (str): La operación a realizar (por ejemplo, "add", "sub", "multi", "divide", etc.).
        """
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
    """
    Limpia la entrada actual y restablece la calculadora a cero.

    Restablece la entrada actual a "0", borra la pantalla y permite una nueva entrada.
    """
    self.result = False
    self.current = "0"
    self.display(0)
    self.input_value = True

def All_Clear_Entry(self):
    """
    Borra completamente la calculadora.

    Limpia la entrada y restablece el total a cero, dejando la calculadora lista para una nueva operación.
    """
    self.Clear_Entry()
    self.total = 0

def pi(self):
    """
    Establece el valor actual en Pi (π) y muestra el resultado.

    Pi (π) es una constante matemática aproximadamente igual a 3.141592653589793.
    """
    self.result = False
    self.current = math.pi
    self.display(self.current)

def e(self):
    """
    Establece el valor actual en e y muestra el resultado.

    'e' es la base del logaritmo natural y es una constante matemática aproximadamente igual a 2.718281828459045.
    """
    self.result = False
    self.current = math.e
    self.display(self.current)

def mathPM(self):
    """
    Cambia el signo del valor actual y muestra el resultado.

    Cambia el signo del valor actual (positivo a negativo o viceversa) y lo muestra en la pantalla.
    """
    self.result = False
    self.current = -(float(txtDisplay.get()))
    self.display(self.current)

def squared(self):
    """
    Calcula la raíz cuadrada del valor actual y muestra el resultado.

    Calcula la raíz cuadrada del valor actual y lo muestra en la pantalla.
    """
    self.result = False
    self.current = math.sqrt(float(txtDisplay.get()))
    self.display(self.current)

def cos(self):
    """
    Calcula el coseno del valor actual (en grados) y muestra el resultado.

    Calcula el coseno del valor actual (en grados) y lo muestra en la pantalla.
    """
    self.result = False
    self.current = math.cos(math.radians(float(txtDisplay.get())))
    self.display(self.current)
  
def cosh(self):
    """
    Calcula el coseno hiperbólico del valor actual (en grados) y muestra el resultado.

    Calcula el coseno hiperbólico del valor actual (en grados) y lo muestra en la pantalla.
    """
    self.result = False
    self.current = math.cosh(math.radians(float(txtDisplay.get())))
    self.display(self.current)

def tan(self):
    """
    Calcula la tangente del valor actual (en grados) y muestra el resultado.

    Calcula la tangente del valor actual (en grados) y lo muestra en la pantalla.
    """
    self.result = False
    self.current = math.tan(math.radians(float(txtDisplay.get())))
    self.display(self.current)

def tanh(self):
    """
    Calcula la tangente hiperbólica del valor actual (en grados) y muestra el resultado.

    Calcula la tangente hiperbólica del valor actual (en grados) y lo muestra en la pantalla.
    """
    self.result = False
    self.current = math.tanh(math.radians(float(txtDisplay.get())))
    self.display(self.current)

def sin(self):
    """
    Calcula el seno del valor actual (en grados) y muestra el resultado.

    Calcula el seno del valor actual (en grados) y lo muestra en la pantalla.
    """
    self.result = False
    self.current = math.sin(math.radians(float(txtDisplay.get())))
    self.display(self.current)

def sinh(self):
    """
    Calcula el seno hiperbólico del valor actual (en grados) y muestra el resultado.

    Calcula el seno hiperbólico del valor actual (en grados) y lo muestra en la pantalla.
    """
    self.result = False
    self.current = math.sinh(math.radians(float(txtDisplay.get())))
    self.display(self.current)

def acosh(self):
    """
    Calcula el coseno hiperbólico inverso del valor actual y muestra el resultado.

    Calcula el coseno hiperbólico inverso del valor actual y lo muestra en la pantalla.
    """
    self.result = False
    self.current = math.acosh(float(txtDisplay.get()))
    self.display(self.current)

def asinh(self):
    """
    Calcula el seno hiperbólico inverso del valor actual y muestra el resultado.

    Calcula el seno hiperbólico inverso del valor actual y lo muestra en la pantalla.
    """
    self.result = False
    self.current = math.asinh(float(txtDisplay.get()))
    self.display(self.current)

def log(self):
    """
    Calcula el logaritmo natural del valor actual y muestra el resultado.

    Calcula el logaritmo natural (base e) del valor actual y lo muestra en la pantalla.
    """
    self.result = False
    self.current = math.log(float(txtDisplay.get()))
    self.display(self.current)

  
def exp(self):
    """
    Calcula la función exponencial de e elevado a la potencia del valor actual y muestra el resultado.

    Calcula la función exponencial de e elevado a la potencia del valor actual y lo muestra en la pantalla.
    """
    self.result = False
    self.current = math.exp(float(txtDisplay.get()))
    self.display(self.current)

def expm1(self):
    """
    Calcula la función exponencial menos 1 de e elevado a la potencia del valor actual y muestra el resultado.

    Calcula la función exponencial menos 1 de e elevado a la potencia del valor actual y lo muestra en la pantalla.
    """
    self.result = False
    self.current = math.expm1(float(txtDisplay.get()))
    self.display(self.current)

def log2(self):
    """
    Calcula el logaritmo en base 2 del valor actual y muestra el resultado.

    Calcula el logaritmo en base 2 del valor actual y lo muestra en la pantalla.
    """
    self.result = False
    self.current = math.log2(float(txtDisplay.get()))
    self.display(self.current)

def log10(self):
    """
    Calcula el logaritmo en base 10 del valor actual y muestra el resultado.

    Calcula el logaritmo en base 10 del valor actual y lo muestra en la pantalla.
    """
    self.result = False
    self.current = math.log10(float(txtDisplay.get()))
    self.display(self.current)

def log1p(self):
    """
    Calcula el logaritmo natural de 1 más el valor actual y muestra el resultado.

    Calcula el logaritmo natural de 1 más el valor actual y lo muestra en la pantalla.
    """
    self.result = False
    self.current = math.log1p(float(txtDisplay.get()))
    self.display(self.current)


def degrees(self):
    """
    Convierte el valor actual de radianes a grados y muestra el resultado.

    Convierte el valor actual de radianes a grados y lo muestra en la pantalla.
    """
    self.result = False
    self.current = math.degrees(float(txtDisplay.get()))
    self.display(self.current)

added_value = Calc()

# Crea un campo de entrada de texto (display) para mostrar los números y resultados.
txtDisplay = Entry(calc, font=('Helvetica', 20, 'bold'),
                   bg='black', fg='white',
                   bd=30, width=28, justify=RIGHT)

# Coloca el campo de entrada en la cuadrícula del contenedor y configura su contenido inicial en "0".
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

# Define los números en el teclado numérico de la calculadora.
numberpad = "789456123"
i = 0
btn = []

# Crea botones numéricos y los coloca en la cuadrícula.
for j in range(2, 5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2,
                          bg='black', fg='white',
                          font=('Helvetica', 20, 'bold'),
                          bd=4, text=numberpad[i]))

        # Coloca cada botón en la cuadrícula en la posición correspondiente.
        btn[i].grid(row=j, column=k, pady=1)

        # Asocia una función lambda a cada botón para manejar los eventos de clic.
        btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
        i += 1
        
# Crea un botón "Clear Entry" que llama a la función 'Clear_Entry' cuando se hace clic.
btnClear = Button(calc, text=chr(67), width=6, height=2, bg='powder blue',
                  font=('Helvetica', 20, 'bold'), bd=4, command=lambda: added_value.Clear_Entry()
                 ).grid(row=1, column=0, pady=1)

# Crea un botón "All Clear Entry" que llama a la función 'All_Clear_Entry' cuando se hace clic.
btnAllClear = Button(calc, text=chr(67) + chr(69), width=6, height=2, bg='powder blue', 
                     font=('Helvetica', 20, 'bold'), bd=4, command=lambda: added_value.All_Clear_Entry()
                    ).grid(row=1, column=1, pady=1)

# Crea un botón con el símbolo de raíz cuadrada (√) que llama a la función 'squared' cuando se hace clic.
btnsq = Button(calc, text="\u221A", width=6, height=2, bg='powder blue', font=('Helvetica', 20, 'bold'),
               bd=4, command=lambda: added_value.squared()
              ).grid(row=1, column=2, pady=1)

# Crea un botón de suma (+) que llama a la función 'operation("add")' cuando se hace clic.
btnAdd = Button(calc, text="+", width=6, height=2, bg='powder blue', font=('Helvetica', 20, 'bold'),
                bd=4, command=lambda: added_value.operation("add")
                ).grid(row=1, column=3, pady=1)
 
# Crea un botón de resta (-) que llama a la función 'operation("sub")' cuando se hace clic.
btnSub = Button(calc, text="-", width=6, height=2, bg='powder blue', font=('Helvetica', 20, 'bold'),
                bd=4, command=lambda: added_value.operation("sub")
                ).grid(row=2, column=3, pady=1)

# Crea un botón de multiplicación (x) que llama a la función 'operation("multi")' cuando se hace clic.
btnMul = Button(calc, text="x", width=6, height=2, bg='powder blue', font=('Helvetica', 20, 'bold'),
                bd=4, command=lambda: added_value.operation("multi")
                ).grid(row=3, column=3, pady=1)

# Crea un botón de división (/) que llama a la función 'operation("divide")' cuando se hace clic.
btnDiv = Button(calc, text="/", width=6, height=2, bg='powder blue', font=('Helvetica', 20, 'bold'),
                bd=4, command=lambda: added_value.operation("divide")
                ).grid(row=4, column=3, pady=1)

# Crea un botón "0" que llama a la función 'numberEnter(0)' cuando se hace clic.
btnZero = Button(calc, text="0", width=6, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'),
                 bd=4, command=lambda: added_value.numberEnter(0)
                 ).grid(row=5, column=0, pady=1)

# Crea un botón "." (punto decimal) que llama a la función 'numberEnter(".")' cuando se hace clic.
btnDot = Button(calc, text=".", width=6, height=2, bg='powder blue', font=('Helvetica', 20, 'bold'),
                bd=4, command=lambda: added_value.numberEnter(".")
                ).grid(row=5, column=1, pady=1)

# Crea un botón "±" (cambio de signo) que llama a la función 'mathPM' cuando se hace clic.
btnPM = Button(calc, text=chr(177), width=6, height=2, bg='powder blue', font=('Helvetica', 20, 'bold'),
              bd=4, command=lambda: added_value.mathPM()
              ).grid(row=5, column=2, pady=1)

# Crea un botón de igual (=) que llama a la función 'sum_of_total' cuando se hace clic.
btnEquals = Button(calc, text="=", width=6, height=2, bg='powder blue', font=('Helvetica', 20, 'bold'),
                   bd=4, command=lambda: added_value.sum_of_total()
                  ).grid(row=5, column=3, pady=1)

# ROW 1:
# Crea un botón "pi" que llama a la función 'pi' cuando se hace clic.
btnPi = Button(calc, text="pi", width=6, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'),
              bd=4, command=lambda: added_value.pi()
              ).grid(row=1, column=4, pady=1)

# Crea un botón "Cos" que llama a la función 'cos' cuando se hace clic.
btnCos = Button(calc, text="Cos", width=6, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'),
               bd=4, command=lambda: added_value.cos()
              ).grid(row=1, column=5, pady=1)
  
# Crea un botón "tan" que llama a la función 'tan' cuando se hace clic.
btntan = Button(calc, text="tan", width=6, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'),
               bd=4, command=lambda: added_value.tan()
              ).grid(row=1, column=6, pady=1)

# Crea un botón "sin" que llama a la función 'sin' cuando se hace clic.
btnsin = Button(calc, text="sin", width=6, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'),
               bd=4, command=lambda: added_value.sin()
              ).grid(row=1, column=7, pady=1)

# ROW 2:
# Crea un botón "^" (potencia) que llama a la función 'operation("potencia")' cuando se hace clic.
btn_potencia = Button(calc, text="^", width=6, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'),
                    bd=4, command=lambda: added_value.operation("potencia")
                   ).grid(row=2, column=4, pady=1)

# Crea un botón "Cosh" que llama a la función 'cosh' cuando se hace clic.
btnCosh = Button(calc, text="Cosh", width=6, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'),
                bd=4, command=lambda: added_value.cosh()
                ).grid(row=2, column=5, pady=1)

# Crea un botón "tanh" que llama a la función 'tanh' cuando se hace clic.
btntanh = Button(calc, text="tanh", width=6, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'),
                bd=4, command=lambda: added_value.tanh()
                ).grid(row=2, column=6, pady=1)

# Crea un botón "sinh" que llama a la función 'sinh' cuando se hace clic.
btnsinh = Button(calc, text="sinh", width=6, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'),
                bd=4, command=lambda: added_value.sinh()
                ).grid(row=2, column=7, pady=1)

# ROW 3:
# Crea un botón "log" que llama a la función 'log' cuando se hace clic.
btnlog = Button(calc, text="log", width=6, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'),
               bd=4, command=lambda: added_value.log()
              ).grid(row=3, column=4, pady=1)

# Crea un botón "exp" que llama a la función 'exp' cuando se hace clic.
btnExp = Button(calc, text="exp", width=6, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'),
               bd=4, command=lambda: added_value.exp()
              ).grid(row=3, column=5, pady=1)

# Crea un botón "Mod" que llama a la función 'operation("mod")' cuando se hace clic.
btnMod = Button(calc, text="Mod", width=6, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'),
               bd=4, command=lambda: added_value.operation("mod")
              ).grid(row=3, column=6, pady=1)

# Crea un botón "e" que llama a la función 'e' cuando se hace clic.
btnE = Button(calc, text="e", width=6, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'),
             bd=4, command=lambda: added_value.e()
            ).grid(row=3, column=7, pady=1)
 
# ROW 4:
# Crea un botón "log10" que llama a la función 'log10' cuando se hace clic.
btnlog10 = Button(calc, text="log10", width=6, height=2, bg='black', fg='white', 
                font=('Helvetica', 20, 'bold'), bd=4, command=lambda: added_value.log10()
                ).grid(row=4, column=4, pady=1)

# Crea un botón "log1p" que llama a la función 'log1p' cuando se hace clic.
btncos = Button(calc, text="log1p", width=6, height=2, bg='black', fg='white', 
                font=('Helvetica', 20, 'bold'), bd=4, command=lambda: added_value.log1p()
                ).grid(row=4, column=5, pady=1)

# Crea un botón "expm1" que llama a la función 'expm1' cuando se hace clic.
btnexpm1 = Button(calc, text="expm1", width=6, height=2, bg='black', fg='white', 
                font=('Helvetica', 20, 'bold'), bd=4, command=lambda: added_value.expm1()
                ).grid(row=4, column=6, pady=1)

# Crea un botón "//" (cociente) que llama a la función 'operation("cociente")' cuando se hace clic.
btnCociente = Button(calc, text="//", width=6, height=2, bg='black', fg='white', 
                font=('Helvetica', 20, 'bold'), bd=4, command=lambda: added_value.operation("cociente")
                ).grid(row=4, column=7, pady=1)

# ROW 5:
# Crea un botón "log2" que llama a la función 'log2' cuando se hace clic.
btnlog2 = Button(calc, text="log2", width=6, height=2, bg='black', fg='white', 
                font=('Helvetica', 20, 'bold'), bd=4, command=lambda: added_value.log2()
                ).grid(row=5, column=4, pady=1)

# Crea un botón "deg" que llama a la función 'degrees' cuando se hace clic.
btndeg = Button(calc, text="deg", width=6, height=2, bg='black', fg='white', 
                font=('Helvetica', 20, 'bold'), bd=4, command=lambda: added_value.degrees()
                ).grid(row=5, column=5, pady=1)

# Crea un botón "acosh" que llama a la función 'acosh' cuando se hace clic.
btnacosh = Button(calc, text="acosh", width=6, height=2, bg='black', fg='white', 
                font=('Helvetica', 20, 'bold'), bd=4, command=lambda: added_value.acosh()
                ).grid(row=5, column=6, pady=1)

# Crea un botón "asinh" que llama a la función 'asinh' cuando se hace clic.
btnasinh = Button(calc, text="asinh", width=6, height=2, bg='black', fg='white', 
                font=('Helvetica', 20, 'bold'), bd=4, command=lambda: added_value.asinh()
                ).grid(row=5, column=7, pady=1)

# Crea una etiqueta "Scientific Calculator" en la parte superior de la calculadora.
lblDisplay = Label(calc, text="Scientific Calculator", font=('Helvetica', 30, 'bold'),
                bg='black', fg='white', justify=CENTER)
lblDisplay.grid(row=0, column=4, columnspan=4)

  
def iExit():
    """
    Función para gestionar la salida de la aplicación.
    Muestra un cuadro de diálogo de confirmación antes de salir.

    Returns:
        None
    """
    iExit = tkinter.messagebox.askyesno("Scientific Calculator", "Do you want to exit ?")
    if iExit > 0:
        root.destroy()  # Cierra la ventana principal de la aplicación.
        return

def Scientific():
    """
    Función para cambiar a la calculadora científica.
    Ajusta la ventana a un tamaño y posición específicos y la hace no redimensionable.

    Returns:
        None
    """
    root.resizable(width=False, height=False)  # Hace que la ventana no sea redimensionable.
    root.geometry("944x568+0+0")  # Establece el tamaño y la posición de la ventana.

def Standard():
    """
    Función para cambiar a la calculadora estándar.
    Ajusta la ventana a un tamaño y posición específicos y la hace no redimensionable.

    Returns:
        None
    """
    root.resizable(width=False, height=False)  # Hace que la ventana no sea redimensionable.
    root.geometry("480x568+0+0")  # Establece el tamaño y la posición de la ventana.

  
menubar = Menu(calc)
  
menubar = Menu(calc)
  
# Menú de la Barra 1:
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label="Standard", command=Standard)
filemenu.add_command(label="Scientific", command=Scientific)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=iExit)

# Menú de la Barra 2:
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_separator()
editmenu.add_command(label="Paste")

root.config(menu=menubar)

# Inicia el bucle principal de la interfaz de usuario.
root.mainloop()
