class ClasseBase:
  def __init__(self, conn):
    self.conn = conn
    self.cursor = self.conn.cursor()

  def inserir(self, tabela, colunas, dados):
    # Implementação genérica de inserção
    placeholders = ', '.join(['?'] * len(dados))
    query = f"INSERT INTO {tabela} ({', '.join(colunas)}) VALUES ({placeholders});"
    self.cursor.execute(query, dados)
    self.conn.commit()
    print(f"\033[0;30;46mRegistro inserido na tabela {tabela} com sucesso!\033[m")
    input("\033[1;44mPressione <ENTER> para continuar...\033[m")
    return

  def atualizar(self, tabela, coluna, valor, condicao):
    # Implementação genérica de atualização
    query = f"UPDATE {tabela} SET {coluna} = ? WHERE {condicao};"
    self.cursor.execute(query, (valor,))
    self.conn.commit()
    print(f"\033[0;30;46mDados atualizados na tabela {tabela} com sucesso!\033[m")
    input("\033[1;44mPressione <ENTER> para continuar...\033[m")
    return

  def consultar(self, tabela):
    # Implementação genérica de consulta
    query = f"SELECT * FROM {tabela};"
    self.cursor.execute(query)
    resultado = self.cursor.fetchall()
    return resultado

  def excluir(self, tabela, condicao):
    # Implementação genérica de exclusão
    query = f"DELETE FROM {tabela} WHERE {condicao};"
    self.cursor.execute(query)
    self.conn.commit()
    print(f"\033[0;30;41mRegistro excluído da tabela {tabela} com sucesso!\033[m")
    input("\033[1;44mPressione <ENTER> para continuar...\033[m")
    return
  
