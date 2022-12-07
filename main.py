# mi primer proyecto, ahorcado en varios sentidos...
#voy por los primeros pasos para armar este juego, descragué una lista de la rae en formato csv con muchas palabras

import csv
import interfaz
import random

def palabra_secreta_diccionario():
    csvfile = open ('diccionario.csv', 'r')
    reader = list(csv.DictReader(csvfile))
    palabra_elegida = random.choice (list(reader))
    palabra_secreta = (palabra_elegida['palabras_encabezado'])
    csvfile.close()
    return palabra_secreta
    
def pedir_letra(letras_repetidas):
    while True:
        letra = input('Ingreses una letra: ')#ingreso letra
        letra = letra.lower() # convierto a minuscula
        if letra in letras_repetidas:
            continue
        elif len(letra) > 1:
            print('Ingrese una sola letra')
            continue        
        else:
            letras_repetidas.append (letra)
            return letra
            break
def verificar_letra(letra, palabra_secreta):
    if letra in palabra_secreta:
        return True
    else:
        return False    

def validar_palabra(letras_repetidas, palabra_secreta):
    verificar = len(palabra_secreta)
    salida = verificar
    while salida > 0:
        for letra in palabra_secreta:
            if letra not in letras_repetidas:
                print('No se adivino la palabra')
                return False
                break
            else:
                salida -= 1
    return True 

if __name__ == "__main__":
    print("\n¡Aquí comienza el juego del ahorcado!\n")
    # Inicializo las variables y listas a utilizar.
    max_cantidad_intentos = 7
    intentos = 0
    letras_repetidas = []
    es_ganador = False
    palabra_secreta_diccionario()
    palabra_secreta = palabra_secreta_diccionario()
   
    interfaz.dibujar(palabra_secreta, letras_repetidas, intentos)
    while intentos < max_cantidad_intentos == 7 and not es_ganador:    
        letra = pedir_letra(letras_repetidas)
        # Verificar si la letra es parte de la palabra secreta        
        if verificar_letra(letra, palabra_secreta) == False:
            # En caso de no estar la letra ingresada en la palabra
            # a adivinar incremento en 1 la variable intentos.
            intentos += 1
              # Dibujar la interfaz
        interfaz.dibujar(palabra_secreta, letras_repetidas, intentos)

        # Validar si la palabra secreta se ha adivinado
        if validar_palabra(letras_repetidas, palabra_secreta) == True:
            es_ganador = True
            break

    if es_ganador:
        print(f'\n¡Usted ha ganado la partida!, palabra secreta {palabra_secreta}!\n')
    else:
        print('\n¡Ahorcado!')
        print(f'\n¡Usted ha perdido la partida!, palabra secreta {palabra_secreta}!\n')
        