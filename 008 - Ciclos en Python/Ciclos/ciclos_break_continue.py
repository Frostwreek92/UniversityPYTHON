print('*** Break y Continue ***')

# Ejemplo con break
print('Palabra break')
for numero in range(1,10):
    if numero % 2 == 0: # Numero par
        print(numero)
        break

# Ejemplo de continue
print('Palabra continue')
for numero in range(1,10):
    if numero % 2 == 1: # Numero impar
        continue
    print(numero)
