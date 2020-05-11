import random
import time

def esperar(tiempo):
	time.sleep(tiempo)
	
def eleccion(palabras):
	tema = int(input('Elige un tema:\n 1: animales\n 2: colores\n 3: comidas\n '))#Pido que el jugador elija un tema
	while(tema>len(palabras)):
		tema = int(input('Elige un tema:\n 1: animales\n 2: colores\n 3: comidas\n '))		
	pal = palabras[tema][random.randrange(len(palabras[tema]))]#Selecciono la palabra a trabajar
	return pal

def separar(pal):
	#armo la estructura de la palabra sobre la cuál se irá armando con las letras 
	#que se ingresen. Comienza con tantas rayas como letras tiene la palabra a adivinar
	pal_separada = []
	for y in pal:
		pal_separada.append(['_ '])
	print ('- '*len(pal))#Muestro por pantalla tantas rayas como letras tenga la palabra a adivinar
	return pal_separada

def preparacion():
	palabras={1:['gato', 'perro','pato','elefante','lobo'], 2:['rojo','azul','verde','amarillo'], 3:['milanesa','pure','pizza','salchicha']}
	ahorcado = [' O ', '/|\\','/ \\'] 
	pal=eleccion(palabras)
	palabra_separada=separar(pal)
	return ahorcado,pal,palabra_separada

def encontre (pal_separada,pal,letra):
	#Guardo las posiciones donde se encuentra		
	cant=0
	for pos in range(len (pal)):
		if pal[pos] == letra:
			pal_separada[pos] = letra				
			cant=cant+ 1
			
	#armo la palabra a mostrar al jugador con su letra elegida
	pal_imprime = ''
	for y in pal_separada:
		pal_imprime = pal_imprime + y[0]
	print (pal_imprime)
	return cant

def noEncontre(cantidad_partes_cuerpo,ahorcado,pal):
	sigue=True
	
	for x in range(cantidad_partes_cuerpo):
		print (ahorcado[x])
	if cantidad_partes_cuerpo == 3:
		esperar(1)
		print()
		print ('Perdiste!. La palabra era:', pal)
		sigue = False
	return sigue
		
def gano(cant,pal):
	sigue=True
	if cant == len(pal):
		esperar(1)
		print()
		print ('GANASTE!!')
		sigue = False
	return sigue
		
def jugar(pal,cuerpo,pal_separada):
	#inicializo variables que permiten saber si se ganó o perdió
	cantidad_letras_adivinadas = 0
	cantidad_partes_cuerpo = 0
	#comienza la interacción con el jugador
	sigue = True
	while sigue:
		#introducción de letras por parte del jugador
		letra = input('Ingresa una letra: ').lower()
		# Si hay al menos una aparición de la letra..
		if letra in pal:
			cantidad_letras_adivinadas = cantidad_letras_adivinadas + encontre(pal_separada,pal,letra)
			sigue=gano(cantidad_letras_adivinadas,pal)
		else:
			#si se equivocó completo el cuerpo
			cantidad_partes_cuerpo=cantidad_partes_cuerpo + 1
			sigue=noEncontre(cantidad_partes_cuerpo,cuerpo,pal)

def main():		
	ahorcado,pal,palabra_separada=preparacion()
	jugar(pal,ahorcado,palabra_separada)
	
if __name__=='__main__'	:
	main()
