from classeBase import ClasseBase


class Sala(ClasseBase):
  def __init__(self, conn):
    super().__init__(conn)

  def inserir_unitario(self, params, values):
    return self.inserir('SALA', params, values)

  def atualizar_coluna(self, values):
    return self.atualizar('SALA', values[0], values[2], f"idSala = {values[1]}")
  
  def consultar_todos(self):
    join_clauses = [
      "UNIDADE ON SALA.idUnidade = UNIDADE.idUnidade"
    ]
    resultado = self.consultar('SALA', join_clauses)
    if resultado:
      print("{:<3} {:<15} {:<15} {:<30} {:<30} {:<30} {:<40} {:<3}".format("ID", "Qtd Assentos", "Id Unidade", "Estado", "Cidade", "Bairro", "Logradouro", "Número"))
      for item in range(len(resultado)):
        print("{:<3} {:<15} {:<15} {:<30} {:<30} {:<30} {:<40} {:<3}".format(resultado[item][0], resultado[item][1], resultado[item][2], resultado[item][4], resultado[item][5], resultado[item][6],  resultado[item][7], resultado[item][8]))
    input("\033[1;44mPressione <ENTER> para continuar...\033[m")
    return

  def excluir_unitario(self, id_sala):
    return self.excluir('SALA', f"idSala = {id_sala}")

