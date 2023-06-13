import schema
import filme
import sala
import funcionario
#import ingresso
#import sessao
#import unidade



def submenu(tabela):
  print(22 * "\033[1m*\033[0m")
  print(f"\033[1m***Menu de {tabela}***\033[0m")
  print(22 * "\033[1m*\033[0m")
  print(f"0. Retornar ao menu principal.\n1. Inserir {tabela}\n2. Atualizar {tabela}\n3. Consultar {tabela}\n4. Excluir {tabela}")
  selecaosub = int(input("Selecione a opção: "))
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
  tabela = 'filme'
  movie = filme.Filme(conn)
  opcaosub = submenu(tabela)
  limpar()
  while opcaosub != 0:            
    if opcaosub == 1:
      values = ('barbie', 'rosa', 'comedia', 100, 12)
      print(movie.inserir_filme(values))
      opcaosub = 3
    if opcaosub == 3:
      print(movie.consultar_filmes())

    limpar()
    
    

    