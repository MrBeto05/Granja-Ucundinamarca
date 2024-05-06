class Produccion:
    def __init__(self, cantidad, unidad):
        self.cantidad = cantidad
        self.unidad = unidad

    def __str__(self):
        return f"{self.cantidad} {self.unidad}"

class Cultivo:
    def __init__(self, nombre, tipo, area, rendimiento):
        self.nombre = nombre
        self.tipo = tipo
        self.area = area
        self.rendimiento = rendimiento

    def calcular_produccion(self):
        produccion = self.rendimiento * self.area
        return Produccion(produccion, "toneladas")

class Animal:
    def __init__(self, especie, raza, edad, peso):
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.peso = peso

    def calcular_produccion(self):
        produccion = self.peso
        return Produccion(produccion, "kg")

class Granja:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cultivos = []
        self.animales = []

    def agregar_cultivo(self):
        try:
            nombre = input("Ingrese el nombre del cultivo: ")
            tipo = input("Ingrese el tipo de cultivo: ")
            area = float(input("Ingrese el área de cultivo: "))
            rendimiento = float(input("Ingrese el rendimiento del cultivo: "))
            cultivo = Cultivo(nombre, tipo, area, rendimiento)
            self.cultivos.append(cultivo)
            print("Cultivo agregado exitosamente.")
        except ValueError:
            print("Error: Ingrese valores numéricos válidos para el área y el rendimiento.")

    def eliminar_cultivo(self):
        nombre = input("Ingrese el nombre del cultivo a eliminar: ")
        encontrado = False
        for cultivo in self.cultivos:
            if cultivo.nombre == nombre:
                self.cultivos.remove(cultivo)
                print("Cultivo eliminado exitosamente.")
                encontrado = True
                break
        if not encontrado:
                print("No se encontró el cultivo ingresado.")

    def agregar_animal(self):
        try:
            especie = input("Ingrese la especie del animal: ")
            raza = input("Ingrese la raza del animal: ")
            edad = int(input("Ingrese la edad del animal: "))
            peso = float(input("Ingrese el peso del animal: "))
            animal = Animal(especie, raza, edad, peso)
            self.animales.append(animal)
            print("Animal agregado exitosamente.")
        except ValueError:
            print("Error: Ingrese valores numéricos válidos para la edad y el peso.")

    def eliminar_animal(self):
        especie = input("Ingrese la especie del animal a eliminar: ")
        encontrado = False
        for animal in self.animales:
            if animal.especie == especie:
                self.animales.remove(animal)
                print("Animal eliminado exitosamente.")
                encontrado = True
                break
        if not encontrado:
            print("No se encontró el animal ingresado.")

    def calcular_produccion_total(self):
        produccion_cultivos = sum(cultivo.calcular_produccion().cantidad for cultivo in self.cultivos)
        produccion_animales = sum(animal.calcular_produccion().cantidad for animal in self.animales)
        produccion_total = produccion_cultivos + produccion_animales
        return Produccion(produccion_total, "toneladas")

    def generar_reporte(self):
        produccion_total = self.calcular_produccion_total()
        print(f"\nProducción total de la Granja {self.nombre}: {produccion_total}")

def menu():
    granja = Granja("Ucundinamarca")
    nom=input(str("Hola, porfavor ingrese su nombre: "))
    while True:
        print(f"\nHola {nom}. Bienvenido a la Granja Ucundinamarca.")
        print("Selecciona una opción:")
        print("1. Agregar cultivo")
        print("2. Eliminar cultivo")
        print("3. Agregar animal")
        print("4. Eliminar animal")
        print("5. Generar reporte de producción")
        print("6. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            granja.agregar_cultivo()
        elif opcion == "2":
            granja.eliminar_cultivo()
        elif opcion == "3":
            granja.agregar_animal()
        elif opcion == "4":
            granja.eliminar_animal()
        elif opcion == "5":
            granja.generar_reporte()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")

menu()