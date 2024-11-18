from Personaje import Personaje

class Humano(Personaje):
    """
    Clase que representa a un humano fuera de la Matrix.
    """
    def __init__(self, nombre: str, nave: str):
        super().__init__(nombre)
        self.nave = nave
    
    def __str__(self):
        return f"{self.nombre}, humano de la nave {self.nave}."
    
    def actuar(self):
        return f"{self.nombre} está entrenando en la nave {self.nave}."
