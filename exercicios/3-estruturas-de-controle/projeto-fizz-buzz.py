# Criaremos um programa para substituir números por palavras em uma lista
# 1. Crie uma lista com 15 números
lista_números = list(range(15,31))
indice = 0
print(lista_números)

for número in lista_números:
  if número % 3 == 0 and número % 5 ==0:
    lista_números[indice] = 'FizzBuzz'
  elif número % 3 == 0:
    lista_números[indice] = 'Fizz'
  elif número % 5 == 0:
    lista_números[indice] = 'Buzz'
  else:
    lista_números[indice] = número
  indice += 1
print(lista_números)

# 2. Crie um for loop para percorrer todos os elementos da lista
# 3. Crie uma estrutura condicional para verificar cada número da lista:
# 3.1 Caso o número seja divisível por 3, substitua-o por "Fizz"
# 3.2 Caso o número seja divisível por 5, substitua-o por "Buzz"
# 3.3 Caso o número seja divisível por 3 e 5, substitua-o por "FizzBuzz"

