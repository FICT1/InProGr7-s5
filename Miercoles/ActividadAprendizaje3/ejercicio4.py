#Ejercicio#4: Cálculo del consumo de combustible
#1. Ingresar la distancia recorrida en kilómetros
#2. Ingresar la cantidad de litros consumidos
#3. Dividir la distancia entre los litros
#4. Guardar el resultado como rendimiento (km/l)
#5. Multiplicar los litros por el precio por litro (definirlo)
#7. Mostrar la distancia, litros y precio por litro
#8. Mostrar el rendimiento del vehículo
#9. Mostrar el gasto total en combustible

print("**Cálculo del consumo de combustible**")
distancia_recorrida = float(input("Ingrese la distancia recorrida en kilómetros: "))
litros_consumidos = float(input("Ingrese la cantidad de litros consumidos: "))
rendimiento = distancia_recorrida / litros_consumidos
precio_por_litro = 1.34 #Segun google  
gasto_total = litros_consumidos * precio_por_litro
print("**********************************************************************")
print(f"La distancia recorrida es de: {distancia_recorrida}km") 
print(f"La cantidad de litros consumidos es de:{litros_consumidos} ")
print(f"El precio por litro es de: $", precio_por_litro)
print(f"El rendimiento del vehículo es de: ", rendimiento, "km/l")
print(f"El gasto total en combustible es de: {gasto_total}$")
print("**********************************************************************")