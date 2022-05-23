import json
from operator import index
import os.path
import sys

def obter_dados():
    
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

def listar_categorias(dados):
    
    categorias = []

    for elemento in dados:
        if elemento ['categoria'] not in categorias:
            categorias.append(elemento['categoria'])  
    return categorias



def listar_por_categoria(dados, categoria):
    
    lista_categorias = []

    for elemento in dados:
        if elemento['categoria'] == categoria:
            lista_categorias.append(elemento)
    return lista_categorias
  


def produto_mais_caro(dados, categoria):
           
    preco_caro = float(dados[0]['preco'])

    for elemento in dados:
        
        if float(elemento['preco']) > preco_caro and elemento['categoria'] == categoria:
            preco_caro = float(elemento['preco'])
            produto_caro = elemento
    return produto_caro  



def produto_mais_barato(dados, categoria):
    
    preco_barato = float(dados[0]['preco'])

    for elemento in dados:

        if float(elemento['preco']) < preco_barato and elemento['categoria'] == categoria:
            preco_barato = float(elemento['preco'])
            produto_barato = elemento
    return produto_barato



def top_10_caros(dados):
        
    for elemento in dados:

        maior = sorted(dados, key = lambda x: float(x['preco']), reverse = True)  
    
    return maior        
    


def top_10_baratos(dados):
    
    for elemento in dados:

        menor = sorted(dados, key = lambda x: [float(x['preco'])])        
       
    return  menor


def linha(tam = 42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu_opcoes():

    lista_opcoes = ['Sair',
    'Listar categorias',
    'Listar produtos de uma categoria',
    'Produto mais caro por categoria',
    'Produto mais barato por categoria',
    'Top 10 produtos mais caros',
    'Top 10 produtos mais baratos' ]
    
    numero_opcao = 0
    cabecalho('MENU DE OPÇÕES')
    for item in lista_opcoes:
       print(f'\033[33m{numero_opcao}\033[m - \033[034m{item}\033[m')
       numero_opcao += 1
    print(linha())

def menu(dados):
    lista_opcoes = ['Sair',
    'Listar categorias',
    'Listar produtos de uma categoria',
    'Produto mais caro por categoria',
    'Produto mais barato por categoria',
    'Top 10 produtos mais caros',
    'Top 10 produtos mais baratos' ]

    opcao_usuario = type(int)
    
    while opcao_usuario != 0:

        menu_opcoes()
        opcao_usuario = int(input('\nDigite a opção desejada: '))
        linha()
                       
        if opcao_usuario == 1:

            print(f'\n{lista_opcoes[opcao_usuario].center(80).upper()}')                       
            categorias = sorted(listar_categorias(dados))
            
            for i in range(1, len(categorias)- 1):
                print(f'{i} - {str(categorias[i].capitalize())}')
            
            print()

        elif opcao_usuario == 2:

            print(f'\n{lista_opcoes[opcao_usuario].center(80).upper()}') 
            categoria = str(input('\nDigite a categoria desejada: ')).lower()
            linha()
            listagem_por_categorias = listar_por_categoria(dados, categoria)

            for i in range(0, len(listagem_por_categorias)):
                print(f'\nID: {listagem_por_categorias[i]["id"]} ................... PREÇO: R$ {listagem_por_categorias[i]["preco"]} {listagem_por_categorias[i]["categoria"]}')

        elif opcao_usuario == 3:   

            print(f'\n{lista_opcoes[opcao_usuario].center(80).upper()}')  
            categoria = str(input('\nDigite a categoria desejada: ')).lower()
            linha()
            maior_preco = produto_mais_caro(dados, categoria)
            print(f'\nID: {maior_preco["id"]} ................... PREÇO: R$ {maior_preco["preco"]} \n')

        elif opcao_usuario == 4:

            print(f'\n{lista_opcoes[opcao_usuario].center(80).upper()}')  
            categoria = str(input('\nDigite a categoria desejada: ')).lower()
            linha()
            menor_preco = produto_mais_barato(dados, categoria)
            print(f'\nID: {menor_preco["id"]} ................... PREÇO: R$ {menor_preco["preco"]} \n') 

        elif opcao_usuario == 5:

            print(f'\n{lista_opcoes[opcao_usuario].center(80).upper()}')  
            for i in range (0, 10):
                top_10 = top_10_caros(dados)
                print(f'\n{i+1} - ID: {top_10[i]["id"]} PREÇO: R$ {top_10[i]["preco"]} CATEGORIA: {top_10[i]["categoria"]}')

        elif opcao_usuario == 6:

            print(f'\n{lista_opcoes[opcao_usuario].center(80).upper()}')  
            for i in range (0, 10):
                top_10 = top_10_baratos(dados)
                print(f'\n{i+1} - ID: {top_10[i]["id"]} PREÇO: R$ {top_10[i]["preco"]} CATEGORIA: {top_10[i]["categoria"]}')

        elif opcao_usuario == 0:
            print('\nSAINDO...\n\nPROGRAMA FINALIZADO COM SUCESSO!')

        else:

            print()
            print(f'OPÇÃO DIGITADA INVÁLIDA! TENTE NOVAMENTE..\n')



# Programa Principal - não modificar!
dados = obter_dados()
menu(dados)
