import repository.load_data as data


def report_stock():
    print("\n" + "=" * 60)
    print(" " * 15 + "RELATÓRIO DE ESTOQUE ATUAL")
    print("=" * 60)

    print(f"{'ID': <5}{'Nome do Produto': <35}{'Preço': <10}{'Estoque': <10}")
    print("-" * 60)

    for produto in data.STOCK_PRODUCT:
        status = ""
        if produto.estoque < 10:
            status = " (BAIXO!)"
        elif produto.estoque < 50:
            status = " (Alerta)"

        print(f"{produto.id: <5}{produto.nome: <35}R$ {produto.preco: <7.2f}{produto.estoque: <10}{status}")

    print("-" * 60)
    print(f"Total de Produtos Cadastrados: {len(data.STOCK_PRODUCT)}")
    print("=" * 60)
