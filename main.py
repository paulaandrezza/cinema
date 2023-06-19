import filme
import funcionario
import ingresso
import sala
import schema
import sessao
import unidade


def login():
  print(22 * "*")
  print("*** Login ***")
  print(22 * "*")
  login = input("Insira seu login: ")
  from getpass import getpass
  senha = getpass('Insira a senha: ')
  return login, senha


def menu():
  print(20 * "\033[1m*\033[0m")
  print('\033[1m***Menu de opções***\033[0m')
  print(20 * "\033[1m*\033[0m")
  print("\033[1m1.\033[0m Funcionário\n\033[1m2.\033[0m Sala\n\033[1m3.\033[0m Filme\n\033[1m4.\033[0m Sessão\n\033[1m5.\033[0m Ingresso\n\033[1m6.\033[0m Unidade\n\033[1m0.\033[0m Sair")
  selecao = int(input("\033[34mSelecione uma opção: \033[0m"))
  return selecao


def submenu(tabela):
  print(22 * "\033[1m*\033[0m")
  print(f"\033[1m***Menu de {tabela}***\033[0m")
  print(22 * "\033[1m*\033[0m")
  print(f"\033[1m1.\033[0m Inserir {tabela}\n\033[1m2.\033[0m Atualizar {tabela}\n\033[1m3.\033[0m Consultar {tabela}\n\033[1m4.\033[0m Excluir {tabela}\n\033[1m0.\033[0m Retornar ao menu principal.")
  selecaosub = int(input("\033[34mSelecione a opção: \033[0m"))
  return selecaosub

def atualizar(columns):
  print(30 * "\033[1m*\033[0m")
  print('\033[1m***  Menu de atualizações  ***\033[0m')
  print(30 * "\033[1m*\033[0m")

  for index, column in enumerate(columns):
    print(f"{index+1}. {column}")

  print("\033[1m0.\033[0m Retornar ao menu anterior.")
  coluna = int(input("\033[34mSelecione uma opção: \033[0m"))
  return coluna

def limpar():
  import os
  from time import sleep

  def screen_clear():
    #Linux ou Mac
    if os.name == 'posix':
      _ = os.system('clear')
    else:
      # Windows
      _ = os.system('cls')
            
    sleep(1)
    screen_clear()


if __name__ == '__main__':
  limpar()
  # print("Iniciando Teste de tarefas...")
  # banco = input("Informe o nome do banco: ")
  # conn = schema.criar_banco(banco)
  conn = schema.criar_banco("cinema.db")
  print(conn)
  theater = sala.Sala(conn)
  movie = filme.Filme(conn)
  employee = funcionario.Funcionario(conn)
  ticket = ingresso.Ingresso(conn)
  # session = sessao.Sessao(conn)
  # unit = unidade.Unidade(conn)

  tables = {
    "funcionario": employee,
    "sala": theater,
    "filme": movie,
    "sessao": "session",
    "ingresso": ticket,
    "unidade": "unit",
  }

  columns = {
    "funcionario": ["login", "senha", "nome", "idUnidade"],
    "sala": ["qtdAssentos"],
    "filme": ["nome", "descricao", "genero", "duracao", "classificacao"],
    "sessao": ["horario", "data", "idFilme", "idSala"],
    "ingresso": ["nomeCliente", "idSessao"],
    "unidade": ["estado", "cidade", "bairro", "logradouro", "numero"],
  }

  limpar()

  print(login())

  limpar()
  opcao = menu()
  limpar()
  while opcao != 0:
    
    if opcao == 1:
      tabela = "funcionario"            
    elif opcao == 2:
      tabela = "sala"
    elif opcao == 3:
      tabela = "filme"
    elif opcao == 4:
      tabela = "sessao"
    elif opcao == 5:
      tabela = "ingresso"
    elif opcao == 6:
      tabela = "unidade"
    else:
      print("\033[31mOpção inválida!\033[0m")
      opcao = menu()
      limpar()
      continue

    opcaosub = submenu(tabela)
    limpar()
    while opcaosub != 0:            
      if opcaosub == 1:
        print(f"\033[33mInserir {tabela}\033[0m")
        if tabela == "funcionario":
          pass
        elif tabela == "filme":
          nameMovie = input("Informe o nome do filme: ")
          descriptionMovie = input("Informe a descrição: ")
          genderMovie = input("Informe o genero do filme: ")
          durationMovie = input("Informe a duração em minutos: ")
          classificationMovie = input("Informe a classificação indicativa: ")
          params = columns[tabela]
          values = (nameMovie, descriptionMovie, genderMovie, durationMovie, classificationMovie)
          print(movie.inserir_filme(params, values))
        elif tabela == "sala":
          pass
        elif tabela == "ingresso":
          pass
        elif tabela == "sessao":
          pass
        elif tabela == "unidade":
          pass

      elif opcaosub == 2:
        print(f"\033[33mAtualizar {tabela}\033[0m")
        op = atualizar(columns[tabela])
        if op == 0: break
        updatedId = int(input(f"Informe o id do(a) {tabela} que deseja atualizar: "))
        newText = input(f"Informe o(a) novo(a) {columns[tabela][op-1]}: ")
        values = (columns[tabela][op-1], updatedId, newText)
        print(tables[tabela].atualizar_coluna(values))

      elif opcaosub == 3: 
        print(f"\033[33mConsultar {tabela}\033[0m")
        print(tables[tabela].consultar_todos())

      elif opcaosub == 4:
        print(f"\033[33mExcluir {tabela}\033[0m")
        if tabela == "funcionario":
          pass
        elif tabela == "filme":
          deleteId = int(input("Informe o id do filme que deseja excluir: "))
          print(movie.excluir_filme(deleteId))
        elif tabela == "sala":
          pass
        elif tabela == "ingresso":
          pass
        elif tabela == "sessao":
          pass
        elif tabela == "unidade":
          pass

      else:
        print("\033[31mOpção inválida!\033[0m")
        opcaosub = submenu(tabela)
        limpar()

      limpar()
      opcaosub = submenu(tabela) 
      limpar()

    opcao = menu()
    limpar()
    
    

    