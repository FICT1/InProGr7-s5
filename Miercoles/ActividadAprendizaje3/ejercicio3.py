#Ejercicio#3: Cálculo de interés compuesto
#1. Ingresar el capital inicial
#2. Ingresar la tasa de interés anual (en porcentaje)
#3. Ingresar la cantidad de años
#4. Convertir la tasa porcentual a decimal
#5. Calcular el valor de (1 + tasa)^años
#6. Multiplicar ese resultado por el capital inicial
#7. Guardar el resultado como monto final
#8. Restar el capital inicial del monto final para obtener el interés ganado
#9. Mostrar el capital inicial, la tasa y los años
#10. Mostrar el monto final y el interés ganado
print("**Calculo de interés compuesto**")
capital_inicial = float(input("Ingrese el capital inicial: "))
tasa_interes = float(input("Ingrese la tasa de interés anual (en porcentaje%): "))
años = int(input("Ingrese la cantidad de años: "))
print("**********************************************************************")
tasa_decimal = tasa_interes / 100
factor= (1 + tasa_decimal) ** años
monto_final = capital_inicial * factor
interes_ganado = monto_final - capital_inicial
print ("El capital inicial es de: ", capital_inicial)
print ("La tasa de interés anual es de: ", tasa_interes, "%")
print ("La cantidad de años es de: ", años)
print ("El monto final es de: ", monto_final)
print ("El interés ganado es de: ", interes_ganado)
print("**********************************************************************")