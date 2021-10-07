def crear_lista():
    lista_pacientes = []
    return lista_pacientes

def validar_edad(edad):
    while True:
        if edad < 17:
            break



def alta(l = crear_lista()):
    a = int(input("Desea dar de alta un paciente? 0 = Si / 1 = no"))
    while a == 0:
        dni = input("Ingrese su DNI por favor.")
        nombre = input("Ingrese su nombre por favor.")
        edad = int(input("Cual es su edad"))
        validar_edad(edad)
        l.append(dni,nombre,edad)