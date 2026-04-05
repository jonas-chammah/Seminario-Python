import random

categorias = {
    "Lenguajes": ["python"],
    "Estructuras": ["lista", "cadena", "bucle"],
    "General": ["programa", "variable", "funcion", "entero"]
}

print("¡Bienvenido al Ahorcado!")
print("Categorias: ")

for cat in categorias.keys():
    print(f"- {cat}")

categoria = input("Elegí una categoría: ")

while categoria not in categorias:
    print("Categoría no válida. Intentalo de nuevo.")
    categoria = input("Elegí una categoría: ")

ListaPalabras = random.sample(categorias[categoria] , len(categorias[categoria]))

while len(ListaPalabras) > 0:
    word = ListaPalabras.pop()
    guessed = []
    attempts = 6
    puntos = 0

    print(f"Nueva ronda, te quedan {len(ListaPalabras)} palabras disponibles en la categoria {categoria}")

    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "

        print(progress)
        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            puntos += 6
            print("¡Ganaste!")
            print (f"¡Obtuviste {puntos} puntos!")
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ")

        if len(letter) != 1 or not letter.isalpha():
            print("Entrada no válida")
            continue

        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            puntos -=1
            print("Esa letra no está en la palabra.")

        print()
        
    else:
        puntos = 0
        print(f"¡Perdiste! La palabra era: {word}")
        print (f"¡Tu puntaje fue de {puntos} puntos!")

    if len(ListaPalabras) > 0:
        OtraRonda = input("Escribe 's' si queres jugar otra ronda o 'n' para terminar el juego: ")
        if OtraRonda != 's':
            print (f"Terminaste el juego, tu puntaje fue: {puntos}")
            break
    else:
        print("No te quedan palabras para jugar en esta categoria")


