def area_circulo(radio):

    pi = 3.1415
    return pi*radio**2


def volumen_cilindro(radio, altura):

    return area_circulo(radio)*altura

print(volumen_cilindro(3,5))
