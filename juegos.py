#import hangman
import reversegam
import tictactoeModificado
import ahorcadoConFuncionesNuevo

import json

def actualizar(nom,l):
	with open('partidas.txt','r') as p:
		datos=json.load(p)
	if nom in datos.keys():
		datos[nom].append(l) #de esta manera si un jugador juega dos veces se le agrega a su nombre lo que jugo como una lista aparte, asi van apareciendo las distintas sesiones de cada uno
	else:
		datos[nom]=l
	return datos

def guardarDatos(datos):
	with open('partidas.txt','w') as p:
		json.dump(datos,p,indent=4) #Uso json porque me parece que queda más prolijo, además para poder leer los datos que se están utilizando es mas sencillo

def imprimir():
	with open('partidas.txt','r') as p:
		datos=json.load(p)
		print(json.dumps(datos,sort_keys=True,indent=4))	

def main(argv):
	nombre=input('Ingrese su nombre: ')
	l=[]
	dic={nombre:l} #Uso un diccionario para poder asignarle al jugador los juegos que jugo durante una sesión de manera prolija
	datos=[]
	sigo_jugando = True
	while sigo_jugando:
		
		print('''
		Elegí con qué juego querés jugar:
		1.- Ahorcado
		2.- Ta-TE-TI
		3.- Otello
		4.- Salir''')

		opcion = input()
		if opcion == '1':
			ahorcadoConFuncionesNuevo.main()
			l.append('Ahorcado')
		elif opcion == '2':
			tictactoeModificado.main()
			l.append('Tic Tac Toe')
		elif opcion == '3':
			reversegam.main()
			l.append('Reversegam')
		elif opcion == '4':
			sigo_jugando = False
	
	datos=actualizar(nombre,l)
	guardarDatos(datos)
	imprimir()
	
	
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
