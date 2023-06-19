from classeBase import ClasseBase


class Sala(ClasseBase):
  def __init__(self, conn):
    super().__init__(conn)

  def inserir_sala(self, params, values):
    return self.inserir('SALA', params, values)

  def atualizar_coluna(self, values):
    return self.atualizar('SALA', values[0], values[2], f"idSala = {values[1]}")

  def consultar_todos(self):
    resultado = self.consultar('SALA')
    if resultado:
      print("{:<3} {:<20} {:<3}".format("ID", "Quantidade de Assentos", "Id Unidade"))
      for item in range(len(resultado)):
        print("{:<3} {:<20} {:<3}".format(resultado[item][0], resultado[item][1], resultado[item][2]))
    input("\033[1;44mPressione <ENTER> para continuar...\033[m")
    return

  def excluir_unitario(self, id_sala):
    return self.excluir('SALA', f"idSala = {id_sala}")

