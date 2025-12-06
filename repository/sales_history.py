import json
from datetime import datetime

HIST_FILE = "historico_vendas.json"


def save_sale_history(carrinho, total_venda):
    try:
        with open(HIST_FILE, "r", encoding="utf-8") as f:
            historico = json.load(f)
    except:
        historico = []

    venda = {
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "itens": [
            {"nome": nome, "quantidade": qtd, "subtotal": sub}
            for nome, qtd, sub in carrinho
        ],
        "total": total_venda
    }

    historico.append(venda)

    with open(HIST_FILE, "w", encoding="utf-8") as f:
        json.dump(historico, f, indent=4)

    print("\nHistórico de vendas atualizado.")
