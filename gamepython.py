import random

# lista de palabras predeterminadas
palabras = ['python', 'programacion', 'ordenador', 'lenguaje', 'desarrollo', 'informatica', 'programa', 'tecnologia']

# seleccionar una palabra al azar
palabra = random.choice(palabras)

# crear la palabra oculta
palabra_oculta = ['_'] * len(palabra)

# lista de letras incorrectas
letras_incorrectas = []

# número de oportunidades restantes
intentos_restantes = 6

# bucle principal del juego
while True:
    # mostrar la palabra oculta
    print(' '.join(palabra_oculta))

    # obtener la letra del jugador
    letra = input('Adivina una letra: ').lower()

    # comprobar si la letra está en la palabra
    if letra in palabra:
        # actualizar la palabra oculta
        for i in range(len(palabra)):
            if palabra[i] == letra:
                palabra_oculta[i] = letra
    else:
        # la letra es incorrecta
        letras_incorrectas.append(letra)
        intentos_restantes -= 1
        print('Esa letra no está en la palabra. Te quedan', intentos_restantes, 'intentos.')

        # dibujar el ahorcado
        if intentos_restantes == 5:
            print('  O')
        elif intentos_restantes == 4:
            print('  O')
            print(' /')
        elif intentos_restantes == 3:
            print('  O')
            print(' /|')
        elif intentos_restantes == 2:
            print('  O')
            print(' /|\\')
        elif intentos_restantes == 1:
            print('  O')
            print(' /|\\')
            print(' /')
        elif intentos_restantes == 0:
            print('  O')
            print(' /|\\')
            print(' / \\')
            print('¡Has perdido! La palabra era', palabra)
            break

    # comprobar si el jugador ha ganado
    if '_' not in palabra_oculta:
        print('¡Felicidades! Has adivinado la palabra.')
        break