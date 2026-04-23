print('*** Repeticion de mensaje ***')

mensaje = input('Proporciona mensaje a repetir: ')
numero_repeticiones = int(input('Ingrese numero de repeticiones: '))

# Iterar sobre el rango de repeticiones
for _ in range(numero_repeticiones): # Con el _ no se usa el valor de indice
    # print(f'{i + 1} - {mensaje}')
    print(mensaje)