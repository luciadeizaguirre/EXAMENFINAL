import pickle
import math
class Figura:
    def __init__(self,color,area):
        self.color=color
        self.area=area
    def __str__(self):
        return f"{self.color} {self.area}"
#Sobreescribimos los operadores necesario para definir la clase base

    def __eq__(self, __o: object) -> bool:
        return self.area == __o.area
    def __gt__(self, __o:object) -> bool:
        return self.area > __o.area
    def __lt__(self, __o: object) -> bool:
        return self.area < __o.area
        
class Triangulo(Figura):
    def __init__(self, color, base, altura) -> None:
        super().__init__(color, base*altura*0.5)
        self.base=base
        self.altura=altura
class Cuadrado(Figura):
    def __init__(self, color, lado) -> None:
        super().__init__(color, lado*lado)
        self.lado=lado
class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color, pi*radio*radio)
        self.radio=radio
lista_figuras=[]
lista_figuras.append(Triangulo("rojo", 2.0,1.0))
lista_figuras.append(Cuadrado("verde",3.0))
lista_figuras.append(Circulo("azul",3.0))

def catalogar(lista_figuras):
    for figura in lista_figuras:
        print(f"clase{type(figura).__name__} con atributos {figura} ")
catalogar(lista_figuras)
print()

