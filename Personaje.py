class Personaje:
    """
    Clase base para representar un personaje en The Matrix.
    """
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.__energia = 100  # Atributo privado
    
    @property
    def energia(self):
        return self.__energia
    
    @energia.setter
    def energia(self, energia: int):
        if 0 <= energia <= 100:
            self.__energia = energia
        else:
            raise ValueError("La energía debe estar entre 0 y 100.")
    
    def __str__(self):
        return f"{self.nombre} (Energía: {self.__energia})"
    
    def actuar(self):
        """
        Método polimórfico para representar la acción del personaje.
        """
        return f"{self.nombre} está en reposo."
