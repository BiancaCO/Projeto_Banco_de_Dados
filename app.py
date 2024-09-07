# Importando as bibliotecas necessárias do Flask e de funções do módulo motorista
from flask import Flask, render_template, request, redirect, url_for, send_file
from motorista import (
    criar_motorista,
    buscar_motorista_por_nome,
    buscar_foto_motorista,
    editar_motorista,
    excluir_motorista,
    buscar_dados_motorista
)
from io import BytesIO

# Inicializa a aplicação Flask
app = Flask(__name__)

# Rota para a página inicial, que renderiza o template 'upload.html'
@app.route('/')
def index():
    return render_template('upload.html')

# Rota para o upload de arquivos de imagem e criação de um novo motorista
@app.route('/upload', methods=['POST'])
def upload_file():
    # Verifica se o arquivo está presente na requisição
    if 'file' not in request.files:
        return 'Nenhum arquivo selecionado', 400
    
    # Obtém o arquivo enviado
    file = request.files['file']
    
    # Verifica se o nome do arquivo está vazio
    if file.filename == '':
        return 'Nenhum arquivo selecionado', 400
    
    if file:
        # Lê o conteúdo do arquivo
        image_data = file.read()
        # Obtém outros dados do motorista do formulário
        nome = request.form['name']
        telefone = request.form['phone']
        linha_id = request.form['linha_id']
        empresa_id = request.form['empresa_id']
        
        # Chama a função para criar um novo motorista com os dados fornecidos
        criar_motorista(nome, telefone, image_data, linha_id, empresa_id)
        
        # Redireciona para a página inicial
        return redirect(url_for('index'))
    return 'Falha no upload', 500

# Rota para buscar motoristas pelo nome
@app.route('/search', methods=['GET'])
def search_motorista():
    # Obtém o nome do motorista da query string
    nome = request.args.get('name')
    if not nome:
        return 'Nome não fornecido', 400
    
    # Busca o motorista pelo nome
    motorista = buscar_motorista_por_nome(nome)
    if motorista:
        # Renderiza o template 'result.html' com os dados do motorista
        return render_template('result.html', motorista=motorista)
    else:
        return 'Motorista não encontrado', 404

# Rota para retornar a foto do motorista com base no ID
@app.route('/foto/<int:motorista_id>')
def foto(motorista_id):
    # Busca a foto do motorista pelo ID
    foto = buscar_foto_motorista(motorista_id)
    if foto:
        # Envia o arquivo de imagem como resposta
        return send_file(BytesIO(foto[0]), mimetype='image/jpeg')
    else:
        return 'Foto não encontrada', 404

# Rota para editar os dados do motorista
@app.route('/edit/<int:motorista_id>', methods=['GET', 'POST'])
def edit_motorista(motorista_id):
    if request.method == 'POST':
        # Obtém os dados atualizados do formulário
        nome = request.form['name']
        telefone = request.form['phone']
        linha_id = request.form['linha_id']
        empresa_id = request.form['empresa_id']
        
        # Chama a função para editar o motorista com os novos dados
        editar_motorista(motorista_id, nome, telefone, linha_id, empresa_id)
        # Redireciona para a busca do motorista com o nome atualizado
        return redirect(url_for('search_motorista', name=nome))
    else:
        # Busca os dados do motorista para edição
        motorista = buscar_dados_motorista(motorista_id)
        if motorista:
            # Renderiza o template 'edit.html' com os dados do motorista
            return render_template('edit.html', motorista=motorista, motorista_id=motorista_id)
        else:
            return 'Motorista não encontrado', 404

# Rota para excluir um motorista
@app.route('/delete/<int:motorista_id>', methods=['POST'])
def delete_motorista(motorista_id):
    # Chama a função para excluir o motorista pelo ID
    excluir_motorista(motorista_id)
    # Redireciona para a página inicial após exclusão
    return redirect(url_for('index'))

# Inicializa o servidor Flask em modo de depuração
if __name__ == '__main__':
    app.run(debug=True)
