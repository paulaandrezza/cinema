from classeBase import ClasseBase


class Unidade(ClasseBase):
  def __init__(self, conn):
    super().__init__(conn)

  def inserir_unitario(self, params, values):
    return self.inserir('UNIDADE', params, values)

  def atualizar_coluna(self, values):
    return self.atualizar('UNIDADE', values[0], values[2], f"idUnidade = {values[1]}")

  def consultar_todos(self):
    resultado = self.consultar('UNIDADE')
    if resultado:
      print("{:<3} {:<30} {:<30} {:<30} {:<40} {:<3}".format("ID", "Estado", "Cidade", "Bairro", "Logradouro", "Número"))
      for item in range(len(resultado)):
        print("{:<3} {:<30} {:<30} {:<30} {:<40} {:<3}".format(resultado[item][0], resultado[item][1], resultado[item][2], resultado[item][3], resultado[item][4], resultado[item][5]))
    input("\033[1;44m\nPressione <ENTER> para continuar...\033[m")
    return

  def excluir_unitario(self, id_unidade):
    return self.excluir('UNIDADE', f"idUnidade = {id_unidade}")

