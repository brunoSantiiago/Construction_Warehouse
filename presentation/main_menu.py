from repository.load_data import load_data
from repository.save_data import save_data
from service.insert_product import insert_product
from service.make_sale import make_sale
from service.report_stock import report_stock
from service.update_stock import update_stock

def main_menu():
    load_data()

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
            insert_product()
        elif escolha == '2':
            update_stock()
        elif escolha == '3':
            make_sale()
        elif escolha == '4':
            report_stock()
        elif escolha == '5':
            save_data()
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 5.")
