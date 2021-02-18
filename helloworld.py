import tkinter as tk
import calendar

lbl=str
i=0

#fuction to add a new event to the schedule
def agenda(i):
    lbl=entry.get()
    print(lbl,i)
    event=tk.Label(ventana,text=lbl,height=5,width=10)
    event.grid(row=i,column=0)
    event.config(fg="black",bg="sky blue")

#fuction to delete an event
def funcion():
    print("Organiza tu horario")

#Create screen and put title
ventana=tk.Tk()
ventana.title("Schedule UNAL")
#Size screen
ventana.geometry('380x380')
#Canvas Color
ventana.configure(background='blue')

#Label days of week
lunes=tk.Label(ventana,text="Lunes",height=5,width=10)
lunes.grid(row=0,column=0)
lunes.config(fg="white",bg="black")

lunes=tk.Label(ventana,text="Martes",height=5,width=10)
lunes.grid(row=0,column=1)
lunes.config(fg="white",bg="gray9")

#Button add event
i=i+1
add=tk.Button(ventana,text="Agregar evento",command=lambda: agenda(i))
add.place(x=140,y=310)
add.config(bg="purple")

#Boxtext input
entry = tk.Entry(ventana, justify=tk.RIGHT)
entry.place(x=140 , y=350)



ventana.mainloop()