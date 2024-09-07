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

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'Nenhum arquivo selecionado', 400
    
    file = request.files['file']
    
    if file.filename == '':
        return 'Nenhum arquivo selecionado', 400
    
    if file:
        image_data = file.read()
        nome = request.form['name']
        telefone = request.form['phone']
        linha_id = request.form['linha_id']
        empresa_id = request.form['empresa_id']
        
        criar_motorista(nome, telefone, image_data, linha_id, empresa_id)
        
        return redirect(url_for('index'))
    return 'Falha no upload', 500

@app.route('/search', methods=['GET'])
def search_motorista():
    nome = request.args.get('name')
    if not nome:
        return 'Nome não fornecido', 400
    
    motorista = buscar_motorista_por_nome(nome)
    if motorista:
        return render_template('result.html', motorista=motorista)
    else:
        return 'Motorista não encontrado', 404

@app.route('/foto/<int:motorista_id>')
def foto(motorista_id):
    foto = buscar_foto_motorista(motorista_id)
    if foto:
        return send_file(BytesIO(foto[0]), mimetype='image/jpeg')
    else:
        return 'Foto não encontrada', 404

@app.route('/edit/<int:motorista_id>', methods=['GET', 'POST'])
def edit_motorista(motorista_id):
    if request.method == 'POST':
        nome = request.form['name']
        telefone = request.form['phone']
        linha_id = request.form['linha_id']
        empresa_id = request.form['empresa_id']
        
        editar_motorista(motorista_id, nome, telefone, linha_id, empresa_id)
        return redirect(url_for('search_motorista', name=nome))
    else:
        motorista = buscar_dados_motorista(motorista_id)
        if motorista:
            return render_template('edit.html', motorista=motorista, motorista_id=motorista_id)
        else:
            return 'Motorista não encontrado', 404

@app.route('/delete/<int:motorista_id>', methods=['POST'])
def delete_motorista(motorista_id):
    excluir_motorista(motorista_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
