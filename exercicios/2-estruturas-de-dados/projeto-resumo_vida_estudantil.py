# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
Estudante ={ }
Estudante['nome'] = input("Qual o seu nome?")
Estudante['ano_linkedIn'] = int(input("Qual ano você conheceu o LinkedIn?"))
Estudante['ano_atual'] = int(input("Qual o ano atual?"))
cursos = input("Quais cursos você já fez?")

Estudante['cursos'] = cursos.split(', ')
# 2. Armazene esses dados em um dicionário

# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.
Total_anos = Estudante['ano_atual'] - Estudante['ano_linkedIn']
total_cursos = len(Estudante['cursos'])

print(f"Oi {Estudante['nome']}, desde {Estudante['ano_linkedIn']} você conhece o LinkedIn. Nesses {Total_anos} anos, você realizou {total_cursos} cursos, sendo o primeiro curso {Estudante['cursos'][0]} e o último curso {Estudante['cursos'][-1]}")