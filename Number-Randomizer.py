# import tkinter as tk


# window = tk.Tk()
# window.title('Number Randomizer')
# window.geometry('400x400')

# icon = tk.PhotoImage(file='logo.png')
# window.iconphoto(True, icon)




# window.mainloop()
import random



print('Random Number Generator')
while True:
    maxNumber = input('Enter maximum the number of range: ')
    minNumber = input('Enter minimum the number of range: ')

    if maxNumber.isdigit() and minNumber.isdigit():
        maxNumber = int(maxNumber)
        minNumber = int(minNumber)

        while True:
            randomNum = random.randrange(minNumber,maxNumber)
            print(f'Random number between {minNumber} and {maxNumber}')
            print('Random number: ',randomNum)
            choice = input('Generate again(y/n): ')
            if choice == 'y':
                continue
            elif choice == 'n':
                break
            else:
                break

        exitProgram = input('Do you want to exit the program? y/n ')
        if exitProgram == 'y':
            break
        else:
            continue
    else:
        print('Must be a number!')