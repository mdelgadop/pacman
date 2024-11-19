from Humano import Humano
from Habilidad import Habilidad

class Neo(Humano):
    """
    Clase específica que representa a Neo. Hereda de Humano.
    """
    def __init__(self, nave: str):
        super().__init__("Neo", nave)
        self.habilidades = []  # Agregación: Neo tiene habilidades
    
    def agregar_habilidad(self, habilidad: Habilidad):
        self.habilidades.append(habilidad)
    
    def mostrar_habilidades(self):
        habilidades_info = ", ".join(f"{h.nombre} (nivel {h.nivel})" for h in self.habilidades)
        return f"Habilidades de Neo: {habilidades_info}"
    
    def actuar(self):
        return f"{self.nombre} está combatiendo a los agentes en la Matrix."
