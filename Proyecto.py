import pandas as pd
import time

# Función para simular un parcial
def simular_parcial(numero_parcial):
    # Cargar preguntas desde CSV
    preguntas = pd.read_csv(f'parcial{numero_parcial}.csv')
    
    # Ejecucion de parcial y calculo de nota
    nota = 0
    for i, pregunta in preguntas.iterrows():
        respuesta = input(f"Pregunta {i+1}: {pregunta['Pregunta']}")
        if respuesta == pregunta['Respuesta']:
            nota += 1
        else:
            print(f"Respuesta incorrecta. La respuesta correcta es: {pregunta['Respuesta']}")
            print(f"Solución: {pregunta['Solución']}")
    
    print(f"Nota: {nota}/{len(preguntas)}")

# Resumen toerico
def resumen_teorico(numero_parcial):
    # Mostrar información teórica del parcial seleccionado
    print("Resumen Teórico Parcial", numero_parcial)

# Resumen de ecuaciones
def resumen_ecuaciones(numero_parcial):
    # Mostrar ecuaciones importantes del parcial seleccionado
    print("Resumen de Ecuaciones Parcial", numero_parcial)

# Practica con Comodin
def practica(numero_parcial):
    # Lógica para realizar la práctica con comodín
    print("Practica Parcial", numero_parcial)

# Menú principal
while True:
    print("Menú:")
    print("1. Simular Parcial")
    print("2. Resumen Teórico")
    print("3. Resumen de Ecuaciones")
    print("4. Práctica")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        num_parcial = input("Seleccione el número de parcial (1, 2 o 3): ")
        simular_parcial(num_parcial)
    elif opcion == "2":
        num_parcial = input("Seleccione el número de parcial (1, 2 o 3): ")
        resumen_teorico(num_parcial)
    elif opcion == "3":
        num_parcial = input("Seleccione el número de parcial (1, 2 o 3): ")
        resumen_ecuaciones(num_parcial)
    elif opcion == "4":
        num_parcial = input("Seleccione el número de parcial (1, 2 o 3): ")
        practica(num_parcial)
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")