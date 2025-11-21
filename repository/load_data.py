import json
import os.path

NAME_FILE = 'dados_deposito.json'
STOCK_PRODUCT = []
PROXIMO_ID = 1


def load_data():
    global  PROXIMO_ID
    global STOCK_PRODUCT

    if not os.path.exists(NAME_FILE):
        print(f"Arquivo de dados '{NAME_FILE}' não encontrado. Iniciando com estoque vazio.")
        return

    try:
        with open(NAME_FILE, mode='r', encoding='utf-8') as json_file:
            data_loads = json.load(json_file)
            if 'produtos' in data_loads and     'id' in data_loads:
                STOCK_PRODUCT = data_loads['produtos']
                PROXIMO_ID = data_loads['id']
                print(f"Dados carregados com sucesso. Total de {len(STOCK_PRODUCT)} produtos.")

            else:
                raise KeyError("Estrutura JSON inválida")

    except json.decoder.JSONDecodeError:
        print(f"Erro ao decodificar JSON em '{NAME_FILE}'. O arquivo pode estar vazio ou corrompido.")
        STOCK_PRODUCT = []
        PROXIMO_ID = 1

    except Exception as e:
        print(e)
        STOCK_PRODUCT = []
        PROXIMO_ID = 1
