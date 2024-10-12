# ubicatec primero colocar de donde viene hacia donde va
#presentar ubicaciones representativs y dentro de las funciones hacer las indicaciones de como llegar de manera sencilla
#ubicaciones considerando que apenas etsan por entrar a la institucion a puntos caracteristicos para comenzar 
def entradaPrincipal_biblioteca ():
    print("¿Estas ingresando con automovil?\n Coloca {S} si es el caso ó {N} si no lo es ")
    respuesta=input()
    if respuesta=="S":
        print("Estaciónate donde prefieras.\n Para llegar a biblioteca, ubica el Oxxo frente al estacionamiento y camina recto hasta llegar al Starbucks,etsara enfrente ")
        respuesta1=input("\t¿Deseas saber lo que tienes que pasar para poder llegar atu destino? [{S},{N}]: ")
        if respuesta =="S":
            print("Lo que vas a tener que ver para llegar  es: \n1-Oxxo \n2-Edificio con resbaladilla \n3-Fuente \n4-Llegaste a tu destino esta enfrente")
        else:
            print("Comprendo")
    else:
        print("Para llegar a biblioteca\nSaliendo de los torniquetes caminaras hasta donde veas el Oxxo es de manera recta."
              "\nUna vez ubicado el Oxxo, giraras a la izaquierda y caminaras de manera recta hasta llegar al Starbucks y estara enfrente el lugar")
        respuesta2=input("\t¿Deseas saber lo que tienes que pasar para poder llegar atu destino? [{S},{N}]: ")
        if respuesta2=="S":
            print("Lo que vas a tener que ver para llegar  es: \n1-Tramo de estacionamiento\n2-Oxxo \n3-Edificio con resbaladilla \n4-Fuente \n4-Llegaste a tu destino esta enfrente")
        else:
            print("Comprendo")
#Lo que hara esta funcion es de la entrada peatonal ote va a dirigir indicaciones hacia l abiblioteca 
def entradaPeatonal_biblioteca ():
    direcciones_texto()
    respuesta11=input("\t¿Deseas saber lo que tienes que pasar para poder llegar atu destino? [{SI},{NO}]: ").lower()
    if respuesta11=="SI":
        print("Lo que vas a tener que ver para llegar es: \n1-Canchas de basquetbol\n2-Alberca \n3-Liston de Maria \n4-TECstore")
    else:
        print("Comprendo")
#lo que hara sera igual que todas las demas funciones dirigirte hacia la binliioteca 
def entradaParque_biblioteca():
    print("¿Estas ingresando con automovil?\n Coloca {S} si es el caso ó {N} si no lo es ")
    respuesta=input()
    if respuesta=="S":
        print("Estaciónate donde prefieras.\n Para llegar a biblioteca, ubica el edificio Cima[es aquel que es un cuadrado gris esta en medio de todo]"
              "\nYa cuando hayas llegado, caminaras hasta la parte del estadio, giras a la izquierda, encontrars bicicletas y una parada de camion [Tomalo si gustas:)]"
              "\nCaminaras hasta estar en la cancha de pasto, giras a la izquierda y caminaras completamente derecho pasaras a un lado del Centro de Congresos"
              "\npasaras de igual forma el pabellon TEC, seguiras caminando de manera recta y tu destino estara de lado derecho")
        respuesta1=input("\t¿Deseas saber lo que tienes que pasar para poder llegar atu destino? [{S},{N}]: ")
        if respuesta1=="S":
            print("Lo que vas a tener que ver para llegar  es: \n1-Cima \n2-Estadio Borrego\n3-Cancha de pasto \n4-Centro de Congreso \n5-Plaza Roja \n6-Pabellon TEC \n6-Fuente")
        else:
            print("Comprendo")
    else:
        print("Una vez que hayas cruzado los torniquetes\n Para llegar a biblioteca, ubica el edificio Cima[es aquel que es un cuadrado gris esta en medio de todo]"
              "\nYa cuando hayas llegado, caminaras hasta la parte del estadio, giras a la izquierda, encontrars bicicletas y una parada de camion [Tomalo si gustas:)]"
              "\nCaminaras hasta estar en la cancha de pasto, giras a la izquierda y caminaras completamente derecho pasaras a un lado del Centro de Congresos"
              "\npasaras de igual forma el pabellon TEC, seguiras caminando de manera recta y tu destino estara de lado derecho")
        respuesta2=input("\t¿Deseas saber lo que tienes que pasar para poder llegar atu destino? [{S},{N}]: ")
        if respuesta2=="S":
            print("Lo que vas a tener que ver para llegar  es: \n1-Cima \n2-Estadio Borrego\n3-Cancha de pasto \n4-Centro de Congreso \n5-Plaza Roja \n6-Pabellon TEC \n6-Fuente")
        else:
            print("Comprendo")

