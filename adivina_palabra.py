import random
IMAGENES_AHORCADO = ['''

+---+
|   |
    |
    |
    |
===== ''','''    

+---+
|   |
o   |
    |
    |
===== ''','''    
+---+
|   |
o   |
|   |
    |
===== ''','''    
+---+
|   |
 o  |
/|  |
    |
===== ''','''    
+---+
|   |
 o  |
/|\ |
    |
===== ''','''    
+---+
|   |
 o  |
/|\ |
/   |
===== ''','''    
+---+
|   |
 o  |
/|\ |
/ \   |
===== ''']

palabras = ''' hormiga babuino tejon murcielago oso 
            castor camello gato almeja cobra pantera coyote 
            cuervo ciervo perro burro pato aguila huron 
            zorro rana cabra ganso halcon leon lagarto 
            llama topo mono alce raton mula salamandra nutria buho 
            panda loro paloma piton conejo carnero rata cuervo rinoceronte 
            salmon foca tiburon oveja mofeta perezoso serpiente 
            araña cigüeña cisne tigre sapo trucha pavo tortuga 
            comadreja ballena lobo wombat cebra '''.split()

print(palabras)

def obtener_palabras_al_azar(lista_de_palabras):
    indice_de_palabras = random.randint(0,len(lista_de_palabras)-1)
    return lista_de_palabras[indice_de_palabras]

def mostrar_tablero(IMAGENES_AHORCADO,letras_incorrectas,letras_correctas,
                    palabra_secreta):
    print(IMAGENES_AHORCADO[len(letras_incorrectas)])
    print()

    print('letras incorrectas','end')
    for letra in letras_incorrectas:
        print(letra, end='')
        print()
        espacios_vacios = '_' * len(palabra_secreta)

        for i in range(len(palabra_secreta)):
            if(palabra_secreta[i] in letras_correctas):
                espacios_vacios = espacios_vacios[:i] + palabra_secreta[i]+
                espacios_vacios[i+1:]



            

