class LineaTeleferico:
    def __init__(self,
                color="",
                tramo="",
                nro_cabinas=0,
                nro_empleados=4,
                empleados = [
                    {"nombre": "Carlos", "paterno": "Gutiérrez", "materno": "Mendoza"},
                    {"nombre": "Laura", "paterno": "Ramírez", "materno": "Flores"},
                    {"nombre": "Miguel", "paterno": "Torres", "materno": "Quispe"},
                    {"nombre": "Andrea", "paterno": "Vargas", "materno": "Salazar"}
                ],  
                edades = [30, 27, 35, 25],
                sueldos = [2800, 2600, 3100, 2500]):
        if nro_empleados < 4:
            raise ValueError("El número mínimo de empleados es 4.")
        if nro_empleados != len(empleados) or nro_empleados != len(edades) or nro_empleados != len(sueldos):
            raise ValueError("El número de empleados, edades y sueldos deben coincidir.")
        self.color = color
        self.tramo = tramo
        self.nro_cabinas = nro_cabinas
        self.nro_empleados = nro_empleados
        self.empleados = empleados
        self.edades = edades
        self.sueldos = sueldos

    def agregar_empleado(self, nombre, paterno, materno, edad, sueldo):
        empleado = {
            "nombre": nombre,
            "paterno": paterno,
            "materno": materno,
        }
        self.empleados.append(empleado)
        self.edades.append(edad)
        self.sueldos.append(sueldo)
        self.nro_empleados += 1
        print(f"Empleado agregado: {nombre} {paterno} {materno} | Edad: {edad} | Sueldo: {sueldo}")

    def eliminar_por_apellido(self, apellido):
        apellido = apellido.strip().lower()
        for i, emp in enumerate(self.empleados):
            if (apellido in emp["paterno"].lower() or
                apellido in emp["materno"].lower()):
                print(f"Eliminando: {emp['nombre']} {emp['paterno']} {emp['materno']}")
                self.empleados.pop(i)
                self.edades.pop(i)
                self.sueldos.pop(i)
                self.nro_empleados -= 1

    def transferir_empleado(self, otro, dato):
        dato = dato.strip().lower()
        for i, emp in enumerate(self.empleados):
            emp_name = f"{emp['nombre']} {emp['paterno']} {emp['materno']}"
            if dato in emp_name.lower():
                otro.agregar_empleado(emp['nombre'], emp['paterno'], emp['materno'], self.edades[i], self.sueldos[i])
                print(f"Empleado transferido: {emp_name} {self.edades[i]} {self.sueldos[i]}")
                self.empleados.pop(i)
                self.edades.pop(i)
                self.sueldos.pop(i)
                self.nro_empleados -= 1
                return
        print(f"Empleado '{dato}' no encontrado en este ministerio.")

    def mostrar_mayores(self, tipo):
        if self.nro_empleados == 0:
            print("No hay empleados en este ministerio.")
            return

        if tipo == "edad":
            max_edad = max(self.edades)
            print(f"Empleados con mayor edad ({max_edad}):")
            for i, edad in enumerate(self.edades):
                if edad == max_edad:
                    print(f"{self.empleados[i]["nombre"]}{self.empleados[i]["paterno"]}{self.empleados[i]["materno"]} - Edad: {edad}")
        elif tipo == "sueldo":
            max_sueldo = max(self.sueldos)
            print(f"Empleados con mayor sueldo ({max_sueldo}):")
            for i, sueldo in enumerate(self.sueldos):
                if sueldo == max_sueldo:
                    print(f"{self.empleados[i]["nombre"]}{self.empleados[i]["paterno"]}{self.empleados[i]["materno"]} - sueldo: {sueldo}")

    def mostrar_info(self):
        print(f"\n== Línea {self.color} ==")
        print(f"Tramo: {self.tramo}")
        print(f"Nro. de cabinas: {self.nro_cabinas}")
        print(f"Nro. de empleados: {self.nro_empleados}")
        for i, emp in enumerate(self.empleados):
            print(f" - {emp['nombre']} {emp['paterno']} {emp['materno']} | Edad: {self.edades[i]} | Sueldo: {self.sueldos[i]}")

empleados = [ {"nombre": "Pedro", "paterno": "Rojas", "materno": "Luna"},
              {"nombre": "Lucy", "paterno": "Sosa", "materno": "Rios"},
              {"nombre": "Ana", "paterno": "Perez", "materno": "Rojas"},
              {"nombre": "Saul", "paterno": "Arce", "materno": "Calle"} ]
edades1 = [35, 43, 26, 29]
sueldos1 = [2500, 3250, 2700, 2500]

linea1 = LineaTeleferico("Rojo", "Estación Central, Estación Cementerio, Estación 16 de Julio", 20, empleados=empleados,edades= edades1,sueldos= sueldos1)
linea2 = LineaTeleferico("Verde", "Tramo B", 15)


# Eliminar empleados con edad 30
linea1.eliminar_por_apellido("Rojas")

# Transferencia de un empleado
entrada = input("Ingresa el nombre o apellido del empleado a transferir: ")
linea1.transferir_empleado(linea2, entrada)

# Mostrar información
linea1.mostrar_info()
linea1.mostrar_mayores("edad")
linea1.mostrar_mayores("sueldo")

linea2.mostrar_info()
linea2.mostrar_mayores("edad")
linea2.mostrar_mayores("sueldo")