def entradaPrincipal_estadio():
    print("¿Estas ingresando con automovil?\n Coloca {S} si es el caso ó {N} si no lo es ")
    respuesta=input()
    if respuesta=="S":
        print("Estaciónate donde prefieras.\n Para llegar al estadio, ubica el Oxxo frente al estacionamiento y caminas recto hasta caminar al centro de congresos,seguiras caminando derecho hasta ver el edificio de Cima y tu destino estara a la izquierda")
        respuesta1=input("\t¿Deseas saber lo que tienes que pasar para poder llegar atu destino? [{S},{N}]: ")
        if respuesta1=="S":
            print("Lo que vas a tener que ver para llegar  es: \n1-Oxxo \n2-Edificio de medios \n3-Plaza roja \n4-Centro de congresos \n5-Gimnasio \n6-Cancha de pasto"
                  "\n6-Cima")
        else:
            print("Comprendo")
    else:
        print("Para llegar al estadio\nSaliendo de los torniquetes caminaras hasta donde veas el Oxxo es de manera recta."
              "\nUna vez ubicado el Oxxo,caminas recto hasta caminar al centro de congresos,seguiras caminando derecho hasta ver el edificio de Cima y tu destino estara a la izquierda")
        respuesta2=input("\t¿Deseas saber lo que tienes que pasar para poder llegar atu destino? [{S},{N}]: ")
        if respuesta2=="S":
            print("Lo que vas a tener que ver para llegar  es: \n1-Tramo de estacionamiento\n2-Oxxo \n3-Edificio de medios \n4-Plaza roja \n5-Centro de congresos \n6-Gimnasio \n7-Cancha de pasto \n6-Cima")
        else:
            print("Comprendo")
def entradaPeatonal_estadio():
    print("Saliendo de los torniquetes, dirigete a la alberca[estara de lado derecho],una vez ahi gira a la izquierda y camina de forma recta,etsara de frente la cancha de pasto"
          "\ngira a la derecha y caminaras de forma recta hasta ver el muro de escalada,gira a la izquierda y camina derecho, ahi estara el estadio :)")
    respuesta11=input("\t¿Deseas saber lo que tienes que pasar para poder llegar atu destino? [{S},{N}]: ")
    if respuesta11=="S":
        print("Lo que vas a tener que ver para llegar es: \n1-Canchas de basquetbol\n2-Alberca \n3-Canchas de padel y tenis \n4-Cancha de pasto \n5-Muro de escalada \n6-Barberia")
    else:
        print("Comprendo")
def entradaParque_estadio():
    print("¿Estas ingresando con automovil?\n Coloca {S} si es el caso ó {N} si no lo es ")
    respuesta=input()
    if respuesta=="S":
        print("Estaciónate donde prefieras.\n Para llegar al estadio, ubica el edificio de Cima[es aquel que es un cuadrado gris esta en medio de todo]"
              "\nestando de frente al edificio gira a la derecha caimnaras de forma recta y estara enfrente")
        respuesta4=input("\t¿Deseas saber lo que tienes que pasar para poder llegar atu destino? [{S},{N}]: ")
        if respuesta4=="S":
            print("Lo que vas a tener que ver para llegar  es: \n1-Cima \n2-Estadio Borrego\n3-Cancha de pasto \n4-Centro de Congreso \n5-Plaza Roja \n6-Pabellon TEC \n6-Fuente")
        else:
            print("Comprendo")
    else:
        print("Una vez que salgas de los torniquetes.\nPara llegar al estadio, ubica el edificio de Cima [es aquel que es un cuadrado gris, está en medio de todo]."
              "\nEstando de frente al edificio, gira a la derecha, caminarás de forma recta y el estadio estará enfrente.")
        respuesta5 = input("\t¿Deseas saber lo que tienes que pasar para poder llegar a tu destino? {S},{N}: ")
        if respuesta5 == "S":
            print("Lo que vas a tener que ver para llegar es: \n1-Cima \n2-Estadio Borrego \n3-Cancha de pasto \n4-Centro de Congreso \n5-Plaza Roja \n6-Pabellón TEC \n7-Fuente")
        else:
            print("Comprendo")
