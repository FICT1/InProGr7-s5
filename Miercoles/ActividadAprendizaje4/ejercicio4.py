#Ejercicio#4. Validar edad mínima para votar
#• Ingresar la edad de una persona.
#$• Si la edad es mayor o igual a 18, mostrar "Puede votar".

edad=int(input("Ingrese su edad: "))
if edad >= 18:
    print("Puede votar")
else:
    print("No puede votar")