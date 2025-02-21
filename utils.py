import os
import sqlite3 as sql
import json

# def load_data(filename):
#     file_path = os.path.join('static', 'data', filename)  # Caminho do arquivo JSON
#     with open(file_path, 'r', encoding='utf-8') as file:
#         data = json.load(file)  # A função json.load() carrega o conteúdo JSON
#     return data  # Retorna o conteúdo convertido para um objeto Python

# def load_template(filename):
#     file_path = os.path.join('templates', filename)
#     with open(file_path, 'r', encoding='utf-8') as file:
#         content = file.read()  
#     return content

# def add_note(title, details):
#     file_path = os.path.join('static', 'data', 'notes.json')  # Caminho do arquivo JSON
    
#     # Carregar os dados atuais do arquivo
#     with open(file_path, "r", encoding="utf-8") as file:
#         json_data = json.load(file)
    
#     # Novo bloco de dados a ser adicionado
#     new_block = {
#         "titulo": title,
#         "detalhes": details
#     }
    
#     # Adicionar o novo bloco à lista
#     json_data.append(new_block)
    
#     # Salvar os dados novamente no arquivo JSON
#     with open(file_path, "w", encoding="utf-8") as file:
#         json.dump(json_data, file, indent=4, ensure_ascii=False)

def add_note_to_db(title, details):
    try:
        con=sql.connect("db_web.db")
        cur=con.cursor()
        cur.execute("insert into notes(TITLE,DETAILS) values (?,?)",(title,details))
        con.commit()
        return True
    except Exception as e:
        return str(e)
