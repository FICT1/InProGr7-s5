#Ejercicio#2: Control de inventario de un producto
#1. Ingresar la cantidad inicial en inventario
#2. Ingresar la cantidad de productos recibidos
#3. Ingresar la cantidad de productos vendidos
#4. Sumar los productos recibidos al inventario inicial
#5. Restar los productos vendidos del total anterior
#. Guardar el resultado como inventario actual
#7. Mostrar el inventario inicial
#8. Mostrar los productos recibidos y vendidos
#9. Mostrar el inventario final disponible

print ("**Control de inventario de un producto**")
inventario_inicial = int(input("Ingrese la cantidad inicial en inventario: "))
productos_recibidos = int(input("Ingrese la cantidad de productos recibidos: "))
productos_vendidos = int(input("Ingrese la cantidad de productos vendidos: "))
print ("**********************************************************************")

inventario_actual = inventario_inicial + productos_recibidos - productos_vendidos
print ("El inventario inicial es de: ", inventario_inicial)
print ("La cantidad de productos recibidos es de: ", productos_recibidos)
print ("La cantidad de productos vendidos es de: ", productos_vendidos)
print ("El inventario final disponible es de: ", inventario_actual)
print ("**********************************************************************")
print ("**Muchas gracias**")