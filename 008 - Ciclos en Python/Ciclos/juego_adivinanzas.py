from random import randint

print('*** Juego de Adivinanza Numerica ***')
num_aleatorio = int(randint(1,50))
contador_fallos = 0
limite_fallos = 10
acertado = False

while not acertado:
    if contador_fallos < limite_fallos:
        print(f'Llevas {contador_fallos} intentos\n')
        numero = int(input('Ingrese un numero: '))
        if numero > num_aleatorio:
            contador_fallos+=1
            print('El numero introducido es mayor\n')
        elif numero < num_aleatorio:
            contador_fallos+=1
            print('El numero introducido es menor\n')
        else:
            acertado = True
            print(f'Has acertado el numero con: {contador_fallos}')

    else:
        print('Has llegado al limite de intentos\n')
        acertado = True