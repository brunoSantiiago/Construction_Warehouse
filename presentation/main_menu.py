from repository.list_sales import list_sale_history
from repository.load_data import load_data
from repository.save_data import save_data
from service.delete_product import delete_product
from service.edit_product import edit_product
from service.insert_product import insert_product
from service.make_sale import make_sale
from service.report_stock import report_stock
from service.search_menu import search_menu
from service.update_stock import update_stock


def executar_menu():
    print("\n" + "*" * 40)
    print("SISTEMA DEPÓSITO DE CONSTRUÇÃO")
    print("*" * 40)
    print("1. Cadastrar Novo Produto (RF01)")
    print("2. Atualizar Estoque (RF02)")
    print("3. Registrar Venda (RF03)")
    print("4. Relatório de Estoque (RF04)")
    print("5. Buscar Produto (RF06)")
    print("6. Editar Produto (RF08)")
    print("7. Excluir Produto (RF07)")
    print("8. Histórico de Vendas (RF11)")
    print("9. Sair e Salvar (RF05)")

    print("*" * 40)

    return input("Selecione uma opção: ").strip()


def main_menu():
    load_data()

    opcoes = {
        "1": insert_product,
        "2": update_stock,
        "3": make_sale,
        "4": report_stock,
        "5": search_menu,
        "6": edit_product,
        "7": delete_product,
        "8": list_sale_history,

        "9": lambda: print("Saindo...")
    }

    while True:
        escolha = executar_menu()

        acao = opcoes.get(escolha)

        if acao:
            if escolha == "9":
                save_data()
                print("Dados salvos com sucesso. Até logo!")
                break

            try:
                acao()
                save_data()
            except Exception as e:
                print(f"⚠ Erro ao executar operação: {e}")
        else:
            print("Opção inválida. Escolha um número de 1 a 5.")
