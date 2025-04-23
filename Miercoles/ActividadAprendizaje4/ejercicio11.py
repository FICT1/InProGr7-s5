#Ejercicio#11. Determinar si hay saldo suficiente para una compra
#• Ingresar precio del producto y saldo disponible.
#• Si el saldo alcanza, permitir la compra.
#• Si no, mostrar “Saldo insuficiente”.
precio_producto = float(input("Ingrese el precio del producto en cordobas: "))
saldo_disponible = float(input("Ingrese el saldo disponible em cordobas: "))
if saldo_disponible >= precio_producto:
    print("Compra permitida")
else:
    print("Saldo insuficiente")


