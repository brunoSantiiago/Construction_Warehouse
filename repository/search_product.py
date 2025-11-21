from repository.load_data import get_stock


def search_product(id_produto):
    for product in get_stock():
        if product['id'] == id_produto:
            return product
    return None


def search_product_by_name(nome_produto):
    # Converte o nome para minúsculas (ou maiúsculas) para comparação Case-Insensitive
    nome_produto_lower = nome_produto.lower().strip()

    for product in get_stock():
        if product['nome'].lower().strip() == nome_produto_lower:
            return product  # Retorna o produto se encontrar
    return None  # Retorna None se não encontrar