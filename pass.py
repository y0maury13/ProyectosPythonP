import random

minus="abcdefghijklmnñopqrstuvwxyz."
mayus=minus.upper()
numeros="0123456789"
simbolos="@$#%^^&*()_!~"
longitud=12
base=minus+mayus+numeros+simbolos
for _ in range(100):
    muestra=random.sample(minus,longitud)
    print(muestra)
    password="".join(muestra)
    print(password)

