import pyodbc

dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                 "Server=localhost;"
                 "Database=TowerCrawler.db")

conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()

cursor.close()
conexao.close()
