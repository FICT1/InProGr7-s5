#Ejercicio#12. Detección de condiciones extremas en servidor
#• Ingresar temperatura y uso de CPU.
#• Si la temperatura > 80 °C o el CPU > 95%, iniciar protocolo de emergencia.

temperatura=int(input("Ingrese la temperatura del servidor: "))
uso_cpu=int(input("Ingrese el uso de CPU del servidor: "))
if temperatura>80 or uso_cpu>95:
    print("Iniciar protocolo de emergencia")
else:
    print("El servidor está en condiciones normales")
