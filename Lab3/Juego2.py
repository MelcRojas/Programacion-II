import random
import tkinter as tk
from tkinter import messagebox

# Clase base Juego
class Juego:
    def __init__(self, master, titulo, color_fondo, vidas=3, filtro=None, siguiente_juego=None):
        self.master = master  # Ventana principal
        self.master.title(titulo)  # Titulo de la ventana
        self.master.configure(bg=color_fondo)  # Color de fondo
        self.vidas = vidas  # Numero de vidas
        self.filtro = filtro  # Filtro para validar si es par o impar
        self.numero_secreto = self.generar_numero()  # Numero aleatorio a adivinar
        self.siguiente_juego = siguiente_juego  # Referencia al siguiente juego

        # Crear un marco contenedor con diseño
        self.frame = tk.Frame(master, bg=color_fondo, padx=20, pady=20, relief="ridge", bd=5)
        self.frame.pack(padx=20, pady=20)

        # Titulo del juego
        tk.Label(self.frame, text="😊 " + titulo + " 😊", font=("Arial", 14, "bold"), bg=color_fondo).pack(pady=5)
        
    # Metodo para generar el numero aleatorio
    def generar_numero(self):
        numeros = range(0, 11)
        if self.filtro:
            numeros = filter(self.filtro, numeros)
        return random.choice(list(numeros))

    # Metodo validaNumero: devuelve true si el numero esta entre 0 y 10
    def valida_numero(self, numero):
        return 0 <= numero <= 10

    # Metodo para jugar
    def juega(self, event=None):
        pass

    def cerrar_y_abrir_siguiente(self):
        self.master.destroy()
        if self.siguiente_juego:
            self.siguiente_juego()

# Clase JuegoAdivinaNumero
class JuegoAdivinaNumero(Juego):
    def __init__(self, master, titulo, color_fondo, vidas=3, filtro=None, siguiente_juego=None):
        super().__init__(master, titulo, color_fondo, vidas, filtro, siguiente_juego)

        # Entrada de texto para ingresar el numero
        self.entry = tk.Entry(self.frame, font=("Arial", 14))
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", self.juega)  # Permite usar Enter para jugar

        # Boton para adivinar
        self.button = tk.Button(
            self.frame,
            text="Adivinar",
            command=self.juega,
            font=("Arial", 12, "bold"),
            bg="#90ee90",
            activebackground="#77dd77",
            relief="raised"
        )
        self.button.pack(pady=10)

        # Etiqueta para mostrar mensajes de resultado
        self.label_mensaje = tk.Label(self.frame, text="", font=("Arial", 12, "bold"), fg="orange", bg=color_fondo)
        self.label_mensaje.pack(pady=5)

        # Etiqueta para mostrar las vidas restantes
        self.label_vidas = tk.Label(self.frame, text=f"💖 Vidas restantes: {self.vidas}", font=("Arial", 12, "bold"), bg=color_fondo)
        self.label_vidas.pack(pady=5)

    def juega(self, event=None):
        try:
            numero = int(self.entry.get())
            self.entry.delete(0, tk.END)

            if not self.valida_numero(numero):
                messagebox.showerror("Error", "Numero fuera de rango. Debe estar entre 0 y 10.")
                return

            if numero == self.numero_secreto:
                messagebox.showinfo("Ganaste", f"¡Adivinaste el numero!\nTe quedaban {self.vidas} vidas.")
                self.cerrar_y_abrir_siguiente()
            else:
                self.vidas -= 1
                if self.vidas > 0:
                    self.label_mensaje.config(text=f"❌ Fallaste. Te quedan {self.vidas} vidas.")
                    self.label_vidas.config(text=f"💖 Vidas restantes: {self.vidas}")
                else:
                    messagebox.showinfo("Perdiste", f"Perdiste. El numero era {self.numero_secreto}.")
                    self.cerrar_y_abrir_siguiente()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un numero valido.")

# Clase JuegoAdivinaPar
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def __init__(self, master, vidas=3, siguiente_juego=None):
        super().__init__(master, "Adivina el Numero PAR", color_fondo="#B3E5FC", vidas=vidas, filtro=lambda x: x % 2 == 0, siguiente_juego=siguiente_juego)

    def valida_numero(self, numero):
        if not (0 <= numero <= 10):
            messagebox.showerror("Error", "Numero fuera de rango. Debe estar entre 0 y 10.")
            return False
        if numero % 2 != 0:
            messagebox.showerror("Error", "El numero debe ser par.")
            return False
        return True

# Clase JuegoAdivinaImpar
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def __init__(self, master, vidas=3, siguiente_juego=None):
        super().__init__(master, "Adivina el Numero IMPAR", color_fondo="#C8E6C9", vidas=vidas, filtro=lambda x: x % 2 != 0, siguiente_juego=siguiente_juego)

    def valida_numero(self, numero):
        if not (0 <= numero <= 10):
            messagebox.showerror("Error", "Numero fuera de rango. Debe estar entre 0 y 10.")
            return False
        if numero % 2 == 0:
            messagebox.showerror("Error", "El numero debe ser impar.")
            return False
        return True

# Clase Aplicacion
def iniciar_juegos():
    root1 = tk.Tk()
    root1.withdraw()

    def abrir_juego_par():
        root2 = tk.Toplevel()
        JuegoAdivinaPar(root2, vidas=3, siguiente_juego=abrir_juego_impar)
        root2.mainloop()

    def abrir_juego_impar():
        root3 = tk.Toplevel()
        JuegoAdivinaImpar(root3, vidas=3)
        root3.mainloop()

    root1 = tk.Toplevel()
    JuegoAdivinaNumero(root1, "Adivina el Numero", color_fondo="#FAD7A0", vidas=3, siguiente_juego=abrir_juego_par)
    root1.mainloop()

# Inicio del programa
if __name__ == "__main__":
    iniciar_juegos()
