num = [1, 2, 5, 8, 9]

def somaLista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + somaLista(lista[1:])

print(f'Lista: {num}')
print('soma: ', somaLista(num))
