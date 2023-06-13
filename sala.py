from classeBase import ClasseBase 

class Sala(ClasseBase):
  def __init__(self, conn):
    super().__init__(conn)

  def inserir_sala(self, sala):
    return self.inserir('sala', sala)

  def atualizar_assentos(self, sala):
    return self.atualizar('sala', 'qtdAssentos', sala[1], f"idSala = {sala[0]}")

  def consultar_salas(self):
    return self.consultar('sala')

  def excluir_sala(self, sala):
    return self.excluir('sala', f"idSala = {sala}")
