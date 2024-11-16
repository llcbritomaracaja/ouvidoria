from operacoesbd import *

'''
OBS:

TABELA CRIADA NO MYSQL:
        
        CREATE table Manifestaçoes(
            codigo int AUTO_INCREMENT,
            nomeUsuario VARCHAR (100),
            topico VARCHAR (100),
            manifestaçao VARCHAR (500),
            tipoManifestaçao VARCHAR (15),
            primary key(codigo)
        );
'''

def listar(conexao):
    listaManifestaçao = listarBancoDados(conexao, "select * from Manifestaçoes")

    if len(listaManifestaçao) <= 0:
        print("Nenhuma manifestação registrada no sistema. ")

    else:
        for item in listaManifestaçao:
            print(f"{item[0]} >> {item[2]}")

def add(conexao):
    nomeUsuario = input("Nome: ")
    topico = input("Tópico de manifestação: ")
    manifestaçao = input("Manifestação: ")
    tipoManifestaçao = -1

    while tipoManifestaçao < 1 or tipoManifestaçao > 3:
        tipoManifestaçao = int(input("Tipo de manifestação [1- Reclamação; 2- Sugestão; 3- Elogio]: "))
        if tipoManifestaçao < 1 or tipoManifestaçao > 3:
            print("ERRO! Digite um número válido")
        else:
            if tipoManifestaçao == 1:
                tipoManifestaçao = "Reclamação"
                break
            elif tipoManifestaçao == 2:
                tipoManifestaçao = "Sugestão"
                break
            elif tipoManifestaçao == 3:
                tipoManifestaçao = "Elogio"
                break



    consulta = "insert into manifestaçoes(nomeUsuario, topico, manifestaçao, tipoManifestaçao) values(%s,%s,%s,%s)"
    dados = [nomeUsuario, topico, manifestaçao, tipoManifestaçao]
    insertNoBancoDados(conexao, consulta, dados)

    print("Manifestação adicionada com sucesso ")

def buscaTipo(conexao):
    qntManif = listarBancoDados(conexao, "select count(codigo) from manifestaçoes")
    for count in qntManif:
        if count[0] == 0:
            print("Nenhuma manifestação registrada no sistema. ")
        else:
            tipoBusca = -1

            while tipoBusca < 1 or tipoBusca > 3:
                tipoBusca = int(input("Selecione o tipo de manifestação desejada [1- Reclamação; 2- Sugestão; 3- Elogio]:"))

                if tipoBusca < 1 or tipoBusca > 3:
                    print("ERRO! Digite um número válido [1- Reclamação; 2- Sugestão; 3- Elogio]. ")

                else:

                    if tipoBusca == 1:
                        consulta = "select * from Manifestaçoes WHERE tipoManifestaçao = 'Reclamação'"
                        consulta2 = "select count(codigo) from manifestaçoes WHERE tipoManifestaçao = 'Reclamação'"
                        tipox = "Reclamação"
                    elif tipoBusca == 2:
                        consulta = "select * from Manifestaçoes WHERE tipoManifestaçao = 'Sugestão'"
                        consulta2 = "select count(codigo) from manifestaçoes WHERE tipoManifestaçao = 'Sugestão'"
                        tipox = "Sugestão"
                    elif tipoBusca == 3:
                        consulta = "select * from Manifestaçoes WHERE tipoManifestaçao = 'Elogio'"
                        consulta2 = "select count(codigo) from manifestaçoes WHERE tipoManifestaçao = 'Elogio'"
                        tipox = "Elogio"

                    tipoLista = listarBancoDados(conexao, consulta)
                    countTipo = listarBancoDados(conexao, consulta2)

                    for y in countTipo:
                        if y[0] == 0:
                            print(f"Nenhuma manifestação de {tipox} disponível ")
                            break
                        else:
                            for x in tipoLista:
                                print(f"Tipo:{tipox}")
                                print(f"{x[0]} >> {x[2]}")
                            break

def count(conexao):
    consulta = "select count(codigo) from manifestaçoes"

    qntManif = listarBancoDados(conexao, consulta)

    for b in qntManif:
        if b[0] == 0:
            print("Nenhuma manifestação registrada no sistema.")
        elif b[0] == 1:
            print("Apenas uma manifestação registrada no sistema.")
        elif b[0] > 1:
            print(f"{b[0]} manifestações registradas no sistema.")

def codeSearch(conexao):
    qntManif = listarBancoDados(conexao, "select count(codigo) from manifestaçoes")
    for count in qntManif:
        if count[0] == 0:
            print("Nenhuma manifestação registrada no sistema. ")
        else:
            resultado = -1

            while resultado < 1:
                listar(conexao)
                codigoPesquisado = int(input("Insira o código da manifestação: "))
                consulta = f"select * from manifestaçoes WHERE codigo = {codigoPesquisado} "
                buscaCodigo = listarBancoDados(conexao, consulta)
                resultado = len(buscaCodigo)

                if resultado < 1:
                    print("Nenhuma manifestação disponível com o código informado. Digite um código válido")

                else:
                    for c in buscaCodigo:
                        print(f"{c[2]}:\n   {c[3]}")
                        break

def remove(conexao):
    qntManif = listarBancoDados(conexao, "select count(codigo) from manifestaçoes")
    for count in qntManif:
        if count[0] == 0:
            print("Nenhuma manifestação registrada no sistema. ")
        else:
            manifRemovid = -1

            while manifRemovid < 1:
                listar(conexao)

                removerManif = int(input("Insira o código da manifestação para removê-la: "))
                consulta = "DELETE FROM manifestaçoes where codigo = %s"
                valores = [removerManif]
                manifRemovid = excluirBancoDados(conexao, consulta, valores)

                if manifRemovid < 1:
                    print("ERRO! Nenhuma manifestação registrada com o código informado.")
                else:
                    print("Manifestação removida com sucesso. ")
                    break

