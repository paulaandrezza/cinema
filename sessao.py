from classeBase import ClasseBase


class Sessao(ClasseBase):
  def __init__(self, conn):
    super().__init__(conn)

  def inserir_sessao(self, params, values):
    return self.inserir('SESSAO', params, values)

  def atualizar_coluna(self, values):
    return self.atualizar('SESSAO', values[0], values[2], f"idSessao = {values[1]}")

  def consultar_todos(self):
    resultado = self.consultar('SESSAO')
    if resultado:
      print("{:<3} {:<10} {:<10} {:<10} {:<10}".format("ID", "Horário", "Data", "idFilme", "idSala"))
      for item in range(len(resultado)):
        print("{:<3} {:<10} {:<10} {:<10} {:<10}".format(resultado[item][0], resultado[item][1], resultado[item][2], resultado[item][3], resultado[item][4]))
    input("\033[1;44mPressione <ENTER> para continuar...\033[m")
    return

  def excluir_unitario(self, id_sessao):
    return self.excluir('SESSAO', f"idSessao = {id_sessao}")

