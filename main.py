from time import sleep
from clients import *

print(GREEN + '='*30)
print(BLUE + 'MENU PRINCIPAL')
print(GREEN + '[ 1 ]' + ' - ' + BLUE + 'CADASTRAR CLIENTE')
print(GREEN + '[ 2 ]' + ' - ' + BLUE + 'VER LISTA DE CLIENTES')
print(GREEN + '[ 3 ]' + ' - ' + BLUE + 'SAIR DO SISTEMA')
print(GREEN + '='*30)

def cors():
    RED = "\033[1;31m"
    BLUE = "\033[1;34m"
    CYAN = "\033[1;36m"
    GREEN = "\033[1;92m"
    RESET = "\033[0;0m"
    BOLD = "\033[1;33m"
    REVERSE = "\033[;7m"

while True:
    

    file = 'file.txt'

    if not file_arq(file):
        create_file(file)

    try:
        option = int(input(RESET + 'DIGITE A OPÇÃO: '))
        if option == 1:
            try:
                nome = str(input('NOME: '))
                idade = int(input('IDADE: '))
                register(file, nome, idade)
                print(GREEN + 'CADASTRADO')
            except ValueError:
                print(BOLD + 'DADOS INVALIDOS,' + GREEN + 'TENTE NOVAMENTE :)')
        elif option == 2:
            view_file(file)
        elif option == 3:
            break
    except ValueError:
            print(RED + 'NÃO ACEITAMOS TEXTO NA OPÇÃO :(')
sleep(1)