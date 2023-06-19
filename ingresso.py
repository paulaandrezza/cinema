from classeBase import ClasseBase


class Ingresso(ClasseBase):
  def __init__(self, conn):
    super().__init__(conn)

  def inserir_ingresso(self, params, values):
    return self.inserir('INGRESSO', params, values)

  def atualizar_coluna(self, values):
    return self.atualizar('INGRESSO', values[0], values[2], f"idIngresso = {values[1]}")

  def consultar_todos(self):
    resultado = self.consultar('INGRESSO')
    if resultado:
      print("{:<3} {:<30} {:<3}".format("ID", "Nome do Cliente", "Id Sessão"))
      for item in range(len(resultado)):
        print("{:<3} {:<30} {:<3}".format(resultado[item][0], resultado[item][1], resultado[item][2]))
    input("\033[1;44mPressione <ENTER> para continuar...\033[m")
    return

  def excluir_unitario(self, id_ingresso):
    return self.excluir('INGRESSO', f"idIngresso = {id_ingresso}")

