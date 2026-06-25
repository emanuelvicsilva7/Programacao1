import json


def carregardados():
    with open('catalogo.json', 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)


def salvardados(dados):
    with open('catalogo.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)


def cadastrar():
    dados = carregardados()

    while True:
        categoria = input('Categoria (Livro ou Filme): ').capitalize()
        if categoria == 'Livro' or categoria == 'Filme':
            break
        print('Digite apenas Livro ou Filme.')

    nome = input('Nome: ').title()
    genero = input('Gênero: ').title()
    ano = input('Ano de lançamento: ')

    item = {
        'categoria': categoria,
        'nome': nome,
        'genero': genero,
        'ano': ano
    }

    dados.append(item)
    salvardados(dados)

    print('Cadastro realizado com sucesso!')


def buscar():
    dados = carregardados()

    if not dados:
        print('Nenhum item cadastrado.')
        return

    print('1 - Categoria')
    print('2 - Gênero')
    print('3 - Ano')
    print('4 - Nome')

    opcao = input("Escolha: ")

    if opcao == '1':
        categorias = set(item['categoria'] for item in dados)

        print('\nCategorias disponíveis:')
        for c in categorias:
            print(c)

        valor = input('\nDigite a categoria: ').capitalize()

        resultados = [
            item for item in dados
            if item['categoria'] == valor
        ]

    elif opcao == '2':
        generos = set(item['genero'] for item in dados)

        print('\nGêneros disponíveis:')
        for g in generos:
            print(g)

        valor = input('\nDigite o gênero: ').title()

        resultados = [
            item for item in dados
            if item['genero'] == valor
        ]

    elif opcao == '3':
        anos = set(item['ano'] for item in dados)

        print('\nAnos disponíveis:')
        for a in anos:
            print(a)

        valor = input('\nDigite o ano: ')

        resultados = [
            item for item in dados
            if item["ano"] == valor
        ]

    elif opcao == '4':
        nomes = set(item['nome'] for item in dados)

        print('\nNomes Cadastrados:')
        for n in nomes:
            print(n)

        valor = input('\nDigite o nome: ').title()

        resultados = [
            item for item in dados
            if item['nome'] == valor
        ]

    else:
        print('Opção inválida!')
        return

    if resultados:
        print('\nResultados da pesquisa:')
        for item in resultados:
            print('-' * 20)
            print('Categoria:', item['categoria'])
            print('Nome:', item['nome'])
            print('Gênero:', item['genero'])
            print('Ano:', item['ano'])
    else:
        print('Nenhum resultado encontrado.')



def editar():
    dados = carregardados()

    if not dados:
        print('Nenhum item cadastrado.')
        return

    print('\nItens cadastrados:')
    for i, item in enumerate(dados):
        print(f'{i + 1} - {item['nome']} ({item['categoria']})')

    indice = int(input('\nDigite o número do item: ')) - 1

    if 0 <= indice < len(dados):
        dados[indice]['categoria'] = input(
            'Nova categoria: '
        ).capitalize()

        dados[indice]['nome'] = input(
            'Novo nome: '
        ).title()

        dados[indice]['genero'] = input(
            'Novo gênero: '
        ).title()

        dados[indice]['ano'] = input(
            'Novo ano: '
        )

        salvardados(dados)
        print('Item editado com sucesso!')

    else:
        print('Item inválido!')


# Apagar item
def apagar():
    dados = carregardados()

    if not dados:
        print('Nenhum item cadastrado.')
        return

    print('\nItens Cadastrados:')
    for i, item in enumerate(dados):
        print(f'{i + 1} - {item['nome']} ({item['categoria']})')

    indice = int(input('\nDigite o número do item: ')) - 1

    if 0 <= indice < len(dados):
        removido = dados.pop(indice)
        salvardados(dados)
        print(f'{removido['nome']} foi removido com sucesso!')

    else:
        print('Item inválido!')


while True:
    print('\nBem vindo ao nosso catálogo! O que deseja fazer?')
    print('1 - Cadastrar')
    print('2 - Buscar')
    print('3 - Editar')
    print('4 - Apagar')
    print('5 - Sair')

    escolha = input('Escolha uma opção: ')

    if escolha == '1':
        cadastrar()
        
    elif escolha == '2':
        buscar()

    elif escolha == '3':
        editar()

    elif escolha == '4':
        apagar()

    elif escolha == '5':
        print('Programa encerrado!')
        break

    else:
        print('Opção inválida!')