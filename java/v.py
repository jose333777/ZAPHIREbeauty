#ASIGNACION
print("Esto es una suma")
ff=int(input(print("ingresa un dato")))
jj=int(input(print("ingresa un segundo dato")))
sm= ff+jj
print("el resultado es: ", sm)
#BUSQUEDA
posdata="Hola nueva york"
print(posdata)
buscar_subcadena=posdata.find("hola nueva york")
print(buscar_subcadena)
#EXTRAER
kenia="ananae ananae"
extraer_subcadena=kenia[1,0]
print(extraer_subcadena)
#UNIR o CONCATENACION
bnm001="bailar"
bnm002="contigo"
guaracha=bnm001 +""+ bnm002
#COMPARACION
print("comparacion")
mensaje1="hola"
mensaje2="hola"
mensaje1==mensaje2
#TALLER-------------------NRO5------------------
#ASIGNACIONES DE VARIABLES 1
p1=int(input(print("ingresa un valor entero: ")))
p2=float(input(print("ingresa un valor flotante: ")))
solution=str(p1 * p2)
print("la solucion es: ", solution)
#ASIGNACION DE VARIABLES 2
Name1=input(print("Ingresa tu primer nombre: "))
Name2=input(print("Ingresa tu segundo nombre: "))
Name3=input(print("Ingresa tu primer apellido: "))
Name4=input(print("Ingresa tu segundo apellido: "))
NombreCompleto= Name1 + Name2 + Name3 + Name4
print("Tu nombre completo es: ", NombreCompleto)
#BUSQUEDA DE INFORMACION 1
posdata=input(print("Ingresa un Texto para encontrar la palabra: "))
Ing=input(print("Ingresa la palabra a buscar: "))
print(posdata)
buscar_subcadena=posdata.find(Ing)
print("se encontró", buscar_subcadena)
#BUSQUEDA DE INFORMACION 2
mone=input(print("Ingresa un nombre "))
mune=input(print("ingresa la lista de nombres "))
BuscarLista=mune.find(mone)
print("se encontro",BuscarLista)
#EXTRAER INFORMACION 1  
kenia="ananae ananae"
extraer_subcadena=kenia[1,1]
print(extraer_subcadena)
#EXTRAER INFORMACION 2
dismiss=input(print("ingresa la palabra que quieres extraer la quinta letra"))
extraer_cadena=kenia[1,5]
print(extraer_cadena)
#UNIR O CONCATENAR 1
bnm001="bailar"
bnm002="contigo"
guaracha=bnm001 +""+ bnm002
print("la union es ", guaracha)
#UNIR O CONCATENAR 2
bmw=input(print("Ingresa una palabra 1 a unir: "))
bmvv=input(print("Ingresa una palabra 2 a unir: "))
unicion= bmw+bmvv
print("la union es: ", unicion)
#COMPARACION 1
mensaje1=input(print("ingresa el nombre permitido"))
mensaje2="Jose"
comparacion=mensaje1==mensaje2
print("el nombre es", comparacion)
#COMPARACION 2
print("comparacion de edad")
edad1="18"
edad2="19"
edad1==edad2
