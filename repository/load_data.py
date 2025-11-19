import json
import os.path

NAME_FILE = 'dados_deposito.json'
STOCK_PRODUCT = []
NEXT_ID = 1


def load_data():
    global NEXT_ID
    global STOCK_PRODUCT

    if not os.path.exists(NAME_FILE):
        print(f"Arquivo de dados '{NAME_FILE}' não encontrado. Iniciando com estoque vazio.")
        return

    try:
        with open(NAME_FILE, mode='r', encoding='utf-8') as json_file:
            data_loads = json.load(json_file)
            if 'produtos' in data_loads and 'next_id' in data_loads:
                STOCK_PRODUCT = data_loads['produtos']
                NEXT_ID = data_loads['next_id']
                print(f"Dados carregados com sucesso. Total de {len(STOCK_PRODUCT)} produtos.")

            else:
                raise KeyError("Estrutura JSON inválida")

    except json.decoder.JSONDecodeError:
        print(f"Erro ao decodificar JSON em '{NAME_FILE}'. O arquivo pode estar vazio ou corrompido.")
        STOCK_PRODUCT = []
        NEXT_ID = 1

    except Exception as e:
        print(e)
        STOCK_PRODUCT = []
        NEXT_ID = 1


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


def search_product(id_produto):
    for product in STOCK_PRODUCT:
        if product['id'] == id_produto:
            return product
    return None
