def verificar_idade(idade):
  """
  Verifica se a pessoa é maior de idade.
  """
  if idade >= 18:
    print("Você é maior de idade.")
  else:
    print("Você é menor de idade.")

# Pede a idade ao usuário
try:
  idade_digitada = int(input("Digite a sua idade: "))
  verificar_idade(idade_digitada)
except ValueError:
  print("Por favor, digite um número inteiro válido para a idade.")