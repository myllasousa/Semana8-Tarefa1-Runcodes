peso = float(input(""))
altura = float(input(""))

def calcular_imc():
    return peso / (altura)**2

imc = calcular_imc()
print(f'{imc:.2f}')

def classificacao():
    if imc < 18.5:
        print("Abaixo do peso")
    elif 18.6 <= imc <= 25.0:
        print("Peso normal")
    elif 26.0 <= imc <= 30.0:
        print("Sobrepeso")
    elif 31.0 <= imc <= 35.0:
        print("Obeso leve")
    elif 36.0 <= imc <= 40.0:
        print("Obeso moderado")
    else:
        print("Obeso mórbido")

classificacao()

