'''Crea una clase Circulo.

Define un atributo llamado radio.

Define los siguientes métodos:

Define un método constructor el cual inicialice el valor del atributo llamado radio.
calcularArea() -> Este método retorna el área del círculo.
calcularPerimetro() -> Este método retorna el perímetro del círculo.
cambiarRadio() -> Este método permite cambiar el radio del círculo.
Fuera de la clase, instancia un objeto de clase Circulo, asignándole un radio inicial.

Muestra por pantalla el área de ese círculo.

Muestra por pantalla el perímetro de ese círculo.'''

import math

class Circulo():
    def __init__(self, radio):
        self.radio = radio

    def calcularArea(self):
        a = round(math.pi * (self.radio ** 2), 2)
        return a

    def calcularPerimetro(self):
        p = round((2 * math.pi) * self.radio, 2)
        return p
    
    def cambioRadio(self, new_radio):
        self.radio = new_radio

    

circulo1 = Circulo(3)


aCirculo1 = circulo1.calcularArea()
print(f"Area Circulo: {aCirculo1}")

pCirculo1 = circulo1.calcularPerimetro()
print(f"Perimetro Circulo: {pCirculo1}")

print("------------------------------------")

circulo1.cambioRadio(7)

new_aCirculo1 = circulo1.calcularArea()
print(f"Nueva Area del Circulo: {new_aCirculo1}")

new_pCirculo1 = circulo1.calcularPerimetro()
print(f"Nuevo Perimetro del Cicurlo: {new_pCirculo1}")







