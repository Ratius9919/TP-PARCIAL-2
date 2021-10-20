import os

def clear():
    os.system("cls")



    

def crear_archivo(lista):
    try:
        with open("turnos.txt","a") as turnos:
            turnos.write(f"{lista}\n")
    except:
        turnos = open("turnos.txt","a")
        turnos.write(f"{lista}")


def crear_lista():
    turnos = [[[]]]
    return turnos




def crear_dni():
    valor = False
    while valor == False:
        try:
            dni = input("Por favor, ingrese su DNI."+" ")
            if int(dni) > 1000000 and int(dni) < 200000000:
                valor = True
        except ValueError:
            print("Ingresaste un valor no valido.")
    return dni




def verificar_mes(valor):
    
    error = True
    while error:
        valor_int = int(valor)
        
        if valor_int >= 1 and valor_int <= 12  :
            error = False
        else:
            valor =input("Recuerde que los meses tienen 2 valores numericos y como maximo llegan al 12./ EJ: MES 06"+" ")

def crear_dia():
    valor = False
    while valor == False:
        try:
            dia = input("Por favor, ingrese el dia del turno."+" ")
            if int(dia) < 32 and int(dia) > 0:
                valor = True
        except ValueError:
            print("Ingresaste un valor no valido.")
    
    return dia

def verificar_minutos(valor):
    
    error = True
    while error == True:
        valor_int = int(valor)
        largo = len(valor)
        numero = valor.isalnum
        print(numero,valor_int)
        if largo == 2 and numero == True and valor_int <= 60 and valor_int >= 0:
            error == False
        else:
            valor = input("Recuerde que los MINUTOS tienen 2 valores numericos y como maximo llegan al 60.//EJ: MIN = 05 "+" ")

def crear_hora():
    valor = False
    while valor == False:
        try:
            hora = input("Por favor, ingrese la hora del turno. Sin los minutos, solo la hora"+" ")
            if int(hora) < 25 and int(hora) > 0:
                valor = True
        except ValueError:
            print("Ingresaste un valor no valido.")
    
    return hora

def agregar_datos(dato1,dato2,dato3,lista):
    largo = len(lista)-1
    largo2 = len(lista[largo])-1
    lista.append(dato1)
    lista[largo][largo].append(dato2)
    lista[largo].append(dato3)
    return lista

def crear_mes():
    valor = False
    while valor == False:
        try:
            mes = input("Por favor, ingrese el mes del turno."+" ")
            if int(mes) < 13 and int(mes) > 0:
                valor = True
        except ValueError:
            print("Ingresaste un valor no valido.")
    
    return mes

def opcion_minutos():
    clear()
    print("Por favor, solicite cual bloque desea solicitar")
    print("A = Turno desde el minuto 00 hasta el 30.")
    print("B = Turno desde el minuto 30 hasta el 00, de la siguiente hora.")
    turno = input("Cual bloque elige, el A o el B"+" ")
    while turno != "A" and turno != "B":
        turno = input("Cual bloque elige, el A o el B"+" ")
    if turno == "A":
        valor = "00"
    elif turno == "B":
        valor = "30"
    
    return valor
             

def __main__(): 
    #Se crean tres listas, una dentro de la otra. La primera lista almacena el DNI,
    #La segunda almacena la fecha
    #y la tercera almacena la hora del turno
    clear()
    dni = crear_dni()
    #verificar_dni(dni)
    clear()
    año = input("Por favor, ingrese el año del turno."+" ")
    clear()
    mes = crear_mes()
    clear()
    dia = crear_dia()
    clear()
    hora = crear_hora()
   
    clear()
    minutos = opcion_minutos()
    #verificar_minutos(minutos)
    clear()
    listado = crear_lista()
    fecha = dia+"/"+mes+"/"+año
    hora_minutos = hora + ":" + minutos
    agregar_datos(hora_minutos,dni,fecha,listado)
    lista_str = str(listado)
    lista_str = lista_str.replace("["," ")
    lista_str = lista_str.replace("]"," ")
    lista_str = lista_str.replace("'"," ")
    lista_str = lista_str.replace(","," ")
    print(lista_str)
    crear_archivo(lista_str)
    


__main__()


