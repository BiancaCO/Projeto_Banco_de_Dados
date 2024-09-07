# cidadea.py

from psycopg2 import sql
import psycopg2
from conectar_banco import ConectarBanco


#Função para aceitar valores NUll
def tratar_input(valor):
    return None if valor.upper() == 'NULL' else valor

#Função para criar Cidade
def criar_cidade(Nome, num_habitantes):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
             # Inserir na tabela Empresa
            query_create = sql.SQL("""
                INSERT INTO Cidade (Nome, num_habitantes)
                VALUES (%s, %s);
            """)
            cur.execute(query_create, (Nome, num_habitantes))

            # Confirma todas as inserções
            conn.commit()

            print("Cidade criada com sucesso!")

    except Exception as e:
        print(f"Erro ao criar Cidade: {e}")
    finally:
        conn.close()

#Função para pesquisar Cidade
def pesquisar_cidade(nome):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:

            query_read = sql.SQL("""
                SELECT * FROM Cidade
                WHERE nome = %s;
            """)

            # Executando a consulta
            cur.execute(query_read, (nome,))
            resultados = cur.fetchall()
                
            # Exibindo os resultados
            if resultados:
                print(resultados)     
    
    except Exception as e:
        print(f"Erro ao pesquisar Cidade: {e}")
    
    finally:
        conn.close()

#Função exclui Cidade
def excluir_cidade(nome):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            query_delete = sql.SQL("""
                DELETE FROM Cidade
                WHERE Nome = %s
            """)
            cur.execute(query_delete, (nome,))
            conn.commit()
            if cur.rowcount > 0:
                print(f"Cidade de nome '{nome}' excluída com sucesso!")
            else:
                print(f"Nenhuma Cidade de nome '{nome}' foi encontrada.")
    except Exception as e:
        print(f"Erro ao excluir Cidade: {e}")
    finally:
        conn.close()

#Função atualiza Cidade
def atualizar_cidade(Nome, num_habitantes):
    conn = ConectarBanco() 
    try:
        with conn.cursor() as cur:
            query_update = """
                UPDATE Cidade
                SET num_habitantes = %s
                WHERE Nome = %s;
            """
            cur.execute(query_update, (num_habitantes, Nome))

            # Confirma todas as atualizações
            conn.commit()

            print("Cidade atualizada com sucesso!")

    except Exception as e:
        print(f"Erro ao atualizar o Cidade: {e}")
    finally:
        conn.close()