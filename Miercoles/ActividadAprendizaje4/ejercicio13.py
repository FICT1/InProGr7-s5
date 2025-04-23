#Ejercicio#13. Menú de operaciones bancarias
#• Ingresar un saldo inicial
#• Mostrar opciones: 1=Vaciar cuenta, 2=Depositar, 3=Retirar.
#• Realizar la acción correspondiente según la opción ingresada.
#• Mostrar nuevo saldo

print("*Bienvenido al sistema bancario Cordobas*")
saldo = float(input("Ingrese su saldo inicial en cordobas: "))
print("Seleccione una opción:")
print("1. Vaciar cuenta")
print("2. Depositar")
print("3. Retirar")
opcion = int(input("Ingrese su opción: "))
if opcion == 1:
    saldo = 0
    print("Su cuenta ha sido vaciada. Su nuevo saldo es:", saldo)
elif opcion == 2:
    deposito = float(input("Ingrese la cantidad a depositar: "))
    saldo += deposito
    print("Su nuevo saldo es:", saldo)
elif opcion == 3:
    retiro = float(input("Ingrese la cantidad a retirar: "))
    if retiro > saldo:
        print("No tiene suficiente saldo para retirar esa cantidad.")
    else:
        saldo -= retiro
        print("Su nuevo saldo es:", saldo)
else:
    print("Opción no válida. Por favor, seleccione una opción válida.")
