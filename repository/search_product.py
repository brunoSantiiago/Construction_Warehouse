from repository.load_data import STOCK_PRODUCT


def search_product(id_produto):
    for product in STOCK_PRODUCT:
        if product['id'] == id_produto:
            return product
    return None
