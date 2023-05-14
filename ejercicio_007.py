def numero_de_palabras(frase):

    return {palabra:len(palabra) for palabra in frase.split()}

print(numero_de_palabras('Hola Mundo'))
