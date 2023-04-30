# Constantes
AÑO_ACTUAL = 2023
from datetime import date

# Inputs
nombre = input("¿Cuál es tu nombre? ")
primer_apellido = input("¿Cuál es tu primer apellido? ")
segundo_apellido = input("¿Cuál es tu segundo apellido? ")
año_de_nacimiento = int(input("¿En qué año naciste? "))
fecha_de_nacimiento = input("¿En qué mes y día naciste? ")

mes_de_nacimiento, dia_de_nacimeinto = map(int, fecha_de_nacimiento.split("-"))
fecha_de_nacimiento = date(año_de_nacimiento, mes_de_nacimiento, dia_de_nacimeinto)

hoy = date.today()
edad = AÑO_ACTUAL-fecha_de_nacimiento.year - ((hoy.month,hoy.day) < (fecha_de_nacimiento.month,fecha_de_nacimiento.day))



print ("Este es tu nombre completo en mayusculas:", (nombre+ " "+ primer_apellido+" "+segundo_apellido).upper())
print ("Este es tu nombre completo en minusculas:", (nombre+ " "+ primer_apellido+" "+segundo_apellido).lower())
print ("Esta es tu fecha de nacimiento:", fecha_de_nacimiento.strftime("%d-%m-%Y"))
print ("Este es tu edad:", edad)
print ("Tu nombre completo tiene:",sum(1 for letra in (nombre + primer_apellido + segundo_apellido) if letra in "AEIOUaeiou"), "vocales")
print ("Tu nombre completo tiene:",len(nombre + primer_apellido + segundo_apellido), "letras")
print ("Tu edad es un carácter de tipo número:", isinstance (edad, int))
print ("¿Tu nombre completo es un carácter de tipo alfanumérico?:", (nombre + primer_apellido + segundo_apellido).isalnum())
print ("Tu edad en 10 años será:", edad + 10)
print ("La media de tu edad actual y tu edad en 20 años es:", (edad + (edad+20)) / 2)
