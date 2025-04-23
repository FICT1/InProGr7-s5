#Ejercicio 2. Detectar si un usuario está inactivo por más de 30 días
#• Ingresar fecha de último inicio de sesión.
#• Calcular los días transcurridos.
#• Si son más de 30, mostrar “Cuenta inactiva”.
import datetime as dt
fecha_inicio_sesion=input("Ultimo dia de ingreso DD-MM-YYYY: ")
fecha_ingreso=dt.datetime.strptime(fecha_inicio_sesion, "%d-%m-%Y")
fecha_actual=dt.datetime.now()

contar = (fecha_actual - fecha_ingreso).days

print(contar)

if(contar > 30):

    print("Cuenta inactiva")
else:
    print("Estamos bien, porfavor ingrese")
