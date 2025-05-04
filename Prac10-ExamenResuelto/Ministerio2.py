class Ministerio:
    def __init__(
        self, nombre="",
        direccion="",
        nro_empleados=4,
        empleados=["Empleado 1", "Empleado 2", "Empleado 3", "Empleado 4"],
        edades=[26, 29, 18, 22],
        sueldos=[2700, 2500, 3000, 3200]
    ):
        if nro_empleados < 4:
            raise ValueError("El número de empleados debe ser al menos 4.")
        if nro_empleados != len(empleados) or nro_empleados != len(edades) or nro_empleados != len(sueldos):
            raise ValueError("El número de empleados, edades y sueldos deben coincidir.")
        self.nombre = nombre
        self.direccion = direccion
        self.nro_empleados = nro_empleados
        self.empleados = empleados
        self.edades = edades
        self.sueldos = sueldos

    def agregar_empleado(self, empleado, edad, sueldo):
        self.empleados.append(empleado)
        self.edades.append(edad)
        self.sueldos.append(sueldo)
        self.nro_empleados += 1

    def eliminar_por_edad(self, edad_objetivo):
        # Eliminar desde el final para evitar errores de índice
        for i in range(len(self.edades) - 1, -1, -1):
            if self.edades[i] == edad_objetivo:
                print(f"Eliminando: {self.empleados[i]} (Edad: {self.edades[i]})")
                self.empleados.pop(i)
                self.edades.pop(i)
                self.sueldos.pop(i)
                self.nro_empleados -= 1

    def transferir_empleado(self, otro, dato):
        dato = dato.strip().lower()
        for i, emp in enumerate(self.empleados):
            if dato in emp.lower():
                otro.agregar_empleado(emp, self.edades[i], self.sueldos[i])
                print(f"Empleado transferido: {emp} {self.edades[i]} {self.sueldos[i]}")
                self.empleados.pop(i)
                self.edades.pop(i)
                self.sueldos.pop(i)
                self.nro_empleados -= 1
                return
        print(f"Empleado '{dato}' no encontrado en este ministerio.")

    def mostrar_menores(self, tipo):
        if self.nro_empleados == 0:
            print("No hay empleados en este ministerio.")
            return

        if tipo == "edad":
            min_edad = min(self.edades)
            print(f"Empleados con menor edad ({min_edad}):")
            for i, edad in enumerate(self.edades):
                if edad == min_edad:
                    print(f"{self.empleados[i]} - Edad: {edad}")
        elif tipo == "sueldo":
            min_sueldo = min(self.sueldos)
            print(f"Empleados con menor sueldo ({min_sueldo}):")
            for i, sueldo in enumerate(self.sueldos):
                if sueldo == min_sueldo:
                    print(f"{self.empleados[i]} - Sueldo: {sueldo}")


# a) Instanciar 2 ministerios
empleados1 = [ "Pedro Rojas Luna", "Lucy Sosa Rios", "Ana Perez Rojas", "Saul Arce Calle"]
edades1 = [35, 43, 26, 29]
sueldos1 = [2500, 3250, 2700, 2500]
ministerio1 = Ministerio("Ministerio de Salud", "Av. Arce #123", 4, empleados1, edades1, sueldos1)
ministerio2 = Ministerio("Ministerio de Educación", "Calle Ayacucho #456")

# b) Eliminar empleados con edad 26
ministerio1.eliminar_por_edad(26)

# c) Transferir un empleado desde ministerio1 hacia ministerio2
nombre_input = input("Ingresa el nombre o apellido del empleado a transferir: ")
ministerio1.transferir_empleado(ministerio2, nombre_input)

# d) Mostrar empleados con menor edad y menor sueldo en ambos ministerios
print("\n-- Ministerio 1 --")
ministerio1.mostrar_menores("edad")
ministerio1.mostrar_menores("sueldo")

print("\n-- Ministerio 2 --")
ministerio2.mostrar_menores("edad")
ministerio2.mostrar_menores("sueldo")
