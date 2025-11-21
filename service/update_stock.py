from presentation.print_product import print_product
from repository.search_product import search_product


def update_stock():
    print("\n--- ATUALIZAÇÃO DE ESTOQUE (ENTRADA) ---")

    while True:
        try:
            id_produto = int(input("Digite o ID do produto para atualizar o estoque: "))
            break
        except ValueError:
            print("ID inválido. Por favor, digite um número inteiro.")

    produto = search_product(id_produto)

    if produto:
        print_product(produto)
        while True:
            try:
                quantidade = int(input("Quantidade a ser adicionada ao estoque: "))
                if quantidade <= 0:
                    print("A quantidade deve ser positiva. Digite novamente.")
                    continue
                break
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

        produto['estoque'] += quantidade
        print(f"\nEstoque de '{produto['nome']}' atualizado. Novo estoque: {produto['estoque']}")
    else:
        print(f"Produto com ID {id_produto} não encontrado.")
