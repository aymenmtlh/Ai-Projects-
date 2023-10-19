from tkinter import * 
from tkinter import ttk
import pyfirmata 
board = pyfirmata.Arduino('COM3')
root = Tk()
root.title('lets play')
root.resizable(900,900) 
red_led= board.get_pin('d:2:o')
green_led2= board.get_pin('d:3:o')
T = Text(root, height = 5, width = 52)
l = Label(root, text = "answer the following question :")
q = Label(root, text = "What is the capital of palastine ")
l.config(font =("Courier", 14))
q.config(font =("Courier", 14))
def display_text():
   global entry
   string= entry.get()
   
   if string== 'Jerusalem': 
        green_led2.write(1)
        label.configure(text='TRUE!')
   else : 
        red_led.write(1)
        label.configure(text='try again  !')
label=Label(root, text="", font=("Courier 22 bold"))
label.pack(pady=10)
entry= Entry(root, width= 40)
entry.focus_set()
entry.pack()
ttk.Button(root, text= "Answer",width= 20, command= display_text).pack(pady=20)
l.pack()
q.pack()
root.mainloop()

