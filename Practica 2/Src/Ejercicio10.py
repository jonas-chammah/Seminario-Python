def inicializarEstadisticas(participantes):
    Estadisticas = {}
    for p in participantes :
        Estadisticas [p] = {"Puntaje" : 0, "Rondas ganadas" : 0, "Mejor ronda" : 0}
    return Estadisticas  

def Rondas (ronda, numRonda, Estadisticas):
    Tema = ronda ["theme"]
    PuntajeRonda = {}
    for participante, jueces in ronda ["scores"].items():
        puntajes = sum(jueces.values())
        PuntajeRonda [participante] = puntajes
        Estadisticas[participante] ["Puntaje"] += puntajes
        if puntajes > Estadisticas [participante] ["Mejor ronda"] :
            Estadisticas [participante] ["Mejor ronda"] = puntajes
    Ganador = max(PuntajeRonda, key=PuntajeRonda.get)
    Estadisticas [Ganador]["Rondas ganadas"] += 1
    print (f"Ronda: {numRonda} - {Tema}: ")
    print (f"Ganador: {Ganador} ({PuntajeRonda[Ganador]} pts)")
    Posiciones = sorted (Estadisticas.items(),key=lambda x: x[1]['Puntaje'], reverse=True)
    print ("TABLA DE POSICIONES PARCIAL: ")
    print ("Cocinero  Puntaje  Rondas ganadas  Mejor ronda  Promedio ")
    print ("------------------------------------------------------------")
    for Pos, (participante, EstadisticasParticipante) in enumerate(Posiciones, 1):
        Promedio = EstadisticasParticipante ["Puntaje"] / numRonda
        print (f"{participante:<10} {EstadisticasParticipante["Puntaje"]:<10} {EstadisticasParticipante["Rondas ganadas"]:<10} {EstadisticasParticipante["Mejor ronda"]:<10} {Promedio :<10}")
    print ("------------------------------------------------------------")

def TablaFinal (Estadisticas, numRonda, participantes):
    Posiciones = sorted (Estadisticas.items(),key=lambda x: x[1]['Puntaje'], reverse=True)
    print ("TABLA DE POSICIONES FINAL: ")
    print ("Cocinero  Puntaje  Rondas ganadas  Mejor ronda  Promedio ")
    print ("------------------------------------------------------------")
    for Pos, (participante, EstadisticasParticipante) in enumerate(Posiciones, 1):
        Promedio = EstadisticasParticipante ["Puntaje"] / numRonda
        print (f"""{participante:<10} {EstadisticasParticipante["Puntaje"]:<10} {EstadisticasParticipante["Rondas ganadas"]:<10} {EstadisticasParticipante["Mejor ronda"]:<10} {Promedio :<10}""")
    print ("------------------------------------------------------------")

