dia1 = int(input(""))
mes1 = int(input(""))
ano1 = int(input(""))

dia2 = int(input(""))
mes2 = int(input(""))
ano2 = int(input(""))

def data_recente():
    if dia2 < dia1 or mes2 < mes1 or ano2 < ano1:
        print(f'{dia1}/{mes1}/{ano1}')
    else:
        print(f'{dia2}/{mes2}/{ano2}')
data_recente()
