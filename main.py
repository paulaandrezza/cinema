import filme
import funcionario
import schema
from sala import ClasseBase, Sala

#import ingresso
#import sessao
#import unidade


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

def atualizarFilme():
  print(30 * "\033[1m*\033[0m")
  print('\033[1m***  Menu de atualizações  ***\033[0m')
  print(30 * "\033[1m*\033[0m")
  print("\033[1m1.\033[0m Nome\n\033[1m2.\033[0m Descrição\n\033[1m3.\033[0m Genero\n\033[1m4.\033[0m Duração\n\033[1m5.\033[0m Classificacao\n\033[1m0.\033[0m Retornar ao menu anterior.")
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
  theater = Sala(conn)
  movie = filme.Filme(conn)
  employee = funcionario.Funcionario(conn)
  #ticket = ingresso.Ingresso(conn)
  #session = sessao.Sessao(conn)
  #unit = unidade.Unidade(conn)
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
          params = (nameMovie, descriptionMovie, genderMovie, durationMovie, classificationMovie)
          print(movie.inserir_filme(params))
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
        if tabela == "funcionario":
          pass
        elif tabela == "filme":
          op = atualizarFilme()
          columns = ['nome', 'descricao', 'genero', 'duracao', 'classificacao']
          idMovie = int(input("Informe o id do filme que deseja atualizar: "))
          newText = input(f"Informe o(a) novo(a) {columns[op-1]}: ")
          params = (columns[op-1], idMovie, newText)
          print(movie.atualizar_coluna(params))
        elif tabela == "sala":
          pass
        elif tabela == "ingresso":
          pass
        elif tabela == "sessao":
          pass
        elif tabela == "unidade":
          pass

      elif opcaosub == 3: 
        print(f"\033[33mConsultar {tabela}\033[0m")
        if tabela == "funcionario":
          pass
        elif tabela == "filme":
          print(movie.consultar_filmes())
        elif tabela == "sala":
          pass
        elif tabela == "ingresso":
          pass
        elif tabela == "sessao":
          pass
        elif tabela == "unidade":
          pass

      elif opcaosub == 4:
        print(f"\033[33mExcluir {tabela}\033[0m")
        if tabela == "funcionario":
          pass
        elif tabela == "filme":
          idMovie = int(input("Informe o id do filme que deseja excluir: "))
          movie.excluir_filme(idMovie)
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
    
    

    