"""Lo que hace esta funcion es verificar el numero del salon al que se dirige se hace con la forma de metr ese numero en una lista 
"""
def encontrar_salon():
    salon=int(input("Ingresa el numero de tu salon: ""{Solo se puede para edifcio 3 y 4 ejemplo[3104 o 4205]}: "))
    lista=[salon]
    for num in lista:
        if str(num)[0]=="3":
            print("Tu edificio esta alado del Oxxo")
            opci=input(("¿Gustas saber cual es el piso de tu salon? {S} {N} "))
            if opci=="S":
                if str(num)[1:3]=="00":
                    print("El piso donde se encuentra tu salon esta en la parte baja del edificio""\nSe encuentran las escaleras al final del pasillo sobre la misma zona donde se encuentra el elevador")
                    print("El ultimo numero que ingresaste es tu salon")
                elif str(num)[1:3]=="10":
                    print("El piso donde se encuentra tu salon esta en el piso entrando al edificio")
                    print("El ultimo numero que ingresaste es tu salon")
                elif str(num)[1]=="1":
                    print("El piso donde se encuentra tu salon esta en el piso entrando al edificio")
                    print("Los ultimos numeros que ingresaste es tu salon")
                elif str(num)[1:3]=="20":
                    print("El piso donde se encuentra tu salon esta en segundo piso,entrando al edificio de lado izquierdo estan las escaleras")
                    print("El ultimo numero que ingresaste es tu salon")
                elif str(num)[1]=="2":
                    print("El piso donde se encuentra tu salon esta en el segundo piso,entrando al edificio de lado izquierdo estan las escaleras ")
                    print("Los ultimos numeros que ingresaste es tu salon")
                elif str (num)[1:3]=="30":
                    print("El piso donde se encuentra tu salon esta en el tercer piso entrando al edificio de lado izquierdo estan las escaleras")
                    print("El ultimo numero que ingresaste es tu salon")
                elif str(num)[1]=="3":
                    print("El piso donde se encuentra tu salon esta en el tercer piso entrando al edificio de lado izquierdo estan las escaleras")
                    print("Los ultimos numeros que ingresaste es tu salon")
                else:
                    print("Dato no valido")
            else:
                print("Comprendo")        
        if str(num)[0]=="4":
            print("Tu edificio se encuentra donde esta la fuente y la TECstore")
            opcion=input("¿Gustas saber cual es el piso de tu salon? {S} {N} ")
            if opcion=="S":
                if str(num)[1:3]=="10":
                    print("El piso donde se encuentra tu salon esta en el piso entrando al edificio")
                    print("El ultimo numero que ingresaste es tu salon")
                elif str(num)[1]=="1":
                    print("El piso donde se encuentra tu salon esta en el piso entrando al edificio")
                    print("Los ultimos numeros que ingresaste es tu salon")
                elif str(num)[1:3]=="20":
                    print("El piso donde se encuentra tu salon esta en segundo piso,entrando al edificio de lado izquierdo estan las escaleras")
                    print("El ultimo numero que ingresaste es tu salon")
                elif str(num)[1]=="2":
                    print("El piso donde se encuentra tu salon esta en el segundo piso,entrando al edificio de lado izquierdo estan las escaleras ")
                    print("Los ultimos numeros que ingresaste es tu salon")
                elif str (num)[1:3]=="30":
                    print("El piso donde se encuentra tu salon esta en el tercer piso entrando al edificio de lado izquierdo estan las escaleras")
                    print("El ultimo numero que ingresaste es tu salon")
                elif str(num)[1]=="3":
                    print("El piso donde se encuentra tu salon esta en el tercer piso entrando al edificio de lado izquierdo estan las escaleras")
                    print("Los ultimos numeros que ingresaste es tu salon")                        
                else:
                    print("Dato invalido")
            else:
                print("Comprendo")
