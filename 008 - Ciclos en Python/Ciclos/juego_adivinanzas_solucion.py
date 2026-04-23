from random import randint

print('*** Juego de Adivinanzas ***')

numero_secreto = randint(1,50)
intentos = 0
adivinanza = None
INTENTOS_MAXIMOS = 5

while adivinanza != numero_secreto and intentos < INTENTOS_MAXIMOS:
    adivinanza = int(input('Adivina el numero secreto (1-50): '))
    # Agregamos ayuda orientar jugador
    if adivinanza < numero_secreto:
        print('El numero secreto es mayor')
    elif adivinanza > numero_secreto:
        print('El numero secreto es menor')
    # Incrementamos la variable de intentos
    intentos += 1

# Conclusion del juego
if adivinanza == numero_secreto:
    print(f'\nFelicidades, adivinaste el numero secreto en: {intentos} intentos')
else:
    print(f'\nHas agotado los intentos máximos: {INTENTOS_MAXIMOS}')
    print(f'El numero secreto era: {numero_secreto}')