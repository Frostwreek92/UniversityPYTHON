print('*** Calculadora en Python ***')
salir = False
menu = '''Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir'''

while not salir:
    print(menu)
    opcion = int(input('Escoje una opcion: '))
    if opcion == 1:
        valor1 = float(input('Ingresa el valor 1: '))
        valor2 = float(input('Ingresa el valor 2: '))
        print(f'Tu resultado es: {valor1 + valor2}\n')
    elif opcion == 2:
        valor1 = float(input('Ingresa el valor 1: '))
        valor2 = float(input('Ingresa el valor 2: '))
        print(f'Tu resultado es: {valor1 - valor2}\n')
    elif opcion == 3:
        valor1 = float(input('Ingresa el valor 1: '))
        valor2 = float(input('Ingresa el valor 2: '))
        print(f'Tu resultado es: {valor1 * valor2}\n')
    elif opcion == 4:
        valor1 = float(input('Ingresa el valor 1: '))
        valor2 = float(input('Ingresa el valor 2: '))
        if valor2 == 0:
            print('Error, no se puede dividir entre 0!\n')
        else:
            print(f'Tu resultado es: {valor1 / valor2}\n')
    elif opcion == 5:
        salir = True
        print('Saliendo...')
    else:
        print('Opcion no valida')