from sumar import sumatoria
from restar import restar
from dividir import dividir
from multiplicacion import multiplicacion
from suma_avanzada import SumaAvanzada

while True:
    try:
        print("\nProyecto de calculadora:")
        print("Menú de opciones:")
        print("1.- SUMAR")
        print("2.- RESTAR")
        print("3.- DIVIDIR")
        print("4.- MULTIPLICACIÓN")
        print("5.- SUMA AVANZADA")
        print("6.- SALIR")
        
        opcion = int(input("Seleccione la opción que desee: "))
        
        if opcion == 1:
            print("Has seleccionado la opción SUMA.")
            a = int(input("Ingresa el primer término de la suma: "))
            b = int(input("Ingresa el segundo término de la suma: "))
            sumatoria_obj = sumatoria()
            print("El resultado es:", sumatoria_obj.sumar(a, b))
        
        elif opcion == 2:
            print("Seleccionaste la opción RESTA.")
            a = int(input("Ingresa el primer término de la resta: "))
            b = int(input("Ingresa el segundo término de la resta: "))
            resta_obj = restar()
            print("El resultado de la resta es:", resta_obj.restar(a, b))
        
        elif opcion == 3:
            print("Seleccionaste la opción DIVISIÓN.")
            a = float(input("Ingresa el numerador de tu operación: "))
            b = float(input("Ingresa el denominador de tu operación: "))
            dividir_obj = dividir()
            print("El resultado de tu división es:", dividir_obj.dividir(a, b))
        
        elif opcion == 4:
            print("Seleccionaste la opción MULTIPLICACIÓN.")
            a = int(input("Ingresa el primer número de tu multiplicación: "))
            b = int(input("Ingresa el segundo número de tu multiplicación: "))
            multiplicacion_obj = multiplicacion()
            print("El resultado de tu multiplicación es:", multiplicacion_obj.multiplicacion(a, b))
        
        elif opcion == 5:
            print("Has ingresado a suma avanzada.")
            cantidad = int(input("Ingrese la cantidad de números que va a sumar: "))
            suma_avanzada_obj = SumaAvanzada()
            suma_avanzada_obj.sumamax(cantidad)
        
        elif opcion == 6:
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 6.")
    
    except ValueError:
        print("Error: Debes ingresar un número válido.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
