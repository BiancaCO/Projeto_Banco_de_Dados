# Empresa.py

from psycopg2 import sql
import psycopg2
from conectar_banco import ConectarBanco


#Função para aceitar valores NUll
def tratar_input(valor):
    return None if valor.upper() == 'NULL' else valor

#Função para criar Empresa
def criar_empresa(Nome, Contato):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
             # Inserir na tabela Empresa
            query_create = sql.SQL("""
                INSERT INTO Empresa (Nome, Contato)
                VALUES (%s, %s);
            """)
            cur.execute(query_create, (Nome, Contato))

            # Confirma todas as inserções
            conn.commit()

            print("Empresa criada com sucesso!")

    except Exception as e:
        print(f"Erro ao criar Empresa: {e}")
    finally:
        conn.close()

#Função para pesquisar Empresa
def pesquisar_empresa(nome):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:

            query_read = sql.SQL("""
                SELECT * FROM Empresa
                WHERE nome = %s;
            """)

            # Executando a consulta
            cur.execute(query_read, (nome,))
            resultados = cur.fetchall()
                
            # Exibindo os resultados
            if resultados:
                print(resultados)     
    
    except Exception as e:
        print(f"Erro ao pesquisar Empresa: {e}")
    
    finally:
        conn.close()

#Função exclui Empresa
def excluir_empresa(nome):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            query_delete = sql.SQL("""
                DELETE FROM Empresa
                WHERE Nome = %s
            """)
            cur.execute(query_delete, (nome,))
            conn.commit()
            if cur.rowcount > 0:
                print(f"Empresa de nome '{nome}' excluída com sucesso!")
            else:
                print(f"Nenhuma Empresa de nome '{nome}' foi encontrada.")
    except Exception as e:
        print(f"Erro ao excluir Empresa: {e}")
    finally:
        conn.close()

#Função atualiza empresa
def atualizar_empresa(Nome, contato):
    conn = ConectarBanco() 
    try:
        with conn.cursor() as cur:
            query_update = """
                UPDATE Empresa
                SET Contato = %s
                WHERE Nome = %s;
            """
            cur.execute(query_update, (contato, Nome))

            # Confirma todas as atualizações
            conn.commit()

            print("Empresa atualizado com sucesso!")

    except Exception as e:
        print(f"Erro ao atualizar a empresa: {e}")
    finally:
        conn.close()