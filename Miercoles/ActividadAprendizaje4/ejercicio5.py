#Ejercicio 5. Verificar si un número es par y es positivo
#• Ingresar un número.
#• Si es mayor que 0, mostrar "El número es positivo".
#• Si es divisible por 2, mostrar “El número es par”
print ("****************************************************")
numero=int(input("Ingrese un número: "))
if (numero>0 and numero%2==0):
    print("El número es positivo y par")
else:
    print("No cumple con los parametros")

print ("****************************************************")