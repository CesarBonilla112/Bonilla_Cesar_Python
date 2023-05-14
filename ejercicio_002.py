#Inputs

nombre = input ("¿Cuál es tu nombre? ")
sexo = input ("¿Cuál es tu sexo? M o F ")
if (sexo == "F" and nombre.lower() < "m") or (sexo == "M" and nombre.lower() > "n"):
    grupo = "A"
    print("Te corresponde el grupo " + grupo)
else:
    grupo = "B"    
    print("Te corresponde el grupo " + grupo)
