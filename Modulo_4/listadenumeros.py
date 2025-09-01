def maior_menor(lista_numeros):
  """
  Recebe uma lista de números e retorna o maior e o menor valor.
  """
  if not lista_numeros:
    print("A lista está vazia.")
    return None, None
  
  maior = max(lista_numeros)
  menor = min(lista_numeros)
  
  return maior, menor

# Exemplo de uso:
numeros = [7, 60, 10, 89, 305, 129, 50, 17, 44, 2099]
maior, menor = maior_menor(numeros)

if maior is not None:
  print(f"O maior número é: {maior}")
  print(f"O menor número é: {menor}")