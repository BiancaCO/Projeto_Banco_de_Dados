# main.py APAGAR APAGAR APAGAR APAGAR APAGAR APAGAR APAGAR
# Essa main é para testar as funções em geral 
from psycopg2 import sql
import Motorista
from Motorista import pesquisar_motorista, criar_motorista, excluir_motorista
from conectar_banco import ConectarBanco

'''
#MENU DE TESTE 
def menu():
    print("1. Criar Motorista")
    print("2. Pesquisar Motorista")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")
    return opcao
'''

#teste da função banco
'''
from conectar_banco import ConectarBanco

def main():
    """
    Função principal para testar a importação e a conexão com o banco de dados.
    """
    conexao = ConectarBanco()
    if conexao:
        print("A conexão foi bem-sucedida.")
        conexao.close()  # Fechar a conexão quando terminar

if __name__ == "__main__":
    main() /






#teste da função criar motorista 
def main():
    nome = input("Nome do motorista: ")
    telefone = input("Telefone do motorista: ")
    foto = Motorista.obter_foto()
    linha_id = input("O motorista vai difirigir em qual linha?: ")
    empresa_id = input("O motorista é de qual empresa?: ")

    if foto is not None:
        Motorista.criar_motorista(nome, telefone, foto, linha_id, empresa_id)
    else:
        print("Não foi possível obter a foto.")

if __name__ == "__main__":
    main()



def main():
    while True:
        opcao = menu()
        
        if opcao == "1":
            nome = input("Nome do motorista: ")
            telefone = input("Telefone do motorista: ")
            foto = input("Foto do motorista (em formato BYTEA): ")
            linha_id = input("ID da linha: ")
            empresa_id = input("ID da empresa: ")
            criar_motorista(nome, telefone, foto, linha_id, empresa_id)
        
        elif opcao == "2":
            nome = input("Nome do motorista para pesquisa: ")
            pesquisar_motorista(nome)
        
        elif opcao == "3":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

'''


def main():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Excluir Motorista teste")
        print("2. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome exato do motorista que deseja excluir: ")
            motoristas = pesquisar_motorista(nome)

            if motoristas:
                print("\n--- Dados do Motorista ---")
                for motorista in motoristas:
                    print(f"ID: {motorista[0]}")
                    print(f"Nome: {motorista[1]}")
                    print(f"Telefone: {motorista[2]}")
                    print(f"Foto: {motorista[3]}")
                    print(f"Linha ID: {motorista[4]}")
                    print(f"Empresa ID: {motorista[5]}")
                    print("-" * 40)

                confirmar = input(f"Você deseja realmente excluir o motorista '{nome}'? (s/n): ")
                if confirmar.lower() == 's':
                    Motorista.excluir_motorista(nome)
                else:
                    print("Exclusão cancelada.")
            else:
                print(f"Nenhum motorista encontrado com o nome '{nome}'.")
        
        elif opcao == "2":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()



