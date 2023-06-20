
import numpy
import os
import msvcrt
import time

lista_rut = []
lista_asiento = [[2,2,2],
                 [4,4,4],
                 [6,6,6]]



def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion in(1,2,3,4,5,6):
                return opcion
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_rut():
    while True:
        try:
            rut = int(input("ingrese su rut (sin digito verificador y sin puntos)"))
            if rut >=1000000 and rut <= 9999999:
              return rut
            else:
                print("DEBE INGRESAR EL RUT ENTRE 1000000 Y 99999999")
        except:
            print("DEBE INGRESAR UN NUMERO ENTERO")
    
def validar_nombre():
    while True:
        nombre = input("ingrese su nombre")
        if len(nombre.strip)>=3:
            return nombre
        else:
            print("DEBE INGRESAR UN NOMBRE QUE TENGA AL MENOS 3 LETRAS")

def validar_correo():
    while True:
            correo = input("Ingrese correo: ")
            if "@" in correo:
                break
            else:
                print("ERROR! correo incorrecto!")

def validar_persona():
    while True:
        try:
            persona = int(input("ingrese cuanta persona quiera ir al restaraunt"))
            if persona >=1 and rut <= 7:
              return persona
            else:
                print("DEBE INGRESAR PERSONA ENTRE 1 Y 7")
        except:
            print("DEBE INGRESAR UN NUMERO ENTERO")
while True:
    print("""
    1 ver restaraunt
    2 reserva mesa
    3 carta
    4 pagar
    5 cancelar 
    6 salir
    """)
    
    opcion = validar_opcion()
    if opcion==1:
      print("el numero de asiento de cada mesa")
      arreglo = numpy.array(lista_asiento)
      print(arreglo)
    elif opcion==2:
      print("reserva mesa")
      rut = lista_rut.append (validar_rut())
      print(lista_rut)
      validar_nombre()
      validar_correo()
      validar_persona()
    


    elif opcion==3:
        pass
    elif opcion==4:
        pass
    elif opcion==5:
        pass
    else:
        break
