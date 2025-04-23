#Ejercicio 9. Encontrar el mayor de tres números
# Ingresar el primer número
# Ingresar el segundo númer
# Ingresar el tercer número
# Si el primero es mayor o igual que el segundo, comparar el primero con el tercero
# Si el primero es menor que el segundo, compara el segundo con el tercero
# Si los tres son iguales, mostrar “Los números son iguales”
print ("***************************************")
print ("Encontrar el mayor de tres numeros")
numero1=int(input("Ingresa el primer numero -> "))
numero2=int(input("Ingresa el segundo numero -> "))
numero3=int(input("Ingresa el tercer numero -> "))

if numero1==numero2 and numero2==numero3:
    print("Los numeros son iguales")
elif numero1>=numero2:
    if numero1>=numero3:
        print("El mayor es el primer numero -> ",numero1)
    else:
        print("El mayor es el tercer numero -> ",numero3)
else:
    if numero2>=numero3:
        print("El mayor es el segundo numero -> ",numero2)
    else:
        print("El mayor es el tercer numero -> ",numero3)
print ("***************************************")