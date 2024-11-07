#adivina el numero  que escoja la variable bot
import random

minimo = 0

dificultad = input("escoje una dificultad  (facil/medio/dificil/extremo):  ")
if dificultad == 'facil':
	maximo = 10
elif dificultad == "medio":
	maximo = 50
elif dificultad == "dificil":
	maximo = 100
elif dificultad == "extremo":
	maximo = 1000
else :
	print("escoje una dificultad:  ")
	maximo = 10
				
bot = random.randint(minimo , maximo)
intentos = 0

while True:
    you =int(input(f'introduce un numero de ({minimo} - {maximo}):   '))


    if you not in range(minimo , maximo + 1):
        print('numero no valido es de ({minimo} - {maximo}) intente de nuevo: ')
        continue

    intentos += 1  # se van acomulando los intentos asta que ganes
    if you == bot:
        print(f'adivinastes el numero felizidades  numero:({you})  intentos:(#{intentos})')
        break # finaliza el bucle, si ganas
    elif you < bot:
        print(f'el numero es mayor a ({you}) intentos: (#{intentos}) ')
    elif you > bot:
        print(f'el nunero es menor a ({you}) intentos: (#{intentos}) ')
       