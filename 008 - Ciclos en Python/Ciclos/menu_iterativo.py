print('*** Sistema de Administracion de Cuentas ***')
salir = False
menu = '''Menu
    1. Crear cuenta
    2. Eliminar cuenta
    3. Salir'''

while not salir:
    print(menu)
    opcion = int(input('Escoje una opcion: '))
    if opcion == 1:
        print('Creando tu cuenta...\n')
    elif opcion == 2:
        print('Eliminando tu cuenta...\n')
    elif opcion == 3:
        print('Saliendo del sistema. Hasta pronto...')
        salir = True
    else:
        print(f'Opcion no valida: {opcion}\n')
else:
    print('Terminando el sistema de administracion de cuentas')