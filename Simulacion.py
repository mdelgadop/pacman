from Programa import Programa

class Simulacion:
    """
    Clase que representa una simulación en la Matrix. Demuestra la composición.
    """
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.programas = []  # Composición: la simulación tiene programas
    
    def agregar_programa(self, programa: Programa):
        self.programas.append(programa)
    
    def __str__(self):
        info_programas = "\n".join(str(p) for p in self.programas)
        return f"Simulación: {self.nombre}\nProgramas:\n{info_programas}"

