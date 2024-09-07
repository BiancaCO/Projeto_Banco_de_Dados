# Terminal.py

from psycopg2 import sql
import psycopg2
from conectar_banco import ConectarBanco


#Função para aceitar valores NUll
def tratar_input(valor):
    return None if valor.upper() == 'NULL' else valor

#Função para criar Empresa
def criar_terminal(Nome, cidade_id):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            query_create = sql.SQL("""
                INSERT INTO Terminal (Nome, cidade_id)
                VALUES (%s, %s);
            """)
            cur.execute(query_create, (Nome, cidade_id))

            # Confirma todas as inserções
            conn.commit()

            print("Terminal criado com sucesso!")

    except Exception as e:
        print(f"Erro ao criar Terminal: {e}")
    finally:
        conn.close()

#Função para pesquisar Empresa
def pesquisar_terminal(nome):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:

            query_read = sql.SQL("""
                SELECT * FROM Terminal
                WHERE nome = %s;
            """)

            # Executando a consulta
            cur.execute(query_read, (nome,))
            resultados = cur.fetchall()
                
            # Exibindo os resultados
            if resultados:
                print(resultados)     
    
    except Exception as e:
        print(f"Erro ao pesquisar Terminal: {e}")
    
    finally:
        conn.close()

#Função exclui Empresa
def excluir_terminal(nome):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            query_delete = sql.SQL("""
                DELETE FROM Terminal
                WHERE Nome = %s
            """)
            cur.execute(query_delete, (nome,))
            conn.commit()
            if cur.rowcount > 0:
                print(f"Terminal de nome '{nome}' excluído com sucesso!")
            else:
                print(f"Nenhum Terminal de nome '{nome}' foi encontrada.")
    except Exception as e:
        print(f"Erro ao excluir Terminal: {e}")
    finally:
        conn.close()

#Função atualiza empresa
def atualizar_terminal(Nome, cidade_id):
    conn = ConectarBanco() 
    try:
        with conn.cursor() as cur:
            query_update = """
                UPDATE Terminal
                SET cidade_id = %s
                WHERE Nome = %s;
            """
            cur.execute(query_update, (cidade_id, Nome))

            # Confirma todas as atualizações
            conn.commit()

            print("Cidade atualizada com sucesso!")

    except Exception as e:
        print(f"Erro ao atualizar o Terminal: {e}")
    finally:
        conn.close()