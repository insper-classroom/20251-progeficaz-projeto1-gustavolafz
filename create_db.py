import sqlite3

# Conectar ao SQLite
con = sqlite3.connect('db_web.db')

# Criar um cursor
cur = con.cursor()

# Remover a tabela "notes" se já existir
cur.execute("DROP TABLE IF EXISTS notes")

# Criar a tabela "notes" com um campo de posição
sql_query = '''
    CREATE TABLE notes (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        TITLE TEXT NOT NULL,
        DETAILS TEXT,
        POSITION INTEGER NOT NULL DEFAULT 0
    )
'''
cur.execute(sql_query)

# Confirmar mudanças
con.commit()

# Fechar a conexão
con.close()
