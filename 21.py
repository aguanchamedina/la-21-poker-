import random

print ("----------------------------")
print ("--------LA 21 POKER---------")
print ("----------------------------")

#INPUT 
jugador=random.randint(1,10)
pc=random.randint(1,10)

#Numeros aleatorios tanto del jugador como del pc"Representando las cartas del juego"
#sum jugador
#dan pac

#PROCESS 
suma_de_puntos_tallador=0
suma_de_puntos_Jugador=0
i=1
diferencia=suma_de_puntos_tallador-suma_de_puntos_Jugador
while i<= 2:
    suma_de_puntos_Jugador=suma_de_puntos_Jugador+jugador
    suma_de_puntos_tallador=suma_de_puntos_tallador+pc
    i=i+1
print("pc",suma_de_puntos_tallador)
print("Jugador",suma_de_puntos_Jugador)
print("¿Quieres seguir jugando?")

X=int(input("1. para seguir jugando o 2. para parar: "))

if X==1: 
    while suma_de_puntos_Jugador<=21 and X!=2:
     
        d= random.randint(1,10)
        
        suma_de_puntos_Jugador=suma_de_puntos_Jugador +d 
        print("jugador",suma_de_puntos_Jugador)
        if suma_de_puntos_Jugador>21:
            print("volaste")
            break
       
        print("¿Quieres seguir jugando?")
        X=int(input("1. para seguir jugando o 2. para parar: "))
        if suma_de_puntos_Jugador>21:
            print("volaste")
            break
        elif X==2:
            while suma_de_puntos_tallador<=suma_de_puntos_Jugador and suma_de_puntos_tallador< 21:
                p=random.randint(1,10)
                suma_de_puntos_tallador = suma_de_puntos_tallador + p
                print("Tallador", suma_de_puntos_tallador)
            if suma_de_puntos_tallador>suma_de_puntos_Jugador and suma_de_puntos_tallador<21:
                if suma_de_puntos_tallador-suma_de_puntos_Jugador==1:
                    print("El tallador gana por un punto")
                else:
                    print("gana el tallador por" , suma_de_puntos_tallador-suma_de_puntos_Jugador, "Puntos")
            elif suma_de_puntos_tallador==suma_de_puntos_Jugador:
                print("gana el pc por ser el tallador")
            if suma_de_puntos_tallador>21:
                print("El tallador ah volado")

elif X==2:
            while suma_de_puntos_tallador<=suma_de_puntos_Jugador and suma_de_puntos_tallador< 21:
                p=random.randint(1,10)
                suma_de_puntos_tallador = suma_de_puntos_tallador + p
                print("Tallador", suma_de_puntos_tallador)
            if suma_de_puntos_tallador>suma_de_puntos_Jugador and suma_de_puntos_tallador<21:
                if suma_de_puntos_tallador-suma_de_puntos_Jugador==1:
                    print("El tallador gana por un punto")
                else:
                    print("gana el tallador por" , suma_de_puntos_tallador-suma_de_puntos_Jugador, "Puntos")
            elif suma_de_puntos_tallador==suma_de_puntos_Jugador:
                print("gana el pc por ser el tallador")
            if suma_de_puntos_tallador>21:
                print("El tallador ah volado")