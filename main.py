def menu_principal():
    print('**####### MENU ######**')
    print('* [1] CADASTRAR ')
    print('* [2] LISTAR ')
    print('* [3] REMOVER ')
    print('* [4] ATUALIZAR ')
    print('* [5] FECHAR ')
    print('########################')

menu_principal()

Escolha_opcao = input("Escolha a opção desejada: ")

if Escolha_opcao == "1":

    galera = list()
    pessoa = dict()
    while True:
        pessoa.clear()
        pessoa['ID'] = str(input('ID: '))
        pessoa['Nome'] = str(input('Nome: '))
        pessoa['Idade'] = str(input('Idade: '))
        pessoa['RG'] = str(input('RG: '))
        galera.append(pessoa.copy())
        while True:
            resp = str(input('Gostaria de cadastrar uma nova pessoa? [1- Sim/2- Não]: '))
            if resp in '12':
                break
            print('ERRO! Informe a operação certa!')
        if resp == '1':
            break
    print('-=' * 30)
    print(galera)

