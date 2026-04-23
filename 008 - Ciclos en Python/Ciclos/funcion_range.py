print('*** Funcion range ***')

print('Secuendia del 0 al 4')
# El valor de inicio por defecto es 0 y el de fin es de 5-1, es decir 4, y los incrementos, de 1 en 1 default
for i in range(5):
    print(i, end=' ')

print('\n\nSecuencia del 10 al 20')
# Incremento tiene valor de 1 por default
for i in range(10, 20 + 1):
    print(i, end=' ')

print('\n\nSecuendia del 20 al 30 de 2 en 2')
for i in range(20, 30 + 1, 2):
    print(i, end=' ')