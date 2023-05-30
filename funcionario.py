class Funcionario:
    
  def __init__(self, conn):
    self.conn = conn
    self.cursor = self.conn.cursor()

  # INSERIR
  def inserir_funcionario(self, funcionario):
    self.cursor.execute("INSERT INTO usuario (login, senha, nome, idUnidade) VALUES (?, ?, ?, ?);", funcionario)
    self.conn.commit()
    return "Funcionário cadastrado(a) com sucesso!"
  
  # ATUALIZAR
  

  # CONSULTAR
  def consultar_funcionario(self):
    self.cursor.execute("SELECT * FROM funcionario;")
    resultado = self.cursor.fetchall()
    if resultado:
      print("{:<10} {:<30}".format("Login", "Nome Completo"))
      for item in range(len(resultado)):
        print("{:<10} {:<30}".format(resultado[item][0], resultado[item][1]))

  # EXCLUIR
  