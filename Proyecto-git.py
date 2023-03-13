from tkinter import *

raiz=Tk()

raiz.title(" 'GOLD GYM'  -  DATABASE.")
raiz.geometry("350x350")

ventana=Frame(raiz, width=400,height=400)
raiz.resizable(True,True)
ventana.pack()

miNombre=StringVar()
miDomicilio=StringVar()
miEdad=StringVar()
miPais=StringVar()
losdatos=StringVar()
losdatos2=StringVar()
losdatos3=StringVar()
losdatos4=StringVar()

raya1=StringVar()
raya2=StringVar()
#------------------------------crear cuadro de entrada de datos------------------------------

cuadroNombre=Entry(ventana,textvariable=miNombre)
cuadroNombre.grid(row=0,column=1,padx=10, pady=10)
cuadroNombre.config(fg="black",justify="center")

cuadroDomicilio=Entry(ventana,textvariable=miDomicilio)
cuadroDomicilio.grid(row=1,column=1,padx=10, pady=10)
cuadroDomicilio.config(fg="black",justify="center")

cuadroEdad=Entry(ventana,textvariable=miEdad)
cuadroEdad.grid(row=2,column=1,padx=10, pady=10)
cuadroEdad.config(fg="black",justify="center",)

cuadroPais=Entry(ventana,textvariable=miPais)
cuadroPais.grid(row=3,column=1,padx=10, pady=10)
cuadroPais.config(fg="black",justify="center")

#DEFINO LO QUE VA A CONTENER CADA ENTRY, ES DECIR ESPECIFíCO QUE DATO VA A INGRESAR.

nombreLabel=Label(ventana,text="NAME: ")
nombreLabel.grid(row=0,column=0, sticky="e",padx=10,pady=10)

domicilioLabel=Label(ventana,text="ADRESS: ")
domicilioLabel.grid(row=1,column=0, sticky="e",padx=10,pady=10)

edadLabel=Label(ventana,text="AGE: ")
edadLabel.grid(row=2,column=0, sticky="e",padx=10,pady=10)

paisLabel=Label(ventana,text="COUNTRY: ")
paisLabel.grid(row=3,column=0, sticky="e",padx=10,pady=10)

#Label de los datos cuando se imprimen, Se llaman con la funcion al apretar el boton

comentLabel=Label(ventana,fg="Green",textvariable=losdatos)
comentLabel.grid(row=5,column=0, sticky="e",padx=5,pady=5)

comentLabel2=Label(ventana,fg="Green",textvariable=losdatos2)
comentLabel2.grid(row=6,column=0, sticky="e",padx=0,pady=0)

comentLabel3=Label(ventana,fg="Green",textvariable=losdatos3)
comentLabel3.grid(row=7,column=0, sticky="e",padx=0,pady=0)

comentLabel4=Label(ventana,fg="Green",textvariable=losdatos4)
comentLabel4.grid(row=8,column=0, sticky="e",padx=0,pady=0)

def generartarjeta():

	comentLabel5 = Label(ventana, text="-----------------------------")
	comentLabel5.grid(row=4, column=0, sticky="e", padx=0, pady=0)
	comentLabel5 = Label(ventana, text="-----------------------------")
	comentLabel5.grid(row=9, column=0, sticky="e", padx=0, pady=0)
	losdatos.set(miNombre.get())
	losdatos2.set(miDomicilio.get())
	losdatos3.set(miEdad.get() + "  Años")
	losdatos4.set(miPais.get())

def enviardatos():
	archivo=open("Socios.txt" ,"a")
	archivo.write("\n" + "Name: " + miNombre.get() +"\n")
	archivo.write("Adress: " + miDomicilio.get() + "\n")
	archivo.write("Age: " + miEdad.get() + "\n")
	archivo.write("Country: " + miPais.get() + "\n")
	archivo.write("---------------------------")
	archivo.close()
	#Elimino los datos de los entry
	cuadroNombre.delete(0, END), cuadroDomicilio.delete(0,END), cuadroEdad.delete(0,END), cuadroPais.delete(0,END)
	#limpio los label de la tarjeta generada
	losdatos.set(""), losdatos2.set(""), losdatos3.set(""), losdatos4.set("")

	comentLabel5 = Label(ventana, text="                                                ")
	comentLabel5.grid(row=4, column=0, sticky="e", padx=0, pady=0)
	comentLabel5 = Label(ventana, text="                                                ")
	comentLabel5.grid(row=9, column=0, sticky="e", padx=0, pady=0)

#Configuración del botón "Generar Tarjeta" .- Generate Card- Button Configuration.

botonGenerateCard=Button(raiz,text="Generate Card", bg="CadetBlue1",fg="black",font=("Arial",11),command=generartarjeta)
botonGenerateCard.pack()

botonSendData=Button(raiz,text="Send Data",bg="red2",fg="Black" ,font=("Arial", 11),command=enviardatos)
botonSendData.pack()

raiz.mainloop()