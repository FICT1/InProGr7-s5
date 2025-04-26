#Comparación de tres números
#Pide al usuario tres números y determina cuál es el mayor, el menor o si todos son iguales.

print("**Comparación de tres números**")
num1 = float(input(f"Ingrese el primer número:\n "))
num2 = float(input("Ingrese el segundo número:\n "))
num3 = float(input("Ingrese el tercer número:\n "))
if num1 == num2 and num2 == num3:
    print("Los tres números son iguales.")
elif num1 > num2 and num1 > num3:
    print("El número mayor es:", num1)
    if num2 < num3:
        print("El número menor es:", num2)
    else:
        print("El número menor es:", num3)
elif num2 > num1 and num2 > num3:
    print("El número mayor es:", num2)
    if num1 < num3:
        print("El número menor es:", num1)
    else:
        print("El número menor es:", num3)
elif num3 > num1 and num3 > num2:
    print("El número mayor es:", num3)
    if num1 < num2:
        print("El número menor es:", num1)
    else:
        print("El número menor es:", num2)
else:
    print("Error en la comparación de números.")