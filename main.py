
import schema


def login():
  print("\033[1;44;1m" + 22 * "*")
  print("*** Login ***")
  print(22 * "*" + "\033[m")
  login = input("Insira seu login: ")
  senha = input("Insira a senha: ")
  return login

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
  print("Iniciando Teste de tarefas...")
  banco = input("Informe o nome do banco: ")
  conn = schema.criar_banco(banco)

  limpar()
