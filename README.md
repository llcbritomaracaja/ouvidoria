# Sistema de Manifestações

Este projeto é um sistema de gerenciamento de manifestações desenvolvido em Python, utilizando uma interface com um banco de dados MySQL. O sistema permite que o usuário registre, consulte e exclua manifestações, que podem ser de três tipos: **Reclamação**, **Sugestão** e **Elogio**.

## 📋 Pré-requisitos

Para executar este projeto, você precisará ter instalado:

- **Python 3.12**
- **MySQL**
- **Biblioteca** `mysql-connector-python`

### Instalação do MySQL Connector

Execute o seguinte comando para instalar o conector do MySQL:

```bash
pip install mysql-connector-python
```

## 🗂️ Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:
- **main.py**: Arquivo principal pela execução do sistema.
- **methods.py**: Contém funções para manipulação e consulta das manifestações no banco de dados.
- **operacoesbd.py**: Gerencia a conexão e as operações com o banco de dados.

## 📄 Tabela do Banco de Dados

A tabela utilizada no banco de dados deve ser criada conforme a estrutura abaixo:

````sql
CREATE TABLE Manifestaçoes (
    codigo INT AUTO_INCREMENT,
    nomeUsuario VARCHAR(100),
    topico VARCHAR(100),
    manifestaçao VARCHAR(500),
    tipoManifestaçao VARCHAR(15),
    PRIMARY KEY (codigo)
);
````

## 🚀 Funcionalidades

### Menu de opções
O sistema apresenta um menu com as seguintes opções:
1. **Listar manifestações**: Exibe todas as manifestações registradas, mostrando o código e o tópico.

2. **Listar manifestações por tipo**: Permite ao usuário filtrar as manifestações pelo tipo (Reclamação, Sugestão ou Elogio).

3. **Criar uma nova manifestação**: Adiciona uma nova manifestação ao banco de dados.

4. **Exibir quantidade de manifestações**: Mostra a quantidade total de manifestações registradas no sistema.

5. **Pesquisar manifestação por código**: Busca e exibe uma manifestação específica pelo código informado.

6. **Excluir uma manifestação por código**: Remove uma manifestação específica pelo código informado.

7. **Sair do sistema**: Encerra o programa.

### Como Executar:
Para iniciar o sistema, execute o arquivo main.py:

````bash
python main.py
````

## 📝 Detalhes dos Arquivos

### main.py
Este é o arquivo principal, responsável pela interação do usuário com o sistema. Ele importa funções do arquivo `methods.py` para executar operações específicas. A conexão com o banco de dados é criada e gerenciada durante a execução.

#### Exemplo de execução:

````python
from operacoesbd import *
from methods import *

# Conectar ao banco de dados
conexao = criarConexao("endereço", "usuario", "senha", "database")
opcao = 0

while opcao != 7:
    print("\n[1] Listar manifestações\n[2] Listar manifestações por tipo\n[3] Criar uma nova manifestação\n[4] Exibir quantidade de manifestações\n[5] Pesquisar manifestação por código\n[6] Excluir uma manifestação por código\n[7] Sair do sistema")
    opcao = int(input("Selecione sua opção: "))

    if opcao == 1:
        listar(conexao)
    elif opcao == 2:
        buscaTipo(conexao)
    elif opcao == 3:
        add(conexao)
    elif opcao == 4:
        count(conexao)
    elif opcao == 5:
        codeSearch(conexao)
    elif opcao == 6:
        remove(conexao)

print("Sessão finalizada com sucesso.")
encerrarConexao(conexao)
````
### methods.py
Contém as funções responsáveis pelas operações de manipulação das manifestações:

- **listar(conexao)**: Lista todas as manifestações registradas.
- **add(conexao)**: Adiciona uma nova manifestação ao banco de dados.
- **buscaTipo(conexao)**: Filtra manifestações pelo tipo (Reclamação, Sugestão, Elogio).
- **count(conexao)**: Exibe o total de manifestações registradas.
- **codeSearch(conexao)**: Pesquisa e exibe uma manifestação pelo código.
- **remove(conexao)**: Exclui uma manifestação específica pelo código.

#### Exemplo de função de adição de manifestação:

````python
def add(conexao):
    nomeUsuario = input("Nome: ")
    topico = input("Tópico de manifestação: ")
    manifestaçao = input("Manifestação: ")
    tipoManifestaçao = input("Tipo de manifestação [1- Reclamação; 2- Sugestão; 3- Elogio]: ")

    tipos = {1: "Reclamação", 2: "Sugestão", 3: "Elogio"}
    tipoManifestaçao = tipos.get(int(tipoManifestaçao), "Inválido")

    consulta = "INSERT INTO manifestaçoes(nomeUsuario, topico, manifestaçao, tipoManifestaçao) VALUES (%s, %s, %s, %s)"
    dados = [nomeUsuario, topico, manifestaçao, tipoManifestaçao]
    insertNoBancoDados(conexao, consulta, dados)
    print("Manifestação adicionada com sucesso.")
````

### operacoesbd.py
Este módulo gerencia as operações com o banco de dados, como a conexão e as consultas. Inclui funções para:
- **criarConexao**: Inicializa a conexão com o banco de dados.
- **encerrarConexao**: Fecha a conexão com o banco de dados.
- **insertNoBancoDados**: Insere registros no banco de dados.
- **listarBancoDados**: Consulta e lista registros do banco de dados.
- **excluirBancoDados**: Exclui registros do banco de dados.

#### Exemplo de função de conexão:
````python
def criarConexao(endereco, usuario, senha, bancodedados):
    try:
        return mysql.connector.connect(
            host=endereco,
            user=usuario,
            password=senha,
            database=bancodedados
        )
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None
````
## 💡 Melhoria Futuras
- Implementar interface gráfica com Tkinter ou PyQt.
- Adicionar funcionalidades para editar manifestações.
- Implementar login de usuário para maior segurança.

## 📜 Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.









