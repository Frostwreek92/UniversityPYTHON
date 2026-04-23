print('*** Validacion campo formulario ***')

nombre_usuario = None

while not nombre_usuario:
    nombre_usuario = input('Ingrese el nombre del usuario: ')

print(f'Nombre de usuario valido: {nombre_usuario}')