import tkinter as tk
from tkinter import messagebox

# Clases de boletos
class Boleto():
    def __init__(self, numero):
        self.numero = numero
        self.precio = 0.0

    def __str__(self):
        return f"Número: {self.numero}, Precio: {self.precio}"

class Palco(Boleto):
    def __init__(self, numero):
        super().__init__(numero)
        self.precio = 100.0

class Platea(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        self.precio = 50.0 if dias_anticipacion >= 10 else 60.0


class Galeria(Platea):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero, dias_anticipacion)
        self.precio = 25.0 if dias_anticipacion >= 10 else 30.0


# Función para procesar la compra
def vender():
    tipo = tipo_var.get()
    try:
        numero = int(entry_numero.get())
    except ValueError:
        messagebox.showerror("Error", "Número inválido.")
        return

    if tipo == "Palco":
        boleto = Palco(numero)
    else:
        try:
            dias = int(entry_dias.get())
        except ValueError:
            messagebox.showerror("Error", "Días inválidos.")
            return
        if tipo == "Platea":
            boleto = Platea(numero, dias)
        elif tipo == "Galeria":
            boleto = Galeria(numero, dias)
        else:
            messagebox.showerror("Error", "Tipo de boleto no válido.")
            return

    info_var.set(str(boleto))

# ventana
root = tk.Tk()
root.title("Teatro Municipal")

tk.Label(root, text="Teatro Municipal", font=("Arial", 20)).pack(pady=10)

# Frame de datos del boleto
frame_datos = tk.LabelFrame(root, text="Datos del Boleto")
frame_datos.pack(padx=10, pady=10, fill="both")

tipo_var = tk.StringVar(value="Palco")
tk.Radiobutton(frame_datos, text="Palco", variable=tipo_var, value="Palco").grid(row=0, column=0, padx=5, pady=5)
tk.Radiobutton(frame_datos, text="Platea", variable=tipo_var, value="Platea").grid(row=0, column=1, padx=5, pady=5)
tk.Radiobutton(frame_datos, text="Galeria", variable=tipo_var, value="Galeria").grid(row=0, column=2, padx=5, pady=5)

tk.Label(frame_datos, text="Número:").grid(row=1, column=0, sticky="e")
entry_numero = tk.Entry(frame_datos)
entry_numero.insert(0, "1")
entry_numero.grid(row=1, column=1, pady=5)

tk.Label(frame_datos, text="Cant. Días para el Evento:").grid(row=2, column=0, sticky="e")
entry_dias = tk.Entry(frame_datos)
entry_dias.grid(row=2, column=1, pady=5)

tk.Button(frame_datos, text="Vende", command=vender).grid(row=3, column=0, pady=10)
tk.Button(frame_datos, text="Salir", command=root.destroy).grid(row=3, column=1)

# Información
frame_info = tk.LabelFrame(root, text="Información")
frame_info.pack(padx=10, pady=5, fill="both")
info_var = tk.StringVar()
tk.Label(frame_info, textvariable=info_var, font=("Arial", 12, "bold"), fg="blue").pack()

root.mainloop()
