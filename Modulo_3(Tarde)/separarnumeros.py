# Conjunto de números a ser verificado
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Listas para armazenar os números pares e ímpares
numeros_pares = []
numeros_impares = []

# Usando um loop para percorrer a lista
for num in numeros:
    # O operador % (módulo) retorna o resto da divisão.
    # Se o resto da divisão por 2 for 0, o número é par.
    if num % 2 == 0:
        numeros_pares.append(num)
    else:
        numeros_impares.append(num)

# Exibindo os resultados
print("--- Verificação de Pares e Ímpares ---")
print(f"Números originais: {numeros}")
print(f"Números pares: {numeros_pares}")
print(f"Números ímpares: {numeros_impares}")