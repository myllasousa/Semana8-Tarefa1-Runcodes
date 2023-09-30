n1 = int(input(""))
n2 = int(input(""))
n3 = int(input(""))
n4 = int(input(""))
n5 = int(input(""))

def media():
    return (n1 + n2 + n3 + n4 + n5) / 5

resultado = media()
print(f'{resultado:.2f}')

numeros = [n1, n2, n3, n4, n5]
for n in numeros:
    if n > resultado:
        print(f'{n:.2f}')
