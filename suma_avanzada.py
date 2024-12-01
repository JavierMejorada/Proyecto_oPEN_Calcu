class SumaAvanzada:
    def sumamax(self, cantidad):
        
        numeros = []

        for i in range(1, cantidad + 1):
            try:
                numero = float(input(f"Ingrese el número {i}: "))  
                numeros.append(numero)
            except ValueError:
                print("Por favor ingresa un número válido.")

        suma_total = sum(numeros)  
        print(f"La suma total de los números ingresados es: {suma_total}")
