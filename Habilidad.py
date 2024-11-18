class Habilidad:
    """
    Clase que representa una habilidad que un personaje puede tener.
    """
    def __init__(self, nombre: str, nivel: int):
        self.nombre = nombre
        self.nivel = nivel