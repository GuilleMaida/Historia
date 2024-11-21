'''import tkinter as tk

def on_button_click_option1():
    label.config(text ="Opcion 1 seleccionada")

def on_button_click_option2():
    label.config(text ="Opcion 2 seleccionada")


def on_button_click():
    #Aca arriba configuramos la ventana como tal:
    popup = tk.Toplevel()
    poput.title("Ventana de popup")
    poput.geometry("200x150")

    #Etiqueta para hacer aparecer la opcion seleccionada
    label = tK.Label(popup, text="Seleccione una opcion")
    label.pack(pady=10)

    #Opcion 1 boton:
    button_option1 = tK.Button(popup, text="Opcion 1", command=on_buttonclick_option1)
    button_option1.pack(pady=5)

    #Opcion 2 boton:
    button_option2 = tK.Button(popup, text="Opcion 2", command=on_buttonclick_option2)
    button_option2.pack(pady=5)

    #Aca tenemos un boton para cerrar la ventana:
    close_button = tk.Botton(popup, text="Cerrar", command=popup.destroy)
    close_button.pack(10)



#Ventana principal
root = tk.Tk()
root.title("Ventana Popup simple - TP1")

#Crear un botoncito para activar el popup de arriba:
button = tk.Button(root, text="Mostrar popup", command=on_button_click)
button.pack(pady=20)

root.mainloop()

'''
#21/11/2024 


opcion1 = "si"
opcion2 = "no"

print("Hace mucho tiempo, vivía un señor llamado Charles")
print("Charles te pregunta tu nombre")

nombre = input("Ingresa tu nombre")
print("Charles te saluda: 'Mucho gusto'" + nombre)
print("Charles te pregunta si quieres pasar a tomar el té con él")

eleccion1 = input("decide por si o por no")
if (eleccion1 == opcion1):
        print("Charles te sirve una taza de té mientras te cuenta su vida")
        print("Charles te pregunta si te gustó su té")
        eleccion2 = input("decide por si o por no")
        if (eleccion2 == opcion1):
                print("Charles dice que a él también le encanta el Earl Grey, y que bueno coincidir")
        elif(eleccion2 == opcion2):
                print("Charles extrae una escopeta y te dispara. Has muerto")
elif (eleccion1 == opcion2):
        print("Charles extrae una escopeta y te dispara. Has muerto")

        
        




