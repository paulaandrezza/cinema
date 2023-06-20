<h1 align="center"> Projeto de CRUD com SQLite e Python | Cinema </h1>

<p align="center">
Este é um projeto simples de CRUD (Create, Read, Update, Delete) desenvolvido em Python, utilizando o banco de dados SQLite. O objetivo deste projeto é demonstrar a implementação básica de operações CRUD utilizando a biblioteca `sqlite3` do Python.
</p>

<br>

## 📑 Funcionalidades

O projeto inclui as seguintes funcionalidades básicas de CRUD:

- **Create**: permite adicionar novos registros ao banco de dados.
- **Read**: possibilita a leitura e exibição dos registros existentes.
- **Update**: permite a atualização de registros existentes no banco de dados.
- **Delete**: possibilita a remoção de registros existentes do banco de dados.

<br>

## 💻 Requisitos

Para executar este projeto, você precisa ter o seguinte instalado:

- Python 3.x
- Biblioteca `sqlite3` (já incluída na biblioteca padrão do Python)
- Biblioteca `matplotlib` (precisa ser instalada)

<br>

## 📝 Instruções de Uso

1. Clone o repositório ou faça o download do código-fonte.
2. Certifique-se de ter o Python instalado corretamente em sua máquina.
3. Abra o terminal e navegue até o diretório do projeto.
4. Instale o `matplotlib` com o seguinte comando:
```
pip install matplotlib
```
5. Execute o arquivo `main.py` usando o comando `python main.py`.
6. Siga as instruções apresentadas no terminal para interagir com o CRUD (Criar, Ler, Atualizar, Excluir registros).

<br>

## 🌳 Estrutura do Projeto

O projeto possui a seguinte estrutura de arquivos:

```
.
├── cinema.db
├── main.py
├── casseBase.py
├── schema.py
├── filme.py
├── funcionario.py
├── grafico.py
├── ingresso.py
├── sala.py
├── sessao.py
└── unidade.py
```

- `main.py`: arquivo principal do projeto que contém o código-fonte para as operações CRUD.
- `cinema.db`: arquivo do banco de dados SQLite que será criado automaticamente quando o programa for executado pela primeira vez.
- `schema.py`: Este arquivo contém o código para criar a estrutura do banco de dados. Ele utiliza a biblioteca sqlite3 para estabelecer uma conexão com o banco de dados e criar as tabelas necessárias, como `"FILME"`, `"FUNCIONARIO"`, `"INGRESSO"`, `"SALA"`, `"SESSAO"` e `"UNIDADE"`.
- `classeBase.py`: Este arquivo contém a classe base com as operações básicas de CRUD, como criar, ler, atualizar e excluir registros no banco de dados. Os outros arquivos herdam dessa classe e fazem modificações específicas para passar os parâmetros corretos.
- `filme.py`: Este arquivo contém a implementação da classe "Filme", que representa os filmes do cinema. Ele contém métodos para criar, atualizar e excluir registros de filmes no banco de dados.
- `funcionario.py`: Este arquivo contém a implementação da classe "Funcionario", que representa os funcionários do cinema. Ele contém métodos para criar, atualizar e excluir registros de funcionários no banco de dados.
- `grafico.py`: Este arquivo contém a implementação de funções relacionadas à geração de gráficos ou visualizações baseadas nos dados do banco de dados.
- `ingresso.py`: Este arquivo contém a implementação da classe "Ingresso", que representa os ingressos do cinema. Ele contém métodos para criar, atualizar e excluir registros de ingressos no banco de dados.
- `sala.py`: Este arquivo contém a implementação da classe "Sala", que representa as salas do cinema. Ele contém métodos para criar, atualizar e excluir registros de salas no banco de dados.
- `sessao.py`: Este arquivo contém a implementação da classe "Sessao", que representa as sessões de filmes do cinema. Ele contém métodos para criar, atualizar e excluir registros de sessões no banco de dados.
- `unidade.py`: Este arquivo contém a implementação da classe "Unidade", que representa as unidades do cinema. Ele contém métodos para criar, atualizar e excluir registros de unidades no banco de dados.

<br>

## 🙌 Contribuição

Contribuições são bem-vindas! Se você quiser adicionar recursos adicionais, corrigir bugs ou melhorar a implementação existente, sinta-se à vontade para abrir um Pull Request.
