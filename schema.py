import sqlite3
from sqlite3 import Error


def criar_banco(banco):
  # Definindo variavel com a conexao com o BD.
  conn = sqlite3.connect(banco)
  # Definindo cursor para manipular dados do BD.
  c = conn.cursor()

  try:
    c.execute("""
    
    """)

    c.execute("""
    """)

    print("Tabelas criadas com sucesso!")
    return conn
  
  except Error as e:
    print(e)