import io
from jjj import juegoah


from Opcion import Opcion
from Escenario import Escenario
from Personaje import Personaje

personaje = Personaje()
escenarioActual = None
final = False
escenarios = {}

WHITE = '\033[37m'
RED = '\033[31m'

print("\n\n")
print("██████╗░███████╗██████╗░██████╗░██╗██████╗░░█████╗░  ███████╗███╗░░██╗  ███████╗██╗░░░░░")
print("██╔══██╗██╔════╝██╔══██╗██╔══██╗██║██╔══██╗██╔══██╗  ██╔════╝████╗░██║  ██╔════╝██║░░░░░")
print("██████╔╝█████╗░░██████╔╝██║░░██║██║██║░░██║██║░░██║  █████╗░░██╔██╗██║  █████╗░░██║░░░░░")
print("██╔═══╝░██╔══╝░░██╔══██╗██║░░██║██║██║░░██║██║░░██║  ██╔══╝░░██║╚████║  ██╔══╝░░██║░░░░░")
print("██║░░░░░███████╗██║░░██║██████╔╝██║██████╔╝╚█████╔╝  ███████╗██║░╚███║  ███████╗███████╗")
print("╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝╚═════╝░░╚════╝░  ╚══════╝╚═╝░░╚══╝  ╚══════╝╚══════╝")
print("")
print("                 ██████╗░░█████╗░░██████╗░██████╗░██╗░░░██╗███████╗")           
print("                 ██╔══██╗██╔══██╗██╔════╝██╔═══██╗██║░░░██║██╔════╝")
print("                 ██████╦╝██║░░██║╚█████╗░██║██╗██║██║░░░██║█████╗░░")
print("                 ██╔══██╗██║░░██║░╚═══██╗╚██████╔╝██║░░░██║██╔══╝░░")
print("                 ██████╦╝╚█████╔╝██████╔╝░╚═██╔═╝░╚██████╔╝███████╗")
print("                 ╚═════╝░░╚════╝░╚═════╝░░░░╚═╝░░░░╚═════╝░╚══════╝")
print(" \n\n\n")
print("                 SI DESEAS INICIAR PRESIONA ENTER PARA CONTINUAR")
print(" \n")

bandera:bool = True
while bandera or opcion == "":
    bandera = False
    opcion=(input(""))
    opcion=opcion
    if opcion == "":
      print("")  
      break 
    else:
      print("opcion incorrecta")
      bandera=True

print("Instruciones: ")
print("Este juegos se trata de una historia interactiva que sumerje al jugador en una historia de\nsupervivencia, se le planteara diferentes situaciones donde el jugador debe tomar la decisión\ncorrecta para sobrevir",RED+"SI ES QUE PUEDE.")
print("\n                                                                Presiona ENTER para continuar")
bandera:bool = True
while bandera or opcion == "":
    bandera = False
    opcion=(input(""))
    opcion=opcion
    if opcion == "":
      print(WHITE+"")  
      break 
    else:
      print("opcion incorrecta")
      bandera=True


with io.open('EscenariosPrincipales.txt', 'r', encoding='utf8') as archivo:

    archivo.seek(0)
    contenido = archivo.read()

    partes = contenido.split("#")

    for p in range(len(partes)):

        if len(partes[p]) > 0:

            escenario = partes[p].split("*")
            partesEscenario = escenario[0].split("|")

            opciones = []

            for e in range(len(escenario)):

                if e > 0:
                    partesOpcion = escenario[e].split("|")
                    o = Opcion(partesOpcion[1].rstrip(), partesOpcion[0])
                    opciones.append(o)

            e = Escenario(partesEscenario[1], opciones)
            
            if 2 < len(partesEscenario):
                e.cambioSupervivencia = int(partesEscenario[2])
            escenarios[partesEscenario[0]] = e

escenarioActual = escenarios['INICIO']

while not final:
    siguiente = escenarioActual.presentar(personaje)
    if siguiente == "TIRO":
      juegoah()
      
    escenarioActual = escenarios[siguiente]



