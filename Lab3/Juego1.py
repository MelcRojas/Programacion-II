import random
import tkinter as tk
from tkinter import messagebox

# Clase base Juego
class Juego:
    def __init__(self, numero_de_vidas):
        self.numero_de_vidas = numero_de_vidas  # Numero de vidas inicial
        self.record = 0  # Maximo de vidas restantes alcanzado
        self.vidas_restantes = numero_de_vidas  # Vidas restantes actuales

    def reiniciaPartida(self):
        self.vidas_restantes = self.numero_de_vidas  # Reinicia las vidas

    def actualizaRecord(self):
        if self.vidas_restantes > self.record:
            self.record = self.vidas_restantes  # Actualiza el record si es mayor

    def quitaVida(self):
        self.vidas_restantes -= 1  # Resta una vida
        return self.vidas_restantes > 0  # Devuelve True si quedan vidas

# Clase derivada JuegoAdivinaNumero
class JuegoAdivinaNumero(Juego):
    def __init__(self, numero_de_vidas):
        super().__init__(numero_de_vidas)  # Llama al constructor de la clase padre
        self.numero_a_adivinar = random.randint(0, 10)  # Numero aleatorio a adivinar
        self.root = tk.Tk()  # Ventana principal
        self.root.title("🎮 Adivina el Numero")
        self.root.configure(bg="#FFDAB9")
        self.root.geometry("400x350")

        # Contenedor para los elementos
        frame = tk.Frame(self.root, bg="#FFE4B5", bd=5, relief="ridge")
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Texto principal y subtitulo
        tk.Label(frame, text="😊 Adivina el numero 😊", font=("Arial", 16, "bold"), bg="#FFE4B5").pack(pady=10)
        tk.Label(frame, text="Adivina un numero del 0 al 10", font=("Arial", 14), bg="#FFE4B5").pack(pady=5)

        # Entrada para el intento del jugador
        self.entry = tk.Entry(frame, font=("Arial", 14), justify="center")
        self.entry.pack(pady=5)

        # Boton para confirmar el intento
        self.boton_adivinar = tk.Button(frame, text="Adivinar", font=("Arial", 14, "bold"), bg="#98FB98", command=self.juega)
        self.boton_adivinar.pack(pady=10)

        # Etiqueta para mostrar mensajes
        self.mensaje = tk.Label(frame, text="", font=("Arial", 14, "bold"), bg="#FFE4B5")
        self.mensaje.pack(pady=5)

        # Etiqueta para mostrar vidas restantes
        self.vidas_label = tk.Label(frame, text=f"💖️ Vidas restantes: {self.vidas_restantes}", font=("Arial", 14, "bold"), bg="#FFE4B5")
        self.vidas_label.pack(pady=5)

        # Permite presionar Enter como alternativa al boton
        self.root.bind('<Return>', lambda event: self.juega())

    def juega(self):
        try:
            intento = int(self.entry.get())  # Convierte el texto a numero
        except ValueError:
            messagebox.showerror("❌ Error", "Ingresa un numero valido.")
            return

        if intento < 0 or intento > 10:
            messagebox.showerror("❌ Error", "El numero debe estar entre 0 y 10.")
            self.entry.delete(0, tk.END)
            return

        # Si el jugador acierta
        if intento == self.numero_a_adivinar:
            messagebox.showinfo("😊 Correcto", "Acertaste! 😎")
            self.actualizaRecord()  # Actualiza el record si aplica
            self.reinicia_juego()  # Reinicia para una nueva ronda
        else:
            if self.quitaVida():
                # Da una pista al jugador
                pista = "mayor" if intento < self.numero_a_adivinar else "menor"
                self.mensaje.config(text=f"❌ Fallaste. El numero es {pista}.", fg="orange")
            else:
                # Si ya no hay vidas, muestra el numero correcto
                messagebox.showinfo("😢 Perdiste", f"No te quedan mas vidas. El numero era: {self.numero_a_adivinar}")
                self.reinicia_juego()
                return

        # Limpia el campo y actualiza el contador de vidas
        self.entry.delete(0, tk.END)
        self.vidas_label.config(text=f"💖️ Vidas restantes: {self.vidas_restantes}")

    def reinicia_juego(self):
        self.reiniciaPartida()  # Reinicia las vidas
        self.numero_a_adivinar = random.randint(0, 10)  # Genera nuevo numero
        self.mensaje.config(text="")  # Limpia mensaje
        self.vidas_label.config(text=f"💖️ Vidas restantes: {self.vidas_restantes}")  # Actualiza etiqueta
        self.entry.delete(0, tk.END)  # Limpia entrada

    def ejecutar(self):
        self.root.mainloop()  # Inicia la aplicacion grafica

# Clase Aplicacion
class Aplicacion:
    def __init__(self):
        self.juego = JuegoAdivinaNumero(3)  # Inicia el juego con 3 vidas

    def ejecutar(self):
        self.juego.ejecutar()  # Ejecuta el juego

# Metodo principal
if __name__ == "__main__":
    app = Aplicacion()
    app.ejecutar()
