#adivina el numero magico  que piense el bot
import random

# el bot piensa en un numero del 1 al 10
bot =random.randint(1,10)
intentos = 0

# para que no termine de repetirse asta que ganes
while True:
    you =int(input('introduce un numero del 1 al 10:  '))

    # valida si el numero que pusistes es del 1 al 10 sino hace que lo pongas de nuevo
    if you not in range(1,11):
        print('numero no valido es del (1 al 10) intente de nuevo: ')
        continue

    intentos += 1  # se van acomulando los intentos asta que ganes
    if you == bot:
        print(f'adivinastes el numero magico felizidades  numero:({you})  intentos:({intentos})')
        break # finaliza el bucle, si ganas
    elif you < bot:
        print(f'el numero magico es mayor a ({you})')
    elif you > bot:
        print(f'el nuemro magico es menor  a  ({you})')
