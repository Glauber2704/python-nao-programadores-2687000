# Crie uma lista apenas com elementos numéricos
lista = []
numerica = [1,1,2,3,4,5]
mista = ['pyhton', 5,7,8,[1,3,4,]]
print(len(numerica))
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora

# Imprima na tela apenas os 5 primeiros elementos da lista
print(mista[0:3])
# Crie um slice na lista para que imprima na tela os elementos de índice par

# Remova da lista o último item

# Insira na lista um novo item
mista.append('gool')
print(mista)
# Remova da lista um item específico
mista.extend(numerica)
print(len(mista))
print(mista)
mista[0] = "oi"
print(mista)
mista.remove(7)
print(mista)
mista.pop()
print(mista[0:-1:2])

