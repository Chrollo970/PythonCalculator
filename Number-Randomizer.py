

import random
import tkinter as tk

DEFAULTFONT = 12
DEFAULTENTRY = 3

def generate():

    try:
        maxNumber = int(maxEntry.get())
        minNumber = int(minEntry.get())
        randomNumLabel.set(random.randrange(minNumber,maxNumber))

    except ValueError:
        randomNumLabel.set("Invalid Input / Invalid Range")




window = tk.Tk()
window.title('Number Randomizer')
window.geometry('500x500')
icon = tk.PhotoImage(file='logo.png')
window.iconphoto(True, icon)

randomNumLabel = tk.StringVar()


title = tk.Label(window, text='Random Number Generator', font=30)
title.pack()

frame = tk.Frame(window,pady=10)
frame.pack()

maxLabel = tk.Label(frame,text='Enter maximum the number of range:', font=DEFAULTFONT )
maxLabel.grid(row=0,column=0)

maxEntry = tk.Entry(frame, width=DEFAULTENTRY)
maxEntry.grid(row=0,column=1)

minLabel = tk.Label(frame,text='Enter minimum the number of range:', font=DEFAULTFONT )
minLabel.grid(row=1,column=0)

minEntry = tk.Entry(frame,width=DEFAULTENTRY)
minEntry.grid(row=1,column=1)

numberLabel = tk.Label(window, textvariable=randomNumLabel, font=10)
numberLabel.pack()

generateButton = tk.Button(window, text='Generate random Number',command=generate , font=DEFAULTFONT, bg='#34a4eb')
generateButton.pack()

window.bind('<Return>', lambda randomNumLabel : generate())



window.mainloop()

# while True:
#     maxNumber = input(' ')
#     minNumber = input('Enter minimum the number of range: ')

#     if maxNumber.isdigit() and minNumber.isdigit():
#         
#         

#         while True:
#             randomNum = random.randrange(minNumber,maxNumber)
#             print(f'Random number between {minNumber} and {maxNumber}')
#             print('Random number: ',randomNum)
#             choice = input('Generate again(y/n): ')
#             if choice == 'y':
#                 continue
#             elif choice == 'n':
#                 break
#             else:
#                 break

#         exitProgram = input('Do you want to exit the program? y/n ')
#         if exitProgram == 'y':
#             break
#         else:
#             continue
#     else:
#         print('Must be a number!')