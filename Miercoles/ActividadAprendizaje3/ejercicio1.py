#Ejercicio#1: Cálculo de promedio de calificaciones
#1. Ingresar la primera calificación
#2. Ingresar la segunda calificación
#3. Ingresar la tercera calificación
#4. Sumar las tres calificaciones
#5. Dividir la suma entre 3
#6. Guardar el resultado como promedio
#7. Mostrar cada calificación ingresada
#8. Mostrar el promedio calculado
print("**********************************************************************")
prira_calificacion = float(input("Ingrese la primera calificación: "))
segda_calificacion = float(input("Ingrese la segunda calificación: ")) 
tera_calificacion = float(input("Ingrese la tercera calificación: "))
print("**********************************************************************")
suma_calificaciones = prira_calificacion + segda_calificacion + tera_calificacion
promedio = suma_calificaciones / 3

print("Tu promedio final es de: ", promedio)