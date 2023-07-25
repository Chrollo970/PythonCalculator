import tkinter as tk

def press(number):
    global equationText
    equationText = equationText + str(number)
    equationLabel.set(equationText)

def equal():

    try:
        global equationText
        total = str(eval(equationText))
        equationLabel.set(total)
        equationText = total

    except SyntaxError:
        equationLabel.set("Syntax Error")
        equationText = ""

    except ZeroDivisionError:
        equationLabel.set("Division Error")
        equationText = ""


def clear():
    global equationText
    global equationLabel
    equationLabel.set("")
    equationText = ""
    

window = tk.Tk()
window.title("Python Calculator")
window.geometry('270x212')
window.resizable(False,False)

windowIcon = tk.PhotoImage(file='logo.png')
window.iconphoto(True,windowIcon)

equationText = ""
equationLabel = tk.StringVar()

BUTTONSIZE = 8

lbl = tk.Label(window,textvariable=equationLabel, bg='white', width=30, height=4,font=('consolas',12))
lbl.pack()
frame = tk.Frame(window)
frame.pack()

button1 = tk.Button(frame,text='1',width=BUTTONSIZE, command=lambda : press(1))
button1.grid(row=1,column=0)

button2 = tk.Button(frame,text='2',width=BUTTONSIZE,command=lambda : press(2))
button2.grid(row=1,column=1)

button3 = tk.Button(frame,text='3',width=BUTTONSIZE,command=lambda : press(3))
button3.grid(row=1,column=2)

btnPlus = tk.Button(frame, text='+', width=BUTTONSIZE,command=lambda : press('+'))
btnPlus.grid(row=1,column=3)

button4 = tk.Button(frame,text='4',width=BUTTONSIZE,command=lambda : press(4))
button4.grid(row=2,column=0)

button5 = tk.Button(frame,text='5',width=BUTTONSIZE,command=lambda : press(5))
button5.grid(row=2,column=1)

button6 = tk.Button(frame,text='6',width=BUTTONSIZE,command=lambda : press(6))
button6.grid(row=2,column=2)

btnMinus = tk.Button(frame,text='-',width=BUTTONSIZE,command=lambda : press('-'))
btnMinus.grid(row=2,column=3)

button7 = tk.Button(frame,text='7',width=BUTTONSIZE,command=lambda : press(7))
button7.grid(row=3,column=0)

button8 = tk.Button(frame,text='8',width=BUTTONSIZE,command=lambda : press(8))
button8.grid(row=3,column=1)

button9 = tk.Button(frame,text='9',width=BUTTONSIZE,command=lambda : press(9))
button9.grid(row=3,column=2)

btnMultiply = tk.Button(frame,text='x',width=BUTTONSIZE,command=lambda : press('*'))
btnMultiply.grid(row=3,column=3)

btnDivide = tk.Button(frame,text='/',width=BUTTONSIZE,command=lambda : press('/'))
btnDivide.grid(row=4,column=0)

btnPeriod = tk.Button(frame,text='.', width=BUTTONSIZE,command=lambda : press('.'))
btnPeriod.grid(row=4,column=1)

button0 = tk.Button(frame,text='0',width=BUTTONSIZE,command=lambda : press(0))
button0.grid(row=4,column=2)

btnEqual = tk.Button(frame,text='=',width=BUTTONSIZE,command=lambda : equal())
btnEqual.grid(row=4,column=3)

btnClear = tk.Button(window,text='Clear',width=32, command=lambda: clear())
btnClear.pack()

window.mainloop()
