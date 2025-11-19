import json

from repository.load_data import STOCK_PRODUCT, NAME_FILE


def save_data():
    global NEXT_ID

    data_for_save = {
        'produtos': STOCK_PRODUCT,
        'next_id': NEXT_ID
    }

    try:
        with open(NAME_FILE, mode='w', encoding='utf-8') as file:

            json.dump(data_for_save, file, indent=4)
        print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"ERRO: Não foi possível salvar os dados. Detalhes: {e}")
