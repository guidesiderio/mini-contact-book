# Crie um dicionário vazio para representar a agenda de contatos

agenda = {}

lista_ids = [0]


# Crie uma função para gerar automaticamente identificadores inteiros para cada novo contato inserido na agenda
def gerar_id_contado(lista_ids):
    id_contato = lista_ids[-1] + 1
    lista_ids.append(id_contato)
    return id_contato

# Crie uma função para ler os dados de um contato
def ler_dados_contato():
    nome = input('Nome: ')
    email = input('Email: ')
    telefone = input('Telefone: ')

    dados_contato = (nome, email, telefone)
    return dados_contato


