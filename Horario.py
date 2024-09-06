#Horario.py

from psycopg2 import sql
import psycopg2
from conectar_banco import ConectarBanco


#Função para aceitar valores NUll
def tratar_input(valor):
    return None if valor.upper() == 'NULL' else valor

#Função para criar Horario
def criar_horario(horario_id, duracao, dia_semana):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            query_create = sql.SQL("""
                INSERT INTO Horario (horario_id, duracao, dia_semana)
                VALUES (%s, %s, %s);
            """)
            cur.execute(query_create, (horario_id, duracao, dia_semana))

            # Confirma todas as inserções
            conn.commit()

            print("Horario criado com sucesso!")

    except Exception as e:
        print(f"Erro ao criar Horario: {e}")
    finally:
        conn.close()

#Função para pesquisar Horario
def pesquisar_horario(horario_id):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:

            query_read = sql.SQL("""
                SELECT * FROM Horario
                WHERE horario_id = %s;
            """)

            # Executando a consulta
            cur.execute(query_read, (horario_id,))
            resultados = cur.fetchall()
                
            # Exibindo os resultados
            if resultados:
                print(resultados)     
    
    except Exception as e:
        print(f"Erro ao pesquisar Horario: {e}")
    
    finally:
        conn.close()

#Função exclui Horario
def excluir_horario(horario_id):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            query_delete = sql.SQL("""
                DELETE FROM Horario
                WHERE horario_id = %s
            """)
            cur.execute(query_delete, (horario_id,))
            conn.commit()
            if cur.rowcount > 0:
                print(f"Horario de nome '{horario_id}' excluída com sucesso!")
            else:
                print(f"Nenhuma Horario de nome '{horario_id}' foi encontrada.")
    except Exception as e:
        print(f"Erro ao excluir Horario: {e}")
    finally:
        conn.close()

#Função atualiza Horario
def atualizar_horario(horario_id, duracao, dia_semana):
    conn = ConectarBanco() 
    try:
        with conn.cursor() as cur:
            query_update = """
                UPDATE Horario
                SET duracao = %s, dia_semana = %s
                WHERE horario_id = %s;
            """
            cur.execute(query_update, (dia_semana, duracao, horario_id ))

            # Confirma todas as atualizações
            conn.commit()

            print("Horario atualizado com sucesso!")

    except Exception as e:
        print(f"Erro ao atualizar o Horario: {e}")
    finally:
        conn.close()