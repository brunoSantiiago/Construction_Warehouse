import json
from repository.sales_history import HIST_FILE


def list_sale_history():
    print("\n================ HISTÓRICO DE VENDAS ================\n")

    try:
        with open(HIST_FILE, "r", encoding="utf-8") as f:
            historico = json.load(f)
    except FileNotFoundError:
        print("Nenhuma venda registrada ainda.")
        return
    except json.JSONDecodeError:
        print("Erro ao ler o histórico. Arquivo corrompido.")
        return

    if not historico:
        print("Nenhuma venda registrada ainda.")
        return

    for i, venda in enumerate(historico, 1):
        print(f"Venda {i} - Data: {venda['data']}")
        print("---------------------------------------------")
        for item in venda["itens"]:
            print(f"{item['quantidade']}x {item['nome']}  - Subtotal: R$ {item['subtotal']:.2f}")
        print(f"TOTAL DA VENDA: R$ {venda['total']:.2f}\n")
        print("---------------------------------------------")

    print("\n================ FIM DO RELATÓRIO ================\n")
