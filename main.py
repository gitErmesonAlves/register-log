RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[1;92m"
RESET = "\033[0;0m"
BOLD = "\033[1;33m"
REVERSE = "\033[;7m"

Users = []
while True:
    print(GREEN + '=' * 30)
    print(BLUE + 'MENU PRINCIPAL')
    print(GREEN + '[ 1 ]' + ' - ' + BLUE + 'CADASTRAR CLIENTE')
    print(GREEN + '[ 2 ]' + ' - ' + BLUE + 'VER LISTA DE CLIENTES')
    print(GREEN + '[ 3 ]' + ' - ' + BLUE + 'SAIR DO SISTEMA')
    print(GREEN + '=' * 30)

    option = int(input(RESET + 'DIGITE A OPÇÃO: '))
    if option == 1:
        client = {'nome': str(input('NOME: ')), 'idade': int(input('IDADE: '))}
        if client not in Users:
            Users.append(client)
            print(GREEN + 'CADASTRADO')
        else:
            print(RED + 'CLIENTE JA CADASTRADO')
    elif option == 2:
        print(CYAN + 'CLIENTES CADASTRADOS')
        for u in Users:
            print(GREEN + 'NOME: {} - IDADE: {}'.format(u['nome'], u['idade']))
    elif option == 3:
        break
