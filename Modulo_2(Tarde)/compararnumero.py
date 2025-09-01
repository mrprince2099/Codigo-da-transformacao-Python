def qual_e_o_maior(num1, num2):
  """
  Compara dois números e mostra qual deles é o maior.
  """
  if num1 > num2:
    print(f"O número {num1} é maior.")
  elif num2 > num1:
    print(f"O número {num2} é maior.")
  else:
    print("Os dois números são iguais.")

# Pede os números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Chama a função para fazer a comparação
qual_e_o_maior(numero1, numero2)