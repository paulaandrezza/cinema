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
    print(f"\033[0;30;46m\nRegistro inserido na tabela {tabela} com sucesso!\033[m")
    input("\033[1;44m\nPressione <ENTER> para continuar...\033[m")
    return

  def atualizar(self, tabela, coluna, valor, condicao):
    # Implementação genérica de atualização
    query = f"UPDATE {tabela} SET {coluna} = ? WHERE {condicao};"
    self.cursor.execute(query, (valor,))
    self.conn.commit()
    print(f"\033[0;30;46m\nDados atualizados na tabela {tabela} com sucesso!\033[m")
    input("\033[1;44m\nPressione <ENTER> para continuar...\033[m")
    return
  
  def consultar(self, tabela, join_clauses=None):
    # Implementação genérica de consulta
    query = f"SELECT * FROM {tabela}"
    
    if join_clauses:
      for join_clause in join_clauses:
        query += f" INNER JOIN {join_clause}"

    query += ";"
    
    self.cursor.execute(query)
    resultado = self.cursor.fetchall()
    
    try:
      if not resultado:
        raise Exception("Nenhum resultado encontrado.")
      return resultado
    except Exception as e:
      print(f"\033[0;30;41m\nErro: {str(e)}\033[m")
      
  def consultar_foreignKey(self, tabela, key, valueKey):
    query = f"SELECT COUNT(*) FROM {tabela} WHERE {key} = {valueKey};"
    self.cursor.execute(query)
    resultado = self.cursor.fetchone()
    return resultado
    

  def excluir(self, tabela, condicao):
    # Implementação genérica de exclusão
    query = f"DELETE FROM {tabela} WHERE {condicao};"
    self.cursor.execute(query)
    self.conn.commit()
    print(f"\033[0;30;41m\nRegistro excluído da tabela {tabela} com sucesso!\033[m")
    input("\033[1;44m\nPressione <ENTER> para continuar...\033[m")
    return
  
