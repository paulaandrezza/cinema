from classeBase import ClasseBase


class Funcionario(ClasseBase):
  def __init__(self, conn):
    super().__init__(conn)

  def inserir_unitario(self, params, values):
    return self.inserir('FUNCIONARIO', params, values)

  def atualizar_coluna(self, values):
    return self.atualizar('FUNCIONARIO', values[0], values[2], f"idFuncionario = {values[1]}")

  def consultar_todos(self):
    join_clauses = [
      "UNIDADE ON FUNCIONARIO.idUnidade = UNIDADE.idUnidade"
    ]
    resultado = self.consultar('FUNCIONARIO', join_clauses)
    if resultado:
      print("{:<3} {:<20} {:<50} {:<15} {:<30} {:<30} {:<30} {:<40} {:<3}".format("ID", "Login", "Nome", "idUnidade", "Estado", "Cidade", "Bairro", "Logradouro", "Número"))
      for item in range(len(resultado)):
        print("{:<3} {:<20} {:<50} {:<15} {:<30} {:<30} {:<30} {:<40} {:<3}".format(resultado[item][0], resultado[item][1], resultado[item][3], resultado[item][4], resultado[item][6],  resultado[item][7], resultado[item][8], resultado[item][9],  resultado[item][10]))
    input("\033[1;44mPressione <ENTER> para continuar...\033[m")
    return

  def excluir_unitario(self, id_funcionario):
    return self.excluir('FUNCIONARIO', f"idFuncionario = {id_funcionario}")


