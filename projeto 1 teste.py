import json
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

def inserir_categoria(dados):
    categorias = listar_categorias(dados)
    categoria = input('\n Digite qual será a categoria: ').replace(" ", '_').lower()
    while categoria not in categorias:
        categoria = input(f' \n {decor()} \n INVÁLIDO! \n Tente novamente: ').replace(" ", '_').lower()
    return categoria.replace(" ", '_').lower()

def listar_por_categoria(dados, categoria):
    lista_categorias = []
    for elemento in dados:
        if elemento['categoria'] == categoria:
            lista_categorias.append(elemento)
    return lista_categorias

def produto_mais_caro(dados, categoria):
    lista_produtos = listar_por_categoria(dados, categoria)
    caro = sorted(lista_produtos, key = lambda x: float(x['preco']), reverse = True)[0]
    return caro

def produto_mais_barato(dados, categoria):
    lista_produtos = listar_por_categoria(dados, categoria)
    barato = sorted(lista_produtos, key = lambda x: float(x['preco']))[0]
    return barato

def top_10_caros(dados):
    for elemento in dados:
        caros = sorted(dados, key = lambda x: float(x['preco']), reverse = True)[:10]
        return caros

def top_10_baratos(dados):
    for elemento in dados:
        baratos = sorted(dados, key = lambda x: [float(x['preco'])])[:10]
        return baratos
     
def decor(tam = 43):
    return '=' * tam

def compute(opcao):
    resultado = ''
    
    if opcao == '1':
        print(f'\n Ok! Aqui estão as categorias: \n')
        categorias = sorted(listar_categorias(dados))
        for i in range(0, len(categorias)):
            resultado = print(f'\n {i + 1} - {str(categorias[i].upper().replace("_", " "))}')
        
    elif opcao == '2':
        categoria = inserir_categoria(dados)
        print(f'\n {decor()}')
        print(f'\n Para a categoria escolhida: {categoria.upper().replace("_", " ")}, aqui estão os respectivos produtos: \n')
        print(f' {decor()} \n')
        listando = listar_por_categoria(dados, categoria)
        for i in range(0, len(listando)):
            resultado =  print(f' {i + 1} - ID: {listando[i]["id"]} | PREÇO: R$ {listando[i]["preco"]} \n')
        
    elif opcao == '3':
        categoria = inserir_categoria(dados)
        print(f'\n {decor()}')
        mais_caro = produto_mais_caro(dados, categoria)
        resultado = print(f'\n Para a categoria escolhida "{categoria.upper().replace("_", " ")}", aqui está o produto mais caro: \n \n ID: {mais_caro["id"]} - PREÇO: R${mais_caro["preco"]}')
        
    elif opcao == '4':
        categoria = inserir_categoria(dados)
        print(f'\n {decor()}')
        mais_barato = produto_mais_barato(dados, categoria)
        resultado = print(f'\n Para a categoria escolhida "{categoria.upper().replace("_", " ")}", aqui está o produto mais barato: \n \n ID: {mais_barato["id"]} - PREÇO: R${mais_barato["preco"]}')
        
    elif opcao == '5':
        print(f'\n Ok! Aqui estão os 10 produtos mais caros: \n ')
        for i in range (0, 10):
                top_10 = top_10_caros(dados)
                resultado = print(f'\n {i+1} - ID: {top_10[i]["id"]} - PREÇO: {top_10[i]["preco"]} - CATEGORIA: {(top_10[i]["categoria"]).upper().replace("_", " ")}')
        
    elif opcao == '6':
        print(f'\n Ok! Aqui estão os 10 produtos mais baratos: \n ')
        for i in range (0, 10):
                top_10_b = top_10_baratos(dados)
                resultado = print(f'\n {i+1} - ID: {top_10_b[i]["id"]} - PREÇO: {top_10_b[i]["preco"]} - CATEGORIA: {top_10_b[i]["categoria"].upper().replace("_", " ")}')
    
    return f'{decor()} \n {resultado} \n {decor()}'


def menu(dados):
    print(f"\n {decor()} \n \n Olá! Aqui está o menu: \n")
    opcao = (input("\n 1. Listar categorias"
                  "\n 2. Listar produtos de uma categoria" 
                  "\n 3. Produto mais caro por categoria" 
                  "\n 4. Produto mais barato por categoria"
                  "\n 5. Top 10 produtos mais caros"
                  "\n 6. Top 10 produtos mais baratos"
                  "\n 0. Sair \n \n Para utilizar o programa, digite aqui o índice da opção escolhida e dê enter:  "))
    print(f'\n {decor()}')
    opcoes = ['1', '2', '3', '4', '5', '6']
    
    while opcao in opcoes:
        compute(opcao)
        print(f"\n {decor()} \n \n Olá! Aqui está o menu: \n")
        opcao = (input("\n 1. Listar categorias"
                  "\n 2. Listar produtos de uma categoria" 
                  "\n 3. Produto mais caro por categoria" 
                  "\n 4. Produto mais barato por categoria"
                  "\n 5. Top 10 produtos mais caros"
                  "\n 6. Top 10 produtos mais baratos"
                  "\n 0. Sair \n \n Para utilizar o programa, digite aqui o índice da opção escolhida e dê enter:  "))
        print(f'\n {decor()}')
    if opcao == '0':
        return None
    else: 
        print(f'\n \n {decor()} Inválido. Tente novamente! \n \n ')
        menu(dados)
        
        

dados = obter_dados()
menu(dados)

