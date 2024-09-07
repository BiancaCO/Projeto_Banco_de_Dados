# Parada.py

from psycopg2 import sql
import psycopg2
from conectar_banco import ConectarBanco


#Função para aceitar valores NUll
def tratar_input(valor):
    return None if valor.upper() == 'NULL' else valor

#Função para criar Parada
def criar_parada(Nome, cidade_id):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            query_create = sql.SQL("""
                INSERT INTO Parada (Nome, cidade_id)
                VALUES (%s, %s);
            """)
            cur.execute(query_create, (Nome, cidade_id))

            # Confirma todas as inserções
            conn.commit()

            print("Parada criada com sucesso!")

    except Exception as e:
        print(f"Erro ao criar Parada: {e}")
    finally:
        conn.close()

#Função para pesquisar Parada
def pesquisar_parada(nome):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:

            query_read = sql.SQL("""
                SELECT * FROM Parada
                WHERE nome = %s;
            """)

            # Executando a consulta
            cur.execute(query_read, (nome,))
            resultados = cur.fetchall()
                
            # Exibindo os resultados
            if resultados:
                print(resultados)     
    
    except Exception as e:
        print(f"Erro ao pesquisar parada: {e}")
    
    finally:
        conn.close()

#Função exclui Parada
def excluir_parada(nome):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            query_delete = sql.SQL("""
                DELETE FROM Parada
                WHERE Nome = %s
            """)
            cur.execute(query_delete, (nome,))
            conn.commit()
            if cur.rowcount > 0:
                print(f"Parada de nome '{nome}' excluída com sucesso!")
            else:
                print(f"Nenhuma Parada de nome '{nome}' foi encontrada.")
    except Exception as e:
        print(f"Erro ao excluir Parada: {e}")
    finally:
        conn.close()

#Função atualiza Parada
def atualizar_parada(Nome, cidade_id):
    conn = ConectarBanco() 
    try:
        with conn.cursor() as cur:
            query_update = """
                UPDATE Parada
                SET cidade_id = %s
                WHERE Nome = %s;
            """
            cur.execute(query_update, (cidade_id, Nome))

            # Confirma todas as atualizações
            conn.commit()

            print("Parada atualizado com sucesso!")

    except Exception as e:
        print(f"Erro ao atualizar a parada: {e}")
    finally:
        conn.close()