print("----CALCULO DEL AÑO ESTUDIANTIL----")
nombre=(input("Ingresa tu nombre completo: "))
institucion=(input("Ingresa el nombre de tu institucion: "))
ine=(input("Ingresa tu CC O TI: "))
año=(input("Ingresa el año a consultar: "))

print("¡¡hola!!😁", nombre, "soy un sistema de probabilidades que calcula tus notas de manera eficaz, porfavor ingresa tus notas en el apartado de aqui😊")

print("======INSTITUCION",institucion,"======")

num1=float(input("Ingresa la nota de ingles cuarto periodo: "))
print("NOTA:",num1)
num2=float(input("Ingresa la nota de quimica cuarto periodo: "))
print(("NOTA:",num2))
num3=float(input("Ingresa la nota de literatura cuarto periodo: "))
print("NOTA:",num3)
num4=float(input("Ingresa la nota de español cuarto periodo: "))
print("NOTA:",num4)
num5=float(input("Ingresa la nota de politica y economia cuarto periodo: "))
print("NOTA:",num5)
num6=float(input("Ingresa la nota de tecnologia cuarto periodo: "))
print("NOTA:",num6)
num7=float(input("Ingresa la nota de matematicas cuarto periodo: "))
print("NOTA:",num7)
num8=float(input("Ingresa la nota de religion cuarto periodo: "))
print("NOTA:",num8)
num9=float(input("Ingresa la nota de filosofia cuarto periodo: "))
print("NOTA:",num9)
num10=float(input("Ingresa la nota de fisica matematicas cuarto periodo: "))
print("NOTA:",num10)
num11=float(input("Ingresa la nota de biologia cuarto periodo: "))
print("NOTA:",num11)
num12=float(input("Ingresa la nota de educacion fisica cuarto periodo: "))
print("NOTA:",num12)
num13=float(input("Ingresa la nota de artistica cuarto periodo: "))
print("NOTA:",num13)
    

p1=float(input("Ingresa la nota de ingles primer periodo: "))
p2=float(input("Ingresa la nota de quimica primer periodo: "))
p3=float(input("Ingresa la nota de literatura primer periodo: "))
p4=float(input("Ingresa la nota de español primer periodo: "))
p5=float(input("Ingresa la nota de politica y economia primer periodo: "))
p6=float(input("Ingresa la nota de tecnologia primer periodo: "))
p7=float(input("Ingresa la nota de matematicas primer periodo: "))
p8=float(input("Ingresa la nota de religion primer periodo: "))
p9=float(input("Ingresa la nota de filosofia primer periodo: "))
p10=float(input("Ingresa la nota de fisica matematicas primer periodo: "))
p11=float(input("Ingresa la nota de biologia primer periodo: "))
p12=float(input("Ingresa la nota de educacion fisica primer periodo: "))
p13=float(input("Ingresa la nota de artistica primer periodo: "))

mm1=float(input("Ingresa la nota de ingles segundo periodo: "))
mm2=float(input("Ingresa la nota de quimica segundo periodo: "))
mm3=float(input("Ingresa la nota de literatura segundo periodo: "))
mm4=float(input("Ingresa la nota de español segundo periodo: "))
mm5=float(input("Ingresa la nota de politica y economia segundo periodo: "))
mm6=float(input("Ingresa la nota de tecnologia segundo periodo: "))
mm7=float(input("Ingresa la nota de matematicas segundo periodo: "))
mm8=float(input("Ingresa la nota de religion segundo periodo: "))
mm9=float(input("Ingresa la nota de filosofia segundo periodo: "))
mm10=float(input("Ingresa la nota de fisica matematicas segundo periodo: "))
mm11=float(input("Ingresa la nota de biologia segundo periodo: "))
mm12=float(input("Ingresa la nota de educacion fisica segundo periodo: "))
mm13=float(input("Ingresa la nota de artistica segundo periodo: "))


