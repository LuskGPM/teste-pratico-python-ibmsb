with open('teste6.txt') as arquivo:
    count = 0
    texto = arquivo.read()

    for l in texto:
        if l.isupper():
            count += 1

print(texto)
print(count)
