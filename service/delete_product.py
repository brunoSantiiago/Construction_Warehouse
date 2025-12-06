from repository.load_data import get_stock
from repository.search_product import search_product


def delete_product():
    print("\n--- EXCLUSÃO DE PRODUTO ---")

    try:
        id_product = int(input("Digite o ID do produto: "))
    except ValueError:
        print("iD iNVÁLIDO!")
        return

    product = search_product(id_product)

    if not product:
        print("Nenhum produto encontrado com esse id.")
        return

    confirm = input(f"Tem certeza que deseja excluir '{product.nome}'? (s/n): ").lower().strip()

    if confirm == "s":
        get_stock().remove(product)
        print("Produto removido com sucesso.")

    else:
        print("Ação cancelada.")
