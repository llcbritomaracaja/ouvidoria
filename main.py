from operacoesbd import *
from methods import *


conexao = criarConexao("endereço", "usuario", "senha", "database")
#Substitua Endereço;Usuário;Senha;Database
opçao = 0

while opçao != 7:
    print("\n[1] Listar manifestações\n[2] Listar manifestações por tipo\n[3] Criar uma nova manifestação\n[4] Exibir quantidade de manifestações \n[5] Pesquisar manifestação por código\n[6] Excluir uma manifestação por código\n[7] Sair do sistema\n")
    #Faz com que o sistema de opções entre em loop, sendo ele finalizado com o usuário apertando o número 7.

    opçao = int(input("Selecione sua opção: "))

    if opçao < 1 or opçao > 7:
        print("ERRO! Digite uma opção válida. ")
        #Caso o usuário insira um número inválido, mensagem de erro aparece.

    else:

        if opçao == 1:
           listar(conexao) #lista o código junto ao tópico respectivo à cada uma das manifestações disponíveis no sistema.

        elif opçao == 2:
            buscaTipo(conexao) #filtra as manifestações do sistema de acordo com o tipo informado pelo usuário (Reclamação, sugestão ou elogio).

        elif opçao == 3:
            add(conexao) #adiciona uma nova manifestação no sistema

        elif opçao == 4:
            count(conexao) #imprime para o usuário o número de manifestações disponíveis no sistema.

        elif opçao == 5:
            codeSearch(conexao) #busca uma determinada manifestação pelo código informado pelo usuário.

        elif opçao == 6:
            remove(conexao) #remove uma manifestação específica do sistema pelo código informado pelo usuário.


print("Sessão finalizada com sucesso")

encerrarConexao(conexao)