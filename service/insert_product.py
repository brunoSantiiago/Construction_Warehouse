from repository.load_data import STOCK_PRODUCT


def insert_product():
    global PROXIMO_ID

    print("\n--- CADASTRO DE NOVO PRODUTO ---")
    nome = input("Nome do Produto (Ex: Cimento CPII 50kg): ").strip()

    while True:
        try:
            preco = float(input("Preço Unitário (R$): ").replace(',', '.'))
            if preco <= 0:
                print("O preço deve ser um valor positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite um número para o preço.")

    while True:
        try:
            estoque_inicial = int(input("Quantidade inicial em Estoque: "))
            if estoque_inicial < 0:
                print("A quantidade inicial não pode ser negativa.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro para o estoque.")

    novo_produto = {
        'id': PROXIMO_ID,
        'nome': nome,
        'preco': preco,
        'estoque': estoque_inicial
    }
    STOCK_PRODUCT.append(novo_produto)
    PROXIMO_ID += 1
    print(f"\nProduto '{nome}' cadastrado com sucesso! ID: {novo_produto['id']}")
