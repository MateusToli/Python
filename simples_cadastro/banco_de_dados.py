'''Script de um simples banco de dados, que mostra ao usuário um menu de opções entre cadastrar uma pessoa,
buscar uma pessoa, editar cadastro, remover cadastro, ou ver a lista atual de cadastrados, além de encerrar o programa. Ao cadastrar, salva as informações
num arquivo csv, que pode ser aproveitado pelo próprio programa para verificar se o usuário já está na base de dados.
'''

import os
import time 
import csv

os.system('cls')

def carregar_cadastros(arquivo):

    cadastros = {}
    if os.path.exists(arquivo):
        with open(arquivo, 'r', newline='', encoding='utf-8') as f: 
            leitor = csv.DictReader(f)
            for linha in leitor:
                nome = linha['nome'].strip().lower()
                cadastros[nome] = {'idade': int(linha['idade']), 'cidade': linha['cidade']}
    return cadastros

def salvar_cadastro_csv(arquivo, nome, dados):
    with open(arquivo, 'a', newline='', encoding='utf-8') as f:
        campos = ['nome', 'idade', 'cidade']
        escritor = csv.DictWriter(f, fieldnames=campos)
        if os.path.getsize(arquivo) == 0: # escreve cabeçalho se arquivo estiver vazio
            escritor.writeheader()
        escritor.writerow({'nome': nome.title(), 'idade': dados['idade'], 'cidade': dados['cidade'].title()})

def sobrescrever_cadastros(arquivo, dados_pessoais):
    with open(arquivo, 'w', newline='', encoding='utf-8') as f:
        campos = ['nome', 'idade', 'cidade']
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        for nome, dados in dados_pessoais.items():
            escritor.writerow({'nome': nome.title(), 'idade': dados['idade'], 'cidade': dados['cidade'].title()})

def cadastro(dados_pessoais, arquivo):

    os.system('cls')
    nome = input('Nome: ').strip().lower()
    if nome in dados_pessoais:
        print('\nUsuário já cadastrado!')
        time.sleep(2)
        os.system('cls')
    else:
        try:
            idade = int(input('Idade: '))
            cidade = input('Cidade: ').strip()
            dados = {'idade': idade, 'cidade': cidade}
            dados_pessoais[nome] = dados
            salvar_cadastro_csv(arquivo, nome, dados)
            print('\nCadastro realizado com sucesso!')
            time.sleep(2)
            os.system('cls')
        except ValueError:
           print('\nIdade inválida. Tente Novamente.')
           time.sleep(2)
           os.system('cls')
           

def busca(dados_pessoais):

    os.system('cls')

    nome = input('Nome a procurar: ').strip().lower()
    if nome in dados_pessoais:
        pessoa = dados_pessoais[nome]
        print(f'\n\nNome: {nome.capitalize()}')
        print(f'Idade: {pessoa['idade']}')
        print(f'Cidade: {pessoa['cidade']}')
    else:
        print('\nPessoa não encontrada.')
        time.sleep(2)
        os.system('cls')

def editar_cadastro(dados_pessoais, arquivo):
    os.system('cls')
    nome = input('Nome da pessoa a ser editado: ').strip().lower()
    if nome in dados_pessoais:
        print(f'\nDados atuais: {dados_pessoais[nome]}')
        try:
            nova_idade = int(input('\nNova idade: '))
            nova_cidade = input('Nova cidade: ').strip()
            dados_pessoais[nome] = {'idade': nova_idade, 'cidade': nova_cidade}
            sobrescrever_cadastros(arquivo, dados_pessoais)
            print('\nCadastro atualizado com sucesso!')
            time.sleep(2)
            os.system('cls')
        except ValueError:
            print('\nIdade Inválida. Tente novamente.')
            time.sleep(2)
            os.system('cls')
    else:
        print('Pessoa não encontrada.')
        time.sleep(2)
        os.system('cls')

def remover_cadastro(dados_pessoais, arquivo):
    os.system('cls')
    nome = input('\nNome da pessoa a remover: ').strip().lower()
    if nome in dados_pessoais:
        confirmacao = input(f'Tem certeza que deseja remover {nome.capitalize()}? (s/n): ').lower()
        if confirmacao == 's':
            del dados_pessoais[nome]
            sobrescrever_cadastros(arquivo, dados_pessoais)
            print('\nUsuário removido com sucesso!')
            time.sleep(2)
            os.system('cls')
        elif confirmacao == 'n':
            print('\nRemoção cancelada')
            time.sleep(2)
            os.system('cls')
        else: 
            print('\nTecla errada. S para sim e N para não.')
            time.sleep(2)
            os.system('cls')
    else: 
        print('\nPessoa não encontrada.')
        time.sleep(2)
        os.system('cls')

    

def lista_pessoas(dados_pessoais):

    os.system('cls')
    if not dados_pessoais:
        print('Nenhum cadastro realizado.')
        time.sleep(2)
        os.system('cls')
    else:
        print('-----Usuários Cadastrados-----')
        for nome, dados in dados_pessoais.items():
            print(f'\nNome: {nome.capitalize()}')
            print(f'Idade: {dados['idade']}')
            print(f'Cidade: {dados['cidade']}')
        

def menu():

    arquivo = 'cadastros.csv'
    dados_pessoais = carregar_cadastros(arquivo)

    while True: 

        print('''
    --- Menu ---
    
    1. Cadastro
    2. Busca
    3. Editar cadastro
    4. Remover cadastro
    5. Usuários cadastrados
    6. Encerrar''')


        opcao = input("\nEscolha uma opção: ")
        match opcao: 
            
            case '1':
                cadastro(dados_pessoais, arquivo)
            case '2':
                busca(dados_pessoais)
            case '3': 
                editar_cadastro(dados_pessoais, arquivo)
            case '4': 
                remover_cadastro(dados_pessoais, arquivo)
            case '5': 
                lista_pessoas(dados_pessoais)
            case '6':
                print('\nEncerrando o programa...')
                time.sleep(2)
                os.system('cls')
                break
            case _:
                print('\nOpção inválida. Tente novamente.')
                time.sleep(2)
                os.system('cls')

menu()




