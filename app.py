import os

restaurantes = [
    {'nome':'Churrasquinho JP', 'categoria':'churrasco', 'ativo':False},
    {'nome':'Sushi', 'categoria':'Japonesa', 'ativo':True},
    {'nome':'Le Spagetti', 'categoria':'Italiana', 'ativo':False},
]

def exibir_nome_do_programa():
    print('''


░██████╗░███████╗░██████╗████████╗░█████╗░██████╗░██████╗░░█████╗░██████╗░██████╗░░██████╗
██╔════╝░██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██╗░█████╗░░╚█████╗░░░░██║░░░██║░░██║██████╔╝██║░░██║███████║██████╔╝██████╔╝╚█████╗░
██║░░╚██╗██╔══╝░░░╚═══██╗░░░██║░░░██║░░██║██╔══██╗██║░░██║██╔══██║██╔═══╝░██╔═══╝░░╚═══██╗
╚██████╔╝███████╗██████╔╝░░░██║░░░╚█████╔╝██║░░██║██████╔╝██║░░██║██║░░░░░██║░░░░░██████╔╝
░╚═════╝░╚══════╝╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░╚═════╝░
          
█▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀ █▀
█▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░ ▄█
''')

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. listar Restaurante')
    print('3. alternar status do Restaurante')
    print('4. sair')


# Funcoes do programa #
def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def finalizar_app():
    exibir_subtitulo('Finalizando o app')

def retorna_ao_menu_principal():
    input('Digite alguma tecla para retornar ao menu principal ')
    main()

def opcao_invalida():
    print('Opção inválida !\n')
    retorna_ao_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do reastaurante: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante,'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso !\n')
    retorna_ao_menu_principal()


def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')

    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

        

    retorna_ao_menu_principal()

def alternar_status_restaurante():
    exibir_subtitulo('Alternando o estado do restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja alter o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso !' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso !'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    retorna_ao_menu_principal()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Voce escolheu a opcao: {opcao_escolhida}')

        if opcao_escolhida == 1 :
            cadastrar_novo_restaurante()
            print('Cadastrando restaurante...')
        elif opcao_escolhida == 2 :
            listar_restaurantes()
            print('Lista de restaurantes')
        elif opcao_escolhida == 3 :
            alternar_status_restaurante()
        elif opcao_escolhida == 4 :
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()