b1=float(input("Ingresa la nota de ingles tercer periodo: "))
b2=float(input("Ingresa la nota de quimica tercer periodo: "))
b3=float(input("Ingresa la nota de literatura tercer periodo: "))
b4=float(input("Ingresa la nota de español tercer periodo: "))
b5=float(input("Ingresa la nota de politica y economia tercer periodo: "))
b6=float(input("Ingresa la nota de tecnologia tercer periodo: "))
b7=float(input("Ingresa la nota de matematicas tercer periodo: "))
b8=float(input("Ingresa la nota de religion tercer periodo: "))
b9=float(input("Ingresa la nota de filosofia tercer periodo: "))
b10=float(input("Ingresa la nota de fisica matematicas tercer periodo: "))
b11=float(input("Ingresa la nota de biologia tercer periodo: "))
b12=float(input("Ingresa la nota de educacion fisica tercer periodo: "))
b13=float(input("Ingresa la nota de artistica tercer periodo: "))


print("====== ESTA ES TU FACTURA ANUAL DE TU ESTUDIO CUARTO PERIODO",año,"======")

suma1= num1+num2+num3+num4+num5+num6+num7+num8+num9+num10+num11+num12+num13
total1= suma1 / 13
prc1= (total1/5.0) * 100
porc1= round(prc1, 1)
prom1= round(total1, 1)

print(nombre,"identificado con numero: ", ine,"estudiante de ", institucion)
print("TU PROMEDIO FUE DE: ",prom1)
print("tu nota de periodo fue de:",prom1)
print(f"tu porcentaje fue de: {porc1}%")

print("====== ESTA ES TU FACTURA ANUAL DE TU ESTUDIO PRIMER PERIODO",año,"======")

suma2= p1+p2+p3+p4+p5+p6+p7+p8+p9+p10+p11+p12+p13
total2= suma2 / 13
prc2= (total2/5.0) * 100
porc2= round(prc2, 1)
prom2= round(total2, 1)

print(nombre,"Identificado con numero ", ine,"estudiante de",institucion)
print("TU PROMEDIO FUE DE:",prom2)
print("tu nota de periodo fue de:",prom2)
print(f"tu procentaje fue de:{porc2}%")

print("====== ESTA ES TU FACTURA ANUAL DE TU ESTUDIO SEGUNDO PERIODO",año,"======")

suma3= mm1+mm2+mm3+mm4+mm5+mm6+mm7+mm8+mm9+mm10+mm11+mm12+mm13
total3= suma3 / 13
prc3= (total3/5.0) * 100
porc3= round(prc3, 1)
prom3= round(total3, 1)

print(nombre,"Identificado con numero ", ine,"estudiante de",institucion)
print("TU PROMEDIO FUE DE:",prom3)
print("tu nota de periodo fue de:",prom3)
print(f"tu procentaje fue de:{porc3}%")

print("====== ESTA ES TU FACTURA ANUAL DE TU ESTUDIO TERCER PERIODO",año,"======")

suma4=b1+b2+b3+b4+b5+b6+b7+b8+b9+b10+b11+b12+b13
total4= suma4 / 13
prc4= (total4/5.0) * 100
porc4= round(prc4, 1)
prom4= round(total4, 1)

print(nombre,"Identificado con numero ", ine,"estudiante de",institucion)
print("TU PROMEDIO FUE DE:",prom4)
print("tu nota de periodo fue de:",prom4)
print(f"tu procentaje fue de:{porc4}%")

print("===== EN ESTE APARTADO DEBERAS LLENAR EL RESULTADO DE LA NOTA FINAL DE CADA PERIODO PARA SACAR UNA FACTURA ANUAL ESCOLAR =====")

fn1=float(input("Ingresa la nota del primer periodo: "))
fn2=float(input("Ingresa la nota del segundo periodo: "))
fn3=float(input("Ingresa la nota del tercer periodo: "))
fn4=float(input("ingresa la nota del cuarto periodo: "))

promfn= (fn1+fn2+fn3+fn4) / 4
prcfn= (promfn / 5.0) * 100
promfnreu= round(promfn, 1)
prcfnreu= round(prcfn, 1)

print(nombre,"tus notas finales son estas:")
print(f"TU PROMEDIO FINAL ES: {promfnreu}")
print(f"TU PORCENTAJE ES:{prcfnreu}%")

if prcfnreu >= 70:
    print("¡¡¡¡😍FELICIDADES GANASTE EL AÑO!!!!")
else:
    print("😭LO SIENTO MUCHO, PERDISTE EL AÑO. ")

