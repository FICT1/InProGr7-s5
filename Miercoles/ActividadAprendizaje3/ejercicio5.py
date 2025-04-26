#Ejercicio#5: Cálculo del consumo de agua por persona
#1. Ingresar el total de litros consumidos en un mes en una vivienda
#2. Ingresar la cantidad de personas que viven en la casa
#3. Dividir los litros totales entre la cantidad de personas
#4. Guardar el resultado como consumo mensual por persona
#5. Dividir el consumo mensual por 30 para obtener el consumo diario
#6. Guardar ese resultado como consumo diario por persona
#7. Mostrar el consumo total del mes
#8. Mostrar la cantidad de personas en la vivienda
#9. Mostrar el consumo mensual y diario por persona
print("**Cálculo del consumo de agua por persona**")
litros_consumidos = float(input("Ingrese el total de litros consumidos en un mes en la vivienda: "))
cantidad_personas = int(input("Ingrese la cantidad de personas que viven en la casa: "))
consumo_mensual_personas = litros_consumidos / cantidad_personas
consumo_diario_personas = consumo_mensual_personas / 30
print("**********************************************************************")
print(f"El consumo total del mes es de: {litros_consumidos} litros")
print(f"La cantidad de personas en la vivienda es de: {cantidad_personas}")
print(f"El consumo mensual por persona es de: {consumo_mensual_personas} litros")
print(f"El consumo diario por persona es de: {consumo_diario_personas} litros")
print("**********************************************************************")
print("**Muchas gracias**")
