import tkinter as tk

def press(number):
    global equationText
    equationText = equationText + str(number)
    equationLabel.set(equationText)

def equal():
    global equationText
    total = str(eval(equationText))
    equationLabel.set(total)
    equationText = total

def clear():
    global equationText
    global equationLabel
    equationLabel.set("")
    equationText = ""
    

window = tk.Tk()
window.title("Calculator")

equationText = ""
equationLabel = tk.StringVar()


lbl = tk.Label(window,textvariable=equationLabel, bg='white', width=60, height=4)
lbl.pack()

button1 = tk.Button(window,text='1',width=5, command=lambda : press(1))
button1.pack()

button2 = tk.Button(window,text='2',width=5,command=lambda : press(2))
button2.pack()

button3 = tk.Button(window,text='3',width=5,command=lambda : press(3))
button3.pack()

btnPlus = tk.Button(window, text='+', width=5,command=lambda : press('+'))
btnPlus.pack()

button4 = tk.Button(window,text='4',width=5,command=lambda : press(4))
button4.pack()

button5 = tk.Button(window,text='5',width=5,command=lambda : press(5))
button5.pack()

button6 = tk.Button(window,text='6',width=5,command=lambda : press(6))
button6.pack()

btnMinus = tk.Button(window,text='-',width=5,command=lambda : press('-'))
btnMinus.pack()

button7 = tk.Button(window,text='7',width=5,command=lambda : press(7))
button7.pack()

button8 = tk.Button(window,text='8',width=5,command=lambda : press(8))
button8.pack()

button9 = tk.Button(window,text='9',width=5,command=lambda : press(9))
button9.pack()

btnMultiply = tk.Button(window,text='x',width=5,command=lambda : press('*'))
btnMultiply.pack()

btnDivide = tk.Button(window,text='/',width=5,command=lambda : press('/'))
btnDivide.pack()

btnPeriod = tk.Button(window,text='.', width=5,command=lambda : press('.'))

button0 = tk.Button(window,text='0',width=5,command=lambda : press(0))
button0.pack()

btnEqual = tk.Button(window,text='=',width=5,command=lambda : equal())
btnEqual.pack()

btnClear = tk.Button(window,text='Clear',width=5, command=lambda: clear())
btnClear.pack()

window.mainloop()
