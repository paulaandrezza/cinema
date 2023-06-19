from classeBase import ClasseBase


class Ingresso(ClasseBase):
  def __init__(self, conn):
    super().__init__(conn)

  def inserir_unitario(self, params, values):
    return self.inserir('INGRESSO', params, values)

  def atualizar_coluna(self, values):
    return self.atualizar('INGRESSO', values[0], values[2], f"idIngresso = {values[1]}")

  def consultar_todos(self):
    join_clauses = [
      "SESSAO ON INGRESSO.idSessao = SESSAO.idSessao"
    ]
    resultado = self.consultar('INGRESSO', join_clauses)
    if resultado:
      print("{:<3} {:<30} {:<15} {:<10} {:<10} {:<10} {:<10}".format("ID", "Nome do Cliente", "Id Sessão", "Horário", "Data", "idFilme", "idSala"))
      for item in range(len(resultado)):
        print("{:<3} {:<30} {:<15} {:<10} {:<10} {:<10} {:<10}".format(resultado[item][0], resultado[item][1], resultado[item][2], resultado[item][4], resultado[item][5], resultado[item][6], resultado[item][7]))
    input("\033[1;44m\nPressione <ENTER> para continuar...\033[m")
    return

  def excluir_unitario(self, id_ingresso):
    return self.excluir('INGRESSO', f"idIngresso = {id_ingresso}")

