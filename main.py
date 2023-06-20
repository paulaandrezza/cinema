import filme
import funcionario
import ingresso
import sala
import schema
import sessao
import unidade
import matplotlib.pyplot as plt
from grafico import Grafico 


def inserir_login():
  print(36 * "\033[1;34m*\033[0m")
  print(f"\033[1;34m***  {'Login': ^26}  ***\033[0m")
  print(36 * "\033[1;34m*\033[0m")
  login = input("Insira seu login: ")
  from getpass import getpass
  senha = getpass('Insira a senha: ')
  return (login, senha)

def login():
  while True:
    user = inserir_login()
    userDB = employee.fazer_login(user)
  
    if userDB is None:
      limpar()
      print("\033[0;30;41m\nUsuário e/ou senha inválidos. Tente Novamente!\033[m")
      input("\033[1;44m\nPressione <ENTER> para continuar...\033[m")
      limpar()
    else:
      print(f"\033[0;30;46m\nLogin realizado com Sucesso!\033[m")
      input("\033[1;44m\nPressione <ENTER> para continuar...\033[m")
      limpar()
      break

def menu():
  print(36 * "\033[1;34m*\033[0m")
  print(f"\033[1;34m***  {'Menu de Opções': ^26}  ***\033[0m")
  print(36 * "\033[1;34m*\033[0m")
  print("\033[1m1.\033[0m Funcionário\n\033[1m2.\033[0m Sala\n\033[1m3.\033[0m Filme\n\033[1m4.\033[0m Sessão\n\033[1m5.\033[0m Ingresso\n\033[1m6.\033[0m Unidade\n\033[1m7.\033[0m Gráfico\n\033[1m0.\033[0m Sair")
  selecao = int(input("\033[34mSelecione uma opção: \033[0m"))
  return selecao

def submenu(tabela):
  print(36 * "\033[1;34m*\033[0m")
  print(f"\033[1;34m***  {f'Menu de {tabela}': ^26}  ***\033[0m")
  print(36 * "\033[1;34m*\033[0m")
  print(f"\033[1m1.\033[0m Inserir {tabela}\n\033[1m2.\033[0m Atualizar {tabela}\n\033[1m3.\033[0m Consultar {tabela}\n\033[1m4.\033[0m Excluir {tabela}\n\033[1m0.\033[0m Retornar ao menu principal.")
  selecaosub = int(input("\033[34mSelecione a opção: \033[0m"))
  return selecaosub

def atualizar(columns):
  print(36 * "\033[1;34m*\033[0m")
  print(f"\033[1;34m***  {'Menu de Atualizações': ^26}  ***\033[0m")
  print(36 * "\033[1;34m*\033[0m")

  for index, column in enumerate(columns):
    print(f"{index+1}. {column}")

  print("\033[1m0.\033[0m Retornar ao menu anterior.")
  coluna = int(input("\033[34mSelecione uma opção: \033[0m"))
  return coluna

def limpar():
  # Importar o módulo os do sistema operacional
  import os
  # Importar um módulo par aguardar um tempo em segundos passados como parametro
  from time import sleep

  def screen_clear():
    #Linux ou Mac
    if os.name == 'posix':
      _ = os.system('clear')
    else:
      # Windows
      _ = os.system('cls')
          
  sleep(0.1)
  screen_clear()


if __name__ == '__main__':
  limpar()
  # print("Iniciando Teste de tarefas...")
  # banco = input("Informe o nome do banco: ")
  # conn = schema.criar_banco(banco)
  conn = schema.criar_banco("cinema.db")
  limpar()
  
  theater = sala.Sala(conn)
  movie = filme.Filme(conn)
  employee = funcionario.Funcionario(conn)
  ticket = ingresso.Ingresso(conn)
  session = sessao.Sessao(conn)
  unit = unidade.Unidade(conn)

  tables = {
    "funcionario":  [employee, 
                     ["login", "senha", "nome", "idUnidade"], 
                     "o",
                     ["o login", "a senha", "o nome", "o id da Unidade"]],
    
    "sala":         [theater, 
                     ["qtdAssentos", "idUnidade"], 
                     "a",
                     ["a quantidade de assentos", "o ID da unidade"]],
    
    "filme":        [movie, 
                     ["nome", "descricao", "genero", "duracao", "classificacao"], 
                     "o",
                     ["o nome", "a descrição", "o gênero", "a duração (em minutos)", "a classificação"]],
    
    "sessao":       [session, 
                     ["horario", "data", "idFilme", "idSala"], 
                     "a",
                     ["o horário", "a data", "o id do filme", "o id da sala"]],
    
    "ingresso":     [ticket, 
                     ["nomeCliente", "idSessao"], 
                     "o",
                     ["o nome do cliente", "o id da sessão"]],
    
    "unidade":      [unit, 
                     ["estado", "cidade", "bairro", "logradouro", "numero"], 
                     "a",
                     ["o estado", "a cidade", "o bairro", "o logradouro", "o número"]],
  }

  tablesNames = ["funcionario", "sala", "filme", "sessao", "ingresso", "unidade"]

  login()
  
  limpar()
  opcao = menu()
  limpar()
  while opcao != 0:
    if opcao >= 1 and opcao <= 6:
      tabela = tablesNames[opcao-1]
      oa = tables[tabela][2]
    elif opcao == 7:
      grafico = Grafico(conn)
      nomes_filmes, quantidades_vendidas = grafico.ingressos_filme()

      plt.bar(nomes_filmes, quantidades_vendidas)
      plt.title('Quantidade de Ingressos Vendidos por Filme')
      plt.xlabel('Filmes')
      plt.ylabel('Quantidade Vendida')
      plt.show()

      opcao = menu()
      limpar()
      continue
    else:
      print("\033[31mOpção inválida!\033[0m")
      opcao = menu()
      limpar()
      continue
    
    limpar()
    opcaosub = submenu(tabela)
    limpar()
    while opcaosub != 0:            
      if opcaosub == 1:
        print(f"\033[33mInserir {tabela}\033[0m")
        
        valuesList = []
        for i in tables[tabela][3]:
          valuesList.append(input(f"Informe {i}: "))
        params = tables[tabela][1]
        values = tuple(valuesList)
        
        tables[tabela][0].inserir_unitario(params, values)
        limpar()

      elif opcaosub == 2:
        print(f"\033[33mAtualizar {tabela}\033[0m")
        op = atualizar(tables[tabela][1])
        if op == 0: break
        updatedId = int(input(f"Informe o id d{oa} {tabela} que deseja atualizar: "))
        newText = input(f"Informe {oa} nov{oa} {tables[tabela][1][op-1]}: ")
        values = (tables[tabela][1][op-1], updatedId, newText)
        print(tables[tabela][0].atualizar_coluna(values))
        limpar()

      elif opcaosub == 3: 
        print(f"\033[33mConsultar {tabela}\033[0m")
        tables[tabela][0].consultar_todos()
        limpar()

      elif opcaosub == 4:
        print(f"\033[33mExcluir {tabela}\033[0m")
        deleteId = int(input(f"Informe o id d{oa} {tabela} que deseja excluir: "))
        print(tables[tabela][0].excluir_unitario(deleteId))
        limpar()

      else:
        print("\033[31mOpção inválida!\033[0m")
        opcaosub = submenu(tabela)
        limpar()

      limpar()
      opcaosub = submenu(tabela) 
      limpar()
    
    opcao = menu()
    limpar()
    
    

    