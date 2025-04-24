#Ejercicio#14. Categorización de edad
#• Ingresar edad.
#• Categorizar como: Niño (0–11), Adolescente (12–17), Adulto (18–64), Adulto mayor
#(65+)

print ("**Categorizacion de edad**")
edad = int(input("Ingrese su edad: "))
if edad >= 0 and edad <= 11:
    print("Niño")
elif edad >= 12 and edad <= 17:
    print("Adolescente")
elif edad >= 18 and edad <= 64:
    print("Adulto")
elif edad >= 65:
    print("Adulto mayor")
else:
    print("Edad no válida")
#