from presentation.print_product import print_product
from repository.search_product import search_product


def edit_product():
    print("\n--- EDITAR PRODUTO ---")

    try:
        id_product = int(input("Digite o ID do produto: "))
    except ValueError:
        print("ID INVÁLIDO")
        return

    product = search_product(id_product)

    if not product:
        print("Nenhum produto encontrado com esse id.")
        return

    print("\nProduto atual:")
    print_product(product)

    novo_nome = input("Novo nome (ENTER para manter): ").strip()
    novo_preco = input("Novo preço (ENTER para manter): ").strip()

    if novo_nome:
        product.nome = novo_nome

    if novo_preco:
        try:
            novo_preco = float(novo_preco.replace(",", "."))
            if novo_preco > 0:
                product.preco = novo_preco
        except ValueError:
            print("Preço inválido, mantendo o antigo.")

    print("\nProduto atualizado com sucesso!")
    print_product(product)
