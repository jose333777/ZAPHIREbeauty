def calcular_promedio(n1, n2, n3):
    return (n1 + n2 + n3) / 3


def mostrar_resultado(nombre, promedio):
    print("\n--- RESULTADO ---")
    print("Estudiante:", nombre)
    print("Promedio:", round(promedio, 2))

    if promedio >= 3.0:
        print("Estado: APROBÓ")
    else:
        print("Estado: REPROBÓ")


def main():
    print("SISTEMA DE NOTAS")

    nombre = input("Ingrese el nombre del estudiante: ")

    notas = []

    for i in range(3):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        notas.append(nota)

    promedio = calcular_promedio(
        notas[0],
        notas[1],
        notas[2]
    )

    mostrar_resultado(nombre, promedio)


main()



















saldo = 500000

def consultar_saldo():
    print(f"\nSu saldo actual es: ${saldo}")

def retirar_dinero(cantidad):
    global saldo

    if cantidad <= saldo:
        saldo -= cantidad
        print(f"\nRetiro exitoso. Nuevo saldo: ${saldo}")
    else:
        print("\nError: Fondos insuficientes.")

while True:
    print("\n===== CAJERO AUTOMÁTICO =====")
    print("1. Consultar Saldo")
    print("2. Retirar Dinero")
    print("3. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        consultar_saldo()

    elif opcion == 2:
        monto = float(input("Ingrese el monto a retirar: "))
        retirar_dinero(monto)

    elif opcion == 3:
        print("\nGracias por usar el cajero automático.")
        break

    else:
        print("\nOpción no válida. Intente nuevamente.")












