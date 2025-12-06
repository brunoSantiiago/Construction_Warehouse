import json
from repository.load_data import get_stock, get_next_id, NAME_FILE


def save_data():
    produtos_para_json = []
    for produto_obj in get_stock():

        produto_dict = {
            'id': produto_obj.id,
            'nome': produto_obj.nome,
            'preco': produto_obj.preco,
            'estoque': produto_obj.estoque
        }
        produtos_para_json.append(produto_dict)

    data_for_save = {
        'produtos': produtos_para_json,
        'next_id': get_next_id()
    }

    try:
        with open(NAME_FILE, mode='w', encoding='utf-8') as file:
            json.dump(data_for_save, file, indent=4)
        print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"ERRO: Não foi possível salvar os dados. Detalhes: {e}")
