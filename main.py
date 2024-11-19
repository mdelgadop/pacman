from Habilidad import Habilidad
from Personaje import Personaje
from Humano import Humano
from Programa import Programa
from Neo import Neo
from Simulacion import Simulacion

# Ejemplo de uso
if __name__ == "__main__":
    # Crear personajes
    morpheo = Personaje("Morpheo")
    trinity = Humano("Trinity", "Nebuchadnezzar")
    neo = Neo("Nebuchadnezzar")
    agente_smith = Programa("Agente Smith", "v2.1")
    
    # Crear habilidades y asignarlas a Neo
    kung_fu = Habilidad("Kung Fu", 10)
    hacking = Habilidad("Hacking", 8)
    neo.agregar_habilidad(kung_fu)
    neo.agregar_habilidad(hacking)
    
    # Crear una simulación y agregar programas
    simulacion = Simulacion("Simulación de prueba")
    simulacion.agregar_programa(agente_smith)
    
    # Ajustar y mostrar la energía de Neo
    neo.energia = 80
    print(neo)
    print(neo.mostrar_habilidades())
    
    # Mostrar la información de la simulación
    print(simulacion)
    
    # Polimorfismo: comportamiento de actuar
    personajes = [neo, agente_smith, trinity, morpheo]
    for personaje in personajes:
        print(personaje.actuar())
