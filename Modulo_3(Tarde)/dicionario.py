# Criando o dicionário com os dados do aluno
# 36
aluno = {
    'nome': 'Fabrício Araújo da Silva',
    'idade': 17,
    'serie': '3º ano do Ensino Médio',
    'notas': [10.0, 9.0, 8.5, 9.5]
}

# Exibindo os dados do dicionário
print("--- Dados do Aluno ---")
print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno['idade']} anos")
print(f"Série: {aluno['serie']}")
print(f"Notas: {aluno['notas']}")

# Exemplo de como acessar uma nota específica
print(f"Nota na 1ª prova: {aluno['notas'][0]}")
print(f"Nota na 2ª prova: {aluno['notas'][1]}")
print(f"Nota na 3ª prova: {aluno['notas'][2]}")
print(f"Nota na 4ª prova: {aluno['notas'][3]}")