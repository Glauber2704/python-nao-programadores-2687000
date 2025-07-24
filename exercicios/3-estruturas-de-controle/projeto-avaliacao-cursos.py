# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning

cursos_linkedin = ['Riscos', 'Controles', 'Auditoria', 'GRC', 'Seguros']

curso_r = 'Riscos'
curso_p = 'Pyhton'
curso_c = 'Controles'

avaliações = {}

if curso_r in cursos_linkedin:
  print(f' O curso {curso_r} está no catalogo')
  avaliações[curso_r] = int(input('Quanl é a nota que você dá para esse curso (0 a 5)?'))
if curso_p in cursos_linkedin:
  print(f' O curso {curso_p} está no catalogo')
  avaliações[curso_p] = int(input('Quanl é a nota que você dá para esse curso (0 a 5)?'))
if curso_c in cursos_linkedin:
  print(f' O curso {curso_c} está no catalogo')
  avaliações[curso_c] = int(input('Quanl é a nota que você dá para esse curso (0 a 5)?'))
else:
  print(f'Infelizmente o curso não compôe o nosso catálogo')

print(avaliações)

# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
# 3. Crie um dicionário vazio para armazenar a nota do curso
# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota
