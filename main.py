if __name__ == '__main__':
    pessoa = dict()
    galera = list()
    menu = 0

    while menu != 5:

        print('==== MENU PRINCIPAL====')
        print('#    [1] CADASTRAR    #')
        print('X    [2] LISTAR       X')
        print('#    [3] EDITAR       #')
        print('X    [4] EXCLUIR      X')
        print('#    [5] SAIR         #')
        print('=======================')

        menu = int(input('Escolha uma opção:'))

        if menu == 1:

            pessoa['Nome'] = str(input('Nome:'))
            pessoa['Idade'] = str(input('Idade:'))
            pessoa['Turma'] = str(input('Turma:'))
            galera.append(pessoa.copy())
            print('Cadastro efetuado!')
            while True:
                resp = str(input('Gostaria de cadastrar uma nova pessoa? [1- Sim/2- Não]: '))
                if resp in '1':
                    pessoa['Nome'] = str(input('Nome:'))
                    pessoa['Idade'] = str(input('Idade:'))
                    pessoa['Turma'] = str(input('Turma:'))
                    galera.append(pessoa.copy())
                    print('Cadastro efetuado!')
                else:
                    break

        elif menu == 2:
            for i in enumerate(galera):
                print(i)

        elif menu == 3:
            modificar = int(input('Informe o ID:'))

            nome = str(input('Nome:'))
            idade = str(input('Idade:'))
            turma = str(input('Turma:'))

            galera[modificar].update({'Nome': nome, 'Idade': idade, 'Turma': turma})
            print('Cadastro alterado!')
            for i in enumerate(galera):
                print(i)

        elif menu == 4:
            delete = int(input('Que cadastro você deseja deletar (informe o ID):'))
            galera.pop(delete)
            print('Cadastro deletado!')

        elif menu == 5:
            print('Finalizado.')