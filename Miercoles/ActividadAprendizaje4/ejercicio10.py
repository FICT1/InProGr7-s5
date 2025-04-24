#Ejercicio 10. Verificación de validez de una fecha
#• Ingresar día, mes, y año.
#• Si el mes es febrero y el día > 29, mostrar error.
#• Si el mes es abril, junio, septiembre o noviembre y el día > 30, mostrar error
#• Si el mes es enero, marzo, mayo, julio, agosto, octubre, diciembre y el día > 31,
# mostrar error


dia=int(input("Ingrese el día DD: "))
mes=int(input("Ingrese el mes MM: "))
año=int(input("Ingrese el año AAAA: "))
if mes==2 and dia>29:
    print("Error: Febrero no tiene más de 29 días.")
elif mes in [4, 6, 9, 11] and dia>30:
    print("Error: El mes ingresado no tiene más de 30 días.")
elif mes in [1, 3, 5, 7, 8, 10, 12] and dia>31:
    print("Error: El mes ingresado no tiene más de 31 días.")
else:
    print("La fecha es válida.") 