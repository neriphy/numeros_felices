#Programa para evaluar si un numero es feliz

numero_a_evaluar = input("Introduce el numero a evaluar: ")
n = numero_a_evaluar

suma = 2
primer_digito = 0
segundo_digito = 0
tercer_digito = 0
cuarto_digito = 0

while suma > 1:
    primer_digito = numero_a_evaluar[0]
    primer_digito = int(primer_digito)
    print(primer_digito)
    try:
        segundo_digito = numero_a_evaluar[1]
        segundo_digito = int(segundo_digito)
        print(segundo_digito)
    except IndexError as Numeromenorandigits:
        pass
    try:
        tercer_digito = numero_a_evaluar[2]
        tercer_digito = int(tercer_digito)
        print(tercer_digito)
    except IndexError as Numeromenorandigits:
        pass
    try:
        cuarto_digito = numero_a_evaluar[3]
        cuarto_digito = int(cuarto_digito)
        print(cuarto_digito)
    except IndexError as Numeromenorandigits:
        pass
    suma = primer_digito ** 2 + segundo_digito ** 2 + tercer_digito ** 2
    print (suma)
    numero_a_evaluar = suma
    numero_a_evaluar = str(numero_a_evaluar)

if suma == 1:
    print(n,"es un numero feliz")