"""Conocer las diferentes actividades que puedes realizar dependiendo de tu horario 
"""
def conocer_actividades():
    print("Vas a colocar tu horario en 24hrs {17}")
    hora=int(input("Ingresa tu hora,para conocer las actividades que puedes realizar: "))
    actividades=["futbol","natacion","basquet","voleibol","tochito"]
    contador=0
    while hora>0 and hora <=24:
        if hora>=8 and hora<11:
            print(f"Las actividades: {actividades[0]},{actividades[1]} y {actividades[2]}")
        elif hora>=11 and hora<14:
            print(f"Las actividades: {actividades[0]} y {actividades[1]}")
        elif  hora>=18 and hora<20:
            print(f"La actividad: {actividades[4]}")
        else:
            print("Lo siento en tu horario no hay yactividades, espera un momento")    
        hora+=3
        contador+=1
        if hora>=24:
            hora=hora%24
        print("\nLa hora en la que se estaria acabando las actividades seria, ",hora)
        numero=input("\nQuieres saber cuantas veces buscas tus actividades?[si/no]").lower()
        if numero !="si":
            break    
    print(f"\nLas veces que se consultaron las actividades fueron {contador}")
def direcciones_texto():
    file=open("direccionesPeatonal_biblioteca","w+")
    lineas=["Saliendo de los torniquetes, dirigete a la alberca[estara de lado derecho],una vez ahi gira a la derecha y camina de forma recta"
          "\nestara donde haya un lugar lleno de ventanales,estara el lugar a la derecha :)"]
    file.writelines(lineas)
    file.seek(0)
    linea1=file.readline()
    linea2=file.readline()
    print(linea1)
    print(linea2)
    file.close()
    
def menu_lugares():
    print("\t ubicaTEC")
    print("¿Por cual entrada ingresaste o vas a ingresar?")
    print("1-Principal\n2-Peatonal\n3-Parque Tecnologico")
    print("Lugar a donde deseas ir")
    print("1-Biblioteca\n2-Estadio")
#Lo que hace el main es tomar en cuenta el primer valor por cual puerta vas a ingresar una vez con el dato va a comparar hasta donde vea a que lugar vas a querer ir
def main():
    while True:
        print("¿Que es lo que deseas hacer?""\n1-Dirigirse a un lugar""\n2-Encontrar tu salon""\n3-Conocer actividades")
        opcion_menu=int(input())
        if opcion_menu==1:
            menu_lugares()
            entrada=int(input("Entrada: "))
            lugar=int(input("Lugar: "))
            if entrada==1 and lugar==1:
                entradaPrincipal_biblioteca()
            elif entrada==2 and lugar==1:
                entradaPeatonal_biblioteca()
            elif entrada==3 and lugar==1:
                entradaParque_biblioteca()
            elif entrada==1 and lugar==2:
                entradaPrincipal_estadio()
            elif entrada==2 and lugar==2:
                entradaPeatonal_estadio()
            elif entrada==3 and lugar==2:
                entradaParque_estadio()
            else:
                print("Dato invalido")
        elif opcion_menu==2:
            print("\t ubicaATEC")
            print("Para ubicar el el edificio de tu salon")
            encontrar_salon()
        elif opcion_menu==3:
            print("\t ubicaTEC")
            conocer_actividades()
            
        else:
            print("Dato invalido")
            
main()
"""Casos de prueba si el usuario ingesa que entra desde la entrada principal (1) y se dirige a (1)
    se desplegara la funcion entradaPrincipal_biblioteca
"""
        
