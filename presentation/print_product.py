def print_product(produto):
    if produto:

        print("-" * 30)
        print(f"ID: {produto.id}")
        print(f"Nome: {produto.nome}")
        print(f"Preço: R$ {produto.preco:.2f}")
        print(f"Estoque: {produto.estoque}")
        print("-" * 30)
    else:
        print("Produto não encontrado.")
