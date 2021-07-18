from tkinter import * 
import tkinter.font as font

window = Tk()


# logo_img = PhotoImage(file='C:/Users/User/Desktop/hangman/1.gif')
# logo = Label(window, width=5000, height=5000,image=logo_img, bg="cyan", compound=CENTER)#, side=RIGHT)#
# logo.image=logo_img
# logo.pack()


game1 = Label(window, text="Hangman",bg="#DDA0DD", width=20,height=5)
b1=Button(window, text="Play", bg='light green', width=20,height=3)
b2=Button(window, text="Instruction", bg='orange', width=20,height=3)
#l1 = Label(window, textvariable=var1, relief=RAISED)
#l2 = Label(window, textvariable=var2, relief=RAISED)#,width=5,height=1) #fg="black", bg="white")
# game1.grid(row=3, column=2)
# b1.grid(row=3, column=3)
# b2.grid(row=3, column=4)

# game1.place(x=300, y=10)
# b1.place(x=500 ,y=400)
# b2.place(x=500, y=500)

myFont = font.Font(size=30, family='Helvetica')
btnFont = font.Font(size=15, family='Helvetica')
# myFont = font.Font()
b1['font'] = btnFont
b2['font'] = btnFont
game1['font'] = myFont

game1.pack(expand=True)
b1.pack(expand=True)
b2.pack(expand=True)

w = 500
h = 500
x = 250
y = 100
# use width x height + x_offset + y_offset (no spaces!)
# window.geometry("%dx%d+%d+%d" % (w, h, x, y))
window.geometry('1500x1500')

window.configure(bg="brown")
window.mainloop()