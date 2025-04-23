#Ejercicio 7. Cálculo de propina según satisfacción
#• Ingresar monto total y nivel de satisfacción (buena/mala).
#• Si es buena, calcular 15% propina; si es mala, 5%.
#• Mostrar total a pagar.

monto_total = float(input("Ingrese el monto total: "))
satisfaccion = input("Ingrese el nivel de satisfacción como (buena/mala): ")
if satisfaccion == "buena":
    propina = monto_total * 0.15
elif satisfaccion == "mala":
    propina = monto_total * 0.05    
print ("El total a pagar es: ", monto_total + propina)