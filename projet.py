import csv 

def dados(texto):
    lista = []
    with open(texto, 'r', encoding='utf-8') as arquivo: 
        leitor = csv.DictReader(arquivo) 
        for linha in leitor: 
            lista.append(linha) 
    return lista 

def contador_genero(quantidade, tipo_buscado):
    qntd = 0 
    antigo_nome = ''
    novo_nome = ''
    mais = 100000000 
    menos = -100000000
    for cont in quantidade:
        if cont['Entreterimento'] == tipo_buscado:
            qntd += 1  
            ano_atual = int(cont['Ano'])
            if ano_atual < mais:
                mais = ano_atual
                antigo_nome = cont['Titulo']
            if ano_atual > menos:
                menos = ano_atual 
                novo_nome = cont['Titulo']
            

    return qntd, antigo_nome, novo_nome


minha_colecao = dados('texto.txt')
pergunta = input('Qual tipo de mídia está buscando?: ')


nova, o_mais_antigo, o_mais_novo = contador_genero(minha_colecao, pergunta)


print(f"Quantidade: {nova}")
print(f"O mais antigo é: {o_mais_antigo}")
print(f"O mais novo é: {o_mais_novo}")