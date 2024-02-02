import random
import tkinter as tk
from tkinter import messagebox
import pickle

class JuegoAdivinanzaGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Juego de Adivinanzas")

        self.label_instrucciones = tk.Label(self.root, text="Elige el rango de números:")
        self.label_instrucciones.pack(pady=10)

        self.scale_rango = tk.Scale(self.root, from_=1, to=100, orient=tk.HORIZONTAL, length=200, resolution=1)
        self.scale_rango.set(50)
        self.scale_rango.pack(pady=10)

        self.label_rango = tk.Label(self.root, text="Rango: 1 - 100")
        self.label_rango.pack(pady=10)

        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=10)

        self.button_adivinar = tk.Button(self.root, text="Adivinar", command=self.verificar_adivinanza)
        self.button_adivinar.pack(pady=10)

        self.label_intentos = tk.Label(self.root, text="Intentos: 0")
        self.label_intentos.pack(pady=10)

        self.menu = tk.Menu(self.root)
        self.menu.add_command(label="Reiniciar Juego", command=self.reiniciar_juego)
        self.menu.add_command(label="Cambiar Dificultad", command=self.cambiar_dificultad)
        self.menu.add_command(label="Salir", command=self.salir)
        self.root.config(menu=self.menu)

        self.cargar_estado()

    def verificar_adivinanza(self):
        rango = int(self.scale_rango.get())

        if not hasattr(self, 'numero_secreto'):  # Si el número secreto aún no ha sido generado
            self.numero_secreto = random.randint(1, rango)

        intento = int(self.entry.get())
        self.intentos += 1

        if intento == self.numero_secreto:
            messagebox.showinfo("¡Correcto! :)", f"¡Has adivinado el numero en {self.intentos} intentos!")
            self.reiniciar_juego()
        elif intento < self.numero_secreto:
            messagebox.showinfo("Incorrecto :(", "El numero es mayor. ¡Intentalo de nuevo! :( ")
        else:
            messagebox.showinfo("Incorrecto :(", "El numero es menor. ¡Intentalo de nuevo! :(")

        self.label_intentos.config(text=f"Intentos: {self.intentos}")
        self.label_rango.config(text=f"Rango: 1 - {rango}")
        self.guardar_estado()

    def reiniciar_juego(self):
        self.intentos = 0
        self.label_intentos.config(text="Intentos: 0")
        self.scale_rango.set(self.rango_guardado)  # Restaurar el rango anterior
        self.label_rango.config(text=f"Rango: 1 - {self.rango_guardado}")

        # Generar un nuevo número secreto
        rango = int(self.scale_rango.get())
        self.numero_secreto = random.randint(1, rango)

    def cambiar_dificultad(self):
        messagebox.showinfo("Cambiar Dificultad", "Puedes ajustar la dificultad cambiando el rango de numeros.")

    def salir(self):
        self.root.destroy()

    def guardar_estado(self):
        estado = {"intentos": self.intentos, "rango": int(self.scale_rango.get())}
        with open("estado_juego.pkl", "wb") as archivo:
            pickle.dump(estado, archivo)

    def cargar_estado(self):
        try:
            with open("estado_juego.pkl", "rb") as archivo:
                estado = pickle.load(archivo)
                self.intentos = estado.get("intentos", 0)
                self.rango_guardado = estado.get("rango", 50)  # Valor predeterminado si 'rango' no está presente
                self.scale_rango.set(self.rango_guardado)
                self.label_rango.config(text=f"Rango: 1 - {self.rango_guardado}")
        except FileNotFoundError:
            # Si el archivo no existe, establecer valores predeterminados
            self.intentos = 0
            self.rango_guardado = 50  # Puedes ajustar el valor predeterminado según tus necesidades
            self.scale_rango.set(self.rango_guardado)
            self.label_rango.config(text=f"Rango: 1 - {self.rango_guardado}")

if __name__ == "__main__":
    juego_gui = JuegoAdivinanzaGUI()
    juego_gui.root.mainloop()
