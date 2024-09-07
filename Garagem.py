# Garagem.py

from psycopg2 import sql
import psycopg2
from conectar_banco import ConectarBanco


#Função para aceitar valores NUll
def tratar_input(valor):
    return None if valor.upper() == 'NULL' else valor

#Função para criar Garagem
def criar_garagem(Nome, num_vagas, empresa_id):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            query_create = sql.SQL("""
                INSERT INTO Garagem (Nome, num_vagas, empresa_id)
                VALUES (%s, %s, %s);
            """)
            cur.execute(query_create, (Nome, num_vagas, empresa_id))

            # Confirma todas as inserções
            conn.commit()

            print("Garagem criada com sucesso!")

    except Exception as e:
        print(f"Erro ao criar Garagem: {e}")
    finally:
        conn.close()

#Função para pesquisar Garagem
def pesquisar_garagem(nome):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:

            query_read = sql.SQL("""
                SELECT * FROM Garagem
                WHERE nome = %s;
            """)

            # Executando a consulta
            cur.execute(query_read, (nome,))
            resultados = cur.fetchall()
                
            # Exibindo os resultados
            if resultados:
                print(resultados)     
    
    except Exception as e:
        print(f"Erro ao pesquisar Garagem: {e}")
    
    finally:
        conn.close()

#Função exclui Garagem
def excluir_garagem(nome):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            query_delete = sql.SQL("""
                DELETE FROM Garagem
                WHERE Nome = %s
            """)
            cur.execute(query_delete, (nome,))
            conn.commit()
            if cur.rowcount > 0:
                print(f"Garagem de nome '{nome}' excluída com sucesso!")
            else:
                print(f"Nenhuma Garagem de nome '{nome}' foi encontrada.")
    except Exception as e:
        print(f"Erro ao excluir Garagem: {e}")
    finally:
        conn.close()

#Função atualiza Garagem
def atualizar_garagem(Nome, num_vagas, empresa_id):
    conn = ConectarBanco() 
    try:
        with conn.cursor() as cur:
            query_update = """
                UPDATE Garagem
                SET empresa_id = %s, num_vagas = %s
                WHERE Nome = %s;
            """
            cur.execute(query_update, (empresa_id, num_vagas, Nome))

            # Confirma todas as atualizações
            conn.commit()

            print("Garagem atualizado com sucesso!")

    except Exception as e:
        print(f"Erro ao atualizar a Garagem: {e}")
    finally:
        conn.close()