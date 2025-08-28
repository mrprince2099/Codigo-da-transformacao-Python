def calculadora_simples():
  """
  Programa de calculadora que faz as 4 operações básicas.
  """
  try:
    # Pede os dois números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    # Pede a operação
    operacao = input("Escolha a operação (+, -, *, /): ")
    
    # Realiza a operação e exibe o resultado
    if operacao == '+':
      resultado = num1 + num2
      print(f"O resultado é: {resultado}")
    elif operacao == '-':
      resultado = num1 - num2
      print(f"O resultado é: {resultado}")
    elif operacao == '*':
      resultado = num1 * num2
      print(f"O resultado é: {resultado}")
    elif operacao == '/':
      # Verifica se o divisor não é zero
      if num2 == 0:
        print("Erro: Não é possível dividir por zero.")
      else:
        resultado = num1 / num2
        print(f"O resultado é: {resultado}")
    else:
      print("Operação inválida.")
      
  except ValueError:
    # Mensagem de erro se a entrada não for um número
    print("Entrada inválida. Por favor, digite apenas números.")

# Chama a função para rodar o programa
calculadora_simples()