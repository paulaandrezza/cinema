class Sala:
  def __ini__(self, conn):
    self.conn = conn
    self.cursor = self.conn.cursor()

  # Inserir
  def iserir_sala(self, sala):
    self.cursor.execute("INSERT INTO sala (idSala, qtdAssentos, idUnidade) VALUES (?, ?, ?);", sala)
    self.conn.commit()
    return "Sala cadastrada com sucesso!"
  
  # Atualizar
  def atualizar_assentos(self, sala):
    self.cursor.execute("UPDATE sala SET qtdAssentos = ? WHERE idSala = ?;", sala)
    self.conn.commit()
    return "Sala atualizada com sucesso!"
  
  # Consultar
  def consultar_salas(self):
    self.cursor.execute("SELECT * FROM sala;")
    resultado = self.cursor.fetchall()
    if resultado:
      print("{:<5} {:<10}".format("n°", "qtd Assentos"))
      for item in range(len(resultado)):
        print("{:<5} {:<10}".format(resultado[item][0], resultado[item][1]))
      input("\033[1;44mPressione <ENTER> para coninuar...\033[m")
  
  # Excluir
  def excluir_sala(self, sala):
    self.cursor.execute("DELETE FROM sala WHERE idSala = ?;", sala)
    self.conn.commit()
    return "Sala excluída com sucesso!"