from repository.load_data import get_stock, get_next_id, set_next_id
from repository.search_product import search_product_by_name

from model.produto import Produto


def insert_product():
    print("\n--- CADASTRO DE NOVO PRODUTO ---")

    while True:
        nome = input("Nome do Produto (Ex: Cimento CPII 50kg): ").strip()

        produto_existente = search_product_by_name(nome)

        if produto_existente:
            print("🛑 ERRO: Já existe um produto com este nome!")
            print(f"Produto existente: ID {produto_existente['id']} - Estoque: {produto_existente['estoque']}")
            print("Tente um nome diferente ou utilize a Opção 2 para atualizar o estoque.")
            continue
        else:
            break

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

    current_id = get_next_id()

    new_product = Produto(
        id_produto=current_id,
        nome=nome,
        preco=preco,
        estoque=estoque_inicial
    )

    # novo_produto = {
    #     'id': current_id,
    #     'nome': nome,
    #     'preco': preco,
    #     'estoque': estoque_inicial
    # }
    get_stock().append(new_product)
    set_next_id(current_id + 1)
    print(f"\n✅ Produto '{new_product.nome}' cadastrado com sucesso! ID: {new_product.id}")
