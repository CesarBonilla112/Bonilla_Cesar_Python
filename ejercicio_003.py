#Inputs

contraseña_inicial = input("Crea tu contraseña ")
contraseña = input("Introduce tu contraseña ")
contraseña_correcta = contraseña_inicial
while contraseña != contraseña_correcta:
    print("Es incorrecto. Por favor introduce la contraseña correcta")
    contraseña = input("Introduce tu contraseña ")
    if contraseña == contraseña_correcta:
        break
