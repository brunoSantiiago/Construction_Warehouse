from tkinter import Menu

from presentation.print_product import print_product
from repository.search_product import search_product, search_product_by_name


def search_menu():
    print("\n--- BUSCAR PRODUTO ---")
    termo = input("\nDigite o id ou nome do produto: ").strip()

    if termo.isdigit():
        product = search_product(int(termo))
        if product:
            print("\nProduto encontrado:")
            print_product(product)

        else:
            print("\nNenhum produto encontrado:")

        return

    product = search_product_by_name(termo)
    if product:
        print("\nProduto encontrado:")
        print_product(product)

    else:
        print("Nenhum produto encontrado com esse nome.")
