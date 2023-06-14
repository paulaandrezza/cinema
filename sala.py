from classeBase import ClasseBase

class Sala(ClasseBase):
  def __init__(self, conn):
    super().__init__(conn)
    

  def inserir_sala(self, sala):
    return inserir('sala', sala)

  def atualizar_assentos(self, sala):
    return atualizar('sala', 'qtdAssentos', sala[1], f"idSala = {sala[0]}")

  def consultar_salas(self):
    return consultar('sala')

  def excluir_sala(self, sala):
    return excluir('sala', f"idSala = {sala}")


# Exemplo de uso:
# conn = # Conexão com o banco de dados

# sala = Sala(conn)
# sala.inserir_sala((1, 100, 1))
# sala.atualizar_assentos((1, 150))
# sala.consultar_salas()
# sala.excluir_sala(1)
