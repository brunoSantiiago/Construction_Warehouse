from repository.search_product import search_product


def make_sale():
    print("\n--- REGISTRO DE VENDA ---")
    carrinho = []
    total_venda = 0.0

    while True:
        entrada_id = input("Digite o ID do produto (ou 'f' para finalizar a venda): ").strip().lower()

        if entrada_id == 'f':
            break

        try:
            id_produto = int(entrada_id)
        except ValueError:
            print("ID inválido ou comando desconhecido. Digite um número ou 'f'.")
            continue

        produto = search_product(id_produto)

        if not produto:
            print(f"Produto com ID {id_produto} não encontrado no catálogo.")
            continue

        while True:
            try:
                quantidade = int(input(f"Quantidade de '{produto['nome']}' a ser vendida: "))
                if quantidade <= 0:
                    print("A quantidade deve ser positiva.")
                    continue
                elif quantidade > produto['estoque']:
                    print(f"Estoque insuficiente. Disponível: {produto['estoque']}")
                    continue
                break
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

        produto['estoque'] -= quantidade
        subtotal = quantidade * produto['preco']
        carrinho.append((produto['nome'], quantidade, subtotal))
        total_venda += subtotal
        print(f"Item adicionado: {quantidade}x {produto['nome']} (Subtotal: R$ {subtotal:.2f})")

    if carrinho:
        print("\n--- RESUMO DA VENDA ---")

        for nome, qtd, sub in carrinho:
            print(f"{qtd: <5} x {nome: <25} R$ {sub:.2f}")

        print("=" * 40)
        print(f"TOTAL GERAL DA VENDA: R$ {total_venda:.2f}")
        print("Venda registrada e estoque atualizado.")
    else:
        print("Venda cancelada. Nenhum item adicionado.")
