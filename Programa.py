from Personaje import Personaje

class Programa(Personaje):
    """
    Clase que representa un programa dentro de la Matrix.
    """
    def __init__(self, nombre: str, version: int):
        super().__init__(nombre)
        self.version = version
    
    def __str__(self):
        return f"{self.nombre}, programa versión {str(self.version)}."
    
    def actuar(self):
        return f"{self.nombre} está ejecutando su protocolo."
