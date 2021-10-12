RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[1;92m"
RESET = "\033[0;0m"
BOLD = "\033[1;33m"
REVERSE = "\033[;7m"


def file_arq(nome):
    try:
        file = open(nome, 'rt') #LEITURA DE ARQUIVO TXT
        file.close()
    except FileNotFoundError:
        return False
    else:
        return True


def create_file(nome):
    try:
        file = open(nome, 'wt+') #SALVE ARQUIVO TXT
        file.close()
    except:
        return print(RED + 'ERRO NA CRIAÇÃO DO ARQUIVO')
    else:
        return print(GREEN + 'CREATED FILE SUCCESS')


def view_file(nome):
    try:
        file = open(nome, 'rt') #VER ARQUIVO TXT
    except:
        return print(RED + 'ERROR')
    else:
        print(CYAN + 'CLIENTES CADASTRADOS')
        print(file.read())


def register(file, nome='<desconhecido>', idade=0):
    try:
        file = open(file, 'at')
    except:
        return print(RED + 'ERROR')
    else:
        try:
            file.write('\n{}            {}'.format(nome, idade))
        except:
            return print(RED + 'ERROR, NÃO CONSEGUIMOS GRAVAR O CADASTRO')
        else:
            file.close()
