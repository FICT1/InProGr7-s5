#Ejercicio 8 Verificación de inicio de sesión
# Ingresar nombre de usuario y clave.
# Si el usuario es “admin” y la clave “1234admin”, permitir acceso.
# Si no, denegar.

nombre_usuario = input ("Ingrese el nombre de usuario: ")
clave = input("Ingrese su clave: ")
if nombre_usuario == "admin" and clave == "1234admin":
    print("**Acceso permitido**")
    print("Bienvenido al sistema")
else:
    print("Acceso denegado")
