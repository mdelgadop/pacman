from Personaje import Personaje
from Humano import Humano
from Programa import Programa
from Neo import Neo
from Habilidad import Habilidad

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

def crear_personaje(nombre:str):
    p = Personaje(nombre + " personaje")
    return p

# Ejemplo de uso
if __name__ == "__main__":
    # Crear personajes
    morpheo = crear_personaje("Morpheo")
    trinity = Humano("Trinity", "Nebuchanazer")
    smith = Programa("Smith", "v1.2")

    kunf_fu = Habilidad("Kung fu", 85)
    salto = Habilidad("Salto", 90)

    personajes = [morpheo, trinity, smith]
    for p in personajes:
        print(p.actuar())

    