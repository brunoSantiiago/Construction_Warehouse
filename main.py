# from presentation.main_menu import main_menu
#
# if __name__ == "__main__":
#     main_menu()

import json
import os


NOME_ARQUIVO = 'dados_deposito.json'
ESTOQUE_PRODUTOS = []
PROXIMO_ID = 1



def carregar_dados():

    global PROXIMO_ID
    global ESTOQUE_PRODUTOS

    if not os.path.exists(NOME_ARQUIVO):
        print(f"Arquivo de dados '{NOME_ARQUIVO}' não encontrado. Iniciando com estoque vazio.")
        return

    try:
        with open(NOME_ARQUIVO, mode='r', encoding='utf-8') as file:
            dados_carregados = json.load(file)

            if 'produtos' in dados_carregados and 'proximo_id' in dados_carregados:
                ESTOQUE_PRODUTOS = dados_carregados['produtos']
                PROXIMO_ID = dados_carregados['proximo_id']
                print(f"Dados carregados com sucesso. Total de {len(ESTOQUE_PRODUTOS)} produtos.")
            else:
                raise KeyError("Estrutura JSON inválida.")

    except json.JSONDecodeError:
        print(f"Erro ao decodificar JSON em '{NOME_ARQUIVO}'. O arquivo pode estar vazio ou corrompido.")
        ESTOQUE_PRODUTOS = []
        PROXIMO_ID = 1
    except Exception as e:
        print(f"Erro inesperado ao carregar dados ({e}). Iniciando com estoque vazio.")
        ESTOQUE_PRODUTOS = []
        PROXIMO_ID = 1


def salvar_dados():
    global PROXIMO_ID

    dados_para_salvar = {
        'produtos': ESTOQUE_PRODUTOS,
        'proximo_id': PROXIMO_ID
    }

    try:
        with open(NOME_ARQUIVO, mode='w', encoding='utf-8') as file:

            json.dump(dados_para_salvar, file, indent=4)
        print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"ERRO: Não foi possível salvar os dados. Detalhes: {e}")


def buscar_produto(id_produto):
    for produto in ESTOQUE_PRODUTOS:

        if produto['id'] == id_produto:
            return produto
    return None



def cadastrar_produto():

    global PROXIMO_ID

    print("\n--- CADASTRO DE NOVO PRODUTO ---")
    nome = input("Nome do Produto (Ex: Cimento CPII 50kg): ").strip()

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

    novo_produto = {
        'id': PROXIMO_ID,
        'nome': nome,
        'preco': preco,
        'estoque': estoque_inicial
    }
    ESTOQUE_PRODUTOS.append(novo_produto)
    PROXIMO_ID += 1
    print(f"\nProduto '{nome}' cadastrado com sucesso! ID: {novo_produto['id']}")


def atualizar_estoque():

    print("\n--- ATUALIZAÇÃO DE ESTOQUE (ENTRADA) ---")

    while True:
        try:
            id_produto = int(input("Digite o ID do produto para atualizar o estoque: "))
            break
        except ValueError:
            print("ID inválido. Por favor, digite um número inteiro.")

    produto = buscar_produto(id_produto)

    if produto:
        imprimir_produto(produto)
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


def realizar_venda():

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

        produto = buscar_produto(id_produto)

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


def relatorio_estoque():
    print("\n" + "=" * 60)
    print(" " * 15 + "RELATÓRIO DE ESTOQUE ATUAL")
    print("=" * 60)

    print(f"{'ID': <5}{'Nome do Produto': <35}{'Preço': <10}{'Estoque': <10}")
    print("-" * 60)

    for produto in ESTOQUE_PRODUTOS:
        status = ""

        if produto['estoque'] < 10:
            status = " (BAIXO!)"

        elif produto['estoque'] < 50:
            status = " (Alerta)"

        print(f"{produto['id']: <5}{produto['nome']: <35}R$ {produto['preco']: <7.2f}{produto['estoque']: <10}{status}")

    print("-" * 60)
    print(f"Total de Produtos Cadastrados: {len(ESTOQUE_PRODUTOS)}")
    print("=" * 60)


def imprimir_produto(produto):
    if produto:
        print("-" * 30)
        print(f"ID: {produto['id']}")
        print(f"Nome: {produto['nome']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
        print(f"Estoque: {produto['estoque']}")
        print("-" * 30)
    else:
        print("Produto não encontrado.")


def menu_principal():
    carregar_dados()

    while True:
        print("\n" + "*" * 40)
        print("SISTEMA DEPÓSITO DE CONSTRUÇÃO MVP")
        print("*" * 40)
        print("1. Cadastrar Novo Produto (RF01)")
        print("2. Consultar / Atualizar Estoque (RF02)")
        print("3. Registrar Venda (RF03)")
        print("4. Relatório de Estoque (RF04)")
        print("5. Sair e Salvar")
        print("*" * 40)

        escolha = input("Selecione uma opção: ").strip()

        if escolha == '1':
            cadastrar_produto()
        elif escolha == '2':
            atualizar_estoque()
        elif escolha == '3':
            realizar_venda()
        elif escolha == '4':
            relatorio_estoque()
        elif escolha == '5':
            salvar_dados()
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 5.")



if __name__ == "__main__":
    menu_principal()