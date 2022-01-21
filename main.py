from tkinter import *

ventana = Tk() # Crea una ventana
ventana.title("Calculator") # Titulo de la ventana
ventana.resizable(0,0) # No se puede cambiar el tamaño de la ventana

i = 0

#Functions

def click_btn(value):
    global i
    e_text.insert(i,value)
    i += 1

def delete():
    global i
    e_text.delete(0,END)
    i = 0

def result():
    global i
    problem = e_text.get()
    result = eval(problem)
    if result < 0:
        e_text.insert(i,"-")
        i += 1
    e_text.delete(0,END)
    e_text.insert(0,result)
    i = 0
#Entrada

e_text = Entry(ventana, bg="white", fg="black", font=("Arial", 20))
e_text.grid(row=0, column=0, columnspan= 4, padx=5, pady=5)

#Crea botones

btn1 = Button(ventana, text="1", width=5, height=2, command=lambda: click_btn(1))
btn2 = Button(ventana, text="2", width=5, height=2, command=lambda: click_btn(2))
btn3 = Button(ventana, text="3", width=5, height=2, command=lambda: click_btn(3))
btn4 = Button(ventana, text="4", width=5, height=2, command=lambda: click_btn(4))
btn5 = Button(ventana, text="5", width=5, height=2, command=lambda: click_btn(5))
btn6 = Button(ventana, text="6", width=5, height=2, command=lambda: click_btn(6))
btn7 = Button(ventana, text="7", width=5, height=2, command=lambda: click_btn(7))
btn8 = Button(ventana, text="8", width=5, height=2, command=lambda: click_btn(8))
btn9 = Button(ventana, text="9", width=5, height=2, command=lambda: click_btn(9))
btn0 = Button(ventana, text="0", width=10, height=2, command=lambda: click_btn(0))

btn_del = Button(ventana, text="AC", width=5, height=2 , command=lambda: delete())
btn_parenthesis1 = Button(ventana, text="(", width=5, height=2, command=lambda: click_btn("("))
btn_parenthesis2 = Button(ventana, text=")", width=5, height=2, command=lambda: click_btn(")"))
btn_point = Button(ventana, text=".", width=5, height=2, command=lambda: click_btn("."))

btn_div = Button(ventana, text="/", width=5, height=2, command=lambda: click_btn("/"))
btn_mult = Button(ventana, text="x", width=5, height=2, command=lambda: click_btn("*"))
btn_plus = Button(ventana, text="+", width=5, height=2, command=lambda: click_btn("+"))
btn_rest = Button(ventana, text="-", width=5, height=2, command=lambda: click_btn("-"))
btn_equal = Button(ventana, text="=", width=10, height=2, command=lambda: result())

#Posicionamiento de los botones
btn_del.grid(row=1, column=0, padx=5, pady=5)
btn_parenthesis1.grid(row=1, column=1, padx=5, pady=5)
btn_parenthesis2.grid(row=1, column=2, padx=5, pady=5)
btn_div.grid(row=1, column=3, padx=5, pady=5)

btn7.grid(row=2, column=0, padx=5, pady=5)
btn8.grid(row=2, column=1, padx=5, pady=5)
btn9.grid(row=2, column=2, padx=5, pady=5)
btn_mult.grid(row=2, column=3, padx=5, pady=5)

btn6.grid(row=3, column=0, padx=5, pady=5)
btn5.grid(row=3, column=1, padx=5, pady=5)
btn4.grid(row=3, column=2, padx=5, pady=5)
btn_rest.grid(row=3, column=3, padx=5, pady=5)

btn3.grid(row=4, column=0, padx=5, pady=5)
btn2.grid(row=4, column=1, padx=5, pady=5)
btn1.grid(row=4, column=2, padx=5, pady=5)
btn_plus.grid(row=4, column=3, padx=5, pady=5)

btn0.grid(row=5, column=1, padx=5, pady=5)
btn_point.grid(row=5, column=0, padx=5, pady=5)
btn_equal.grid(row=5, column=2, padx=5, pady=5)


ventana.mainloop() # Muestra la ventana 