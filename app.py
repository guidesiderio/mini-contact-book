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

# Crie uma função que insira os dados de um novo contato na agenda de contatos
def inserir_contato(dados_contato):
    chave_contato = gerar_id_contado(lista_ids)
    # agenda[chave_contato] = dados_contato    
    agenda.update({chave_contato: dados_contato})

# Crie uma função que mostre o menu de opções da agenda
def menu():
    print('Opções da Agenda: ')    
    print('1 - Inserir contato')
    print('2 - Listar contato(s)')
    print('3 - Sair')

# Crie uma função que mostre todos os contatos
def mostrar_contato(agenda):
    for contato in agenda:
        print(contato)   


