# Dicionário vazio para representar a agenda de contatos
agenda = {}

# Função para gerar identificadores inteiros para cada novo contato inserido na agenda
lista_ids = [0]
def gerar_id_contado(lista_ids):
    id_contato = lista_ids[-1] + 1
    lista_ids.append(id_contato)
    return id_contato

# Função para ler os dados de um contato
def ler_dados_contato():
    nome = input('Nome: ')
    email = input('Email: ')
    telefone = input('Telefone: ')

    dados_contato = (nome, email, telefone)
    return dados_contato

# Função para inserir os dados de um novo contato na agenda de contatos
def inserir_contato(dados_contato):
    chave_contato = gerar_id_contado(lista_ids)
    # agenda[chave_contato] = dados_contato
    agenda.update({chave_contato: dados_contato})

# Função que mostre o menu de opções da agenda
def mostrar_menu():
    print('Opções da Agenda:')
    print('1 - Inserir contato')
    print('2 - Listar contato(s)')
    print('3 - Sair')

# Função que lista todos os contatos
def mostrar_contato(agenda):
    quant_contato = len(agenda)
    if quant_contato == 0:
        print('Agenda vazia!')
    else:
        items = agenda.items()
        for contato in items:
            print(contato)

# Aplicação
mostrar_menu()
ler_opcao = input('Digite uma opção: ')
opcao = int(ler_opcao)
print()

while (opcao != 3):
    if opcao == 1:
        print('Inserir contato:')
        dados_contato = ler_dados_contato()
        inserir_contato(dados_contato)
        print()
    if opcao == 2:
        print('Listar contato(s):')
        mostrar_contato(agenda)
        print()
    if opcao == 3:
        print('Fim do programa!')
        print()

    mostrar_menu()
    ler_opcao = input('Digite uma opção: ')
    opcao = int(ler_opcao)
    print()
