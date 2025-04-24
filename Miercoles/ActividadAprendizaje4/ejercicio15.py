#Ejercicio#15. Simulador de sistema de puntuación de conducta
#• Ingresar puntos (0 a 10).
#• Mostrar: “Excelente” si el número está entre 9 y 10, “Bueno” si el número está entre 7
#y 8, “Regular” si el número está entre 5 y 6, “Deficiente” si el número es < 5.
#• Si el valor es negativo o mayor a 10, mostrar error.

print ("**Simulador de sistema de puntuación de conducta**")
puntos = int(input("Ingrese puntos (0 a 10): "))
if puntos < 0 or puntos > 10:
    print ("Error: El valor ingresado es negativo o mayor a 10.")
else:
    if puntos >= 9 and puntos <= 10:
        print ("Excelente")
    elif puntos >= 7 and puntos <= 8:
        print ("Bueno")
    elif puntos >= 5 and puntos <= 6:
        print ("Regular")
    else:
        print ("Deficiente")