"""Lee el fichero "Challenge22.txt" incluido en el proyecto, calcula su
 * resultado e imprímelo.
 * - El .txt se corresponde con las entradas de una calculadora.
 * - Cada línea tendrá un número o una operación representada por un
 *   símbolo (alternando ambos).
 * - Soporta números enteros y decimales.
 * - Soporta las operaciones suma "+", resta "-", multiplicación "*"
 *   y división "/".
 * - El resultado se muestra al finalizar la lectura de la última
 *   línea (si el .txt es correcto).
 * - Si el formato del .txt no es correcto, se indicará que no se han
 *   podido resolver las operaciones."""
 
def calcular_resultado(archivo):
    try:
        with open(archivo, 'r') as f:
            lineas = f.read().splitlines()

        # Validar formato del archivo (debe alternar números y operadores)
        if len(lineas) % 2 == 0:
            print("Formato del archivo incorrecto: no alterna números y operadores correctamente.")
            return

        # Inicializar el resultado con el primer número
        resultado = float(lineas[0])

        # Recorrer las líneas alternando operador y número
        for i in range(1, len(lineas), 2):
            operador = lineas[i]
            try:
                numero = float(lineas[i + 1])
            except ValueError:
                print("Formato del archivo incorrecto: no se puede convertir a número.")
                return

            # Realizar la operación según el operador
            if operador == '+':
                resultado += numero
            elif operador == '-':
                resultado -= numero
            elif operador == '*':
                resultado *= numero
            elif operador == '/':
                if numero == 0:
                    print("Error: división por cero.")
                    return
                resultado /= numero
            else:
                print(f"Operador desconocido: {operador}")
                return

        print(f"El resultado es: {resultado}")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo}'.")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

# Llamada a la función
calcular_resultado("/Users/aitor/Portfolio/Retos de programación/aux/Challenge22.txt")
