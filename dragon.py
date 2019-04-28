import random
import time

def mostrar_introduccion():
    print('Estás en una tierra llena de dragones. Frente a tí')
    print('hay dos cuevas. En una de ellas, el dragón es generoso y')
    print('amigable y compartirá su tesoro contigo. El otro dragón')
    print('es codicioso y está hambriento, y te devorará inmediatamente.')
    print()

def elegir_cueva():
    cueva = ''
    while cueva != '1' and cueva != '2':
        print('¿A qué cueva quieres entrar? (1 ó 2)')
        cueva = input()
    return cueva 
def explorar_cueva(cueva_elegida):
       print('Te aproximas a la cueva...')
       time.sleep(2)
       print('Es oscura y espeluznante...')
       time.sleep(2)
       print('¡Un gran dragon aparece súbitamente frente a tí! Abre sus fauces ..')
       print()
       time.sleep(2)

       cueva_amigable = random.randint(1,2)
       if cueva_elegida == str(cueva_amigable):
           print('Te regala su tesoro')
       else:
           print('Te engulle de un bocado')

jugar_de_nuevo = 'si'

while jugar_de_nuevo == 'si' or jugar_de_nuevo == 's':
    mostrar_introduccion()
    numero_de_cueva = elegir_cueva()
    explorar_cueva(numero_de_cueva) 
    print('Jugar de nuevo (si | no)')
    jugar_de_nuevo =input()


