def Menu():
    print()
    print ("TORNEO")
    print("1.Agregar Equipo")
    print("2.Agregar Resultado")
    print("3.Ver Tabla")
    print("4.Eliminar Equipo")
    print("5.Salir")
    return input("Elegi una opcion: ")
Torneo = {}
while True:
    opcion = Menu()
    if opcion == "1":
        Nombre = input ("Nombre del equipo: ")
        if Nombre in Torneo:
            print("El equipo ya esta en el torneo")
        else:
            Torneo [Nombre] = {"Puntos":0}
            print (f"{Nombre} fue agregado al torneo")
    elif opcion == "2":
        try:
            Local = input ("Equipo local: ")
            Visitante = input ("Equipo visitante: ")
            if Local not in Torneo or Visitante not in Torneo:
                print ("Uno o los dos equipos no forman parte del torneo")
                continue
            Resultado = input ("Ingresa el resultado separado de un guion '-': ")
            GolesLocal, GolesVisitante = map(int, Resultado.split ("-"))
            if GolesLocal > GolesVisitante:
                Torneo [Local]["Puntos"] += 3
            elif GolesLocal < GolesVisitante:
                Torneo [Visitante]["Puntos"] +=3
            else:
                Torneo [Local]["Puntos"] += 1
                Torneo [Visitante]["Puntos"] +=1
            print ("Resultado cargado")
        except ValueError:
            print ("Resultado mal ingresado")
    elif opcion == "3":
        if not Torneo:
            print ("El torneo no tiene nigun equipo")
            continue
        Tabla = sorted (Torneo.items(), key=lambda x: x[1]["Puntos"], reverse=True)
        print ("TORNEO")
        print(F"Equipo----Puntos")
        for equipo, Puntos in Tabla:
            print(f"{equipo}----{Puntos}")
    elif opcion == "4":
        Nombre = input ("Equipo a eliminar: ")
        if Nombre in Torneo:
            del Torneo [Nombre]
            print(f"El equipo {Nombre} fue eliminado del torneo")
        else:
            print ("Ese equipo no pertenece al torneo")
    elif opcion == "5":
        break
    else:
        print ("Opcion no valida")
            
    