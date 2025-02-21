import sqlite3 as sql

def index():
    con = sql.connect("db_web.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM notes")
    data = cur.fetchall()
    con.close()
    return data

def submit(title, details):
    try:
        con = sql.connect("db_web.db")
        cur = con.cursor()

        # Obter o maior valor de POSITION atualmente no banco de dados
        cur.execute("SELECT MAX(POSITION) FROM notes")
        max_position = cur.fetchone()[0]
        new_position = (max_position + 1) if max_position is not None else 1  # Define a nova posição

        # Inserir a nova nota com a posição calculada
        cur.execute("INSERT INTO notes (TITLE, DETAILS, POSITION) VALUES (?, ?, ?)", (title, details, new_position))

        con.commit()
        con.close()
        return True
    except Exception as e:
        return str(e)

def delete(note_id):
    try:
        con=sql.connect("db_web.db")
        cur=con.cursor()
        cur.execute("delete from notes where ID=?",(note_id,))
        con.commit()
        return True
    except Exception as e:
        return str(e)

def get_note(note_id):
    con = sql.connect("db_web.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM notes WHERE ID=?", (note_id,))
    data = cur.fetchone()
    con.close()

    if data:
        # Aqui você acessa os dados da Row como se fosse um dicionário
        return {"ID": data["ID"], "TITLE": data["TITLE"], "DETAILS": data["DETAILS"]}
    return None


def update_note(id, title, details):
    """Atualiza os dados do usuário no banco de dados."""
    try:
        con = sql.connect("db_web.db")
        cur = con.cursor()
        cur.execute("UPDATE notes SET TITLE=?, DETAILS=? WHERE ID=?", (title, details, id))
        con.commit()
        con.close()
        return True
    except Exception as e:
        return str(e)


import sqlite3 as sql

def update_card_order(order):
    try:
        con = sql.connect("db_web.db")
        cur = con.cursor()
        
        for item in order:
            card_id = item["id"]
            new_position = item["position"]
            cur.execute("UPDATE cards SET position=? WHERE ID=?", (new_position, card_id))
        
        con.commit()
        con.close()
        return True
    except Exception as e:
        return str(e)
