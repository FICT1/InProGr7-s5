#Tipo de triángulo
#Ingresa tres lados de un triángulo y determina si es equilátero, isósceles o escaleno.
#!= signfica desigualdad
# == significa igualdad

print("**Tipo de triángulo**")
lado1 = float(input("Ingrese el primer lado: "))
lado2 = float(input("Ingrese el segundo lado: "))
lado3 = float(input("Ingrese el tercer lado: "))
if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("Los lados deben ser mayores que cero.")
elif lado1 == lado2 and lado2 == lado3:
    print("El triángulo es equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triángulo es isósceles.")
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("El triángulo es escaleno.")
elif lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
    print("Los lados no forman un triángulo.")
else:
    print("Error en la clasificación del triángulo.")
