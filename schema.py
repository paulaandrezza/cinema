import sqlite3
from sqlite3 import Error


def criar_banco(banco):
  # Definindo variavel com a conexao com o BD.
  conn = sqlite3.connect(banco)
  # Definindo cursor para manipular dados do BD.
  c = conn.cursor()

  try:
    c.execute("""
    CREATE TABLE IF NOT EXISTS "FILME" ("idFilme"	INTEGER NOT NULL,	"nome"	TEXT NOT NULL,	"descricao"	TEXT NOT NULL,	"genero"	TEXT NOT NULL, "duracao"	INTEGER NOT NULL,	"classificacao"	NUMERIC NOT NULL,	PRIMARY KEY("idFilme"));
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS "FUNCIONARIO" ("idFuncionario"	INTEGER NOT NULL, "login"	TEXT NOT NULL, "senha"	TEXT NOT NULL, "nome"	INTEGER NOT NULL, "idUnidade"	INTEGER NOT NULL, FOREIGN KEY("idUnidade") REFERENCES "UNIDADE"("idUnidade"), PRIMARY KEY("idFuncionario" AUTOINCREMENT));
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS "INGRESSO" ("idIngresso"	INTEGER NOT NULL,	"nomeCliente"	TEXT NOT NULL,	"idSessao"	INTEGER NOT NULL, PRIMARY KEY("idingresso"), FOREIGN KEY("idSessao") REFERENCES "SESSAO"("idSessao"));
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS "SALA" ("idSala"	INTEGER NOT NULL, "qtdAssentos"	INTEGER NOT NULL,	"idUnidade"	INTEGER,	PRIMARY KEY("idSala"),	FOREIGN KEY("idUnidade") REFERENCES "UNIDADE"("idUnidade"));
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS "SESSAO" ("idSessao"	INTEGER NOT NULL,	"horario"	TEXT NOT NULL,	"data"	TEXT NOT NULL,	"idFilme"	INTEGER NOT NULL,	"idSala"	INTEGER NOT NULL,	PRIMARY KEY("idSessao" AUTOINCREMENT),	FOREIGN KEY("idSala") REFERENCES "SALA"("idSala"),	FOREIGN KEY("idFilme") REFERENCES "FILME"("idFilme"));
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS "UNIDADE" ("idUnidade"	INTEGER NOT NULL,	"estado"	TEXT NOT NULL,	"cidade"	TEXT NOT NULL,	"bairro"	TEXT NOT NULL,	"logradouro"	TEXT NOT NULL,	"numero"	INTEGER NOT NULL,	PRIMARY KEY("idUnidade"));
    """)

    print("Tabelas criadas com sucesso!")
    return conn
  
  except Error as e:
    print(e)