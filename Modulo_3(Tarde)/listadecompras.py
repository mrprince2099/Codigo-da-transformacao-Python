lista_de_compras = []

while True:
    print("\n--- Gerenciador de Lista de Compras ---")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Visualizar lista")
    print("4. Sair")
    
    escolha = input("Digite a sua escolha (1-4): ")

    if escolha == '1':
        item = input("Digite o item a ser adicionado: ")
        lista_de_compras.append(item)
        print(f"'{item}' foi adicionado à lista.")
    
    elif escolha == '2':
        item = input("Digite o item a ser removido: ")
        if item in lista_de_compras:
            lista_de_compras.remove(item)
            print(f"'{item}' foi removido da lista.")
        else:
            print(f"'{item}' não está na lista.")

    elif escolha == '3':
        print("\nSua lista de compras:")
        if not lista_de_compras:
            print("A lista está vazia.")
        else:
            for item in lista_de_compras:
                print(f"- {item}")
    
    elif escolha == '4':
        print("Saindo do programa. Até mais!")
        break
    
    else:
        print("Escolha inválida. Por favor, tente novamente.")