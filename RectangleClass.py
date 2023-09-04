'''Crea una clase Rectangulo.

Define los atributos llamados longitud y ancho.

Define los siguientes métodos:

Define un método constructor el cual inicialice los valores de sus atributos.
calcularArea() -> Este método retorna el área del rectángulo.
calcularPerimetro() -> Este método retorna el perímetro del rectángulo.
cambiarLongitud() -> Este método permite cambiar la longitud del rectángulo.
cambiarAncho() -> Este método permite cambiar el ancho del rectángulo.
Fuera de la clase, instancia un objeto de clase Rectangulo, asignándole los valores iniciales.

Muestra por pantalla el área de ese rectángulo.

Muestra por pantalla el perímetro de ese rectángulo.'''

class Rectangle():
    def __init__(self, long, ancho):
        self.long = long
        self.ancho = ancho

    def calcularArea(self):
        a = self.long * self.ancho
        return a

    def calcularPerimetro(self):
        p = (2 * self.long) * (2 * self.ancho)
        return p
    
    def cambiarLongitud(self, newLongitud):
        self.long = newLongitud
    
    def cambiarAncho(self, newAncho):
        self.ancho = newAncho

rectangle = Rectangle(4, 7)

aRectangle = rectangle.calcularArea()
print(f"El area del rectangulo es: {aRectangle}")

pRectangle = rectangle.calcularPerimetro()
print(f"El perimetro del rectangulo es: {pRectangle}")

rectangle.cambiarLongitud(8)
rectangle.cambiarAncho(12)

new_aCirculo = rectangle.calcularArea()
print(f"El nuevo area del rectangulo es: {new_aCirculo}")

new_pCirculo = rectangle.calcularPerimetro()
print(f"El nuevo perimetro del rectangulo es: {new_pCirculo}")






