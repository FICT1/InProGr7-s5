#Escribe un programa que solicite al usuario su edad y determine si es un niño, adolescente, adulto o adulto mayor.
print("**Clasificación por edad**")
edad = int(input("Ingrese su edad: "))
if edad < 0:
    print("Edad no válida")
elif edad <= 12 and edad >= 0:
    print("Eres un niño")
elif edad <= 17 and edad >= 13:
    print("Eres un adolescente")
elif edad <= 64 and edad >= 18:
    print("Eres un adulto")
elif edad <= 130:
    print("Eres un adulto mayor")
else:
    print("Edad no válida")
