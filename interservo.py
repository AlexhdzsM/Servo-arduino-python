import serial
from tkinter import*
import time
#--------------------------------------------------------------------------------

try:
    arduino=serial.Serial('COM4',9600)
except:
    print('No se puede conectar con el puerto')

#--Funciones----------------------------------------------------------------------
def ask_quit():
    root.destroy()
    arduino.close()

def pos():
    posicion = var.get()
    angulo= str(posicion)
    arduino.write((angulo+'\n').encode())
    
#--Creacion de la interfaz----------------------------------------------------------
root=Tk()

root.protocol("WM_DELETE_WINDOW", ask_quit)#protocolo para cerrar con x

root.title("Control de servo")
root.config(bg="black")
milabel=Label(root, text="Controlar posicion de servomotor", bg="black", fg="white", font=("Comic Sans MS",14))
milabel.place(x=5,y=5)
var = DoubleVar()
posservo = Scale(root, orient='horizontal', from_=0, to=180, variable = var)
posservo.place(x=100, y=50)

boton=Button(root, text="accionar motor", command=pos )
boton.place(x=110, y=100)

milabel2=Label(root, text="Mariano Hernández", bg="black", fg="white", font=("Comic Sans MS",10))
milabel2.place(x=2,y=150)

root.minsize(300,200)

root.mainloop()