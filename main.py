import schema
import filme
import sala
import funcionario
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
  print("\033[1m1.\033[0m Funcionário\n\033[1m2.\033[0m Sala\n\033[1m3.\033[0m Ingresso\n\033[1m4.\033[0m Sessão\n\033[1m5.\033[0m Unidade\n\033[1m6.\033[0m Sair")
  selecao = int(input("\033[34mSelecione uma opção: \033[0m"))
  return selecao


def submenu(tabela):
  print(22 * "\033[1m*\033[0m")
  print(f"\033[1m***Menu de {tabela}***\033[0m")
  print(22 * "\033[1m*\033[0m")
  print(f"\033[1m0.\033[0m Retornar ao menu principal.\n\033[1m1.\033[0m Inserir {tabela}\n\033[1m2.\033[0m Atualizar {tabela}\n\033[1m3.\033[0m Consultar {tabela}\n\033[1m4.\033[0m Excluir {tabela}")
  selecaosub = int(input("\033[34mSelecione a opção: \033[0m"))
  return selecaosub


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

  limpar()

  print(login())

  limpar()
  opcao = menu()
  limpar()
  while opcao != 6:
    theater = sala.Sala(conn)
    movie = filme.Filme(conn)
    employee = funcionario.Funcionario(conn)
    ticket = ingresso.Ingresso(conn)
    session = sessao.Sessao(conn)
    unit = unidade.Unidade(conn)
    if opcao == 1:
      tabela = "funcionario"            
    elif opcao == 2:
      tabela = "sala"
    elif opcao == 3:
      tabela = "ingresso"
    elif opcao == 4:
      tabela = "sessao"
    elif opcao == 5:
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
        elif tabela == "movie":
          pass
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
        elif tabela == "movie":
          pass
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
        elif tabela == "movie":
          pass
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
        elif tabela == "movie":
          pass
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
    
    

    