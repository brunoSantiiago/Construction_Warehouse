from repository.load_data import get_stock, get_next_id, set_next_id
# Removida a importação de search_product_by_name, pois não é mais usada.
from model.produto import Produto


def insert_product():
    print("\n--- CADASTRO DE NOVO PRODUTO ---")

    # 1. Entrada de Nome (Sem verificação de duplicidade)
    nome = input("Nome do Produto (Ex: Cimento CPII 50kg): ").strip()

    # 2. Entrada e Validação de Preço
    while True:
        try:
            preco = float(input("Preço Unitário (R$): ").replace(',', '.'))
            if preco <= 0:
                print("O preço deve ser um valor positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite um número para o preço.")

    # 3. Entrada e Validação de Estoque Inicial
    while True:
        try:
            estoque_inicial = int(input("Quantidade inicial em Estoque: "))
            if estoque_inicial < 0:
                print("A quantidade inicial não pode ser negativa.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro para o estoque.")

    # 4. Criação e Inserção do Objeto Produto
    current_id = get_next_id()

    new_product = Produto(
        id_produto=current_id,
        nome=nome,
        preco=preco,
        estoque=estoque_inicial
    )

    get_stock().append(new_product)
    set_next_id(current_id + 1)
    print(f"\n✅ Produto '{new_product.nome}' cadastrado com sucesso! ID: {new_product.id}")