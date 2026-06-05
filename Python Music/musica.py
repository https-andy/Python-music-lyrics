import time # De esta manera podemos controlar el tiempo de la animación
import sys #Esto importa el modulo sys, que nos ayuda a manejar parámetros específicos del sistema, como imprimir en pantalla


# Estos son códigos de color usados para cambiar el color del texto en la terminal
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'   # Esto restablece el color al valor normal

lyrics = [
    (RED, "Te vi bailar, brillando con tu ausencia"),
    (GREEN, "Sin sentir piedad chocando con las mesas"),
    (YELLOW, "Te burlaste de todos, te reíste de mí"),
    (BLUE, "Tus amigos escaparon de vos"),
    (MAGENTA, "y a mí me volvió loco tu forma de ser"),
    (CYAN, "A mí me vuelve loco tu forma de ser"),
    (RESET, "Tu egoísmo y tu soledad"),
    (RED, "Son estrellas en la noche de la mediocridad"),
    (GREEN, "Me vuelve loco tu forma de ser"),
    (YELLOW, "A mi me volvió loco tu forma de ser"),
    (BLUE, "Tu egoísmo y tu soledad"),
    (MAGENTA, "Son joyas en el barro de la mediocridad"),
]

# Función para animar texto letra por letra con color
def animate_text(color, text):
    for char in text:  # Recorrer cada carácter del texto
        sys.stdout.write(color + char + RESET)  # Imprimir el carácter con el color especificado
        sys.stdout.flush()  # Mostrar inmediatamente el carácter en pantalla
        time.sleep(0.05)  # Esperar 0.05 segundos antes de imprimir el siguiente carácter
    print()  # Imprimir una nueva línea después de terminar el texto

# Función principal para mostrar la letra con animación
def main():
    for color, line in lyrics:  # Recorrer cada tupla de la lista lyrics
        animate_text(color, line)  # Llamar a la función animate_text para mostrar cada línea
        time.sleep(2.5)  # Esperar 2.5 segundos antes de mostrar la siguiente línea

# Esta condición asegura que la función principal se ejecute solo si este archivo se ejecuta directamente
if __name__ == "__main__":
    main()  # Llamar a la función principal para iniciar el programa