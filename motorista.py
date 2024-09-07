# Motorista.py

# Nesta função motorista funciona perfeitamente criar e pesquisar motoristas as outras funções ainda estão sendo implementadas
from psycopg2 import sql
import psycopg2
from conectar_banco import ConectarBanco

#Função Criar Motorista
def criar_motorista(nome, telefone, foto, linha_id, empresa_id):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            query = sql.SQL("""
                INSERT INTO Motorista (Nome, Telefone, Foto, Linha_id, Empresa_id)
                VALUES (%s, %s, %s, %s, %s)
            """)
            cur.execute(query, (nome, telefone, foto, linha_id, empresa_id))
            conn.commit()
            print("Motorista criado com sucesso!")
    except Exception as e:
        print(f"Erro ao criar motorista: {e}")
    finally:
        conn.close()

#Função Obter foto 
def obter_foto():
    caminho_foto = input("Caminho para a foto: ")
    try:
        with open(caminho_foto, 'rb') as f:
            return f.read()
    except FileNotFoundError:
        print("Arquivo de foto não encontrado.")
        return None
    


#Função Pesquisar Motorista
def pesquisar_motorista(nome):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            # Comparação exata e sensível ao caso
            query = sql.SQL("""
                SELECT * FROM Motorista
                WHERE Nome = %s AND LENGTH(Nome) = LENGTH(%s)
            """)
            cur.execute(query, (nome, nome))
            resultados = cur.fetchall()
            if resultados:
                for resultado in resultados:
                    print(f"ID: {resultado[0]}")
                    print(f"Nome: {resultado[1]}")
                    print(f"Telefone: {resultado[2]}")
                    print(f"Foto: {resultado[3]}")  # Supondo que o campo Foto é em formato BYTEA
                    print(f"Linha ID: {resultado[4]}")
                    print(f"Empresa ID: {resultado[5]}")
                    print("-" * 40)
            else:
                print("Nenhum motorista encontrado com esse nome.")
    except Exception as e:
        print(f"Erro ao pesquisar motorista: {e}")
    finally:
        conn.close()


# Função Excluir Motorista pelo Nome
def excluir_motorista(nome):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            query = sql.SQL("""
                DELETE FROM Motorista
                WHERE Nome = %s
            """)
            cur.execute(query, (nome,))
            conn.commit()
            if cur.rowcount > 0:
                print(f"Motorista com o nome '{nome}' excluído com sucesso!")
            else:
                print(f"Nenhum motorista encontrado com o nome '{nome}'.")
    except Exception as e:
        print(f"Erro ao excluir motorista: {e}")
    finally:
        conn.close()


#Função Atualizar Motorista 
def alterar_motorista(id_motorista, nome=None, telefone=None, foto=None, linha_id=None, empresa_id=None):
    conn = ConectarBanco()
    try:
        with conn.cursor() as cur:
            # Cria uma lista de colunas que serão atualizadas
            campos_atualizacao = []
            valores = []

            if nome is not None:
                campos_atualizacao.append("Nome = %s")
                valores.append(nome)
            if telefone is not None:
                campos_atualizacao.append("Telefone = %s")
                valores.append(telefone)
            if foto is not None:
                campos_atualizacao.append("Foto = %s")
                valores.append(foto)
            if linha_id is not None:
                campos_atualizacao.append("Linha_id = %s")
                valores.append(linha_id)
            if empresa_id is not None:
                campos_atualizacao.append("Empresa_id = %s")
                valores.append(empresa_id)

            if not campos_atualizacao:
                print("Nenhum dado foi fornecido para atualização.")
                return

            # Concatena os campos de atualização
            query = sql.SQL("""
                UPDATE Motorista
                SET {}
                WHERE id = %s
            """).format(sql.SQL(', ').join(sql.SQL(campo) for campo in campos_atualizacao))

            valores.append(id_motorista)
            cur.execute(query, tuple(valores))
            conn.commit()
            print("Motorista atualizado com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar motorista: {e}")
    finally:
        conn.close()




    

