import tkinter as tk
import calendar

lbl=str

def agenda():
    lbl=entry.get()
    print(lbl)

def funcion():
    print("Organiza tu horario")

#Create screen and put title
ventana=tk.Tk()
ventana.title("Schedule UNAL")
#Size screen
ventana.geometry('380x380')
#Canvas Color
ventana.configure(background='red')

#Label days of week
lunes=tk.Label(ventana,text="Lunes",height=5,width=10)
lunes.grid(row=0,column=0)
lunes.config(fg="white",bg="black")

#Button add event
add=tk.Button(ventana,text="Agregar evento",command=agenda)
add.place(x=140,y=310)
add.config(bg="blue")

#Boxtext input
entry = tk.Entry(ventana, justify=tk.RIGHT)
entry.place(x=140 , y=350)
    

ventana.mainloop()