#Menú de operaciones básicas
#Presenta un menú con las opciones: sumar, restar, multiplicar o dividir dos números. Elige la opción con un número y realiza la operación

print("**Menú de operaciones básicas**")
calculadora = int(input("Elija una opción (numeros):\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n-> "))
if calculadora == 1:
    print("*****************************************************")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 + num2
    print("La suma es:", resultado)
elif calculadora == 2:
    print("*****************************************************")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 - num2
    print("La resta es:", resultado)
elif calculadora == 3:
    print("*****************************************************")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 * num2
    print("La multiplicación es:", resultado)
elif calculadora == 4:
    print("*****************************************************")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    if num2 != 0:
        resultado = num1 / num2
        print("La división es:", resultado)
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Opción no válida. Por favor, elija una opción del 1 al 4.")
print("**Fin del programa**")
