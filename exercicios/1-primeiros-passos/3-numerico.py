data_nascimento = '05-10-1976'
idade_numerica = 46
altura = 1.74

# Descubra o tipo de dado de cada variável acima
tipo_data_nascimento = type(data_nascimento)
tipo_idade_numerica = type(idade_numerica)
tipo_altura = type(altura)

print(tipo_data_nascimento)
print(tipo_idade_numerica)
print(tipo_altura)

print(idade_numerica)
# Realize uma operação entre dados do tipo string e inteiro
soma = altura + idade_numerica
decimal = 30/8
print(soma)
print(int(decimal))
# Realize uma operação entre dados do tipo inteiro e float
print(f'Hoje eu estudei python por {1+10} horas.')