# Importa as bibliotecas necessárias
import psycopg2
from psycopg2 import sql
from conectar_banco import ConectarBanco  # Função para conectar ao banco de dados
from io import BytesIO

# Função para criar um novo motorista no banco de dados
def criar_motorista(nome, telefone, foto, linha_id, empresa_id):
    # Estabelece a conexão com o banco de dados
    conn = ConectarBanco()
    try:
        # Cria um cursor para executar comandos SQL
        with conn.cursor() as cur:
            # Define a query SQL para inserir um novo motorista
            query = sql.SQL("""
                INSERT INTO Motorista (Nome, Telefone, Foto, Linha_id, Empresa_id)
                VALUES (%s, %s, %s, %s, %s)
            """)
            # Executa a query com os parâmetros fornecidos
            cur.execute(query, (nome, telefone, psycopg2.Binary(foto), linha_id, empresa_id))
            # Confirma a transação
            conn.commit()
            print("Motorista criado com sucesso!")
    except Exception as e:
        # Em caso de erro, imprime a mensagem de erro
        print(f"Erro ao criar motorista: {e}")
    finally:
        # Fecha a conexão com o banco de dados
        conn.close()

# Função para buscar um motorista pelo nome
def buscar_motorista_por_nome(nome):
    # Estabelece a conexão com o banco de dados
    conn = ConectarBanco()
    try:
        # Cria um cursor para executar comandos SQL
        with conn.cursor() as cur:
            # Define a query SQL para buscar o motorista pelo nome
            query = sql.SQL("""
                SELECT Motorista_id, Nome, Telefone FROM Motorista WHERE Nome = %s
            """)
            # Executa a query com o parâmetro fornecido
            cur.execute(query, (nome,))
            # Retorna o resultado da consulta (uma tupla com o id, nome e telefone do motorista)
            return cur.fetchone()
    except Exception as e:
        # Em caso de erro, imprime a mensagem de erro
        print(f"Erro ao pesquisar motorista: {e}")
        return None
    finally:
        # Fecha a conexão com o banco de dados
        conn.close()

# Função para buscar a foto de um motorista pelo ID
def buscar_foto_motorista(motorista_id):
    # Estabelece a conexão com o banco de dados
    conn = ConectarBanco()
    try:
        # Cria um cursor para executar comandos SQL
        with conn.cursor() as cur:
            # Define a query SQL para buscar a foto do motorista pelo ID
            query = sql.SQL("""
                SELECT Foto FROM Motorista WHERE Motorista_id = %s
            """)
            # Executa a query com o parâmetro fornecido
            cur.execute(query, (motorista_id,))
            # Retorna o resultado da consulta (a foto do motorista em formato BYTEA)
            return cur.fetchone()
    except Exception as e:
        # Em caso de erro, imprime a mensagem de erro
        print(f"Erro ao recuperar foto: {e}")
        return None
    finally:
        # Fecha a conexão com o banco de dados
        conn.close()

# Função para editar os dados de um motorista
def editar_motorista(motorista_id, nome, telefone, linha_id, empresa_id):
    # Estabelece a conexão com o banco de dados
    conn = ConectarBanco()
    try:
        # Cria um cursor para executar comandos SQL
        with conn.cursor() as cur:
            # Define a query SQL para atualizar os dados do motorista
            query = sql.SQL("""
                UPDATE Motorista
                SET Nome = %s, Telefone = %s, Linha_id = %s, Empresa_id = %s
                WHERE Motorista_id = %s
            """)
            # Executa a query com os parâmetros fornecidos
            cur.execute(query, (nome, telefone, linha_id, empresa_id, motorista_id))
            # Confirma a transação
            conn.commit()
    except Exception as e:
        # Em caso de erro, imprime a mensagem de erro
        print(f"Erro ao editar motorista: {e}")
    finally:
        # Fecha a conexão com o banco de dados
        conn.close()

# Função para excluir um motorista pelo ID
def excluir_motorista(motorista_id):
    # Estabelece a conexão com o banco de dados
    conn = ConectarBanco()
    try:
        # Cria um cursor para executar comandos SQL
        with conn.cursor() as cur:
            # Define a query SQL para excluir o motorista pelo ID
            query = sql.SQL("DELETE FROM Motorista WHERE Motorista_id = %s")
            # Executa a query com o parâmetro fornecido
            cur.execute(query, (motorista_id,))
            # Confirma a transação
            conn.commit()
    except Exception as e:
        # Em caso de erro, imprime a mensagem de erro
        print(f"Erro ao excluir motorista: {e}")
    finally:
        # Fecha a conexão com o banco de dados
        conn.close()

# Função para buscar os dados de um motorista pelo ID
def buscar_dados_motorista(motorista_id):
    # Estabelece a conexão com o banco de dados
    conn = ConectarBanco()
    try:
        # Cria um cursor para executar comandos SQL
        with conn.cursor() as cur:
            # Define a query SQL para buscar os dados do motorista pelo ID
            query = sql.SQL("""
                SELECT Nome, Telefone, Linha_id, Empresa_id FROM Motorista WHERE Motorista_id = %s
            """)
            # Executa a query com o parâmetro fornecido
            cur.execute(query, (motorista_id,))
            # Retorna o resultado da consulta (uma tupla com os dados do motorista)
            return cur.fetchone()
    except Exception as e:
        # Em caso de erro, imprime a mensagem de erro
        print(f"Erro ao buscar dados do motorista: {e}")
        return None
    finally:
        # Fecha a conexão com o banco de dados
        conn.close()
