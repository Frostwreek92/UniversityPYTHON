print('*** Creacion y Validacion de un Password ***')
password = str(input('Ingresa tu password (debe tener al menos 6 caracteres): '))

# Validar el password
while len(password) < 6:
    print('El password debe tener al menos 6 caracteres')
    password = input('Ingresa tu password: ')
else:
    print('El valor de password ya es correcto')