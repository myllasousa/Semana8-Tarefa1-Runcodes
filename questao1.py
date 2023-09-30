dia = int(input(""))
mes = int(input(""))
ano = int(input(""))

nasc_dia = int(input(""))
nasc_mes = int(input(""))
nasc_ano = int(input(""))

def idade_atual():
    return ano - nasc_ano

idade = idade_atual()
if dia < nasc_dia or mes < nasc_mes:
    idade = idade - 1
print(idade)
