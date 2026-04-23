print('*** Aplicacion de Cajero Automatico ***')
salir = False
DEPOSITO_INICIAL = 1000
saldo_actual = DEPOSITO_INICIAL
menu = '''Operaciones que puedes realizar:
    1. Consultar saldo
    2. Retirar saldo
    3. Depositar saldo
    4. Salir'''

while not salir:
    print(menu)
    opcion = int(input('Escoje una opcion: '))
    if opcion == 1:
        print(f'Tu saldo actual es: {saldo_actual:.2f}\n')
    elif opcion == 2:
        saldo_retirar = float(input('Introduce saldo a retirar: '))
        if saldo_retirar <= saldo_actual:
            saldo_actual -= saldo_retirar
            print(f'Tu nuevo saldo es: {saldo_actual:.2f}\n')
        else:
            print(f'No cuentas con el saldo suficiente, el saldo actual es: {saldo_actual}\n')
    elif opcion == 3:
        saldo_depositar = float(input('Introduce saldo a depositar: '))
        saldo_actual += saldo_depositar
        print('Tu nuevo saldo es: {saldo_actual:.2f}\n')
    elif opcion == 4:
        salir = True
        print('Saliendo...')
    else:
        print(f'Opcion invalida, selecciona optra opcion: {opcion}\n')