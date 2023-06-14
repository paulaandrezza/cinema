from classeBase import ClasseBase

class Ingresso(ClasseBase):
  def __init__(self, conn):
    super().__init__(conn)

  def inserir_ingresso(self, values):
    params = ['nome', 'descricao', 'genero', 'duracao', 'classificacao']
    return self.inserir('INGRESSO', params, values)

  def atualizar_descricao(self, filme):
    return self.atualizar('INGRESSO', 'descricao', filme[1], f"idFilme = {filme[0]}")

  def consultar_ingressos(self):
    return self.consultar('INGRESSO')

  def excluir_ingresso(self, id_filme):
    return self.excluir('INGRESSO', f"idFilme = {id_filme}")