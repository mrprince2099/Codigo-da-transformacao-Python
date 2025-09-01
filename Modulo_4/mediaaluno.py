def calcular_media(notas):
  """
  Calcula a média de uma lista de notas e determina a aprovação.
  """
  if not notas:
    print("Não há notas para calcular.")
    return

  media = sum(notas) / len(notas)
  print(f"A média do aluno é: {media:.2f}")

  if media >= 7:
    print("Aluno Aprovado!")
  else:
    print("Aluno Reprovado.")

# Exemplo de uso:
notas_aluno = [7.5, 7.0, 10.0]
calcular_media(notas_aluno)