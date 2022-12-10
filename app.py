# Crie um dicionário vazio para representar a agenda de contatos

agenda = {}

lista_ids = [0]

def gerar_id_contado(lista_ids):
    id_contato = lista_ids[-1] + 1
    lista_ids.append(id_contato)
    return id_contato


