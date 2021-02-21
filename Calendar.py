import tkinter as tk
import random


#Create vector with the months
months = ['Enero','Febrero','Marzo',
          'Abril','Mayo','Junio','Julio']

color=['aquamarine','moccasin','hotpink','lightgreen','coral']

#Create screen and configure
screen = tk.Tk()
screen.title("Calendar").pack()
screen.configure(background='sky blue')
screen.geometry('500x500')

#Configure the frame
frame = tk.Frame(screen)
frame.grid(row=0, column=0)

#Bucle to print the labels with the months
for y, t in enumerate(months):
    for x,row in enumerate(row.split(' ')):
            text = tk.Label(screen, text=t,height=5,width=12,borderwidth = 1,relief="groove")
            text.grid(row=x, column=y)
            text.bind("<Button-1>", callback)
            text.configure(bg=color[random.randrange(3)],font=("calibri",12,'bold'))

#return the month you choose
def callback(event):
    lab = event.widget
    text = lab["text"]
    print(text)

screen.mainloop()